"""
Database Manager for Atlas v2

Handles all database operations:
- SQLite database initialization and schema
- Content CRUD operations
- Queue management
- Processing logs
- Migration support

Design principles:
- Never lose data
- Async operations
- Comprehensive logging
- Backward compatibility
"""

import asyncio
import sqlite3
import aiosqlite
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    """Manages all database operations for Atlas v2"""

    def __init__(self, db_path: str = "data/atlas_v2.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    async def initialize(self):
        """Initialize database with required tables"""
        logger.info("🗄️ Initializing Atlas v2 database...")

        async with aiosqlite.connect(self.db_path) as db:
            # Content metadata table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS content_metadata (
                    content_id TEXT PRIMARY KEY,
                    source_url TEXT NOT NULL,
                    source_name TEXT NOT NULL,
                    content_type TEXT NOT NULL,
                    title TEXT,
                    validation_status TEXT DEFAULT 'pending',
                    quality_score REAL DEFAULT 0.0,
                    word_count INTEGER DEFAULT 0,
                    extraction_method TEXT,
                    metadata_json TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """)

            # Processing queue table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS processing_queue (
                    content_id TEXT PRIMARY KEY,
                    source_url TEXT NOT NULL,
                    source_name TEXT NOT NULL,
                    content_type TEXT NOT NULL,
                    status TEXT DEFAULT 'pending',
                    priority TEXT DEFAULT 'normal',
                    retry_count INTEGER DEFAULT 0,
                    metadata_json TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    started_at TEXT,
                    completed_at TEXT,
                    FOREIGN KEY (content_id) REFERENCES content_metadata(content_id)
                )
            """)

            # Processing logs table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS processing_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content_id TEXT NOT NULL,
                    operation TEXT NOT NULL,
                    status TEXT NOT NULL,
                    message TEXT,
                    details_json TEXT,
                    duration_seconds REAL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (content_id) REFERENCES content_metadata(content_id)
                )
            """)

            # Legacy migration tracking
            await db.execute("""
                CREATE TABLE IF NOT EXISTS migration_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    legacy_id TEXT,
                    legacy_url TEXT,
                    new_content_id TEXT,
                    migration_status TEXT,
                    migration_notes TEXT,
                    migrated_at TEXT NOT NULL
                )
            """)

            # Create indexes for performance
            await db.execute("CREATE INDEX IF NOT EXISTS idx_content_source ON content_metadata(source_name)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_content_type ON content_metadata(content_type)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_queue_status ON processing_queue(status)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_queue_priority ON processing_queue(priority)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_log_content_id ON processing_log(content_id)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_log_timestamp ON processing_log(timestamp DESC)")

            await db.commit()

        logger.info("✅ Database initialization complete")

    async def content_exists(self, content_id: str) -> bool:
        """Check if content already exists"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "SELECT 1 FROM content_metadata WHERE content_id = ?",
                (content_id,)
            )
            result = await cursor.fetchone()
            return result is not None

    async def url_exists(self, url: str) -> Optional[str]:
        """Check if URL already processed, return content_id if exists"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute(
                "SELECT content_id FROM content_metadata WHERE source_url = ?",
                (url,)
            )
            result = await cursor.fetchone()
            return result[0] if result else None

    async def enqueue_content(
        self,
        content_id: str,
        source_url: str,
        source_name: str,
        content_type: str,
        metadata: Dict[str, Any],
        priority: str = 'normal'
    ):
        """Add content to processing queue"""
        now = datetime.now().isoformat()

        async with aiosqlite.connect(self.db_path) as db:
            # Insert into queue
            await db.execute("""
                INSERT INTO processing_queue (
                    content_id, source_url, source_name, content_type,
                    status, priority, metadata_json, created_at, updated_at
                ) VALUES (?, ?, ?, ?, 'pending', ?, ?, ?, ?)
            """, (
                content_id, source_url, source_name, content_type,
                priority, json.dumps(metadata), now, now
            ))

            # Also create metadata record
            await db.execute("""
                INSERT OR IGNORE INTO content_metadata (
                    content_id, source_url, source_name, content_type,
                    title, metadata_json, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                content_id, source_url, source_name, content_type,
                metadata.get('title', ''), json.dumps(metadata), now, now
            ))

            await db.commit()

        await self.log_operation(content_id, 'enqueue', 'success', f"Queued for processing (priority: {priority})")

    async def update_queue_status(self, content_id: str, status: str):
        """Update processing queue status"""
        now = datetime.now().isoformat()

        async with aiosqlite.connect(self.db_path) as db:
            # Update status and timestamp
            if status == 'processing':
                await db.execute("""
                    UPDATE processing_queue
                    SET status = ?, started_at = ?, updated_at = ?
                    WHERE content_id = ?
                """, (status, now, now, content_id))
            elif status in ['completed', 'failed']:
                await db.execute("""
                    UPDATE processing_queue
                    SET status = ?, completed_at = ?, updated_at = ?
                    WHERE content_id = ?
                """, (status, now, now, content_id))
            elif status == 'retry':
                # Increment retry count
                await db.execute("""
                    UPDATE processing_queue
                    SET status = 'pending', retry_count = retry_count + 1, updated_at = ?
                    WHERE content_id = ?
                """, (now, content_id))
            else:
                await db.execute("""
                    UPDATE processing_queue
                    SET status = ?, updated_at = ?
                    WHERE content_id = ?
                """, (status, now, content_id))

            await db.commit()

    async def get_pending_items(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get pending items for processing"""
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row

            cursor = await db.execute("""
                SELECT * FROM processing_queue
                WHERE status = 'pending' AND retry_count < 3
                ORDER BY priority DESC, created_at ASC
                LIMIT ?
            """, (limit,))

            rows = await cursor.fetchall()
            return [dict(row) for row in rows]

    async def get_queue_size(self) -> Dict[str, int]:
        """Get queue size by status"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("""
                SELECT status, COUNT(*) as count
                FROM processing_queue
                GROUP BY status
            """)
            rows = await cursor.fetchall()
            return {row[0]: row[1] for row in rows}

    async def store_processed_content(
        self,
        content_id: str,
        extracted_content: str,
        validation_result: Dict[str, Any],
        extraction_method: str,
        processing_metadata: Dict[str, Any] = None
    ):
        """Store successfully processed content"""
        now = datetime.now().isoformat()

        # Save content to file
        content_dir = Path("content/processed")
        content_dir.mkdir(parents=True, exist_ok=True)

        # Save markdown file
        markdown_path = content_dir / f"{content_id}.md"
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(extracted_content)

        # Save metadata JSON
        metadata_path = content_dir / f"{content_id}.json"
        full_metadata = {
            "content_id": content_id,
            "extraction_method": extraction_method,
            "validation": validation_result,
            "processing_metadata": processing_metadata or {},
            "processed_at": now,
            "content_length": len(extracted_content),
            "file_path": str(markdown_path)
        }

        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(full_metadata, f, indent=2, ensure_ascii=False)

        # Update database
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                UPDATE content_metadata
                SET validation_status = ?, quality_score = ?, word_count = ?,
                    extraction_method = ?, updated_at = ?
                WHERE content_id = ?
            """, (
                validation_result['status'],
                validation_result.get('score', 0.0),
                len(extracted_content.split()),
                extraction_method,
                now,
                content_id
            ))

            await db.commit()

        await self.log_operation(
            content_id, 'store', 'success',
            f"Content stored: {len(extracted_content)} chars, validation: {validation_result['status']}",
            {"file_path": str(markdown_path), "validation": validation_result}
        )

    async def log_operation(
        self,
        content_id: str,
        operation: str,
        status: str,
        message: str,
        details: Dict[str, Any] = None,
        duration: float = 0.0
    ):
        """Log processing operation"""
        now = datetime.now().isoformat()

        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO processing_log (
                    content_id, operation, status, message,
                    details_json, duration_seconds, timestamp
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                content_id, operation, status, message,
                json.dumps(details) if details else None,
                duration, now
            ))

            await db.commit()

    async def get_processing_stats(self) -> Dict[str, Any]:
        """Get processing statistics"""
        async with aiosqlite.connect(self.db_path) as db:
            # Content counts by type
            cursor = await db.execute("""
                SELECT content_type, COUNT(*) as count
                FROM content_metadata
                GROUP BY content_type
            """)
            content_by_type = dict(await cursor.fetchall())

            # Queue status counts
            cursor = await db.execute("""
                SELECT status, COUNT(*) as count
                FROM processing_queue
                GROUP BY status
            """)
            queue_by_status = dict(await cursor.fetchall())

            # Validation status counts
            cursor = await db.execute("""
                SELECT validation_status, COUNT(*) as count
                FROM content_metadata
                WHERE validation_status IS NOT NULL
                GROUP BY validation_status
            """)
            validation_by_status = dict(await cursor.fetchall())

            # Recent activity (last 24 hours)
            cursor = await db.execute("""
                SELECT operation, status, COUNT(*) as count
                FROM processing_log
                WHERE timestamp > datetime('now', '-1 day')
                GROUP BY operation, status
            """)
            recent_activity = await cursor.fetchall()

            return {
                "content_by_type": content_by_type,
                "queue_by_status": queue_by_status,
                "validation_by_status": validation_by_status,
                "recent_activity": [
                    {"operation": row[0], "status": row[1], "count": row[2]}
                    for row in recent_activity
                ]
            }

    async def get_last_processed_timestamp(self) -> Optional[str]:
        """Get timestamp of last processed item"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("""
                SELECT MAX(completed_at) FROM processing_queue
                WHERE status = 'completed'
            """)
            result = await cursor.fetchone()
            return result[0] if result and result[0] else None

    async def health_check(self) -> bool:
        """Check database health"""
        try:
            async with aiosqlite.connect(self.db_path) as db:
                cursor = await db.execute("SELECT 1")
                await cursor.fetchone()
                return True
        except Exception as e:
            logger.error(f"Database health check failed: {e}")
            return False

    async def migrate_legacy_content(self, legacy_data: List[Dict[str, Any]]) -> Dict[str, int]:
        """Migrate content from legacy Atlas database"""
        logger.info(f"🔄 Starting migration of {len(legacy_data)} legacy items...")

        migrated_count = 0
        skipped_count = 0
        error_count = 0

        async with aiosqlite.connect(self.db_path) as db:
            for item in legacy_data:
                try:
                    # Generate new content ID
                    from .id_generator import generate_id_from_legacy_url

                    legacy_url = item.get('url', '')
                    legacy_source = item.get('source', '')
                    metadata = json.loads(item.get('metadata', '{}')) if item.get('metadata') else {}

                    new_content_id = generate_id_from_legacy_url(legacy_url, legacy_source, metadata)

                    # Check if already migrated
                    if await self.content_exists(new_content_id):
                        skipped_count += 1
                        continue

                    # Insert content metadata
                    now = datetime.now().isoformat()
                    await db.execute("""
                        INSERT INTO content_metadata (
                            content_id, source_url, source_name, content_type,
                            title, validation_status, word_count,
                            metadata_json, created_at, updated_at
                        ) VALUES (?, ?, ?, ?, ?, 'migrated', ?, ?, ?, ?)
                    """, (
                        new_content_id,
                        legacy_url,
                        legacy_source,
                        item.get('content_type', 'unknown'),
                        item.get('title', ''),
                        len(item.get('content', '').split()) if item.get('content') else 0,
                        json.dumps(metadata),
                        item.get('created_at', now),
                        now
                    ))

                    # Log migration
                    await db.execute("""
                        INSERT INTO migration_log (
                            legacy_id, legacy_url, new_content_id,
                            migration_status, migration_notes, migrated_at
                        ) VALUES (?, ?, ?, 'success', 'Auto-migrated from legacy Atlas', ?)
                    """, (
                        item.get('id'),
                        legacy_url,
                        new_content_id,
                        now
                    ))

                    # Save content file if available
                    if item.get('content') and len(item['content']) > 1000:
                        content_dir = Path("content/processed")
                        content_dir.mkdir(parents=True, exist_ok=True)

                        markdown_path = content_dir / f"{new_content_id}.md"
                        with open(markdown_path, 'w', encoding='utf-8') as f:
                            f.write(item['content'])

                    migrated_count += 1

                except Exception as e:
                    logger.error(f"Migration error for {item.get('url', 'unknown')}: {e}")
                    error_count += 1

            await db.commit()

        logger.info(f"✅ Migration complete: {migrated_count} migrated, {skipped_count} skipped, {error_count} errors")

        return {
            "migrated": migrated_count,
            "skipped": skipped_count,
            "errors": error_count
        }

    async def get_content_details(self, content_id: str) -> Optional[Dict[str, Any]]:
        """Get content details for processing"""
        async with aiosqlite.connect(self.db_path) as db:
            cursor = await db.execute("""
                SELECT content_id, source_url, source_name, content_type, title, metadata_json
                FROM content_metadata
                WHERE content_id = ?
            """, (content_id,))

            row = await cursor.fetchone()
            if row:
                return {
                    'content_id': row[0],
                    'source_url': row[1],
                    'source_name': row[2],
                    'content_type': row[3],
                    'title': row[4],
                    'metadata': json.loads(row[5]) if row[5] else {}
                }
            return None

    async def update_content_status(self, content_id: str, status: str, metadata: Dict[str, Any] = None):
        """Update content processing status and metadata"""
        async with aiosqlite.connect(self.db_path) as db:
            # Update processing queue
            await db.execute("""
                UPDATE processing_queue
                SET status = ?, updated_at = ?, completed_at = ?
                WHERE content_id = ?
            """, (status, datetime.now().isoformat(),
                  datetime.now().isoformat() if status == 'completed' else None, content_id))

            # Update content metadata if provided
            if metadata:
                # Get existing metadata
                cursor = await db.execute("""
                    SELECT metadata_json FROM content_metadata WHERE content_id = ?
                """, (content_id,))
                row = await cursor.fetchone()

                existing_meta = json.loads(row[0]) if row and row[0] else {}
                existing_meta.update(metadata)

                await db.execute("""
                    UPDATE content_metadata
                    SET metadata_json = ?, updated_at = ?
                    WHERE content_id = ?
                """, (json.dumps(existing_meta), datetime.now().isoformat(), content_id))

            await db.commit()

    async def close(self):
        """Clean up database connections"""
        # aiosqlite handles connection cleanup automatically
        pass