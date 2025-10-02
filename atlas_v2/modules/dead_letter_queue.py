"""
Dead Letter Queue Management for Atlas v2

Handles permanently failed or non-processable URLs to prevent queue pollution
and maintain processing efficiency.

Key Features:
- Quarantines non-processable URLs (file://, invalid schemes, etc.)
- Tracks failure reasons and retry counts
- Provides analysis of failure patterns
- Supports manual review and recovery operations
"""

import asyncio
import aiosqlite
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import logging

from .url_classifier import URLClassification, ProcessingStrategy

logger = logging.getLogger(__name__)

class FailureType(Enum):
    PERMANENT = "permanent"          # Will never succeed (file:// URLs)
    TEMPORARY = "temporary"          # Might succeed with retry
    UNSUPPORTED = "unsupported"      # Not supported content type
    RATE_LIMITED = "rate_limited"    # External rate limiting
    NETWORK_ERROR = "network_error"  # Network connectivity issues

class QuarantineReason(Enum):
    FILE_SCHEME = "file_scheme"              # file:// URLs not supported
    INVALID_SCHEME = "invalid_scheme"        # Unsupported URL scheme
    UNSUPPORTED_CONTENT = "unsupported_content"  # Unsupported file types
    RATE_LIMIT = "rate_limit"                # Rate limited by source
    AUTHENTICATION = "authentication"        # Requires authentication
    PAYWALL = "paywall"                      # Behind paywall
    NOT_FOUND = "not_found"                  # 404 Not Found
    SERVER_ERROR = "server_error"            # 5xx server errors
    TIMEOUT = "timeout"                      # Request timeouts
    UNKNOWN = "unknown"                      # Unknown failure reason

@dataclass
class DeadLetterItem:
    """Dead letter queue item"""
    content_id: str
    source_url: str
    source_name: str
    original_error: str
    failure_type: FailureType
    quarantine_reason: QuarantineReason
    retry_count: int
    classification: URLClassification
    quarantined_at: str
    notes: str
    metadata: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for database storage"""
        data = asdict(self)
        data['classification'] = asdict(self.classification)
        data['failure_type'] = self.failure_type.value
        data['quarantine_reason'] = self.quarantine_reason.value
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DeadLetterItem':
        """Create from database dictionary"""
        classification_data = data.pop('classification', {})
        classification = URLClassification(**classification_data)

        data['failure_type'] = FailureType(data['failure_type'])
        data['quarantine_reason'] = QuarantineReason(data['quarantine_reason'])
        data['classification'] = classification

        return cls(**data)

class DeadLetterQueue:
    """Manages dead letter queue operations"""

    def __init__(self, db_path: str = "../data/atlas.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    async def initialize(self):
        """Initialize dead letter queue tables"""
        logger.info("🔧 Initializing dead letter queue...")

        async with aiosqlite.connect(self.db_path) as db:
            # Dead letter queue table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS dead_letter_queue (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content_id TEXT UNIQUE NOT NULL,
                    source_url TEXT NOT NULL,
                    source_name TEXT NOT NULL,
                    original_error TEXT NOT NULL,
                    failure_type TEXT NOT NULL,
                    quarantine_reason TEXT NOT NULL,
                    retry_count INTEGER DEFAULT 0,
                    classification_json TEXT NOT NULL,
                    quarantined_at TEXT NOT NULL,
                    notes TEXT DEFAULT '',
                    metadata_json TEXT DEFAULT '{}'
                )
            """)

            # Create indexes
            await db.execute("CREATE INDEX IF NOT EXISTS idx_dlq_source ON dead_letter_queue(source_name)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_dlq_failure_type ON dead_letter_queue(failure_type)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_dlq_quarantine_reason ON dead_letter_queue(quarantine_reason)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_dlq_quarantined_at ON dead_letter_queue(quarantined_at)")

            await db.commit()

        logger.info("✅ Dead letter queue initialized")

    async def quarantine_item(
        self,
        content_id: str,
        source_url: str,
        source_name: str,
        original_error: str,
        classification: URLClassification,
        retry_count: int = 0,
        notes: str = "",
        metadata: Dict[str, Any] = None
    ) -> bool:
        """
        Quarantine an item in the dead letter queue

        Args:
            content_id: Unique content identifier
            source_url: Original URL
            source_name: Source name/podcast
            original_error: Error message
            classification: URL classification result
            retry_count: Number of retry attempts
            notes: Additional notes
            metadata: Additional metadata

        Returns:
            True if successfully quarantined
        """
        try:
            # Determine failure type and quarantine reason
            failure_type = self._classify_failure(original_error, classification)
            quarantine_reason = self._determine_quarantine_reason(classification, original_error)

            # Create dead letter item
            item = DeadLetterItem(
                content_id=content_id,
                source_url=source_url,
                source_name=source_name,
                original_error=original_error,
                failure_type=failure_type,
                quarantine_reason=quarantine_reason,
                retry_count=retry_count,
                classification=classification,
                quarantined_at=datetime.now().isoformat(),
                notes=notes,
                metadata=metadata or {}
            )

            async with aiosqlite.connect(self.db_path) as db:
                await db.execute("""
                    INSERT OR REPLACE INTO dead_letter_queue (
                        content_id, source_url, source_name, original_error,
                        failure_type, quarantine_reason, retry_count,
                        classification_json, quarantined_at, notes, metadata_json
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    item.content_id,
                    item.source_url,
                    item.source_name,
                    item.original_error,
                    item.failure_type.value,
                    item.quarantine_reason.value,
                    item.retry_count,
                    json.dumps(item.classification.to_dict()),
                    item.quarantined_at,
                    item.notes,
                    json.dumps(item.metadata)
                ))

                await db.commit()

            logger.info(f"🚫 Quarantined {source_url[:100]}... - {quarantine_reason.value}")
            return True

        except Exception as e:
            logger.error(f"Error quarantining item {content_id}: {e}")
            return False

    async def get_quarantined_items(
        self,
        limit: int = 100,
        failure_type: FailureType = None,
        quarantine_reason: QuarantineReason = None,
        days_ago: int = 30
    ) -> List[DeadLetterItem]:
        """Get quarantined items with optional filtering"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                # Build query with filters
                conditions = ["quarantined_at > ?"]
                params = [datetime.now() - timedelta(days=days_ago)]

                if failure_type:
                    conditions.append("failure_type = ?")
                    params.append(failure_type.value)

                if quarantine_reason:
                    conditions.append("quarantine_reason = ?")
                    params.append(quarantine_reason.value)

                query = f"""
                    SELECT * FROM dead_letter_queue
                    WHERE {' AND '.join(conditions)}
                    ORDER BY quarantined_at DESC
                    LIMIT ?
                """
                params.append(limit)

                cursor = await db.execute(query, params)
                rows = await cursor.fetchall()

                # Convert to DeadLetterItem objects
                items = []
                for row in rows:
                    # Convert row to dict
                    row_dict = {
                        'content_id': row[1],
                        'source_url': row[2],
                        'source_name': row[3],
                        'original_error': row[4],
                        'failure_type': row[5],
                        'quarantine_reason': row[6],
                        'retry_count': row[7],
                        'classification': json.loads(row[8]),
                        'quarantined_at': row[9],
                        'notes': row[10],
                        'metadata': json.loads(row[11]) if row[11] else {}
                    }
                    items.append(DeadLetterItem.from_dict(row_dict))

                return items

        except Exception as e:
            logger.error(f"Error getting quarantined items: {e}")
            return []

    async def get_quarantine_stats(self, days_ago: int = 30) -> Dict[str, Any]:
        """Get statistics about quarantined items"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                # Total count
                cursor = await db.execute("""
                    SELECT COUNT(*) FROM dead_letter_queue
                    WHERE quarantined_at > ?
                """, (datetime.now() - timedelta(days=days_ago),))
                total_count = (await cursor.fetchone())[0]

                # By failure type
                cursor = await db.execute("""
                    SELECT failure_type, COUNT(*) as count
                    FROM dead_letter_queue
                    WHERE quarantined_at > ?
                    GROUP BY failure_type
                    ORDER BY count DESC
                """, (datetime.now() - timedelta(days=days_ago),))
                by_failure_type = dict(await cursor.fetchall())

                # By quarantine reason
                cursor = await db.execute("""
                    SELECT quarantine_reason, COUNT(*) as count
                    FROM dead_letter_queue
                    WHERE quarantined_at > ?
                    GROUP BY quarantine_reason
                    ORDER BY count DESC
                """, (datetime.now() - timedelta(days=days_ago),))
                by_quarantine_reason = dict(await cursor.fetchall())

                # By source
                cursor = await db.execute("""
                    SELECT source_name, COUNT(*) as count
                    FROM dead_letter_queue
                    WHERE quarantined_at > ?
                    GROUP BY source_name
                    ORDER BY count DESC
                    LIMIT 10
                """, (datetime.now() - timedelta(days=days_ago),))
                by_source = dict(await cursor.fetchall())

                return {
                    'total_quarantined': total_count,
                    'by_failure_type': by_failure_type,
                    'by_quarantine_reason': by_quarantine_reason,
                    'by_source': by_source,
                    'period_days': days_ago
                }

        except Exception as e:
            logger.error(f"Error getting quarantine stats: {e}")
            return {
                'total_quarantined': 0,
                'by_failure_type': {},
                'by_quarantine_reason': {},
                'by_source': {},
                'period_days': days_ago,
                'error': str(e)
            }

    async def remove_item(self, content_id: str) -> bool:
        """Remove item from dead letter queue"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                cursor = await db.execute("""
                    DELETE FROM dead_letter_queue WHERE content_id = ?
                """, (content_id,))
                await db.commit()

                if cursor.rowcount > 0:
                    logger.info(f"🗑️ Removed {content_id} from dead letter queue")
                    return True
                else:
                    logger.warning(f"Item {content_id} not found in dead letter queue")
                    return False

        except Exception as e:
            logger.error(f"Error removing item {content_id}: {e}")
            return False

    async def attempt_recovery(self, content_id: str) -> bool:
        """
        Attempt to recover an item from dead letter queue
        Returns True if item should be re-queued for processing
        """
        try:
            async with aiosqlite.connect(self.db_path) as db:
                cursor = await db.execute("""
                    SELECT * FROM dead_letter_queue WHERE content_id = ?
                """, (content_id,))
                row = await cursor.fetchone()

                if not row:
                    logger.warning(f"Item {content_id} not found in dead letter queue")
                    return False

                # Parse item
                item_dict = {
                    'content_id': row[1],
                    'source_url': row[2],
                    'source_name': row[3],
                    'original_error': row[4],
                    'failure_type': row[5],
                    'quarantine_reason': row[6],
                    'retry_count': row[7],
                    'classification': json.loads(row[8]),
                    'quarantined_at': row[9],
                    'notes': row[10],
                    'metadata': json.loads(row[11]) if row[11] else {}
                }
                item = DeadLetterItem.from_dict(item_dict)

                # Check if recovery is possible
                if self._is_recoverable(item):
                    # Remove from dead letter queue
                    await self.remove_item(content_id)

                    # Log recovery attempt
                    logger.info(f"🔄 Recovered {content_id} from dead letter queue")
                    return True
                else:
                    logger.info(f"❌ {content_id} not recoverable - remains quarantined")
                    return False

        except Exception as e:
            logger.error(f"Error attempting recovery for {content_id}: {e}")
            return False

    def _classify_failure(self, error: str, classification: URLClassification) -> FailureType:
        """Classify failure type from error message and classification"""
        error_lower = error.lower()

        if classification.processing_strategy == ProcessingStrategy.FILE_LOCAL:
            return FailureType.PERMANENT
        elif classification.processing_strategy == ProcessingStrategy.UNSUPPORTED:
            return FailureType.UNSUPPORTED
        elif '404' in error_lower or 'not found' in error_lower:
            return FailureType.PERMANENT
        elif 'rate limit' in error_lower or '429' in error_lower:
            return FailureType.RATE_LIMITED
        elif 'timeout' in error_lower or 'connection' in error_lower:
            return FailureType.NETWORK_ERROR
        elif any(code in error_lower for code in ['500', '502', '503', '504']):
            return FailureType.TEMPORARY
        else:
            return FailureType.PERMANENT

    def _determine_quarantine_reason(self, classification: URLClassification, error: str) -> QuarantineReason:
        """Determine specific quarantine reason"""
        if classification.processing_strategy == ProcessingStrategy.FILE_LOCAL:
            return QuarantineReason.FILE_SCHEME
        elif classification.processing_strategy == ProcessingStrategy.UNSUPPORTED:
            if 'file://' in classification.original_url:
                return QuarantineReason.FILE_SCHEME
            else:
                return QuarantineReason.INVALID_SCHEME
        elif '404' in error.lower() or 'not found' in error.lower():
            return QuarantineReason.NOT_FOUND
        elif 'rate limit' in error.lower() or '429' in error.lower():
            return QuarantineReason.RATE_LIMIT
        elif 'timeout' in error.lower():
            return QuarantineReason.TIMEOUT
        elif any(code in error.lower() for code in ['500', '502', '503', '504']):
            return QuarantineReason.SERVER_ERROR
        else:
            return QuarantineReason.UNKNOWN

    def _is_recoverable(self, item: DeadLetterItem) -> bool:
        """Check if a quarantined item is recoverable"""
        # File scheme URLs are never recoverable
        if item.quarantine_reason in [QuarantineReason.FILE_SCHEME, QuarantineReason.INVALID_SCHEME]:
            return False

        # Not found errors are not recoverable
        if item.quarantine_reason == QuarantineReason.NOT_FOUND:
            return False

        # Unsupported content is not recoverable
        if item.quarantine_reason == QuarantineReason.UNSUPPORTED_CONTENT:
            return False

        # Network errors and server errors might be recoverable
        if item.quarantine_reason in [QuarantineReason.TIMEOUT, QuarantineReason.SERVER_ERROR]:
            return True

        # Rate limited items are recoverable after cooldown
        if item.quarantine_reason == QuarantineReason.RATE_LIMIT:
            quarantined_time = datetime.fromisoformat(item.quarantined_at)
            cooldown_period = timedelta(hours=1)  # 1 hour cooldown for rate limits
            return datetime.now() - quarantined_time > cooldown_period

        # Default to not recoverable
        return False

# Global dead letter queue instance
_dlq = DeadLetterQueue()

async def initialize_dlq():
    """Initialize dead letter queue"""
    await _dlq.initialize()

async def quarantine_item(
    content_id: str,
    source_url: str,
    source_name: str,
    original_error: str,
    classification: URLClassification,
    retry_count: int = 0,
    notes: str = "",
    metadata: Dict[str, Any] = None
) -> bool:
    """Quarantine an item in the dead letter queue"""
    return await _dlq.quarantine_item(
        content_id, source_url, source_name, original_error,
        classification, retry_count, notes, metadata
    )

async def get_quarantine_stats(days_ago: int = 30) -> Dict[str, Any]:
    """Get dead letter queue statistics"""
    return await _dlq.get_quarantine_stats(days_ago)