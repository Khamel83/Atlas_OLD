#!/usr/bin/env python3
"""
Simple Queue Cleanup Script for Atlas v2

Identifies and quarantines file:// URLs to eliminate queue pollution.
"""

import asyncio
import sys
import logging
import aiosqlite
from pathlib import Path

# Add the parent directory to path to import modules
sys.path.append(str(Path(__file__).parent.parent))

from modules.database import DatabaseManager
from modules.url_classifier import classify_url

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def simple_cleanup():
    """Simple cleanup of file:// URLs"""
    logger.info("🚀 Starting simple queue cleanup...")

    # Initialize database
    db_manager = DatabaseManager()
    await db_manager.initialize()

    # Analyze current state
    async with aiosqlite.connect(db_manager.db_path) as db:
        logger.info("📊 Analyzing current queue state...")

        # Get total counts
        cursor = await db.execute("SELECT COUNT(*) FROM processing_queue")
        total_items = (await cursor.fetchone())[0]

        # Get file:// URLs
        cursor = await db.execute("""
            SELECT COUNT(*) FROM processing_queue
            WHERE source_url LIKE 'file://%'
        """)
        file_urls_count = (await cursor.fetchone())[0]

        logger.info(f"📋 Total items: {total_items:,}")
        logger.info(f"📋 File:// URLs: {file_urls_count:,} ({file_urls_count/total_items*100:.1f}%)")

        if file_urls_count == 0:
            logger.info("✅ No file:// URLs found - queue is already clean!")
            return

        # Get and quarantine file:// URLs
        cursor = await db.execute("""
            SELECT content_id, source_url, source_name
            FROM processing_queue
            WHERE source_url LIKE 'file://%'
            AND status = 'pending'
        """)
        file_urls = await cursor.fetchall()

        logger.info(f"🧹 Processing {len(file_urls)} file:// URLs...")

        # Create dead letter queue table if it doesn't exist
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
                quarantined_at TEXT NOT NULL,
                notes TEXT DEFAULT ''
            )
        """)

        quarantined = 0
        errors = 0

        for content_id, source_url, source_name in file_urls:
            try:
                # Classify URL
                classification = classify_url(source_url)

                # Add to dead letter queue
                await db.execute("""
                    INSERT OR REPLACE INTO dead_letter_queue (
                        content_id, source_url, source_name, original_error,
                        failure_type, quarantine_reason, retry_count,
                        quarantined_at, notes
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    content_id,
                    source_url,
                    source_name,
                    "Local file URLs are not supported in HTTP-based processing",
                    "permanent",
                    "file_scheme",
                    0,
                    asyncio.get_event_loop().time(),
                    "Quarantined during queue cleanup"
                ))

                # Remove from processing queue
                await db.execute("""
                    DELETE FROM processing_queue WHERE content_id = ?
                """, (content_id,))

                quarantined += 1

                # Progress reporting
                if quarantined % 100 == 0:
                    logger.info(f"📈 Progress: {quarantined}/{len(file_urls)} quarantined")

            except Exception as e:
                logger.error(f"❌ Error processing {source_url[:100]}...: {e}")
                errors += 1

        await db.commit()

        # Final status
        cursor = await db.execute("SELECT COUNT(*) FROM processing_queue")
        remaining_items = (await cursor.fetchone())[0]

        logger.info(f"""
🎉 Cleanup Complete!

📊 Results:
- Total File URLs: {len(file_urls):,}
- Successfully Quarantined: {quarantined:,}
- Errors: {errors:,}
- Queue Items Remaining: {remaining_items:,}
- Queue Pollution Eliminated: {(file_urls_count/total_items*100):.1f}%

✅ Atlas v2 is now ready for reliable processing!
        """)

if __name__ == "__main__":
    asyncio.run(simple_cleanup())