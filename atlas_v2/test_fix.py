#!/usr/bin/env python3
"""
Test the content processing fix
"""

import asyncio
import sys
sys.path.append('.')

from modules.database import DatabaseManager
from modules.real_content_processor import RealContentProcessor
from modules.config_manager import ConfigManager

async def test_fix():
    """Test that the fix works by processing one item"""

    db_manager = DatabaseManager()
    await db_manager.initialize()

    config_manager = ConfigManager()

    # Get any item from processing_queue to test (prefer pending items)
    import aiosqlite
    async with aiosqlite.connect(db_manager.db_path) as db:
        # First try to find pending items
        cursor = await db.execute("""
            SELECT content_id, source_url, source_name, content_type
            FROM processing_queue
            WHERE status = 'pending'
            LIMIT 1
        """)
        row = await cursor.fetchone()

        # If no pending items, try completed items that don't have processed_content
        if not row:
            cursor = await db.execute("""
                SELECT pq.content_id, pq.source_url, pq.source_name, pq.content_type
                FROM processing_queue pq
                LEFT JOIN processed_content pc ON pq.content_id = pc.content_id
                WHERE pq.status = 'completed' AND pc.content_id IS NULL
                LIMIT 1
            """)
            row = await cursor.fetchone()

        # If still no items, get any item
        if not row:
            cursor = await db.execute("""
                SELECT content_id, source_url, source_name, content_type
                FROM processing_queue
                LIMIT 1
            """)
            row = await cursor.fetchone()

    if not row:
        print("❌ No items found in processing_queue to test")
        await db_manager.close()
        return

    content_id, source_url, source_name, content_type = row
    print(f"🧪 Testing fix with: {content_id} ({source_url})")

    # Check current state
    async with aiosqlite.connect(db_manager.db_path) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM processed_content")
        before_count = (await cursor.fetchone())[0]

        cursor = await db.execute("SELECT COUNT(*) FROM processed_content WHERE content_id = ?", (content_id,))
        exists_before = (await cursor.fetchone())[0]

    print(f"📊 Before fix: {before_count} items in processed_content")
    print(f"📊 Item {content_id} exists in processed_content: {exists_before}")

    # Process the item using the enhanced processor
    async with RealContentProcessor(db_manager, config_manager) as processor:
        result = await processor.process_content(content_id)
        print(f"🔄 Processing result: {result}")

    # Check if it was added to processed_content
    async with aiosqlite.connect(db_manager.db_path) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM processed_content WHERE content_id = ?", (content_id,))
        exists_after = (await cursor.fetchone())[0]

    async with aiosqlite.connect(db_manager.db_path) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM processed_content")
        after_count = (await cursor.fetchone())[0]

    print(f"📊 After fix: {after_count} items in processed_content")
    print(f"📊 Item {content_id} exists in processed_content: {exists_after}")

    # Success criteria
    if exists_after > exists_before and after_count > before_count:
        print("✅ SUCCESS: Fix works! Item was properly added to processed_content table")
    else:
        print("❌ FAILURE: Fix didn't work")

    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(test_fix())