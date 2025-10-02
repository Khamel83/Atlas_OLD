#!/usr/bin/env python3
"""
Atlas Backlog Recovery Script
Reprocess completed items that lack processed_content entries to recover their actual content

This fixes the massive backlog where 32,793 items were marked as "completed"
but never had their content actually stored in the processed_content table.
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, Any, List
import aiosqlite
import sys
sys.path.append('.')

from modules.database import DatabaseManager
from modules.real_content_processor import RealContentProcessor
from modules.config_manager import ConfigManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BacklogRecovery:
    """Recover content from completed items that lack processed_content entries"""

    def __init__(self, db_manager: DatabaseManager, config_manager: ConfigManager):
        self.db_manager = db_manager
        self.config_manager = config_manager
        self.stats = {
            'total_backlog': 0,
            'processed': 0,
            'successful': 0,
            'failed': 0,
            'already_have_content': 0,
            'errors': []
        }

    async def analyze_backlog(self) -> Dict[str, Any]:
        """Analyze the backlog size and composition"""
        logger.info("🔍 Analyzing backlog...")

        query = """
        SELECT
            pq.source_name,
            pq.content_type,
            COUNT(*) as count,
            MIN(pq.created_at) as oldest,
            MAX(pq.created_at) as newest
        FROM processing_queue pq
        LEFT JOIN processed_content pc ON pq.content_id = pc.content_id
        WHERE pq.status = 'completed' AND pc.content_id IS NULL
        GROUP BY pq.source_name, pq.content_type
        ORDER BY count DESC
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(query)
            results = await cursor.fetchall()

        analysis = {
            'total_backlog': 0,
            'by_source': {},
            'by_type': {},
            'details': []
        }

        for row in results:
            source, content_type, count, oldest, newest = row
            analysis['total_backlog'] += count
            analysis['by_source'][source] = analysis['by_source'].get(source, 0) + count
            analysis['by_type'][content_type] = analysis['by_type'].get(content_type, 0) + count

            analysis['details'].append({
                'source': source,
                'content_type': content_type,
                'count': count,
                'oldest': oldest,
                'newest': newest
            })

        self.stats['total_backlog'] = analysis['total_backlog']
        return analysis

    async def get_backlog_items(self, limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
        """Get items from the backlog to process"""
        query = """
        SELECT
            pq.content_id,
            pq.source_url,
            pq.source_name,
            pq.content_type,
            pq.metadata_json
        FROM processing_queue pq
        LEFT JOIN processed_content pc ON pq.content_id = pc.content_id
        WHERE pq.status = 'completed' AND pc.content_id IS NULL
        ORDER BY pq.created_at ASC
        LIMIT ? OFFSET ?
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(query, (limit, offset))
            results = await cursor.fetchall()

        items = []
        for row in results:
            content_id, source_url, source_name, content_type, metadata_json = row
            items.append({
                'content_id': content_id,
                'source_url': source_url,
                'source_name': source_name,
                'content_type': content_type,
                'metadata_json': metadata_json
            })

        return items

    async def process_backlog_item(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Process a single backlog item"""
        content_id = item['content_id']
        source_url = item['source_url']
        source_name = item['source_name']
        content_type = item['content_type']

        try:
            logger.info(f"🔄 Reprocessing: {content_id} ({source_url})")

            # Check if content already exists (in case another process got to it)
            async with aiosqlite.connect(self.db_manager.db_path) as db:
                cursor = await db.execute(
                    "SELECT COUNT(*) FROM processed_content WHERE content_id = ?",
                    (content_id,)
                )
                if (await cursor.fetchone())[0] > 0:
                    logger.info(f"✅ Content already exists: {content_id}")
                    self.stats['already_have_content'] += 1
                    return {"status": "already_exists", "content_id": content_id}

            # Use the RealContentProcessor to extract and store content
            async with RealContentProcessor(self.db_manager, self.config_manager) as processor:
                result = await processor.process_content(content_id)

            # Check if processing was successful
            async with aiosqlite.connect(self.db_manager.db_path) as db:
                cursor = await db.execute(
                    "SELECT COUNT(*) FROM processed_content WHERE content_id = ?",
                    (content_id,)
                )
                content_exists = (await cursor.fetchone())[0] > 0

            if content_exists:
                logger.info(f"✅ Successfully recovered content: {content_id}")
                self.stats['successful'] += 1
                return {"status": "success", "content_id": content_id}
            else:
                logger.warning(f"⚠️ Processing completed but no content stored: {content_id}")
                self.stats['failed'] += 1
                return {"status": "failed_no_content", "content_id": content_id}

        except Exception as e:
            logger.error(f"❌ Failed to reprocess {content_id}: {e}")
            self.stats['failed'] += 1
            self.stats['errors'].append(f"{content_id}: {str(e)}")
            return {"status": "error", "content_id": content_id, "error": str(e)}

        finally:
            self.stats['processed'] += 1

    async def process_backlog_batch(self, batch_size: int = 50, max_batches: int = None) -> Dict[str, Any]:
        """Process backlog in batches"""
        logger.info(f"🚀 Starting backlog recovery (batch_size: {batch_size})")

        start_time = datetime.now()
        batch_count = 0
        items_processed = 0

        while True:
            # Check if we've reached max batches
            if max_batches and batch_count >= max_batches:
                logger.info(f"Reached maximum batch limit ({max_batches})")
                break

            # Get next batch
            items = await self.get_backlog_items(limit=batch_size, offset=items_processed)
            if not items:
                logger.info("No more items to process")
                break

            logger.info(f"📦 Processing batch {batch_count + 1}: {len(items)} items")
            batch_count += 1

            # Process batch items concurrently (but limit concurrency)
            semaphore = asyncio.Semaphore(5)  # Max 5 concurrent processing
            async def process_with_semaphore(item):
                async with semaphore:
                    return await self.process_backlog_item(item)

            batch_results = await asyncio.gather(
                *[process_with_semaphore(item) for item in items],
                return_exceptions=True
            )

            # Count successful results in this batch
            batch_successful = sum(1 for result in batch_results
                                 if isinstance(result, dict) and result.get("status") == "success")
            batch_failed = sum(1 for result in batch_results
                             if isinstance(result, dict) and result.get("status") != "success")

            logger.info(f"📊 Batch {batch_count} results: {batch_successful} successful, {batch_failed} failed")

            items_processed += len(items)

            # Small delay between batches to prevent overwhelming
            await asyncio.sleep(0.1)

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        final_report = {
            'stats': self.stats,
            'items_processed': items_processed,
            'batches_processed': batch_count,
            'duration_seconds': round(duration, 2),
            'items_per_second': round(items_processed / duration, 2) if duration > 0 else 0,
            'timestamp': end_time.isoformat()
        }

        logger.info(f"✅ Backlog recovery complete: {final_report['stats']['successful']} successful, "
                   f"{final_report['stats']['failed']} failed in {duration:.1f}s")

        return final_report

    async def estimate_completion_time(self, items_processed: int, duration_seconds: float) -> Dict[str, Any]:
        """Estimate completion time for remaining items"""
        if items_processed == 0 or duration_seconds == 0:
            return {"estimated_hours": "unknown", "items_per_hour": 0}

        items_per_hour = (items_processed / duration_seconds) * 3600
        remaining_items = self.stats['total_backlog'] - items_processed
        estimated_hours = remaining_items / items_per_hour if items_per_hour > 0 else float('inf')

        return {
            "items_per_hour": round(items_per_hour, 1),
            "remaining_items": remaining_items,
            "estimated_hours": round(estimated_hours, 1)
        }

async def main():
    """Main backlog recovery process"""
    logger.info("🚀 Atlas Backlog Recovery Started")

    db_manager = DatabaseManager()
    await db_manager.initialize()

    try:
        config_manager = ConfigManager()
        recovery = BacklogRecovery(db_manager, config_manager)

        # First analyze the backlog
        analysis = await recovery.analyze_backlog()
        logger.info(f"📊 Found {analysis['total_backlog']} items in backlog needing recovery")

        print(f"\n📋 BACKLOG ANALYSIS:")
        print(f"🔢 Total items needing recovery: {analysis['total_backlog']}")
        print(f"📂 By source: {analysis['by_source']}")
        print(f"📝 By type: {analysis['by_type']}")

        if analysis['total_backlog'] == 0:
            print("✅ No backlog items found - everything is already processed!")
            return

        # Process first batch to test
        print(f"\n🧪 Processing first batch to test recovery...")
        first_batch_report = await recovery.process_backlog_batch(batch_size=10, max_batches=1)

        # Estimate completion time
        if first_batch_report['items_processed'] > 0:
            time_estimate = await recovery.estimate_completion_time(
                first_batch_report['items_processed'],
                first_batch_report['duration_seconds']
            )
            print(f"\n⏱️ COMPLETION ESTIMATE:")
            print(f"📈 Processing rate: {time_estimate['items_per_hour']} items/hour")
            print(f"🕐 Estimated time: {time_estimate['estimated_hours']} hours")
            print(f"📊 Remaining items: {time_estimate['remaining_items']}")

            # Ask for confirmation for full processing
            if time_estimate['estimated_hours'] > 1:
                print(f"\n⚠️ This will take approximately {time_estimate['estimated_hours']:.1f} hours")
                print("💡 Consider running in background or in smaller batches")

                # For now, just show the analysis and first batch results
                print(f"\n🎯 FIRST BATCH RESULTS:")
                print(f"✅ Successful: {first_batch_report['stats']['successful']}")
                print(f"❌ Failed: {first_batch_report['stats']['failed']}")
                print(f"⏱️ Duration: {first_batch_report['duration_seconds']:.1f}s")
                print(f"📈 Rate: {first_batch_report['items_per_second']:.1f} items/second")

                print(f"\n💡 To continue full recovery, run with --full flag")
                return

        # If --full flag provided, process all items
        if '--full' in sys.argv:
            print(f"\n🚀 PROCESSING FULL BACKLOG...")
            final_report = await recovery.process_backlog_batch(batch_size=50)

            print(f"\n🎯 FINAL RESULTS:")
            print(f"✅ Successfully recovered: {final_report['stats']['successful']}")
            print(f"❌ Failed to recover: {final_report['stats']['failed']}")
            print(f"📊 Items processed: {final_report['items_processed']}")
            print(f"📦 Batches: {final_report['batches_processed']}")
            print(f"⏱️ Total duration: {final_report['duration_seconds']:.1f}s")
            print(f"📈 Overall rate: {final_report['items_per_second']:.1f} items/second")

            # Save report
            with open('backlog_recovery_report.json', 'w') as f:
                import json
                json.dump(final_report, f, indent=2)

            print(f"📄 Detailed report saved to: backlog_recovery_report.json")

    finally:
        await db_manager.close()

if __name__ == "__main__":
    asyncio.run(main())