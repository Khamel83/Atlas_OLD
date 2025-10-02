#!/usr/bin/env python3
"""
Atlas Document Recovery Mechanism
Recovers stuck documents by creating processing queue entries for valid content

Purpose: Fix the 19,415 documents stuck in metadata that never reached processing queue
"""

import asyncio
import logging
import json
from datetime import datetime
from typing import Dict, Any, List, Optional
import aiosqlite
import os

from modules.database import DatabaseManager
from modules.enhanced_queue_manager import enqueue_url

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DocumentRecovery:
    """Recover stuck documents from metadata table"""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.stats = {
            'total_stuck': 0,
            'recovered': 0,
            'failed': 0,
            'skipped': 0,
            'errors': []
        }

    async def diagnose_stuck_documents(self) -> Dict[str, Any]:
        """Diagnose the stuck documents issue"""
        logger.info("🔍 Diagnosing stuck documents...")

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
        GROUP BY source_name, content_type
        ORDER BY count DESC
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(query)
            results = await cursor.fetchall()

        diagnosis = {
            'total_stuck': 0,
            'by_source': {},
            'by_type': {},
            'age_analysis': {}
        }

        for row in results:
            source, content_type, count, oldest, newest = row
            diagnosis['total_stuck'] += count

            diagnosis['by_source'][source] = diagnosis['by_source'].get(source, 0) + count
            diagnosis['by_type'][content_type] = diagnosis['by_type'].get(content_type, 0) + count

            if oldest:
                diagnosis['age_analysis'][f"{source}_{content_type}"] = {
                    'count': count,
                    'oldest': oldest,
                    'newest': newest,
                    'days_stuck': (datetime.now() - datetime.fromisoformat(oldest)).days
                }

        return diagnosis

    async def get_stuck_documents(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get stuck documents that need recovery"""
        logger.info(f"📋 Getting stuck documents (limit: {limit})...")

        query = """
        SELECT cm.content_id, cm.source_name, cm.content_type, cm.source_url, cm.metadata_json,
               cm.created_at, cm.validation_status
        FROM content_metadata cm
        WHERE cm.content_id NOT IN (
            SELECT DISTINCT content_id FROM processing_queue
        )
        AND cm.content_type IN ('document', 'transcript', 'article')
        AND cm.source_url LIKE 'file://%'
        ORDER BY cm.created_at ASC
        LIMIT ?
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(query, (limit,))
            results = await cursor.fetchall()

        stuck_docs = []
        for row in results:
            stuck_docs.append({
                'id': row[0],
                'source_name': row[1],
                'content_type': row[2],
                'url': row[3],
                'metadata': json.loads(row[4]) if row[4] else {},
                'created_at': row[5],
                'processing_status': row[6]
            })

        return stuck_docs

    async def validate_document(self, doc: Dict[str, Any]) -> bool:
        """Validate if document is recoverable"""
        try:
            # Check if URL is accessible and valid
            url = doc['url']

            # Must be file:// URL
            if not url.startswith('file://'):
                return False

            # Check if file exists
            import os
            file_path = url.replace('file://', '')
            if not os.path.exists(file_path):
                logger.warning(f"File not found: {file_path}")
                return False

            # Check if file is readable
            if not os.access(file_path, os.R_OK):
                logger.warning(f"File not readable: {file_path}")
                return False

            # Check file size (skip empty files)
            if os.path.getsize(file_path) == 0:
                logger.warning(f"File is empty: {file_path}")
                return False

            return True

        except Exception as e:
            logger.error(f"Error validating document {doc['id']}: {e}")
            return False

    async def recover_document(self, doc: Dict[str, Any]) -> bool:
        """Recover a single document by adding it to processing queue"""
        try:
            # Use enhanced queue manager to add to processing queue
            success, message, content_id = await enqueue_url(
                url=doc['url'],
                source_name=doc['source_name'],
                content_type=doc['content_type'],
                metadata=doc['metadata']
            )

            if success:
                logger.info(f"✅ Recovered document {doc['id']}: {doc['url']}")
                self.stats['recovered'] += 1
                return True
            else:
                logger.warning(f"⚠️ Failed to recover {doc['id']}: {message}")
                self.stats['failed'] += 1
                return False

        except Exception as e:
            logger.error(f"❌ Error recovering document {doc['id']}: {e}")
            self.stats['errors'].append(f"Document {doc['id']}: {str(e)}")
            self.stats['failed'] += 1
            return False

    async def recover_batch(self, batch_size: int = 50) -> Dict[str, Any]:
        """Recover a batch of stuck documents"""
        logger.info(f"🔄 Starting document recovery batch (size: {batch_size})...")

        # Get stuck documents
        stuck_docs = await self.get_stuck_documents(batch_size)

        if not stuck_docs:
            logger.info("✅ No stuck documents found to recover")
            return self.stats

        logger.info(f"📋 Found {len(stuck_docs)} stuck documents to process")
        self.stats['total_stuck'] = len(stuck_docs)

        # Process each document
        for doc in stuck_docs:
            # Validate document
            if not await self.validate_document(doc):
                self.stats['skipped'] += 1
                continue

            # Attempt recovery
            await self.recover_document(doc)

        return self.stats

    async def full_recovery(self, max_documents: int = 1000) -> Dict[str, Any]:
        """Run full recovery process"""
        logger.info(f"🚀 Starting full document recovery (max: {max_documents})...")

        start_time = datetime.now()
        total_recovered = 0

        # First, diagnose the issue
        diagnosis = await self.diagnose_stuck_documents()
        logger.info(f"📊 Diagnosis: {diagnosis['total_stuck']} stuck documents found")

        # Process in batches
        batch_size = 50
        remaining = min(max_documents, diagnosis['total_stuck'])

        while remaining > 0:
            current_batch = min(batch_size, remaining)

            # Reset stats for this batch
            self.stats = {
                'total_stuck': 0,
                'recovered': 0,
                'failed': 0,
                'skipped': 0,
                'errors': []
            }

            # Recover batch
            batch_results = await self.recover_batch(current_batch)
            total_recovered += batch_results['recovered']

            logger.info(f"📊 Batch results: {batch_results['recovered']} recovered, "
                       f"{batch_results['failed']} failed, {batch_results['skipped']} skipped")

            remaining -= current_batch

            # Small delay between batches
            if remaining > 0:
                await asyncio.sleep(1)

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        final_report = {
            'diagnosis': diagnosis,
            'total_recovered': total_recovered,
            'duration_seconds': round(duration, 2),
            'timestamp': end_time.isoformat()
        }

        logger.info(f"✅ Full recovery complete: {total_recovered} documents recovered in {duration:.1f}s")
        return final_report

async def main():
    """Main recovery process"""
    logger.info("🚀 Atlas Document Recovery Mechanism")

    db_manager = DatabaseManager()
    await db_manager.initialize()

    try:
        recovery = DocumentRecovery(db_manager)

        # Run full recovery
        report = await recovery.full_recovery(max_documents=500)  # Start with 500

        # Display results
        print("\n📊 RECOVERY REPORT:")
        print(f"🔍 Total stuck documents: {report['diagnosis']['total_stuck']}")
        print(f"✅ Total recovered: {report['total_recovered']}")
        print(f"⏱️ Duration: {report['duration_seconds']} seconds")

        print("\n📋 Stuck by source:")
        for source, count in report['diagnosis']['by_source'].items():
            print(f"  {source}: {count}")

        print("\n📋 Stuck by type:")
        for content_type, count in report['diagnosis']['by_type'].items():
            print(f"  {content_type}: {count}")

        # Save detailed report
        with open('document_recovery_report.json', 'w') as f:
            json.dump(report, f, indent=2)

        print(f"\n📄 Detailed report saved to: document_recovery_report.json")

    finally:
        await db_manager.close()

if __name__ == "__main__":
    asyncio.run(main())