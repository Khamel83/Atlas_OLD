#!/usr/bin/env python3
"""
Quick transcript harvester - practical approach using OPML data
Focus on actually getting results, not perfect architecture
"""

import json
import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin
import xml.etree.ElementTree as ET
from datetime import datetime
import hashlib
from concurrent.futures import ThreadPoolExecutor
import os

class QuickTranscriptHarvester:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        # Initialize database
        self.db_path = "data/atlas.db"
        self._init_database()
        
        # Load OPML data
        self.feeds = self._load_opml_feeds()
        
        # Results tracking
        self.results = {
            'found': 0,
            'processed': 0,
            'errors': 0
        }

    def _load_opml_feeds(self):
        """Load podcast feeds from OPML file"""
        feeds = {}
        try:
            tree = ET.parse('atlas_podcasts.opml')
            root = tree.getroot()
            
            for outline in root.findall('.//outline[@type="rss"]'):
                name = outline.get('text', '')
                url = outline.get('xmlUrl', '')
                if name and url:
                    feeds[name] = url
                    
        except Exception as e:
            print(f"Error loading OPML: {e}")
            
        print(f"📡 Loaded {len(feeds)} podcast feeds")
        return feeds

    def _init_database(self):
        """Initialize database with required tables"""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            # Create content table for transcripts
            conn.execute("""
                CREATE TABLE IF NOT EXISTS content (
                    id TEXT PRIMARY KEY,
                    title TEXT,
                    content TEXT,
                    content_type TEXT DEFAULT 'transcript',
                    url TEXT,
                    podcast_name TEXT,
                    episode_title TEXT,
                    created_date TEXT,
                    word_count INTEGER,
                    processed INTEGER DEFAULT 1
                )
            """)
            
            # Create podcast_episodes table for tracking
            conn.execute("""
                CREATE TABLE IF NOT EXISTS podcast_episodes (
                    id TEXT PRIMARY KEY,
                    podcast_name TEXT,
                    title TEXT,
                    description TEXT,
                    audio_url TEXT,
                    published_date TEXT,
                    duration INTEGER,
                    has_transcript INTEGER DEFAULT 0
                )
            """)

    def harvest_all_transcripts(self):
        """Main harvesting function - get transcripts from all sources"""
        print("🚀 Starting quick transcript harvest...")
        
        # Priority podcasts we know have transcripts
        priority_targets = {
            "Lex Fridman Podcast": self._harvest_lex_fridman,
            "This American Life": self._harvest_this_american_life,
            "EconTalk": self._harvest_econtalk,
        }
        
        # Process priority targets first
        for podcast_name, harvest_func in priority_targets.items():
            if podcast_name in self.feeds:
                print(f"\n🎯 Processing priority target: {podcast_name}")
                try:
                    found = harvest_func(self.feeds[podcast_name])
                    print(f"   ✅ Found {found} transcripts")
                    self.results['found'] += found
                except Exception as e:
                    print(f"   ❌ Error: {e}")
                    self.results['errors'] += 1
                
                # Brief pause between podcasts
                time.sleep(1)
        
        # Try a few more podcasts with RSS-embedded transcript discovery
        remaining = [name for name in self.feeds.keys() if name not in priority_targets.keys()][:10]
        print(f"\n🔍 Checking {len(remaining)} additional podcasts for RSS-embedded transcripts...")
        
        for podcast_name in remaining:
            try:
                found = self._check_rss_for_transcripts(podcast_name, self.feeds[podcast_name])
                if found > 0:
                    print(f"   🎉 {podcast_name}: Found {found} transcripts!")
                    self.results['found'] += found
            except Exception as e:
                print(f"   ⚠️  {podcast_name}: {e}")
                self.results['errors'] += 1

        # Print final results
        self._print_summary()

    def _harvest_lex_fridman(self, rss_url):
        """Harvest Lex Fridman transcripts using known pattern"""
        # Get recent episodes from RSS
        episodes = self._get_recent_episodes(rss_url, limit=20)
        found_count = 0
        
        for episode in episodes:
            try:
                # Extract guest name from title
                guest_match = re.search(r'#\d+\s*[-–]\s*([^:]+)', episode['title'])
                if not guest_match:
                    continue
                
                guest_name = guest_match.group(1).strip()
                slug = re.sub(r'[^\w\s-]', '', guest_name.lower())
                slug = re.sub(r'[-\s]+', '-', slug).strip('-')
                
                transcript_url = f"https://lexfridman.com/{slug}-transcript"
                
                # Check if already exists
                if self._transcript_exists(episode['title'], "Lex Fridman Podcast"):
                    continue
                
                # Fetch transcript
                response = self.session.get(transcript_url, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Try different content selectors
                    content = None
                    for selector in ['.transcript', '#transcript', 'main', 'article']:
                        elem = soup.select_one(selector)
                        if elem:
                            text = elem.get_text(strip=True)
                            if len(text) > 5000:  # Must be substantial
                                content = text
                                break
                    
                    if content:
                        self._save_transcript(
                            episode['title'],
                            content,
                            transcript_url,
                            "Lex Fridman Podcast",
                            episode['title']
                        )
                        found_count += 1
                        print(f"      ✅ {episode['title'][:50]}...")
                        
            except Exception as e:
                print(f"      ❌ {episode['title'][:50]}: {e}")
                continue
        
        return found_count

    def _harvest_this_american_life(self, rss_url):
        """Harvest This American Life transcripts"""
        episodes = self._get_recent_episodes(rss_url, limit=10)
        found_count = 0
        
        for episode in episodes:
            try:
                # Extract episode number
                ep_match = re.search(r'(\d+):', episode['title'])
                if not ep_match:
                    continue
                
                ep_num = ep_match.group(1)
                transcript_url = f"https://www.thisamericanlife.org/{ep_num}/transcript"
                
                if self._transcript_exists(episode['title'], "This American Life"):
                    continue
                
                response = self.session.get(transcript_url, timeout=15)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Look for transcript content
                    transcript_content = soup.find('div', class_='transcript-section') or \
                                       soup.find('div', class_='transcript') or \
                                       soup.find('main')
                    
                    if transcript_content:
                        text = transcript_content.get_text(strip=True)
                        if len(text) > 2000:
                            self._save_transcript(
                                episode['title'],
                                text,
                                transcript_url,
                                "This American Life",
                                episode['title']
                            )
                            found_count += 1
                            print(f"      ✅ {episode['title'][:50]}...")
                            
            except Exception as e:
                print(f"      ❌ {episode['title'][:50]}: {e}")
                continue
        
        return found_count

    def _harvest_econtalk(self, rss_url):
        """Harvest EconTalk transcripts (partial success expected)"""
        episodes = self._get_recent_episodes(rss_url, limit=5)
        found_count = 0
        
        for episode in episodes:
            try:
                if self._transcript_exists(episode['title'], "EconTalk"):
                    continue
                
                # Try common URL patterns
                title_slug = re.sub(r'[^\w\s-]', '', episode['title'].lower())
                title_slug = re.sub(r'[-\s]+', '-', title_slug).strip('-')
                
                test_urls = [
                    f"https://www.econtalk.org/{title_slug}/",
                    f"https://www.econtalk.org/podcast/{title_slug}/",
                ]
                
                for test_url in test_urls:
                    try:
                        response = self.session.get(test_url, timeout=10)
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.text, 'html.parser')
                            
                            transcript_div = soup.find('div', class_='transcript')
                            if transcript_div:
                                text = transcript_div.get_text(strip=True)
                                if len(text) > 2000:
                                    self._save_transcript(
                                        episode['title'],
                                        text,
                                        test_url,
                                        "EconTalk",
                                        episode['title']
                                    )
                                    found_count += 1
                                    print(f"      ✅ {episode['title'][:50]}...")
                                    break
                    except:
                        continue
                        
            except Exception as e:
                continue
        
        return found_count

    def _check_rss_for_transcripts(self, podcast_name, rss_url):
        """Check RSS feed for embedded transcript URLs"""
        found_count = 0
        
        try:
            response = self.session.get(rss_url, timeout=10)
            response.raise_for_status()
            
            # Parse RSS XML
            root = ET.fromstring(response.content)
            
            # Look for items with transcript links
            for item in root.findall('.//item')[:5]:  # Check first 5 episodes
                title_elem = item.find('title')
                if title_elem is None:
                    continue
                    
                title = title_elem.text or ""
                
                if self._transcript_exists(title, podcast_name):
                    continue
                
                # Look for transcript URLs in various elements
                transcript_url = None
                
                # Check for transcript links in description
                desc_elem = item.find('description')
                if desc_elem and desc_elem.text:
                    desc_text = desc_elem.text
                    # Look for transcript URLs
                    transcript_matches = re.findall(r'https?://[^\s<>"]+transcript[^\s<>"]*', desc_text, re.I)
                    if transcript_matches:
                        transcript_url = transcript_matches[0]
                
                # Check for custom transcript elements
                if not transcript_url:
                    for elem in item:
                        if 'transcript' in elem.tag.lower() or 'transcript' in str(elem.attrib).lower():
                            transcript_url = elem.text or elem.get('url', '')
                            break
                
                if transcript_url and transcript_url.startswith('http'):
                    try:
                        # Fetch and validate transcript
                        resp = self.session.get(transcript_url, timeout=10)
                        if resp.status_code == 200:
                            soup = BeautifulSoup(resp.text, 'html.parser')
                            text = soup.get_text(strip=True)
                            
                            if len(text) > 1000:  # Minimum transcript length
                                self._save_transcript(
                                    title,
                                    text,
                                    transcript_url,
                                    podcast_name,
                                    title
                                )
                                found_count += 1
                                print(f"      📡 RSS transcript: {title[:50]}...")
                                
                    except:
                        continue
                        
        except Exception as e:
            print(f"      ⚠️  RSS parsing error: {e}")
        
        return found_count

    def _get_recent_episodes(self, rss_url, limit=10):
        """Get recent episodes from RSS feed"""
        try:
            response = self.session.get(rss_url, timeout=15)
            response.raise_for_status()
            
            root = ET.fromstring(response.content)
            episodes = []
            
            for item in root.findall('.//item')[:limit]:
                title_elem = item.find('title')
                if title_elem is not None and title_elem.text:
                    episodes.append({
                        'title': title_elem.text.strip(),
                        'description': getattr(item.find('description'), 'text', '') or ''
                    })
            
            return episodes
            
        except Exception as e:
            print(f"      Error fetching RSS: {e}")
            return []

    def _transcript_exists(self, episode_title, podcast_name):
        """Check if transcript already exists in database"""
        with sqlite3.connect(self.db_path) as conn:
            result = conn.execute("""
                SELECT 1 FROM content 
                WHERE episode_title = ? AND podcast_name = ? AND content_type = 'transcript'
            """, (episode_title, podcast_name)).fetchone()
        return result is not None

    def _save_transcript(self, title, content, url, podcast_name, episode_title):
        """Save transcript to database"""
        content_id = hashlib.sha256(f"{podcast_name}_{episode_title}_{url}".encode()).hexdigest()[:16]
        word_count = len(content.split())
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO content (
                    id, title, content, content_type, url, podcast_name, 
                    episode_title, created_date, word_count, processed
                ) VALUES (?, ?, ?, 'transcript', ?, ?, ?, ?, ?, 1)
            """, (
                content_id, title, content, url, podcast_name,
                episode_title, datetime.now().isoformat(), word_count
            ))

    def _print_summary(self):
        """Print harvesting summary with stats"""
        print(f"\n📊 HARVEST SUMMARY:")
        print(f"   📝 Transcripts found: {self.results['found']}")
        print(f"   ⚠️  Errors encountered: {self.results['errors']}")
        
        # Get database stats
        with sqlite3.connect(self.db_path) as conn:
            total_transcripts = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'transcript'").fetchone()[0]
            total_words = conn.execute("SELECT SUM(word_count) FROM content WHERE content_type = 'transcript'").fetchone()[0] or 0
            
            print(f"   📚 Total transcripts in database: {total_transcripts}")
            print(f"   💭 Total words indexed: {total_words:,}")
            
            # Top podcasts by transcript count
            top_podcasts = conn.execute("""
                SELECT podcast_name, COUNT(*) as count 
                FROM content 
                WHERE content_type = 'transcript' AND podcast_name IS NOT NULL
                GROUP BY podcast_name 
                ORDER BY count DESC 
                LIMIT 5
            """).fetchall()
            
            if top_podcasts:
                print(f"\n🏆 Top Podcasts by Transcript Count:")
                for podcast, count in top_podcasts:
                    print(f"     {podcast}: {count} transcripts")

if __name__ == "__main__":
    harvester = QuickTranscriptHarvester()
    harvester.harvest_all_transcripts()