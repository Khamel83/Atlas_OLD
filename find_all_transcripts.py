#!/usr/bin/env python3
"""Find transcripts for all active podcasts by discovering their source of truth"""

import requests
from bs4 import BeautifulSoup
import re
import sqlite3
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET
import time
from concurrent.futures import ThreadPoolExecutor
import json

class TranscriptFinder:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        self.db_path = Path.home() / "dev" / "atlas" / "atlas.db"
        
        # Known transcript patterns
        self.patterns = {
            "lex fridman": self._try_lex_fridman,
            "this american life": self._try_this_american_life,
            "econtalk": self._try_econtalk,
            "hard fork": self._try_nytimes,
            "ezra klein": self._try_nytimes,
            "planet money": self._try_npr,
            "npr politics": self._try_npr,
            "today explained": self._try_vox,
            "conversations with tyler": self._try_tyler_cowen,
            "knowledge project": self._try_fs_blog,
            "radiolab": self._try_radiolab,
        }

    def get_active_podcasts(self):
        """Get all active podcasts from database"""
        conn = sqlite3.connect(self.db_path)
        podcasts = conn.execute("""
            SELECT name, category, count_target, transcript_only
            FROM podcasts 
            WHERE excluded = 0
            ORDER BY count_target DESC
        """).fetchall()
        conn.close()
        return podcasts

    def get_rss_episodes(self, podcast_name, limit=10):
        """Get episodes from RSS - using OPML data"""
        # RSS URLs from your OPML (the ones we know work)
        rss_urls = {
            "Political Gabfest": "https://feeds.megaphone.fm/slatespoliticalgabfest",
            "The NPR Politics Podcast": "https://feeds.npr.org/510310/podcast.xml",
            "Today, Explained": "https://feeds.megaphone.fm/VMP5705694065",
            "The Cognitive Revolution | AI Builders, Researchers, and Live Player Analysis": "https://feeds.megaphone.fm/RINTP3108857801",
            "ACQ2 by Acquired": "https://feeds.transistor.fm/acq2",
            "Accidental Tech Podcast": "https://cdn.atp.fm/rss/public?wtvryzdm",
            "Acquired": "https://feeds.transistor.fm/acquired",
            "Against the Rules with Michael Lewis": "https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/f4e26994-3ddb-4ec7-b855-ae32006cd5de/ea4fae0c-3282-4cfd-b315-ae32006cd5ec/podcast.rss",
            "Decoder with Nilay Patel": "https://feeds.megaphone.fm/recodedecode",
            "Greatest Of All Talk (Stratechery Plus Edition)": "https://goat.passport.online/feed/podcast/6EynvegSpNaDpnt4DJsHzD",
            "Plain English with Derek Thompson": "https://feeds.megaphone.fm/plain-english",
            "Practical AI": "https://feeds.transistor.fm/practical-ai-machine-learning-data-science-llm",
            "Sharp Tech with Ben Thompson": "https://sharptech.fm/feed/podcast/MMs7xScDXhCnUAesQqB2Xa",
            "Stratechery": "https://rss.stratechery.passport.online/feed/podcast/MMs7xScDXhCnUAesQqB2Xa",
            "The Trojan Horse Affair": "https://feeds.simplecast.com/B9KgArY4",
            "The Vergecast": "https://feeds.megaphone.fm/vergecast",
            "Planet Money": "https://feeds.npr.org/510289/podcast.xml",
            "Slate Money": "https://feeds.megaphone.fm/slatemoney",
            "The Indicator from Planet Money": "https://feeds.npr.org/510325/podcast.xml",
            "Slate Culture": "https://feeds.megaphone.fm/slatesculturegabfest",
            "The Prestige TV Podcast": "https://feeds.megaphone.fm/tvconcierge",
            "The Rewatchables": "https://feeds.megaphone.fm/the-rewatchables",
            "99% Invisible": "https://feeds.simplecast.com/BqbsxVfO",
            "Radiolab": "https://feeds.simplecast.com/EmVW7VGp",
            "Recipe Club": "https://feeds.megaphone.fm/dave-chang-recipe-club",
            "Ringer Food": "https://feeds.megaphone.fm/house-of-carbs",
            "The Recipe with Kenji and Deb": "https://rss.pdrl.fm/cd4580/feed.therecipepodcast.com/",
            "Conversations with Tyler": "https://cowenconvos.libsyn.com/rss",
            "EconTalk": "https://feeds.simplecast.com/wgl4xEgL",
            "Hard Fork": "https://feeds.simplecast.com/l2i9YnTd",
            "Lex Fridman Podcast": "https://lexfridman.com/feed/podcast/",
            "The Ezra Klein Show": "https://feeds.simplecast.com/82FI35Px",
            "The Journal.": "https://video-api.wsj.com/podcast/rss/wsj/the-journal",
            "The Knowledge Project with Shane Parrish": "https://feeds.megaphone.fm/FSMI7575968096",
            "This American Life": "https://www.thisamericanlife.org/podcast/rss.xml"
        }
        
        rss_url = rss_urls.get(podcast_name)
        if not rss_url:
            return []
        
        try:
            response = self.session.get(rss_url, timeout=15)
            response.raise_for_status()
            
            root = ET.fromstring(response.content)
            episodes = []
            
            for item in root.findall('.//item')[:limit]:
                title_elem = item.find('title')
                if title_elem is not None and title_elem.text:
                    episodes.append({'title': title_elem.text.strip()})
            
            return episodes
        except Exception as e:
            print(f"      RSS error for {podcast_name}: {e}")
            return []

    def transcript_exists(self, title, podcast_name):
        """Check if transcript exists"""
        conn = sqlite3.connect(self.db_path)
        result = conn.execute("""
            SELECT 1 FROM content 
            WHERE (title LIKE ? OR title LIKE ?) 
            AND content_type = 'transcript' 
            LIMIT 1
        """, (f"%{title[:50]}%", f"%{podcast_name}%{title[:30]}%")).fetchone()
        conn.close()
        return result is not None

    def add_transcript(self, title, content, url, podcast_name):
        """Add transcript to database"""
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            INSERT INTO content (
                title, url, content, content_type, metadata, 
                created_at, updated_at
            ) VALUES (?, ?, ?, 'transcript', ?, ?, ?)
        """, (
            f"[TRANSCRIPT] {title}",
            url,
            content,
            f'{{"podcast": "{podcast_name}", "episode": "{title}"}}',
            datetime.now().isoformat(),
            datetime.now().isoformat()
        ))
        conn.commit()
        conn.close()

    # Transcript extraction methods
    def _try_lex_fridman(self, episodes, podcast_name):
        """Lex Fridman transcripts"""
        found = 0
        for episode in episodes:
            title = episode['title']
            if self.transcript_exists(title, podcast_name):
                continue
                
            guest_match = re.search(r'#\d+\s*[-–]\s*([^:]+)', title)
            if not guest_match:
                continue
            
            guest_name = guest_match.group(1).strip()
            slug = re.sub(r'[^\w\s-]', '', guest_name.lower())
            slug = re.sub(r'[-\s]+', '-', slug).strip('-')
            
            url = f"https://lexfridman.com/{slug}-transcript"
            
            try:
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    content = soup.get_text(strip=True)
                    
                    if content and len(content) > 5000:
                        self.add_transcript(title, content, url, podcast_name)
                        found += 1
                        print(f"      ✅ {title[:60]}...")
            except:
                pass
            
            time.sleep(0.2)
        
        return found

    def _try_this_american_life(self, episodes, podcast_name):
        """This American Life transcripts"""
        found = 0
        for episode in episodes:
            title = episode['title']
            if self.transcript_exists(title, podcast_name):
                continue
                
            ep_match = re.search(r'(\d+):', title)
            if not ep_match:
                continue
            
            ep_num = ep_match.group(1)
            url = f"https://www.thisamericanlife.org/{ep_num}/transcript"
            
            try:
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    content_div = soup.find('div', class_='transcript-section') or soup.find('main')
                    
                    if content_div:
                        content = content_div.get_text(strip=True)
                        if len(content) > 2000:
                            self.add_transcript(title, content, url, podcast_name)
                            found += 1
                            print(f"      ✅ {title[:60]}...")
            except:
                pass
            
            time.sleep(0.3)
        
        return found

    def _try_econtalk(self, episodes, podcast_name):
        """EconTalk transcripts"""
        found = 0
        for episode in episodes[:5]:
            title = episode['title']
            if self.transcript_exists(title, podcast_name):
                continue
                
            slug = re.sub(r'[^\w\s-]', '', title.lower())
            slug = re.sub(r'[-\s]+', '-', slug).strip('-')[:50]
            
            for test_url in [f"https://www.econtalk.org/{slug}/", f"https://www.econtalk.org/podcast/{slug}/"]:
                try:
                    response = self.session.get(test_url, timeout=8)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        transcript_div = soup.find('div', class_='transcript')
                        
                        if transcript_div:
                            content = transcript_div.get_text(strip=True)
                            if len(content) > 2000:
                                self.add_transcript(title, content, test_url, podcast_name)
                                found += 1
                                print(f"      ✅ {title[:60]}...")
                                break
                except:
                    continue
                    
            time.sleep(0.5)
        
        return found

    def _try_nytimes(self, episodes, podcast_name):
        """NYTimes podcasts (requires login, skip for now)"""
        return 0

    def _try_npr(self, episodes, podcast_name):
        """NPR transcripts"""
        found = 0
        for episode in episodes[:5]:
            title = episode['title']
            if self.transcript_exists(title, podcast_name):
                continue
            
            slug = re.sub(r'[^\w\s-]', '', title.lower())
            slug = re.sub(r'[-\s]+', '-', slug).strip('-')[:40]
            
            test_urls = [
                f"https://www.npr.org/transcripts/{slug}",
                f"https://www.npr.org/{slug}/transcript",
            ]
            
            for test_url in test_urls:
                try:
                    response = self.session.get(test_url, timeout=8)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        content = soup.get_text(strip=True)
                        
                        if len(content) > 3000:
                            self.add_transcript(title, content, test_url, podcast_name)
                            found += 1
                            print(f"      ✅ {title[:60]}...")
                            break
                except:
                    continue
                    
            time.sleep(0.3)
        
        return found

    def _try_vox(self, episodes, podcast_name):
        """Vox podcasts"""
        return 0  # Skip for now

    def _try_tyler_cowen(self, episodes, podcast_name):
        """Conversations with Tyler"""
        return 0  # Skip for now

    def _try_fs_blog(self, episodes, podcast_name):
        """Knowledge Project"""
        return 0  # Skip for now

    def _try_radiolab(self, episodes, podcast_name):
        """Radiolab transcripts"""
        return 0  # Skip for now

    def process_podcast(self, podcast_name, category, count_target, transcript_only):
        """Process a single podcast for transcripts"""
        print(f"📻 {podcast_name} ({category})")
        
        # Get episodes
        episode_limit = min(20, max(5, count_target // 10)) if count_target > 0 else 5
        episodes = self.get_rss_episodes(podcast_name, limit=episode_limit)
        
        if not episodes:
            print(f"      ⚠️  No episodes found")
            return 0
        
        print(f"      📻 Got {len(episodes)} episodes")
        
        # Find appropriate pattern
        found = 0
        for pattern_key, pattern_func in self.patterns.items():
            if pattern_key in podcast_name.lower():
                found = pattern_func(episodes, podcast_name)
                break
        
        if found > 0:
            print(f"      🎉 Found {found} transcripts!")
        else:
            print(f"      😕 No transcripts found")
        
        return found

    def main(self):
        print("🚀 Finding transcripts for ALL active podcasts...")
        
        podcasts = self.get_active_podcasts()
        print(f"📻 Processing {len(podcasts)} active podcasts")
        
        # Get starting count
        conn = sqlite3.connect(self.db_path)
        start_count = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'transcript'").fetchone()[0]
        conn.close()
        
        print(f"📝 Starting with {start_count} transcripts\n")
        
        total_found = 0
        for i, (podcast_name, category, count_target, transcript_only) in enumerate(podcasts, 1):
            print(f"{i}/{len(podcasts)} ", end="")
            found = self.process_podcast(podcast_name, category, count_target, transcript_only)
            total_found += found
            
            # Brief pause between podcasts
            time.sleep(0.5)
        
        # Final results
        conn = sqlite3.connect(self.db_path)
        end_count = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'transcript'").fetchone()[0]
        conn.close()
        
        print(f"\n📈 RESULTS:")
        print(f"   📝 New transcripts found: {total_found}")
        print(f"   📊 Total transcripts: {start_count} → {end_count}")
        
        if total_found > 0:
            print("\n✅ Successfully found transcripts across your podcast collection!")

if __name__ == "__main__":
    finder = TranscriptFinder()
    finder.main()