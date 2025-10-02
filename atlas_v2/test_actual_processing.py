#!/usr/bin/env python3
"""
Test actual content processing through the full pipeline
"""

import asyncio
import sys
import json
sys.path.append('.')

from modules.enhanced_processor import get_enhanced_processor
from modules.database import DatabaseManager
from modules.config_manager import ConfigManager

async def test_actual_processing():
    """Test actual content processing pipeline"""

    db_manager = DatabaseManager()
    await db_manager.initialize()

    config_manager = ConfigManager()

    print("🧪 Testing actual content processing pipeline...")

    # Get enhanced processor
    processor = await get_enhanced_processor(db_manager, config_manager)

    # Test Lex Fridman episode processing
    test_content_id = "test-lex-fridman-donald-trump-2025-fixed"
    test_url = "https://lexfridman.com/donald-trump"
    test_source = "Lex Fridman Podcast"

    # Add to queue
    try:
        await db_manager.enqueue_content(
            test_content_id,
            test_url,
            test_source,
            'podcast',
            {'title': 'Donald Trump Interview Test'},
            'high'
        )
    except Exception as e:
        print(f"⚠️ Content already exists in queue, using existing: {test_content_id}")
        # Skip update - just proceed with processing the existing content

    print(f"📝 Added to queue: {test_content_id}")

    # Process through pipeline using the enhanced processor
    result = await processor._execute_base_processing(test_content_id)

    print(f"📊 Processing result: {result['status']}")
    print(f"💬 Message: {result['message']}")

    # Check if it was stored in database
    import aiosqlite
    async with aiosqlite.connect("atlas_v2/data/atlas_v2.db") as db:
        cursor = await db.execute(
            "SELECT COUNT(*) FROM processed_content WHERE content_id = ?",
            (test_content_id,)
        )
        count = (await cursor.fetchone())[0]
        print(f"🗄️ Stored in database: {'Yes' if count > 0 else 'No'}")

        if count > 0:
            cursor = await db.execute(
                "SELECT content, content_type FROM processed_content WHERE content_id = ?",
                (test_content_id,)
            )
            row = await cursor.fetchone()
            content, content_type = row
            print(f"📄 Content type: {content_type}")
            print(f"📏 Content length: {len(content)} characters")
            print(f"📝 First 100 chars: {content[:100]}...")

    await db_manager.close()
    await processor.close()

if __name__ == "__main__":
    asyncio.run(test_actual_processing())