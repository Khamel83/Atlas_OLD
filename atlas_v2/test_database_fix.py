#!/usr/bin/env python3
"""
Test database fix - create missing processed_content table
"""

import asyncio
import sys
import aiosqlite
from pathlib import Path

# Add project root to path
sys.path.append('.')

from modules.database import DatabaseManager

async def main():
    print("🔧 Testing database fix...")

    # Initialize database
    db_manager = DatabaseManager()
    await db_manager.initialize()

    # Check if processed_content table exists
    async with aiosqlite.connect(db_manager.db_path) as db:
        cursor = await db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='processed_content'")
        result = await cursor.fetchone()

        if result:
            print("✅ processed_content table exists!")

            # Check table structure
            cursor = await db.execute("PRAGMA table_info(processed_content)")
            columns = await cursor.fetchall()
            print("📋 Table structure:")
            for col in columns:
                print(f"  - {col[1]} ({col[2]})")

            # Test inserting into processed_content
            print("\n🧪 Testing insert into processed_content...")
            await db.execute("""
                INSERT OR REPLACE INTO processed_content
                (content_id, content_type, content, metadata_json, created_at)
                VALUES (?, ?, ?, ?, ?)
            """, (
                'test-content-123',
                'article',
                '# Test Article\n\nThis is a test article to verify the processed_content table works.',
                '{"title": "Test Article", "source": "test"}',
                '2025-10-01T10:45:00.000000'
            ))
            await db.commit()

            # Verify insertion
            cursor = await db.execute("SELECT COUNT(*) FROM processed_content")
            count = (await cursor.fetchone())[0]
            print(f"✅ Successfully inserted test content. Total items: {count}")

            # Retrieve and display the test content
            cursor = await db.execute("SELECT content_id, content_type, LEFT(content, 100) FROM processed_content WHERE content_id = 'test-content-123'")
            result = await cursor.fetchone()
            if result:
                print(f"📄 Retrieved test content: {result[0]} ({result[1]}) - {result[2]}...")

        else:
            print("❌ processed_content table does not exist!")

    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(main())