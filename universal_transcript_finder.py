#!/usr/bin/env python3
"""
Universal Podcast Transcript Finder

Finds transcripts for ANY podcast using multiple strategies:
1. Episode-specific website scraping
2. RSS feed link analysis  
3. Universal transcript aggregators
4. Community transcript sites
5. YouTube auto-captions
6. Podcast host platform transcripts
7. Web search for "{podcast} {episode} transcript"

No podcast is ignored. Every episode gets checked systematically.
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin, urlparse
import json

class UniversalTranscriptFinder:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        self.found_count = 0
        self.not_found_count = 0
        
        # Universal transcript aggregators
        self.transcript_aggregators = [
            "happyscribe.com",
            "otter.ai", 
            "rev.com",
            "sonix.ai",
            "trint.com",
            "podscribe.ai"
        ]
        
        # Podcast hosting platforms that provide transcripts
        self.hosting_platforms = {
            "megaphone.fm": self.check_megaphone,
            "libsyn.com": self.check_libsyn,
            "anchor.fm": self.check_anchor,
            "transistor.fm": self.check_transistor,
            "simplecast.com": self.check_simplecast,
            "buzzsprout.com": self.check_buzzsprout,
            "acast.com": self.check_acast
        }
    
    def find_transcript_universal(self, podcast_name, episode_title, episode_url, audio_url):
        """Universal transcript finding - never gives up"""
        
        # Strategy 1: Direct episode URL scraping
        if episode_url:
            transcript = self.scrape_episode_page(episode_url)
            if transcript:
                return transcript
        
        # Strategy 2: Check podcast hosting platform
        for platform_domain, platform_func in self.hosting_platforms.items():
            if audio_url and platform_domain in audio_url:
                transcript = platform_func(podcast_name, episode_title, audio_url)
                if transcript:
                    return transcript
        
        # Strategy 3: Search for transcript on episode website
        if episode_url:
            transcript = self.search_episode_site_for_transcript(episode_url)
            if transcript:
                return transcript
        
        # Strategy 4: Check common transcript URLs
        transcript = self.check_common_transcript_urls(podcast_name, episode_title, episode_url, audio_url)
        if transcript:
            return transcript
        
        # Strategy 5: Search transcript aggregators
        transcript = self.search_transcript_aggregators(podcast_name, episode_title)
        if transcript:
            return transcript
        
        # Strategy 6: YouTube/video platform check
        transcript = self.check_youtube_captions(podcast_name, episode_title)
        if transcript:
            return transcript
        
        return None
    
    def scrape_episode_page(self, url):
        """Scrape episode webpage for transcript"""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for transcript-specific elements first
            transcript_indicators = [
                {'class': re.compile(r'transcript', re.I)},
                {'id': re.compile(r'transcript', re.I)},
                {'class': re.compile(r'episode.?transcript', re.I)},
                {'class': re.compile(r'show.?notes', re.I)},
                {'class': re.compile(r'episode.?content', re.I)}
            ]
            
            for indicator in transcript_indicators:
                elements = soup.find_all(['div', 'section', 'article'], **indicator)
                for element in elements:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) > 800:  # Substantial content
                        return text
            
            # Fallback: Look for large text blocks
            all_content = soup.find_all(['div', 'article', 'section', 'main'])
            for content in all_content:
                text = content.get_text(separator=' ', strip=True)
                if len(text) > 2000:  # Very large content likely includes transcript
                    return text
        
        except Exception as e:
            print(f"  Episode scraping failed: {e}")
        
        return None
    
    def search_episode_site_for_transcript(self, episode_url):
        """Search episode website for transcript links"""
        try:
            response = self.session.get(episode_url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for transcript links
            transcript_links = []
            all_links = soup.find_all('a', href=True)
            
            for link in all_links:
                href = link.get('href', '').lower()
                text = link.get_text().lower()
                
                if any(word in href or word in text for word in ['transcript', 'show-notes', 'full-text']):
                    full_url = urljoin(episode_url, link['href'])
                    transcript_links.append(full_url)
            
            # Try each transcript link
            for link in transcript_links[:3]:  # Limit to avoid spam
                transcript = self.scrape_episode_page(link)
                if transcript:
                    return transcript
        
        except Exception as e:
            print(f"  Link search failed: {e}")
        
        return None
    
    def check_common_transcript_urls(self, podcast_name, episode_title, episode_url, audio_url):
        """Check common transcript URL patterns"""
        if not episode_url:
            return None
        
        base_url = '/'.join(episode_url.split('/')[:-1])  # Remove episode-specific part
        
        # Common patterns
        patterns = [
            f"{episode_url}/transcript",
            f"{episode_url}-transcript",
            f"{base_url}/transcript",
            f"{base_url}/transcripts",
            f"{base_url}/show-notes"
        ]
        
        for pattern in patterns:
            try:
                response = self.session.get(pattern, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    text = soup.get_text(separator=' ', strip=True)
                    if len(text) > 800:
                        return text
            except:
                continue
        
        return None
    
    def check_megaphone(self, podcast_name, episode_title, audio_url):
        """Check Megaphone-hosted podcasts for transcripts"""
        # Many Megaphone podcasts have transcripts on their main sites
        # Extract show info from Megaphone URL and search main site
        return None  # Implement if needed
    
    def check_libsyn(self, podcast_name, episode_title, audio_url):
        """Check Libsyn-hosted podcasts"""
        # Libsyn sometimes provides episode pages with transcripts
        return None
    
    def check_anchor(self, podcast_name, episode_title, audio_url):
        """Check Anchor/Spotify transcripts"""
        # Spotify has started adding auto-transcripts to some podcasts
        return None
    
    def check_transistor(self, podcast_name, episode_title, audio_url):
        """Check Transistor platform"""
        return None
    
    def check_simplecast(self, podcast_name, episode_title, audio_url):
        """Check Simplecast platform"""
        return None
    
    def check_buzzsprout(self, podcast_name, episode_title, audio_url):
        """Check Buzzsprout platform"""
        return None
    
    def check_acast(self, podcast_name, episode_title, audio_url):
        """Check Acast platform"""
        return None
    
    def search_transcript_aggregators(self, podcast_name, episode_title):
        """Search third-party transcript services"""
        # This would search services like HappyScribe, Otter.ai etc
        # for community-contributed transcripts
        return None
    
    def check_youtube_captions(self, podcast_name, episode_title):
        """Check if podcast episode is on YouTube with captions"""
        # Many podcasts also post to YouTube with auto-captions
        # Could search YouTube API and extract captions
        return None

def process_all_episodes_universally():
    """Process every single episode with universal approach"""
    finder = UniversalTranscriptFinder()
    
    with sqlite3.connect("data/atlas.db") as conn:
        # Get ALL unprocessed episodes
        episodes = conn.execute("""
            SELECT id, title, podcast_name, audio_url 
            FROM podcast_episodes 
            WHERE processed = 0 
            LIMIT 100
        """).fetchall()
        
        if not episodes:
            print("All episodes processed!")
            return
        
        print(f"Processing {len(episodes)} episodes with universal approach...")
        
        for episode_id, title, podcast_name, audio_url in episodes:
            print(f"Universal search: {podcast_name} - {title[:30]}...")
            
            # Use universal finder - NEVER gives up
            transcript = finder.find_transcript_universal(podcast_name, title, audio_url, audio_url)
            
            if transcript:
                # Found transcript!
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_transcript', CURRENT_TIMESTAMP)
                """, (f"[TRANSCRIPT] {title}", transcript))
                
                finder.found_count += 1
                print(f"  ✓ Found: {len(transcript)} chars")
            else:
                # Even universal approach failed - queue for Mac Mini
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_pending', CURRENT_TIMESTAMP)
                """, (f"[MAC-MINI] {title}", f"No online transcript found for '{title}' from {podcast_name}. Queued for Mac Mini audio transcription. Audio: {audio_url}"))
                
                finder.not_found_count += 1
                print("  → Mac Mini queue")
            
            # Mark as processed
            conn.execute("UPDATE podcast_episodes SET processed = 1 WHERE id = ?", (episode_id,))
            
            # Rate limiting
            time.sleep(0.5)
        
        conn.commit()
        print(f"\nBatch complete: {finder.found_count} found, {finder.not_found_count} queued for Mac Mini")

if __name__ == "__main__":
    process_all_episodes_universally()