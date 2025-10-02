"""
Enhanced Queue Manager for Atlas v2

Production-grade queue management with deduplication, prioritization,
and intelligent routing to eliminate queue pollution and handle high-volume inputs.

Key Features:
- URL deduplication to prevent duplicate processing
- Priority-based queue ordering
- Intelligent routing based on URL classification
- Queue pressure monitoring and backpressure handling
- Batch processing with configurable sizes
- Comprehensive queue analytics and monitoring
"""

import asyncio
import aiosqlite
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from enum import Enum
import logging

from .url_classifier import classify_url, generate_content_id, ProcessingStrategy
from .dead_letter_queue import quarantine_item

logger = logging.getLogger(__name__)

class QueueStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRY = "retry"
    QUARANTINED = "quarantined"

class PriorityLevel(Enum):
    CRITICAL = 100    # User-submitted, high-value content
    HIGH = 80         # Recent podcast episodes, breaking news
    NORMAL = 50       # Regular content processing
    LOW = 20          # Bulk ingestion, backlog items
    CLEANUP = 10      # Queue maintenance tasks

@dataclass
class QueueItem:
    """Queue item with enhanced metadata"""
    content_id: str
    source_url: str
    normalized_url: str
    source_name: str
    content_type: str
    priority: int
    status: QueueStatus
    retry_count: int
    processing_strategy: ProcessingStrategy
    metadata: Dict[str, Any]
    created_at: str
    updated_at: str
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    next_retry_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for database storage"""
        data = asdict(self)
        data['status'] = self.status.value
        data['processing_strategy'] = self.processing_strategy.value
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'QueueItem':
        """Create from database dictionary"""
        data['status'] = QueueStatus(data['status'])
        data['processing_strategy'] = ProcessingStrategy(data['processing_strategy'])
        return cls(**data)

class EnhancedQueueManager:
    """Enhanced queue manager with production-grade features"""

    def __init__(self, db_path: str = "../data/atlas.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.max_batch_size = 50
        self.max_concurrent_processing = 10
        self.backpressure_threshold = 1000

    async def initialize(self):
        """Initialize enhanced queue tables and indexes"""
        logger.info("🚀 Initializing enhanced queue manager...")

        async with aiosqlite.connect(self.db_path) as db:
            # Add new columns to existing processing_queue table
            try:
                await db.execute("ALTER TABLE processing_queue ADD COLUMN normalized_url TEXT")
                await db.execute("ALTER TABLE processing_queue ADD COLUMN processing_strategy TEXT")
                await db.execute("ALTER TABLE processing_queue ADD COLUMN next_retry_at TEXT")
            except aiosqlite.OperationalError:
                # Columns might already exist
                pass

            # Add new columns to content_metadata table
            try:
                await db.execute("ALTER TABLE content_metadata ADD COLUMN url_scheme TEXT")
                await db.execute("ALTER TABLE content_metadata ADD COLUMN url_domain TEXT")
                await db.execute("ALTER TABLE content_metadata ADD COLUMN is_processable BOOLEAN DEFAULT TRUE")
                await db.execute("ALTER TABLE content_metadata ADD COLUMN failure_reason TEXT")
            except aiosqlite.OperationalError:
                # Columns might already exist
                pass

            # Create deduplication index for processable URLs (ignore if fails due to existing data)
            try:
                await db.execute("""
                    CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_processable_url
                    ON content_metadata(source_url) WHERE is_processable = TRUE
                """)
            except Exception as e:
                if "UNIQUE constraint failed" in str(e):
                    logger.warning("⚠️ Skipping unique index creation due to existing data")
                else:
                    raise

            # Create performance indexes for queue operations
            await db.execute("""
                CREATE INDEX IF NOT EXISTS idx_processing_strategy
                ON processing_queue(status, processing_strategy, priority DESC, created_at)
            """)

            await db.execute("""
                CREATE INDEX IF NOT EXISTS idx_retry_timing
                ON processing_queue(retry_count, next_retry_at, status)
                WHERE next_retry_at IS NOT NULL
            """)

            await db.execute("""
                CREATE INDEX IF NOT EXISTS idx_queue_priority_status
                ON processing_queue(status DESC, priority DESC, created_at ASC)
            """)

            await db.commit()

        logger.info("✅ Enhanced queue manager initialized")

    async def enqueue_url(
        self,
        url: str,
        source_name: str,
        content_type: str = "web",
        priority: PriorityLevel = PriorityLevel.NORMAL,
        metadata: Dict[str, Any] = None
    ) -> Tuple[bool, str, Optional[str]]:
        """
        Enqueue a URL for processing with deduplication

        Args:
            url: The URL to enqueue
            source_name: Source name/podcast
            content_type: Type of content
            priority: Processing priority
            metadata: Additional metadata

        Returns:
            (success, message, content_id)
        """
        try:
            # Classify URL
            classification = classify_url(url)

            # Generate content ID
            content_id = generate_content_id(url, source_name)

            # Check if URL is processable
            if not classification.is_processable:
                # Quarantine non-processable URLs immediately
                await quarantine_item(
                    content_id=content_id,
                    source_url=url,
                    source_name=source_name,
                    original_error=f"Non-processable URL: {classification.failure_reason}",
                    classification=classification,
                    notes="Quarantined during enqueue due to non-processable URL"
                )

                return False, f"URL quarantined: {classification.failure_reason}", content_id

            # Check for duplicates
            existing_content_id = await self._check_duplicate(url, classification.normalized_url)
            if existing_content_id:
                logger.info(f"🔄 Duplicate URL detected: {url[:100]}... -> {existing_content_id}")
                return False, f"Duplicate of existing content: {existing_content_id}", existing_content_id

            # Enqueue with enhanced metadata
            await self._enqueue_item(
                content_id=content_id,
                original_url=url,
                normalized_url=classification.normalized_url,
                source_name=source_name,
                content_type=content_type,
                priority=priority.value,
                processing_strategy=classification.processing_strategy,
                metadata=metadata or {}
            )

            logger.info(f"✅ Enqueued {url[:100]}... with priority {priority.value}")
            return True, f"Successfully enqueued with content_id: {content_id}", content_id

        except Exception as e:
            logger.error(f"Error enqueuing URL {url[:100]}...: {e}")
            return False, f"Enqueue error: {str(e)}", None

    async def _check_duplicate(self, original_url: str, normalized_url: str) -> Optional[str]:
        """Check if URL already exists (duplicate detection)"""
        async with aiosqlite.connect(self.db_path) as db:
            # Check original URL first
            cursor = await db.execute("""
                SELECT content_id FROM content_metadata
                WHERE source_url = ? AND is_processable = TRUE
            """, (original_url,))
            result = await cursor.fetchone()
            if result:
                return result[0]

            # Check normalized URL (handles tracking parameters, etc.)
            cursor = await db.execute("""
                SELECT content_id FROM content_metadata
                WHERE source_url = ? AND is_processable = TRUE
            """, (normalized_url,))
            result = await cursor.fetchone()
            if result:
                return result[0]

            return None

    async def _enqueue_item(
        self,
        content_id: str,
        original_url: str,
        normalized_url: str,
        source_name: str,
        content_type: str,
        priority: int,
        processing_strategy: ProcessingStrategy,
        metadata: Dict[str, Any]
    ):
        """Enqueue item in database"""
        now = datetime.now().isoformat()

        async with aiosqlite.connect(self.db_path) as db:
            # Insert into processing queue
            await db.execute("""
                INSERT INTO processing_queue (
                    content_id, source_url, source_name, content_type,
                    status, priority, normalized_url, processing_strategy,
                    metadata_json, created_at, updated_at
                ) VALUES (?, ?, ?, ?, 'pending', ?, ?, ?, ?, ?, ?)
            """, (
                content_id, original_url, source_name, content_type,
                priority, normalized_url, processing_strategy.value,
                json.dumps(metadata), now, now
            ))

            # Insert into content metadata with classification info
            await db.execute("""
                INSERT OR IGNORE INTO content_metadata (
                    content_id, source_url, source_name, content_type,
                    title, url_scheme, url_domain, is_processable,
                    metadata_json, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                content_id, original_url, source_name, content_type,
                metadata.get('title', ''),
                original_url.split('://')[0] if '://' in original_url else 'unknown',
                self._extract_domain(original_url),
                True,  # Processable URLs are marked as such
                json.dumps(metadata),
                now, now
            ))

            await db.commit()

    def _extract_domain(self, url: str) -> str:
        """Extract domain from URL"""
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            return parsed.netloc.lower() if parsed.netloc else 'unknown'
        except:
            return 'unknown'

    async def get_next_batch(
        self,
        limit: int = None,
        processing_strategy: ProcessingStrategy = None
    ) -> List[QueueItem]:
        """Get next batch of items for processing"""
        if limit is None:
            limit = self.max_batch_size

        try:
            async with aiosqlite.connect(self.db_path) as db:
                db.row_factory = aiosqlite.Row

                # Build query with conditions
                conditions = ["status = 'pending'"]
                params = []

                if processing_strategy:
                    conditions.append("processing_strategy = ?")
                    params.append(processing_strategy.value)

                # Check for retry timing
                conditions.append("(next_retry_at IS NULL OR next_retry_at <= ?)")
                params.append(datetime.now().isoformat())

                query = f"""
                    SELECT * FROM processing_queue
                    WHERE {' AND '.join(conditions)}
                    ORDER BY priority DESC, created_at ASC
                    LIMIT ?
                """
                params.append(limit)

                cursor = await db.execute(query, params)
                rows = await cursor.fetchall()

                # Convert to QueueItem objects
                items = []
                for row in rows:
                    item = QueueItem(
                        content_id=row['content_id'],
                        source_url=row['source_url'],
                        normalized_url=row['normalized_url'] if row['normalized_url'] else row['source_url'],
                        source_name=row['source_name'],
                        content_type=row['content_type'],
                        priority=row['priority'],
                        status=QueueStatus(row['status']),
                        retry_count=row['retry_count'],
                        processing_strategy=ProcessingStrategy(row['processing_strategy'] if row['processing_strategy'] else 'http_content'),
                        metadata=json.loads(row['metadata_json']) if row['metadata_json'] else {},
                        created_at=row['created_at'],
                        updated_at=row['updated_at'],
                        started_at=row['started_at'],
                        completed_at=row['completed_at'],
                        next_retry_at=row['next_retry_at']
                    )
                    items.append(item)

                # Mark items as processing
                if items:
                    await self._mark_items_processing([item.content_id for item in items])

                return items

        except Exception as e:
            logger.error(f"Error getting next batch: {e}")
            return []

    async def _mark_items_processing(self, content_ids: List[str]):
        """Mark items as processing"""
        if not content_ids:
            return

        now = datetime.now().isoformat()
        placeholders = ','.join(['?' for _ in content_ids])

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(f"""
                UPDATE processing_queue
                SET status = 'processing', started_at = ?, updated_at = ?
                WHERE content_id IN ({placeholders})
            """, [now, now] + content_ids)

            await db.commit()

    async def update_item_status(
        self,
        content_id: str,
        status: QueueStatus,
        error_message: str = None,
        retry_delay_minutes: int = None
    ):
        """Update item status with intelligent retry logic"""
        now = datetime.now().isoformat()

        async with aiosqlite.connect(self.db_path) as db:
            if status == QueueStatus.COMPLETED:
                await db.execute("""
                    UPDATE processing_queue
                    SET status = ?, completed_at = ?, updated_at = ?
                    WHERE content_id = ?
                """, (status.value, now, now, content_id))

            elif status == QueueStatus.FAILED:
                # Check if should retry
                cursor = await db.execute("""
                    SELECT retry_count FROM processing_queue WHERE content_id = ?
                """, (content_id,))
                retry_count = (await cursor.fetchone())[0]

                if retry_count < 3:  # Max 3 retries
                    # Schedule retry with exponential backoff
                    delay_minutes = retry_delay_minutes or (5 * (2 ** retry_count))  # 5, 10, 20 minutes
                    retry_at = datetime.now() + timedelta(minutes=delay_minutes)

                    await db.execute("""
                        UPDATE processing_queue
                        SET status = 'retry', retry_count = retry_count + 1,
                            next_retry_at = ?, updated_at = ?, failure_reason = ?
                        WHERE content_id = ?
                    """, (retry_at.isoformat(), now, error_message, content_id))
                else:
                    # Max retries reached, mark as permanently failed
                    await db.execute("""
                        UPDATE processing_queue
                        SET status = 'failed', updated_at = ?, failure_reason = ?
                        WHERE content_id = ?
                    """, (now, f"Max retries reached: {error_message}", content_id))

            elif status == QueueStatus.PROCESSING:
                await db.execute("""
                    UPDATE processing_queue
                    SET status = ?, started_at = ?, updated_at = ?
                    WHERE content_id = ?
                """, (status.value, now, now, content_id))

            else:
                await db.execute("""
                    UPDATE processing_queue
                    SET status = ?, updated_at = ?, failure_reason = ?
                    WHERE content_id = ?
                """, (status.value, now, error_message, content_id))

            await db.commit()

    async def get_queue_stats(self) -> Dict[str, Any]:
        """Get comprehensive queue statistics"""
        async with aiosqlite.connect(self.db_path) as db:
            # Basic status counts
            cursor = await db.execute("""
                SELECT status, COUNT(*) as count
                FROM processing_queue
                GROUP BY status
            """)
            status_counts = dict(await cursor.fetchall())

            # Processing strategy counts
            cursor = await db.execute("""
                SELECT processing_strategy, COUNT(*) as count
                FROM processing_queue
                WHERE status = 'pending'
                GROUP BY processing_strategy
            """)
            strategy_counts = dict(await cursor.fetchall())

            # Priority distribution
            cursor = await db.execute("""
                SELECT
                    CASE
                        WHEN priority >= 80 THEN 'high'
                        WHEN priority >= 50 THEN 'normal'
                        ELSE 'low'
                    END as priority_level,
                    COUNT(*) as count
                FROM processing_queue
                WHERE status = 'pending'
                GROUP BY priority_level
            """)
            priority_distribution = dict(await cursor.fetchall())

            # Age analysis
            cursor = await db.execute("""
                SELECT
                    CASE
                        WHEN created_at > datetime('now', '-1 hour') THEN 'hour'
                        WHEN created_at > datetime('now', '-1 day') THEN 'day'
                        WHEN created_at > datetime('now', '-1 week') THEN 'week'
                        ELSE 'older'
                    END as age_bucket,
                    COUNT(*) as count
                FROM processing_queue
                WHERE status = 'pending'
                GROUP BY age_bucket
            """)
            age_distribution = dict(await cursor.fetchall())

            # Processing rate (last hour)
            cursor = await db.execute("""
                SELECT COUNT(*) as count
                FROM processing_queue
                WHERE status = 'completed'
                AND completed_at > datetime('now', '-1 hour')
            """)
            processing_rate = (await cursor.fetchone())[0]

            # Queue pressure
            cursor = await db.execute("""
                SELECT COUNT(*) as count
                FROM processing_queue
                WHERE status IN ('pending', 'retry')
            """)
            pending_count = (await cursor.fetchone())[0]

            return {
                'status_counts': status_counts,
                'strategy_counts': strategy_counts,
                'priority_distribution': priority_distribution,
                'age_distribution': age_distribution,
                'processing_rate_per_hour': processing_rate,
                'pending_count': pending_count,
                'backpressure_active': pending_count > self.backpressure_threshold,
                'queue_health': self._calculate_queue_health(status_counts, processing_rate, pending_count)
            }

    def _calculate_queue_health(self, status_counts: Dict[str, int], processing_rate: int, pending_count: int) -> str:
        """Calculate overall queue health score"""
        # Base score
        health_score = 100

        # Penalize high pending count
        if pending_count > 1000:
            health_score -= 30
        elif pending_count > 500:
            health_score -= 15
        elif pending_count > 100:
            health_score -= 5

        # Penalize low processing rate
        if processing_rate == 0:
            health_score -= 50
        elif processing_rate < 10:
            health_score -= 25
        elif processing_rate < 30:
            health_score -= 10

        # Penalize high failure count
        failed_count = status_counts.get('failed', 0)
        if failed_count > 100:
            health_score -= 20
        elif failed_count > 50:
            health_score -= 10
        elif failed_count > 10:
            health_score -= 5

        # Determine health category
        if health_score >= 80:
            return "excellent"
        elif health_score >= 60:
            return "good"
        elif health_score >= 40:
            return "fair"
        elif health_score >= 20:
            return "poor"
        else:
            return "critical"

    async def cleanup_old_items(self, days_ago: int = 30) -> Dict[str, int]:
        """Clean up old completed and failed items"""
        cutoff_date = datetime.now() - timedelta(days=days_ago)

        async with aiosqlite.connect(self.db_path) as db:
            # Delete old completed items
            cursor = await db.execute("""
                DELETE FROM processing_queue
                WHERE status = 'completed' AND completed_at < ?
            """, (cutoff_date.isoformat(),))
            completed_deleted = cursor.rowcount

            # Delete old failed items (keep dead letter queue records)
            cursor = await db.execute("""
                DELETE FROM processing_queue
                WHERE status = 'failed' AND updated_at < ?
            """, (cutoff_date.isoformat(),))
            failed_deleted = cursor.rowcount

            await db.commit()

            logger.info(f"🧹 Cleaned up {completed_deleted} completed and {failed_deleted} failed items")

            return {
                'completed_deleted': completed_deleted,
                'failed_deleted': failed_deleted,
                'total_deleted': completed_deleted + failed_deleted
            }

# Global queue manager instance
_queue_manager = EnhancedQueueManager()

async def initialize_queue():
    """Initialize enhanced queue manager"""
    await _queue_manager.initialize()

async def enqueue_url(
    url: str,
    source_name: str,
    content_type: str = "web",
    priority: PriorityLevel = PriorityLevel.NORMAL,
    metadata: Dict[str, Any] = None
) -> Tuple[bool, str, Optional[str]]:
    """Enqueue URL with deduplication"""
    return await _queue_manager.enqueue_url(url, source_name, content_type, priority, metadata)

async def get_next_batch(limit: int = 50) -> List[QueueItem]:
    """Get next batch of items for processing"""
    return await _queue_manager.get_next_batch(limit)

async def get_queue_stats() -> Dict[str, Any]:
    """Get queue statistics"""
    return await _queue_manager.get_queue_stats()

async def update_item_status(
    content_id: str,
    status: QueueStatus,
    error_message: str = None,
    retry_delay_minutes: int = None
):
    """Update item status with intelligent retry logic"""
    return await _queue_manager.update_item_status(content_id, status, error_message, retry_delay_minutes)