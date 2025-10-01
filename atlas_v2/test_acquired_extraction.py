#!/usr/bin/env python3
"""
Test Acquired.fm transcript extraction
"""

import asyncio
import sys
sys.path.append('.')

from modules.real_content_processor import RealContentProcessor
from modules.database import DatabaseManager
from modules.config_manager import ConfigManager

async def test_acquired_extraction():
    """Test Acquired.fm transcript extraction"""

    db_manager = DatabaseManager()
    await db_manager.initialize()

    config_manager = ConfigManager()

    print("🎙️ Testing Acquired.fm transcript extraction...")

    # Test the URL conversion
    processor = RealContentProcessor(db_manager, config_manager)

    test_urls = [
        "https://www.acquired.fm/episodes/google",
        "https://www.acquired.fm/episodes/the-steve-ballmer-interview",
        "https://www.acquired.fm/episodes/epic-systems-mychart"
    ]

    for url in test_urls:
        transcript_url = processor.get_transcript_url(url)
        print(f"📝 {url} -> {transcript_url}")

    # Test actual transcript extraction
    print("\n🎙️ Testing actual Acquired.fm transcript extraction...")

    test_url = "https://www.acquired.fm/episodes/google"

    async with RealContentProcessor(db_manager, config_manager) as processor:
        result = await processor.extract_podcast_transcript(test_url, "test-acquired-google")

        print(f"📊 Result: {result['status']}")
        print(f"💬 Message: {result['message']}")

        if result['status'] == 'success':
            content_preview = result['content'][:500] + "..." if len(result['content']) > 500 else result['content']
            print(f"📄 Content preview: {content_preview}")
            print(f"📏 Content length: {len(result['content'])} characters")

            # Check if it looks like a real transcript
            if "Ben:" in result['content'] and "David:" in result['content']:
                print("✅ Found conversational transcript format (Ben:/David:)")
            else:
                print("⚠️  May not be a proper transcript format")
        else:
            # Debug: manually fetch and check what we're getting
            import aiohttp
            from bs4 import BeautifulSoup

            async with aiohttp.ClientSession() as session:
                async with session.get(test_url) as response:
                    html = await response.text()
                    print(f"📄 HTML length: {len(html)} characters")

                    soup = BeautifulSoup(html, 'html.parser')

                    # Check for transcript indicators in the raw HTML
                    if 'transcript' in html.lower():
                        print("✅ 'transcript' found in HTML")
                    else:
                        print("❌ 'transcript' NOT found in HTML")

                    # Check for Ben:/David: patterns
                    if 'Ben:' in html and 'David:' in html:
                        print("✅ Found Ben:/David: patterns in HTML")
                    else:
                        print("❌ Ben:/David: patterns NOT found in HTML")

                    # Look for transcript container specifically
                    transcript_container = soup.select_one('.transcript-container')
                    if transcript_container:
                        print("✅ Found .transcript-container")
                        print(f"📏 Container content length: {len(transcript_container.get_text())}")
                    else:
                        print("❌ .transcript-container NOT found")

                    # Look for specific acquired.fm selectors
                    for selector in ['.rich-text-block-7', '.rich-text-block-6', '#transcript']:
                        element = soup.select_one(selector)
                        if element:
                            print(f"✅ Found {selector}")
                            print(f"📏 Content length: {len(element.get_text())}")
                            preview = element.get_text()[:200]
                            print(f"📝 Preview: {preview}...")
                        else:
                            print(f"❌ {selector} NOT found")

    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(test_acquired_extraction())