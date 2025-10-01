#!/usr/bin/env python3
"""
RSS Feed Processing System for Atlas v2
Extracts podcasts from OPML and processes episodes with unique IDs
"""

import xml.etree.ElementTree as ET
import feedparser
import asyncio
import aiohttp
import aiosqlite
import hashlib
import json
from datetime import datetime
from urllib.parse import urlparse
from typing import Dict, List, Optional, Tuple
import re
import sys

sys.path.append('.')

from modules.database import DatabaseManager

class RSSProcessor:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            headers={'User-Agent': 'Mozilla/5.0 (compatible; Atlas-RSS-Processor/1.0)'}
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    def parse_opml(self, opml_path: str) -> List[Dict]:
        """Parse OPML file and extract RSS feeds"""
        feeds = []

        tree = ET.parse(opml_path)
        root = tree.getroot()

        # Find all RSS outlines
        for outline in root.findall('.//outline[@type="rss"]'):
            feed = {
                'name': outline.get('text', ''),
                'rss_url': outline.get('xmlUrl', ''),
                'apple_id': outline.get('applePodcastsID', ''),
                'processed_count': 0
            }
            if feed['rss_url'] and feed['name']:
                feeds.append(feed)

        return feeds

    def generate_podcast_id(self, podcast_name: str, rss_url: str) -> str:
        """Generate unique podcast ID"""
        content = f"{podcast_name.lower().strip()}:{rss_url}"
        return hashlib.md5(content.encode()).hexdigest()[:12]

    def generate_episode_id(self, podcast_id: str, episode_title: str, episode_url: str) -> str:
        """Generate unique episode ID that tracks back to podcast"""
        content = f"{podcast_id}:{episode_title.lower().strip()}:{episode_url}"
        return hashlib.md5(content.encode()).hexdigest()[:16]

    async def fetch_rss_feed(self, rss_url: str) -> Optional[Dict]:
        """Fetch and parse RSS feed"""
        try:
            if not self.session:
                return None

            async with self.session.get(rss_url) as response:
                if response.status != 200:
                    print(f"❌ HTTP {response.status}: {rss_url}")
                    return None

                content = await response.text()
                feed = feedparser.parse(content)
                return feed

        except Exception as e:
            print(f"❌ RSS fetch failed: {e} - {rss_url}")
            return None

    async def extract_episodes(self, feed: Dict, podcast_id: str, limit: int = None) -> List[Dict]:
        """Extract episodes from RSS feed"""
        episodes = []

        if not feed or not feed.get('entries'):
            return episodes

        entries = feed.get('entries', [])
        if limit:
            entries = entries[:limit]

        for entry in entries:
            try:
                # Extract episode information
                title = entry.get('title', '').strip()
                link = entry.get('link', '')
                pub_date = entry.get('published', entry.get('updated', ''))

                # Skip if missing essential data
                if not title or not link:
                    continue

                # Extract audio URL if available
                audio_url = None
                if hasattr(entry, 'enclosures') and entry.enclosures:
                    for enclosure in entry.enclosures:
                        if enclosure.get('type', '').startswith('audio/'):
                            audio_url = enclosure.get('href', '')
                            break

                # Generate unique episode ID
                episode_id = self.generate_episode_id(podcast_id, title, link)

                episode = {
                    'episode_id': episode_id,
                    'podcast_id': podcast_id,
                    'title': title,
                    'link': link,
                    'audio_url': audio_url,
                    'pub_date': pub_date,
                    'description': entry.get('summary', entry.get('description', ''))[:500],
                    'processed': False
                }

                episodes.append(episode)

            except Exception as e:
                print(f"⚠️ Episode extraction error: {e}")
                continue

        return episodes

    async def create_podcast_tables(self):
        """Create database tables for podcast processing"""
        async with aiosqlite.connect(self.db_manager.db_path) as db:
            # Podcasts table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS podcasts (
                    podcast_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    rss_url TEXT NOT NULL,
                    apple_id TEXT,
                    created_at TEXT NOT NULL,
                    last_processed TEXT,
                    total_episodes INTEGER DEFAULT 0
                )
            """)

            # Episodes table
            await db.execute("""
                CREATE TABLE IF NOT EXISTS podcast_episodes (
                    episode_id TEXT PRIMARY KEY,
                    podcast_id TEXT NOT NULL,
                    title TEXT NOT NULL,
                    link TEXT NOT NULL,
                    audio_url TEXT,
                    pub_date TEXT,
                    description TEXT,
                    processed BOOLEAN DEFAULT FALSE,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY (podcast_id) REFERENCES podcasts(podcast_id)
                )
            """)

            # Create indexes
            await db.execute("CREATE INDEX IF NOT EXISTS idx_podcasts_name ON podcasts(name)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_episodes_podcast ON podcast_episodes(podcast_id)")
            await db.execute("CREATE INDEX IF NOT EXISTS idx_episodes_processed ON podcast_episodes(processed)")

            await db.commit()

    async def store_podcast(self, podcast: Dict) -> str:
        """Store podcast in database"""
        async with aiosqlite.connect(self.db_manager.db_path) as db:
            podcast_id = self.generate_podcast_id(podcast['name'], podcast['rss_url'])

            await db.execute("""
                INSERT OR REPLACE INTO podcasts
                (podcast_id, name, rss_url, apple_id, created_at)
                VALUES (?, ?, ?, ?, ?)
            """, (
                podcast_id,
                podcast['name'],
                podcast['rss_url'],
                podcast['apple_id'],
                datetime.now().isoformat()
            ))

            await db.commit()
            return podcast_id

    async def store_episodes(self, episodes: List[Dict]):
        """Store episodes in database"""
        if not episodes:
            return

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            for episode in episodes:
                await db.execute("""
                    INSERT OR REPLACE INTO podcast_episodes
                    (episode_id, podcast_id, title, link, audio_url, pub_date, description, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    episode['episode_id'],
                    episode['podcast_id'],
                    episode['title'],
                    episode['link'],
                    episode['audio_url'],
                    episode['pub_date'],
                    episode['description'],
                    datetime.now().isoformat()
                ))

            await db.commit()

    async def process_all_feeds(self, opml_path: str, limit_per_podcast: int = 50):
        """Process all RSS feeds from OPML file"""
        print("🎙️ Processing RSS feeds from OPML...")

        # Create tables
        await self.create_podcast_tables()

        # Parse OPML
        feeds = self.parse_opml(opml_path)
        print(f"📡 Found {len(feeds)} RSS feeds in OPML")

        total_episodes = 0
        successful_feeds = 0

        for i, feed in enumerate(feeds, 1):
            print(f"\n📡 [{i}/{len(feeds)}] Processing: {feed['name']}")

            try:
                # Store podcast
                podcast_id = await self.store_podcast(feed)

                # Fetch RSS feed
                rss_data = await self.fetch_rss_feed(feed['rss_url'])
                if not rss_data:
                    print(f"❌ Failed to fetch RSS for {feed['name']}")
                    continue

                # Extract episodes
                episodes = await self.extract_episodes(rss_data, podcast_id, limit_per_podcast)
                if episodes:
                    await self.store_episodes(episodes)
                    total_episodes += len(episodes)
                    successful_feeds += 1
                    print(f"✅ {feed['name']}: {len(episodes)} episodes")
                else:
                    print(f"⚠️ No episodes found for {feed['name']}")

            except Exception as e:
                print(f"❌ Error processing {feed['name']}: {e}")
                continue

        print(f"\n📊 RSS Processing Complete:")
        print(f"✅ Successful feeds: {successful_feeds}/{len(feeds)}")
        print(f"🎧 Total episodes extracted: {total_episodes:,}")

        return total_episodes

    async def get_episodes_for_processing(self, limit: int = 100) -> List[Dict]:
        """Get unprocessed episodes for transcript extraction"""
        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute("""
                SELECT
                    pe.episode_id,
                    pe.podcast_id,
                    pe.title,
                    pe.link,
                    pe.audio_url,
                    pe.pub_date,
                    p.name as podcast_name,
                    p.rss_url
                FROM podcast_episodes pe
                JOIN podcasts p ON pe.podcast_id = p.podcast_id
                WHERE pe.processed = FALSE
                ORDER BY pe.pub_date DESC
                LIMIT ?
            """, (limit,))

            episodes = []
            async for row in cursor:
                episodes.append({
                    'episode_id': row[0],
                    'podcast_id': row[1],
                    'title': row[2],
                    'link': row[3],
                    'audio_url': row[4],
                    'pub_date': row[5],
                    'podcast_name': row[6],
                    'rss_url': row[7]
                })

            return episodes

    async def mark_episode_processed(self, episode_id: str):
        """Mark episode as processed"""
        async with aiosqlite.connect(self.db_manager.db_path) as db:
            await db.execute("""
                UPDATE podcast_episodes
                SET processed = TRUE
                WHERE episode_id = ?
            """, (episode_id,))
            await db.commit()

async def main():
    """Main processing function"""
    db_manager = DatabaseManager()
    await db_manager.initialize()

    async with RSSProcessor(db_manager) as processor:
        # Process OPML file
        total_episodes = await processor.process_all_feeds('podcast_opml.opml', limit_per_podcast=50)

        if total_episodes > 0:
            # Get some episodes for processing
            episodes = await processor.get_episodes_for_processing(10)
            print(f"\n🎧 Ready to process {len(episodes)} episodes for transcripts")

            for episode in episodes[:3]:  # Show first 3
                print(f"  - {episode['podcast_name']}: {episode['title']}")

    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(main())