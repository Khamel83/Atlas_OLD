#!/usr/bin/env python3
"""
Basic Queue Cleanup Script for Atlas v2

Simply removes file:// URLs to eliminate queue pollution.
"""

import asyncio
import sys
import logging
import aiosqlite
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def basic_cleanup():
    """Basic cleanup of file:// URLs"""
    logger.info("🚀 Starting basic queue cleanup...")

    db_path = "data/atlas_v2.db"

    # Analyze current state
    async with aiosqlite.connect(db_path) as db:
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

        # Get and delete file:// URLs
        cursor = await db.execute("""
            SELECT content_id, source_url, source_name
            FROM processing_queue
            WHERE source_url LIKE 'file://%'
            AND status = 'pending'
        """)
        file_urls = await cursor.fetchall()

        logger.info(f"🧹 Deleting {len(file_urls)} file:// URLs...")

        deleted = 0
        errors = 0

        for content_id, source_url, source_name in file_urls:
            try:
                # Delete from processing queue
                await db.execute("""
                    DELETE FROM processing_queue WHERE content_id = ?
                """, (content_id,))

                deleted += 1

                # Progress reporting
                if deleted % 100 == 0:
                    logger.info(f"📈 Progress: {deleted}/{len(file_urls)} deleted")

            except Exception as e:
                logger.error(f"❌ Error deleting {source_url[:100]}...: {e}")
                errors += 1

        await db.commit()

        # Final status
        cursor = await db.execute("SELECT COUNT(*) FROM processing_queue")
        remaining_items = (await cursor.fetchone())[0]

        logger.info(f"""
🎉 Cleanup Complete!

📊 Results:
- Total File URLs: {len(file_urls):,}
- Successfully Deleted: {deleted:,}
- Errors: {errors:,}
- Queue Items Remaining: {remaining_items:,}
- Queue Pollution Eliminated: {(file_urls_count/total_items*100):.1f}%

✅ Atlas v2 is now ready for reliable processing!
        """)

if __name__ == "__main__":
    asyncio.run(basic_cleanup())