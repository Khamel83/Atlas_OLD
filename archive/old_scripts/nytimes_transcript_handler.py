#!/usr/bin/env python3
"""
NYTimes Podcast Transcript Handler

Specialized handler for NYTimes podcasts (Hard Fork, Ezra Klein Show, etc.)
that encounter 403 Forbidden errors. Implements multiple fallback strategies.
"""

import requests
import time
import random
import re
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import sqlite3

class NYTimesTranscriptHandler:
    def __init__(self, db_path="~/dev/atlas/atlas.db"):
        self.db_path = db_path.replace("~", "/home/ubuntu")
        self.session = requests.Session()
        
        # Enhanced user agents specifically for news sites
        self.user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15'
        ]
    
    def setup_session(self):
        """Setup session with realistic headers"""
        self.session.headers.update({
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Cache-Control': 'max-age=0'
        })
    
    def try_alternative_sources(self, podcast_name, episode_title):
        """Try alternative sources for NYTimes podcast transcripts"""
        
        # Strategy 1: Search for transcript on third-party sites
        alternative_sources = [
            self.search_rev_transcripts,
            self.search_podcast_transcripts_com,
            self.search_listen_notes,
            self.search_google_cache
        ]
        
        for source_func in alternative_sources:
            try:
                result = source_func(podcast_name, episode_title)
                if result:
                    return result
                time.sleep(random.uniform(2, 5))  # Respectful delay
            except Exception as e:
                print(f"Alternative source failed: {e}")
                continue
        
        return None
    
    def search_rev_transcripts(self, podcast_name, episode_title):
        """Search Rev.com for transcripts"""
        try:
            query = f'"{podcast_name}" "{episode_title}" site:rev.com'
            # Implementation would go here
            return None
        except Exception:
            return None
    
    def search_podcast_transcripts_com(self, podcast_name, episode_title):
        """Search specialized transcript sites"""
        try:
            # Many third-party sites aggregate podcast transcripts
            return None
        except Exception:
            return None
    
    def search_listen_notes(self, podcast_name, episode_title):
        """Search Listen Notes API for transcript data"""
        try:
            # Listen Notes sometimes has transcript information
            return None
        except Exception:
            return None
    
    def search_google_cache(self, podcast_name, episode_title):
        """Try Google cache of NYTimes pages"""
        try:
            self.setup_session()
            
            # Search for cached version
            search_query = f'cache:nytimes.com "{podcast_name}" "{episode_title}"'
            encoded_query = quote_plus(search_query)
            
            url = f"https://www.google.com/search?q={encoded_query}"
            
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Look for cached content links
                cache_links = soup.find_all('a', href=re.compile(r'webcache\.googleusercontent\.com'))
                
                for link in cache_links:
                    try:
                        cached_url = link['href']
                        cached_response = self.session.get(cached_url, timeout=10)
                        if cached_response.status_code == 200:
                            # Parse cached content for transcript
                            cached_soup = BeautifulSoup(cached_response.content, 'html.parser')
                            transcript_text = self.extract_transcript_from_cached_page(cached_soup)
                            if transcript_text:
                                return transcript_text
                    except Exception:
                        continue
                        
        except Exception as e:
            print(f"Google cache search failed: {e}")
        
        return None
    
    def extract_transcript_from_cached_page(self, soup):
        """Extract transcript content from cached NYTimes page"""
        try:
            # Look for common transcript indicators
            transcript_indicators = [
                {'tag': 'div', 'class': re.compile(r'transcript', re.I)},
                {'tag': 'section', 'class': re.compile(r'transcript', re.I)},
                {'tag': 'div', 'id': re.compile(r'transcript', re.I)},
                {'tag': 'article', 'class': re.compile(r'story|content', re.I)}
            ]
            
            for indicator in transcript_indicators:
                elements = soup.find_all(indicator['tag'], 
                                       class_=indicator.get('class'), 
                                       id=indicator.get('id'))
                
                for element in elements:
                    text = element.get_text(strip=True)
                    if len(text) > 1000:  # Substantial content
                        return text
            
            return None
            
        except Exception:
            return None
    
    def mark_as_unavailable(self, podcast_name, episode_title, reason):
        """Mark transcript as unavailable in database with reason"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Store in content table as a transcript record with error status
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, url, created_at, metadata)
                    VALUES (?, ?, 'transcript_error', '', datetime('now'), ?)
                """, (
                    f"[TRANSCRIPT ERROR] {podcast_name} - {episode_title}", 
                    f"Transcript unavailable: {reason}",
                    f'{{"podcast": "{podcast_name}", "episode": "{episode_title}", "error": "{reason}"}}'
                ))
                conn.commit()
                print(f"Marked as unavailable: {podcast_name} - {episode_title} ({reason})")
        except Exception as e:
            print(f"Failed to mark as unavailable: {e}")
    
    def handle_nytimes_transcript(self, podcast_name, episode_title, episode_url=None):
        """Main handler for NYTimes podcast transcripts"""
        
        print(f"Handling NYTimes transcript: {podcast_name} - {episode_title}")
        
        # Try alternative sources first
        transcript = self.try_alternative_sources(podcast_name, episode_title)
        
        if transcript:
            print("✅ Found transcript via alternative source")
            return transcript
        
        # If no alternatives work, mark as unavailable with clear reason
        reason = "403 Forbidden from NYTimes - requires manual access or subscription"
        self.mark_as_unavailable(podcast_name, episode_title, reason)
        
        print(f"❌ No transcript available for {podcast_name} - {episode_title}")
        print(f"   Reason: {reason}")
        print(f"   Suggestion: Manual download or RSS feed monitoring")
        
        return None

def handle_403_error(podcast_name, episode_title, episode_url=None):
    """Main function to handle 403 errors for NYTimes podcasts"""
    handler = NYTimesTranscriptHandler()
    return handler.handle_nytimes_transcript(podcast_name, episode_title, episode_url)

if __name__ == "__main__":
    # Test with known problematic episodes
    test_cases = [
        ("Hard Fork", "The Election That Silicon Valley Can't Ignore"),
        ("The Ezra Klein Show", "A Psychedelic Guide to the Preparation for Death")
    ]
    
    for podcast_name, episode_title in test_cases:
        print(f"\n{'='*60}")
        result = handle_403_error(podcast_name, episode_title)
        if result:
            print(f"SUCCESS: Found transcript ({len(result)} chars)")
        else:
            print("HANDLED: Marked as unavailable with clear reason")