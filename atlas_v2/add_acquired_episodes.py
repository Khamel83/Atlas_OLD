#!/usr/bin/env python3
"""
Add some Acquired.fm episodes to the processing queue for testing
"""

import asyncio
import sys
import aiosqlite

sys.path.append('.')

from modules.database import DatabaseManager

async def add_acquired_episodes():
    """Add test Acquired.fm episodes to queue"""

    db_manager = DatabaseManager()
    await db_manager.initialize()

    print("📝 Adding Acquired.fm episodes to queue...")

    # Known Acquired.fm episodes
    episodes = [
        ("acquired-google", "https://www.acquired.fm/episodes/google", "Acquired - Google"),
        ("acquired-tesla", "https://www.acquired.fm/episodes/tesla", "Acquired - Tesla"),
        ("acquired-amazon", "https://www.acquired.fm/episodes/amazon", "Acquired - Amazon"),
        ("acquired-apple", "https://www.acquired.fm/episodes/apple", "Acquired - Apple"),
        ("acquired-microsoft", "https://www.acquired.fm/episodes/microsoft", "Acquired - Microsoft"),
        ("acquired-facebook", "https://www.acquired.fm/episodes/facebook", "Acquired - Facebook"),
        ("acquired-netflix", "https://www.acquired.fm/episodes/netflix", "Acquired - Netflix"),
        ("acquired-uber", "https://www.acquired.fm/episodes/uber", "Acquired - Uber"),
        ("acquired-lyft", "https://www.acquired.fm/episodes/lyft", "Acquired - Lyft"),
        ("acquired-airbnb", "https://www.acquired.fm/episodes/airbnb", "Acquired - Airbnb"),
    ]

    success_count = 0

    for content_id, url, title in episodes:
        try:
            await db_manager.enqueue_content(
                content_id,
                url,
                "Acquired Podcast",
                'podcast',
                {'title': title},
                'high'
            )
            success_count += 1
            print(f"✅ Added: {title}")
        except Exception as e:
            print(f"⚠️  {title} already exists: {e}")

    print(f"\n📊 Added {success_count} new episodes to queue")

    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(add_acquired_episodes())