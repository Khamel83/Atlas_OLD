#!/usr/bin/env python3
"""
Systematic Transcript Scraper

Uses the authoritative source mapping to systematically find transcripts
for all 1,736 podcast episodes instead of guessing.
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import time
from urllib.parse import urljoin, urlparse
import json
from podcast_transcript_mapping import get_transcript_sources

class SystematicTranscriptScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        self.success_count = 0
        self.failure_count = 0
        
    def scrape_npr_family(self, url, selectors=[".transcript", ".storytext", ".story-text"]):
        """Scrape NPR family podcasts (This American Life, Planet Money, etc.)"""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            for selector in selectors:
                elements = soup.select(selector)
                for element in elements:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) > 1000:  # Substantial transcript
                        return text
            
            # Fallback: look for large text blocks
            all_text_elements = soup.find_all(['div', 'article', 'section'])
            for element in all_text_elements:
                text = element.get_text(separator=' ', strip=True)
                if len(text) > 2000:  # Very substantial content
                    return text
                    
        except Exception as e:
            print(f"  NPR scraper error: {e}")
            
        return None
    
    def scrape_slate_network(self, url):
        """Scrape Slate podcasts - they convert audio to articles"""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Slate article body
            article_body = soup.find(['div', 'article'], class_=re.compile(r'article-body|post-content', re.I))
            if article_body:
                text = article_body.get_text(separator=' ', strip=True)
                if len(text) > 800:
                    return text
                    
        except Exception as e:
            print(f"  Slate scraper error: {e}")
            
        return None
    
    def scrape_nytimes_wsj(self, url):
        """Scrape NYTimes/WSJ professional journalism transcripts"""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Professional journalism selectors
            selectors = ['.story-body-text', '.article-body', '.post-content', '.story-content']
            
            for selector in selectors:
                elements = soup.select(selector)
                for element in elements:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) > 1200:  # Professional transcript length
                        return text
                        
        except Exception as e:
            print(f"  NYT/WSJ scraper error: {e}")
            
        return None
    
    def scrape_tech_podcasts(self, podcast_name, url):
        """Scrape tech podcasts with known transcript sources"""
        if "accidental tech" in podcast_name.lower():
            # Try catatp.fm community transcripts
            ep_match = re.search(r'(\d+)', url or "")
            if ep_match:
                try:
                    transcript_url = f"https://catatp.fm/{ep_match.group(1)}"
                    response = self.session.get(transcript_url, timeout=15)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        content = soup.find('div', class_=re.compile(r'transcript|content'))
                        if content:
                            text = content.get_text(separator=' ', strip=True)
                            if len(text) > 500:
                                return text
                except:
                    pass
        
        # General tech podcast approach
        try:
            if url:
                response = self.session.get(url, timeout=15)
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Look for transcript/content sections
                selectors = ['.transcript', '.article-body', '.post-content', '.episode-content']
                for selector in selectors:
                    elements = soup.select(selector)
                    for element in elements:
                        text = element.get_text(separator=' ', strip=True)
                        if len(text) > 800:
                            return text
        except:
            pass
            
        return None
    
    def scrape_business_podcasts(self, url):
        """Scrape business/strategy podcasts with detailed show notes"""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Business podcast selectors
            selectors = ['.post-content', '.episode-notes', '.show-notes', '.article-body']
            
            for selector in selectors:
                elements = soup.select(selector)
                for element in elements:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) > 1000:  # Detailed show notes
                        return text
                        
        except Exception as e:
            print(f"  Business scraper error: {e}")
            
        return None
    
    def get_transcript_for_episode(self, podcast_name, episode_title, episode_url):
        """Get transcript using systematic approach based on podcast mapping"""
        
        sources = get_transcript_sources(podcast_name)
        
        if "primary" not in sources:
            return None
            
        # Route to appropriate scraper based on known sources
        primary_url = sources["primary"]
        
        # NPR Family
        if "npr.org" in primary_url or "thisamericanlife.org" in primary_url or "radiolab.org" in primary_url:
            return self.scrape_npr_family(episode_url or primary_url)
        
        # Slate Network
        elif "slate.com" in primary_url:
            return self.scrape_slate_network(episode_url or primary_url)
        
        # NYTimes/WSJ Professional
        elif "nytimes.com" in primary_url or "wsj.com" in primary_url:
            return self.scrape_nytimes_wsj(episode_url or primary_url)
        
        # Tech Podcasts
        elif any(tech in primary_url for tech in ["atp.fm", "catatp.fm", "theverge.com", "changelog.com"]):
            return self.scrape_tech_podcasts(podcast_name, episode_url or primary_url)
        
        # Business/Strategy
        elif any(biz in primary_url for biz in ["acquired.fm", "stratechery.com", "fs.blog", "lexfridman.com"]):
            return self.scrape_business_podcasts(episode_url or primary_url)
        
        # Generic fallback
        else:
            return self.scrape_generic(episode_url or primary_url)
    
    def scrape_generic(self, url):
        """Generic transcript scraping fallback"""
        if not url:
            return None
            
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Generic transcript indicators
            transcript_selectors = [
                '.transcript', '.episode-transcript', '.show-transcript',
                '.article-body', '.post-content', '.entry-content',
                '.episode-content', '.show-content'
            ]
            
            for selector in transcript_selectors:
                elements = soup.select(selector)
                for element in elements:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) > 800:
                        return text
                        
        except Exception as e:
            print(f"  Generic scraper error: {e}")
            
        return None

def process_episodes_systematically():
    """Process episodes using systematic approach"""
    scraper = SystematicTranscriptScraper()
    
    with sqlite3.connect("data/atlas.db") as conn:
        # Get unprocessed episodes
        episodes = conn.execute("""
            SELECT id, title, podcast_name, audio_url 
            FROM podcast_episodes 
            WHERE processed = 0 
            LIMIT 10
        """).fetchall()
        
        if not episodes:
            print("No episodes to process")
            return False
        
        for episode_id, title, podcast, audio_url in episodes:
            print(f"Processing: {podcast} - {title[:40]}...")
            
            # Use systematic approach
            transcript = scraper.get_transcript_for_episode(podcast, title, audio_url)
            
            if transcript:
                # Found real transcript!
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_transcript', CURRENT_TIMESTAMP)
                """, (f"[TRANSCRIPT] {title}", transcript))
                
                scraper.success_count += 1
                print(f"  ✓ Found transcript: {len(transcript)} chars")
            else:
                # Queue for Mac Mini processing
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_pending', CURRENT_TIMESTAMP)
                """, (f"[PENDING] {title}", f"Episode '{title}' from {podcast} queued for Mac Mini transcription. Audio: {audio_url or 'RSS feed'}"))
                
                scraper.failure_count += 1
                print("  → Queued for Mac Mini")
            
            # Mark as processed
            conn.execute("""
                UPDATE podcast_episodes 
                SET processed = 1 
                WHERE id = ?
            """, (episode_id,))
            
            # Rate limiting
            time.sleep(1)
        
        conn.commit()
        print(f"Batch complete: {scraper.success_count} transcripts found, {scraper.failure_count} queued for Mac Mini")
        return True

def run_systematic_processor():
    """Run systematic processor continuously"""
    print("Starting Systematic Transcript Scraper...")
    print("Using authoritative source mapping for all 35 podcasts")
    
    total_found = 0
    total_queued = 0
    
    try:
        while True:
            success = process_episodes_systematically()
            if success:
                print("Batch processed, sleeping 30 seconds...")
            else:
                print("No more episodes, sleeping 60 seconds...")
                time.sleep(60)
                continue
            time.sleep(30)
            
    except KeyboardInterrupt:
        print(f"\nStopped. Total found: {total_found}, Total queued: {total_queued}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--continuous":
        run_systematic_processor()
    else:
        process_episodes_systematically()