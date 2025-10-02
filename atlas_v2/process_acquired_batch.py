#!/usr/bin/env python3
"""
Process a batch of Acquired.fm episodes to test the pipeline
"""

import asyncio
import sys
import aiosqlite
import random
from pathlib import Path

sys.path.append('.')

from modules.real_content_processor import RealContentProcessor
from modules.database import DatabaseManager
from modules.config_manager import ConfigManager

async def process_acquired_batch():
    """Process 50 Acquired.fm episodes"""

    db_manager = DatabaseManager()
    await db_manager.initialize()

    config_manager = ConfigManager()

    print("🎙️ Processing 50 Acquired.fm episodes...")

    # Get Acquired.fm episodes from queue
    async with aiosqlite.connect("atlas_v2/data/atlas_v2.db") as db:
        cursor = await db.execute("""
            SELECT content_id, source_url, source_name
            FROM processing_queue
            WHERE source_url LIKE '%acquired.fm%'
            LIMIT 50
        """)
        episodes = await cursor.fetchall()

    if not episodes:
        print("❌ No Acquired.fm episodes found in queue")
        return

    print(f"📝 Found {len(episodes)} Acquired.fm episodes to process")

    success_count = 0
    failure_count = 0

    async with RealContentProcessor(db_manager, config_manager) as processor:
        for i, (content_id, source_url, source_name) in enumerate(episodes, 1):
            print(f"\n🎙️ Processing {i}/{len(episodes)}: {content_id}")
            print(f"📝 URL: {source_url}")

            try:
                result = await processor.process_content(content_id)

                if result['status'] == 'success':
                    success_count += 1
                    content_length = len(result.get('content', ''))
                    print(f"✅ SUCCESS: {result['message']}")
                    print(f"📏 Content: {content_length:,} characters")
                else:
                    failure_count += 1
                    print(f"❌ FAILED: {result['message']}")

            except Exception as e:
                failure_count += 1
                print(f"💥 ERROR: {e}")

    print(f"\n📊 Batch Results:")
    print(f"✅ Successful: {success_count}")
    print(f"❌ Failed: {failure_count}")
    print(f"📈 Success Rate: {success_count/len(episodes)*100:.1f}%")

    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(process_acquired_batch())