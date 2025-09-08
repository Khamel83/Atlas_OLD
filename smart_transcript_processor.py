#!/usr/bin/env python3
"""
Smart Transcript-First Podcast Processor

Finds existing transcripts online instead of downloading/transcribing MP3s.
Much faster and more efficient approach.
"""

import sqlite3
import time
import sys
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import json
from pathlib import Path

class SmartTranscriptFinder:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        # Known transcript patterns and sources
        self.transcript_sources = {
            # NPR Family
            "this american life": self.find_tal_transcript,
            "planet money": self.find_npr_transcript,
            "radiolab": self.find_radiolab_transcript,
            
            # Tech Podcasts
            "accidental tech podcast": self.find_atp_transcript,
            "the vergecast": self.find_verge_transcript,
            "hard fork": self.find_nytimes_transcript,
            
            # Business/Strategy
            "acquired": self.find_acquired_transcript,
            "stratechery": self.find_stratechery_transcript,
            
            # Slate Network
            "political gabfest": self.find_slate_transcript,
            "slate money": self.find_slate_transcript,
            "slate culture": self.find_slate_transcript,
        }
    
    def find_transcript(self, podcast_name, episode_title, episode_url=None):
        """Try to find existing transcript for episode"""
        podcast_key = podcast_name.lower().strip()
        
        # Try specific scrapers first
        for source_key, scraper_func in self.transcript_sources.items():
            if source_key in podcast_key:
                try:
                    transcript = scraper_func(episode_title, episode_url)
                    if transcript:
                        return transcript
                except Exception as e:
                    print(f"  Scraper {source_key} failed: {e}")
        
        # Try generic approaches
        return self.find_generic_transcript(podcast_name, episode_title, episode_url)
    
    def find_tal_transcript(self, title, url):
        """This American Life has excellent transcripts"""
        if not url:
            return None
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # TAL transcript sections
            transcript_divs = soup.find_all(['div', 'section'], 
                                          class_=re.compile(r'transcript|story-text', re.IGNORECASE))
            
            transcript_text = ""
            for div in transcript_divs:
                text = div.get_text(separator=' ', strip=True)
                if len(text) > 200:  # Substantial content
                    transcript_text += text + "\n\n"
            
            return transcript_text.strip() if len(transcript_text) > 500 else None
        except:
            return None
    
    def find_npr_transcript(self, title, url):
        """NPR podcasts often have transcripts"""
        if not url:
            return None
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # NPR transcript patterns
            transcript_sections = soup.find_all(['div', 'article'], 
                                              class_=re.compile(r'transcript|storytext|story-text', re.IGNORECASE))
            
            text = ""
            for section in transcript_sections:
                content = section.get_text(separator=' ', strip=True)
                if len(content) > 200:
                    text += content + "\n\n"
            
            return text.strip() if len(text) > 500 else None
        except:
            return None
    
    def find_radiolab_transcript(self, title, url):
        """Radiolab transcripts from WNYC"""
        if not url:
            return None
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for transcript content
            transcript_content = soup.find(['div', 'section'], 
                                         class_=re.compile(r'transcript|body|content', re.IGNORECASE))
            
            if transcript_content:
                text = transcript_content.get_text(separator=' ', strip=True)
                return text if len(text) > 500 else None
        except:
            return None
    
    def find_atp_transcript(self, title, url):
        """ATP has community transcripts at catatp.fm"""
        try:
            # Extract episode number from title
            ep_match = re.search(r'(\d+)', title)
            if not ep_match:
                return None
            
            ep_num = ep_match.group(1)
            transcript_url = f"https://catatp.fm/{ep_num}"
            
            response = self.session.get(transcript_url, timeout=15)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Find transcript content
                content_div = soup.find('div', class_=re.compile(r'transcript|content'))
                if content_div:
                    text = content_div.get_text(separator=' ', strip=True)
                    return text if len(text) > 500 else None
        except:
            return None
    
    def find_verge_transcript(self, title, url):
        """The Verge sometimes has transcripts"""
        if not url:
            return None
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Verge article content
            content_div = soup.find(['div', 'article'], 
                                  class_=re.compile(r'article-body|content|transcript', re.IGNORECASE))
            
            if content_div:
                text = content_div.get_text(separator=' ', strip=True)
                return text if len(text) > 1000 else None
        except:
            return None
    
    def find_nytimes_transcript(self, title, url):
        """NY Times podcasts sometimes have transcripts"""
        if not url:
            return None
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # NYT content patterns
            content_div = soup.find(['section', 'div'], 
                                  class_=re.compile(r'story-body|article-body|transcript', re.IGNORECASE))
            
            if content_div:
                text = content_div.get_text(separator=' ', strip=True)
                return text if len(text) > 1000 else None
        except:
            return None
    
    def find_acquired_transcript(self, title, url):
        """Acquired sometimes has show notes that work as transcripts"""
        if not url:
            return None
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for detailed show notes
            notes_section = soup.find(['div', 'section'], 
                                    class_=re.compile(r'notes|content|transcript', re.IGNORECASE))
            
            if notes_section:
                text = notes_section.get_text(separator=' ', strip=True)
                return text if len(text) > 800 else None
        except:
            return None
    
    def find_stratechery_transcript(self, title, url):
        """Stratechery audio posts often have full text versions"""
        if not url:
            return None
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Stratechery post content
            content_div = soup.find(['div', 'article'], 
                                  class_=re.compile(r'post-content|entry-content|content', re.IGNORECASE))
            
            if content_div:
                text = content_div.get_text(separator=' ', strip=True)
                return text if len(text) > 1000 else None
        except:
            return None
    
    def find_slate_transcript(self, title, url):
        """Slate podcasts sometimes have transcripts"""
        if not url:
            return None
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Slate article content
            content_div = soup.find(['div', 'article'], 
                                  class_=re.compile(r'article-body|transcript|content', re.IGNORECASE))
            
            if content_div:
                text = content_div.get_text(separator=' ', strip=True)
                return text if len(text) > 800 else None
        except:
            return None
    
    def find_generic_transcript(self, podcast_name, title, url):
        """Generic transcript search strategies"""
        if not url:
            return None
        
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for common transcript indicators
            transcript_indicators = [
                'transcript', 'full-transcript', 'episode-transcript',
                'show-notes', 'episode-notes', 'full-text'
            ]
            
            for indicator in transcript_indicators:
                elements = soup.find_all(['div', 'section', 'article'], 
                                       class_=re.compile(indicator, re.IGNORECASE))
                
                for element in elements:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) > 800:  # Substantial content
                        return text
            
            # Fallback: look for long text blocks
            all_divs = soup.find_all(['div', 'article', 'section'])
            for div in all_divs:
                text = div.get_text(separator=' ', strip=True)
                if len(text) > 2000:  # Very long content likely transcript
                    return text
            
        except Exception as e:
            print(f"  Generic search failed: {e}")
        
        return None

transcript_finder = SmartTranscriptFinder()

def process_episodes():
    """Process episodes by finding existing transcripts online"""
    with sqlite3.connect("data/atlas.db") as conn:
        # Get unprocessed episodes
        episodes = conn.execute("""
            SELECT id, title, podcast_name, audio_url 
            FROM podcast_episodes 
            WHERE processed = 0 
            LIMIT 5
        """).fetchall()
        
        if not episodes:
            print("No episodes to process")
            return False
        
        for episode_id, title, podcast, audio_url in episodes:
            print(f"Processing: {title[:50]}...")
            
            # Try to find existing transcript online
            transcript = transcript_finder.find_transcript(podcast, title, audio_url)
            
            if transcript:
                # Found transcript online!
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_transcript', CURRENT_TIMESTAMP)
                """, (f"[TRANSCRIPT] {title}", transcript))
                print(f"  ✓ Found transcript online: {len(transcript)} chars")
            else:
                # No transcript found, add placeholder for Mac Mini processing later
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_placeholder', CURRENT_TIMESTAMP)
                """, (f"[PENDING] {title}", f"Episode '{title}' from {podcast} - audio available at {audio_url or 'RSS feed'}. Transcript pending Mac Mini processing."))
                print("  → Queued for Mac Mini transcription")
            
            # Mark as processed
            conn.execute("""
                UPDATE podcast_episodes 
                SET processed = 1 
                WHERE id = ?
            """, (episode_id,))
        
        conn.commit()
        print(f"Processed {len(episodes)} episodes")
        return True

def run_continuous():
    """Run processor every 30 seconds"""
    print("Starting smart transcript-first processor...")
    
    try:
        while True:
            if process_episodes():
                print("Work done, sleeping 30 seconds...")
            else:
                print("No work found, sleeping 30 seconds...")
            time.sleep(30)
    except KeyboardInterrupt:
        print("\nProcessor stopped by user")
    except Exception as e:
        print(f"Processor error: {e}")
        time.sleep(60)  # Wait before potential restart

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--continuous':
        run_continuous()
    else:
        process_episodes()