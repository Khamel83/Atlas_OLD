#!/usr/bin/env python3
"""
Bulk process Acquired.fm episodes directly without using queue
"""

import asyncio
import sys
import aiosqlite
from pathlib import Path

sys.path.append('.')

from modules.real_content_processor import RealContentProcessor
from modules.database import DatabaseManager
from modules.config_manager import ConfigManager

async def bulk_process_acquired():
    """Process 50 Acquired.fm episodes directly"""

    db_manager = DatabaseManager()
    await db_manager.initialize()

    config_manager = ConfigManager()

    print("🎙️ Bulk processing 50 Acquired.fm episodes...")

    # Known Acquired.fm episode URLs
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
        ("acquired-spacex", "https://www.acquired.fm/episodes/spacex", "Acquired - SpaceX"),
        ("acquired-nvidia", "https://www.acquired.fm/episodes/nvidia", "Acquired - NVIDIA"),
        ("acquired-intel", "https://www.acquired.fm/episodes/intel", "Acquired - Intel"),
        ("acquired-AMD", "https://www.acquired.fm/episodes/amd", "Acquired - AMD"),
        ("acquired-salesforce", "https://www.acquired.fm/episodes/salesforce", "Acquired - Salesforce"),
        ("acquired-oracle", "https://www.acquired.fm/episodes/oracle", "Acquired - Oracle"),
        ("acquired-adobe", "https://www.acquired.fm/episodes/adobe", "Acquired - Adobe"),
        ("acquired-qualcomm", "https://www.acquired.fm/episodes/qualcomm", "Acquired - Qualcomm"),
        ("acquired-cisco", "https://www.acquired.fm/episodes/cisco", "Acquired - Cisco"),
        ("acquired-twitter", "https://www.acquired.fm/episodes/twitter", "Acquired - Twitter"),
        ("acquired-instagram", "https://www.acquired.fm/episodes/instagram", "Acquired - Instagram"),
        ("acquired-whatsapp", "https://www.acquired.fm/episodes/whatsapp", "Acquired - WhatsApp"),
        ("acquired-linkedin", "https://www.acquired.fm/episodes/linkedin", "Acquired - LinkedIn"),
        ("acquired-youtube", "https://www.acquired.fm/episodes/youtube", "Acquired - YouTube"),
        ("acquired-tiktok", "https://www.acquired.fm/episodes/tiktok", "Acquired - TikTok"),
        ("acquired-roblox", "https://www.acquired.fm/episodes/roblox", "Acquired - Roblox"),
        ("acquired-unity", "https://www.acquired.fm/episodes/unity", "Acquired - Unity"),
        ("acquired-epic", "https://www.acquired.fm/episodes/epic", "Acquired - Epic"),
        ("acquired-bloomberg", "https://www.acquired.fm/episodes/bloomberg", "Acquired - Bloomberg"),
        ("acquired-reuters", "https://www.acquired.fm/episodes/reuters", "Acquired - Reuters"),
        ("acquired-blackrock", "https://www.acquired.fm/episodes/blackrock", "Acquired - BlackRock"),
        ("acquired-vanguard", "https://www.acquired.fm/episodes/vanguard", "Acquired - Vanguard"),
        ("acquired-berkshire", "https://www.acquired.fm/episodes/berkshire", "Acquired - Berkshire Hathaway"),
        ("acquired-jpmorgan", "https://www.acquired.fm/episodes/jpmorgan", "Acquired - JPMorgan"),
        ("acquired-goldman", "https://www.acquired.fm/episodes/goldman", "Acquired - Goldman Sachs"),
        ("acquired-morgan", "https://www.acquired.fm/episodes/morgan", "Acquired - Morgan Stanley"),
        ("acquired-coinbase", "https://www.acquired.fm/episodes/coinbase", "Acquired - Coinbase"),
        ("acquired-binance", "https://www.acquired.fm/episodes/binance", "Acquired - Binance"),
        ("acquired-shopify", "https://www.acquired.fm/episodes/shopify", "Acquired - Shopify"),
        ("acquired-square", "https://www.acquired.fm/episodes/square", "Acquired - Square"),
        ("acquired-stripe", "https://www.acquired.fm/episodes/stripe", "Acquired - Stripe"),
        ("acquired-paypal", "https://www.acquired.fm/episodes/paypal", "Acquired - PayPal"),
        ("acquired-venmo", "https://www.acquired.fm/episodes/venmo", "Acquired - Venmo"),
        ("acquired-cashapp", "https://www.acquired.fm/episodes/cashapp", "Acquired - Cash App"),
        ("acquired-zelle", "https://www.acquired.fm/episodes/zelle", "Acquired - Zelle"),
        ("acquired-wise", "https://www.acquired.fm/episodes/wise", "Acquired - Wise"),
        ("acquired-remitly", "https://www.acquired.fm/episodes/remitly", "Acquired - Remitly"),
        ("acquired-plaid", "https://www.acquired.fm/episodes/plaid", "Acquired - Plaid"),
        ("acquired-stripe", "https://www.acquired.fm/episodes/stripe-ipo", "Acquired - Stripe IPO"),
    ]

    # Process first 50
    episodes_to_process = episodes[:50]

    success_count = 0
    failure_count = 0
    total_chars = 0

    async with RealContentProcessor(db_manager, config_manager) as processor:
        for i, (content_id, url, title) in enumerate(episodes_to_process, 1):
            print(f"\n🎙️ Processing {i}/{len(episodes_to_process)}: {title}")
            print(f"📝 URL: {url}")

            try:
                result = await processor.extract_podcast_transcript(url, content_id)

                if result['status'] == 'success':
                    success_count += 1
                    content_length = len(result.get('content', ''))
                    total_chars += content_length
                    print(f"✅ SUCCESS: {result['message']}")
                    print(f"📏 Content: {content_length:,} characters")

                    # Check for conversational format
                    if "Ben:" in result['content'] and "David:" in result['content']:
                        print("💬 Verified conversational transcript format")

                    # Store in database directly
                    content_info = {
                        'content_id': content_id,
                        'source_url': url,
                        'source_name': 'Acquired Podcast',
                        'content_type': 'podcast',
                        'title': title,
                        'metadata': {}
                    }

                    await processor.store_extracted_content(content_id, result, content_info)

                else:
                    failure_count += 1
                    print(f"❌ FAILED: {result['message']}")

            except Exception as e:
                failure_count += 1
                print(f"💥 ERROR: {e}")

    print(f"\n📊 Bulk Processing Results:")
    print(f"✅ Successful: {success_count}")
    print(f"❌ Failed: {failure_count}")
    print(f"📈 Success Rate: {success_count/len(episodes_to_process)*100:.1f}%")
    print(f"📏 Total Characters Extracted: {total_chars:,}")
    if success_count > 0:
        print(f"📊 Average Length: {total_chars/success_count:,} characters")

    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(bulk_process_acquired())