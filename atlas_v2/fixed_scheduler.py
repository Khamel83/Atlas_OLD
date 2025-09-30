#!/usr/bin/env python3
"""
Fixed Atlas v2 Scheduler
Manually trigger backlog processing and verify it works
"""

import sqlite3
import json
import asyncio
import sys
import os
from pathlib import Path

# Add modules path
sys.path.append('/home/ubuntu/dev/atlas/atlas_v2')

from modules.processor import ContentProcessor
from modules.database import DatabaseManager
from modules.config_manager import ConfigManager

async def force_process_backlog():
    """Force process backlog items manually"""
    print("🔧 Force processing Atlas v2 backlog...")

    # Initialize components
    config_manager = ConfigManager()
    db_manager = DatabaseManager()
    processor = ContentProcessor(db_manager, config_manager)

    await db_manager.initialize()

    # Get pending items
    pending_items = await db_manager.get_pending_items(limit=10)
    print(f"📋 Found {len(pending_items)} pending items to process")

    if not pending_items:
        print("✅ No pending items found!")
        return

    processed_count = 0
    for item in pending_items:
        content_id = item['content_id']
        print(f"🔄 Processing {content_id}...")

        try:
            # Update status
            await db_manager.update_queue_status(content_id, 'processing')

            # Process content
            result = await processor.process_content(content_id)

            if result['status'] == 'success':
                print(f"✅ Successfully processed {content_id}")
                await db_manager.update_queue_status(content_id, 'completed')
                processed_count += 1
            else:
                print(f"❌ Failed to process {content_id}: {result['message']}")
                await db_manager.update_queue_status(content_id, 'failed')

        except Exception as e:
            print(f"❌ Error processing {content_id}: {e}")
            await db_manager.update_queue_status(content_id, 'failed')

    print(f"🎯 Processed {processed_count} items successfully")
    await db_manager.close()

def check_processing_status():
    """Check current Atlas v2 processing status"""
    print("📊 Checking Atlas v2 status...")

    # Check database
    conn = sqlite3.connect("/home/ubuntu/dev/atlas/atlas_v2/data/atlas_v2.db")

    # Queue status
    cursor = conn.execute("""
        SELECT status, COUNT(*) FROM processing_queue GROUP BY status
    """)
    queue_status = dict(cursor.fetchall())
    print(f"📋 Queue status: {queue_status}")

    # Content status
    cursor = conn.execute("""
        SELECT content_type, COUNT(*) FROM processed_content GROUP BY content_type
    """)
    content_status = dict(cursor.fetchall())
    print(f"📄 Content status: {content_status}")

    # Total counts
    total_queue = conn.execute("SELECT COUNT(*) FROM processing_queue").fetchone()[0]
    total_content = conn.execute("SELECT COUNT(*) FROM processed_content").fetchone()[0]

    print(f"📊 Total in queue: {total_queue}")
    print(f"📊 Total processed: {total_content}")

    conn.close()

    return {
        'queue_status': queue_status,
        'content_status': content_status,
        'total_queue': total_queue,
        'total_content': total_content
    }

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Atlas v2 Scheduler Control')
    parser.add_argument('--check', action='store_true', help='Check processing status')
    parser.add_argument('--process', action='store_true', help='Force process backlog')

    args = parser.parse_args()

    if args.check:
        check_processing_status()
    elif args.process:
        asyncio.run(force_process_backlog())
    else:
        print("Usage: python3 fixed_scheduler.py --check or --process")