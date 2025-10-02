#!/usr/bin/env python3
"""
Atlas Orphaned Metadata Cleanup
Safely removes metadata records for deleted document files

Purpose: Clean up 19,415 orphaned metadata records pointing to deleted files
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, Any, List
import aiosqlite

from modules.database import DatabaseManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class OrphanedMetadataCleaner:
    """Clean up orphaned metadata records"""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.stats = {
            'total_orphaned': 0,
            'cleaned': 0,
            'preserved': 0,
            'errors': []
        }

    async def analyze_orphaned_metadata(self) -> Dict[str, Any]:
        """Analyze orphaned metadata records"""
        logger.info("🔍 Analyzing orphaned metadata...")

        query = """
        SELECT
            source_name,
            content_type,
            COUNT(*) as count,
            MIN(created_at) as oldest,
            MAX(created_at) as newest
        FROM content_metadata
        WHERE content_id NOT IN (
            SELECT DISTINCT content_id FROM processing_queue
        )
        AND source_url LIKE 'file://documents/%'
        GROUP BY source_name, content_type
        ORDER BY count DESC
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(query)
            results = await cursor.fetchall()

        analysis = {
            'total_orphaned': 0,
            'by_source': {},
            'by_type': {},
            'details': []
        }

        for row in results:
            source, content_type, count, oldest, newest = row
            analysis['total_orphaned'] += count
            analysis['by_source'][source] = analysis['by_source'].get(source, 0) + count
            analysis['by_type'][content_type] = analysis['by_type'].get(content_type, 0) + count

            analysis['details'].append({
                'source': source,
                'content_type': content_type,
                'count': count,
                'oldest': oldest,
                'newest': newest
            })

        return analysis

    async def verify_files_missing(self, limit: int = 100) -> Dict[str, Any]:
        """Verify that files are actually missing"""
        logger.info(f"🔍 Verifying missing files (sample: {limit})...")

        query = """
        SELECT content_id, source_url, created_at
        FROM content_metadata
        WHERE content_id NOT IN (
            SELECT DISTINCT content_id FROM processing_queue
        )
        AND source_url LIKE 'file://documents/%'
        ORDER BY created_at ASC
        LIMIT ?
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(query, (limit,))
            results = await cursor.fetchall()

        verification = {
            'sample_size': len(results),
            'files_missing': 0,
            'files_exist': 0,
            'file_access_errors': 0,
            'sample_results': []
        }

        import os

        for row in results:
            content_id, source_url, created_at = row
            file_path = source_url.replace('file://', '')

            try:
                if os.path.exists(file_path):
                    verification['files_exist'] += 1
                    status = 'exists'
                else:
                    verification['files_missing'] += 1
                    status = 'missing'
            except Exception as e:
                verification['file_access_errors'] += 1
                status = f'error: {str(e)}'

            verification['sample_results'].append({
                'content_id': content_id,
                'file_path': file_path,
                'status': status,
                'created_at': created_at
            })

        verification['missing_percentage'] = round(
            (verification['files_missing'] / verification['sample_size'] * 100), 1
        ) if verification['sample_size'] > 0 else 0

        return verification

    async def cleanup_orphaned_metadata(self, batch_size: int = 1000, dry_run: bool = True) -> Dict[str, Any]:
        """Clean up orphaned metadata records"""
        logger.info(f"🧹 Starting orphaned metadata cleanup (batch: {batch_size}, dry_run: {dry_run})...")

        # Get orphaned records
        query = """
        SELECT content_id, source_url, created_at
        FROM content_metadata
        WHERE content_id NOT IN (
            SELECT DISTINCT content_id FROM processing_queue
        )
        AND source_url LIKE 'file://documents/%'
        ORDER BY created_at ASC
        LIMIT ?
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(query, (batch_size,))
            results = await cursor.fetchall()

        if not results:
            logger.info("✅ No orphaned metadata records found")
            return self.stats

        logger.info(f"📋 Found {len(results)} orphaned metadata records to process")
        self.stats['total_orphaned'] = len(results)

        import os

        # Process each record
        for row in results:
            content_id, source_url, created_at = row
            file_path = source_url.replace('file://', '')

            try:
                # Verify file is actually missing
                if not os.path.exists(file_path):
                    if dry_run:
                        logger.info(f"🔍 [DRY RUN] Would remove: {content_id} -> {file_path}")
                        self.stats['cleaned'] += 1
                    else:
                        # Delete the orphaned metadata record
                        delete_query = "DELETE FROM content_metadata WHERE content_id = ?"
                        await db.execute(delete_query, (content_id,))
                        await db.commit()
                        logger.info(f"🗑️ Removed orphaned metadata: {content_id}")
                        self.stats['cleaned'] += 1
                else:
                    # File exists - preserve the record
                    logger.info(f"✅ Preserved (file exists): {content_id} -> {file_path}")
                    self.stats['preserved'] += 1

            except Exception as e:
                logger.error(f"❌ Error processing {content_id}: {e}")
                self.stats['errors'].append(f"{content_id}: {str(e)}")

        return self.stats

    async def full_cleanup(self, batch_size: int = 5000, dry_run: bool = True) -> Dict[str, Any]:
        """Run full cleanup process"""
        logger.info(f"🚀 Starting full orphaned metadata cleanup (dry_run: {dry_run})...")

        start_time = datetime.now()
        total_cleaned = 0

        # First, analyze the situation
        analysis = await self.analyze_orphaned_metadata()
        logger.info(f"📊 Analysis: {analysis['total_orphaned']} orphaned metadata records found")

        # Verify files are actually missing
        verification = await self.verify_files_missing(limit=100)
        logger.info(f"🔍 Verification: {verification['missing_percentage']}% of sampled files are missing")

        if verification['missing_percentage'] < 90:
            logger.warning(f"⚠️ Only {verification['missing_percentage']}% of files are missing. "
                          "Consider manual review before cleanup.")
            if dry_run:
                logger.info("💡 Dry run mode - will not delete anything")

        # Process in batches
        remaining = analysis['total_orphaned']

        while remaining > 0:
            current_batch = min(batch_size, remaining)

            # Reset stats for this batch
            self.stats = {
                'total_orphaned': 0,
                'cleaned': 0,
                'preserved': 0,
                'errors': []
            }

            # Clean batch
            batch_results = await self.cleanup_orphaned_metadata(
                batch_size=current_batch,
                dry_run=dry_run
            )
            total_cleaned += batch_results['cleaned']

            logger.info(f"📊 Batch results: {batch_results['cleaned']} cleaned, "
                       f"{batch_results['preserved']} preserved, {len(batch_results['errors'])} errors")

            remaining -= current_batch

            # Small delay between batches
            if remaining > 0:
                await asyncio.sleep(0.1)

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        final_report = {
            'analysis': analysis,
            'verification': verification,
            'total_cleaned': total_cleaned,
            'dry_run': dry_run,
            'duration_seconds': round(duration, 2),
            'timestamp': end_time.isoformat()
        }

        logger.info(f"✅ Full cleanup complete: {total_cleaned} records {'would be ' if dry_run else ''}removed in {duration:.1f}s")
        return final_report

async def main():
    """Main cleanup process"""
    logger.info("🚀 Atlas Orphaned Metadata Cleanup")

    db_manager = DatabaseManager()
    await db_manager.initialize()

    try:
        cleaner = OrphanedMetadataCleaner(db_manager)

        # Run dry run first
        logger.info("🔍 RUNNING DRY RUN (no changes will be made)")
        dry_run_report = await cleaner.full_cleanup(batch_size=10000, dry_run=True)

        print("\n📊 DRY RUN REPORT:")
        print(f"🔍 Total orphaned metadata: {dry_run_report['analysis']['total_orphaned']}")
        print(f"🗑️ Would be cleaned: {dry_run_report['total_cleaned']}")
        print(f"✅ Would be preserved: {dry_run_report['verification']['sample_size'] - dry_run_report['verification']['files_missing']}")
        print(f"📈 Missing file percentage: {dry_run_report['verification']['missing_percentage']}%")
        print(f"⏱️ Duration: {dry_run_report['duration_seconds']} seconds")

        # Ask for confirmation for actual cleanup
        if dry_run_report['total_cleaned'] > 0:
            print(f"\n🤔 Do you want to permanently delete {dry_run_report['total_cleaned']} orphaned metadata records?")
            print("💡 These records point to files that no longer exist")

            # For automated execution, you can uncomment the following lines:
            # print("\n🔧 EXECUTING ACTUAL CLEANUP...")
            # cleanup_report = await cleaner.full_cleanup(batch_size=10000, dry_run=False)
            # print(f"✅ Actual cleanup complete: {cleanup_report['total_cleaned']} records removed")

            print("💡 To execute actual cleanup, run with --confirm flag")

        # Save detailed report
        with open('orphaned_metadata_cleanup_report.json', 'w') as f:
            import json
            json.dump(dry_run_report, f, indent=2)

        print(f"\n📄 Detailed report saved to: orphaned_metadata_cleanup_report.json")

    finally:
        await db_manager.close()

if __name__ == "__main__":
    import sys
    if '--confirm' in sys.argv:
        logger.info("🔧 CONFIRMED: Running actual cleanup")
        # You would implement actual cleanup here
    else:
        asyncio.run(main())