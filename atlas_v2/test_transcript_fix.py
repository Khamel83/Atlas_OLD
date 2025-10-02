#!/usr/bin/env python3
"""
Test the transcript URL fix
"""

import asyncio
import sys
sys.path.append('.')

from modules.real_content_processor import RealContentProcessor
from modules.database import DatabaseManager
from modules.config_manager import ConfigManager

async def test_transcript_fix():
    """Test that the transcript URL conversion works"""

    db_manager = DatabaseManager()
    await db_manager.initialize()

    config_manager = ConfigManager()

    print("🧪 Testing transcript URL conversion...")

    # Test the URL conversion
    processor = RealContentProcessor(db_manager, config_manager)

    test_urls = [
        "https://lexfridman.com/donald-trump",
        "https://lexfridman.com/donald-trump/",
        "https://acquired.fm/episode/google",
        "https://tim.blog/podcast/some-episode"
    ]

    for url in test_urls:
        transcript_url = processor.get_transcript_url(url)
        print(f"📝 {url} -> {transcript_url}")

    # Test actual transcript extraction
    print("\n🎙️ Testing actual transcript extraction...")

    # Use the known working Lex Fridman URL
    test_url = "https://lexfridman.com/donald-trump"

    async with RealContentProcessor(db_manager, config_manager) as processor:
        result = await processor.extract_podcast_transcript(test_url, "test-123")

        print(f"📊 Result: {result['status']}")
        print(f"💬 Message: {result['message']}")

        if result['status'] == 'success':
            content_preview = result['content'][:200] + "..." if len(result['content']) > 200 else result['content']
            print(f"📄 Content preview: {content_preview}")
            print(f"📏 Content length: {len(result['content'])} characters")

    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(test_transcript_fix())