#!/usr/bin/env python3
"""
Fixed Transcript Finder

Uses the actual Atlas infrastructure to find podcast transcripts.
No more broken imports - uses real web fetching capabilities.
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import re
from urllib.parse import urljoin, urlparse
import json

class RealTranscriptFinder:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Known transcript patterns for major podcast networks
        self.transcript_patterns = {
            "EconTalk": {
                "base_url": "https://www.econtalk.org/",
                "selectors": [".transcript-content", ".post-content", ".entry-content"],
                "title_to_slug": self.econtalk_title_to_slug
            },
            "Hard Fork": {
                "base_url": "https://www.nytimes.com/column/hard-fork",
                "selectors": [".story-body-text", ".article-body"],
                "search_approach": "nytimes_search"
            },
            "Stratechery": {
                "base_url": "https://stratechery.com/",
                "selectors": [".entry-content", ".post-content"],
                "approach": "stratechery_approach"
            }
        }
    
    def econtalk_title_to_slug(self, title):
        """Convert EconTalk title to URL slug"""
        # Remove author names in parentheses
        title = re.sub(r'\s*\([^)]*\)\s*', '', title)
        # Convert to slug
        slug = title.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[-\s]+', '-', slug)
        return slug.strip('-')
    
    def fetch_web_content(self, url, timeout=15):
        """Fetch web content with error handling"""
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"    Error fetching {url}: {e}")
            return None
    
    def extract_transcript_from_html(self, html, selectors):
        """Extract transcript content using CSS selectors"""
        if not html:
            return None
            
        soup = BeautifulSoup(html, 'html.parser')
        
        for selector in selectors:
            elements = soup.select(selector)
            for element in elements:
                text = element.get_text(separator=' ', strip=True)
                # Check if this looks like transcript content
                if len(text) > 1000 and self.looks_like_transcript(text):
                    return text
        
        return None
    
    def looks_like_transcript(self, text):
        """Check if text looks like a transcript"""
        # Simple heuristics for transcript detection
        text_lower = text.lower()
        
        # Positive indicators
        transcript_indicators = [
            'transcript', 'conversation', 'interview', 'host:', 'guest:',
            'speaker:', 'russ:', 'ezra:', 'ben:', 'thompson:'
        ]
        
        # Negative indicators
        negative_indicators = [
            'subscribe', 'newsletter', 'advertisement', 'privacy policy',
            'terms of service', 'cookie policy'
        ]
        
        positive_score = sum(1 for indicator in transcript_indicators if indicator in text_lower)
        negative_score = sum(1 for indicator in negative_indicators if indicator in text_lower)
        
        return positive_score > negative_score and positive_score > 0
    
    def try_econtalk_transcript(self, title):
        """Try to find EconTalk transcript"""
        config = self.transcript_patterns["EconTalk"]
        slug = config["title_to_slug"](title)
        url = f"{config['base_url']}{slug}/"
        
        print(f"    Trying EconTalk URL: {url}")
        
        html = self.fetch_web_content(url)
        if html:
            transcript = self.extract_transcript_from_html(html, config["selectors"])
            if transcript:
                return transcript
        
        # Try alternate URL patterns
        alt_urls = [
            f"{config['base_url']}{slug}/",
            f"{config['base_url']}transcript-{slug}/",
            f"{config['base_url']}{slug}-transcript/"
        ]
        
        for alt_url in alt_urls:
            print(f"    Trying alternate URL: {alt_url}")
            html = self.fetch_web_content(alt_url)
            if html:
                transcript = self.extract_transcript_from_html(html, config["selectors"])
                if transcript:
                    return transcript
        
        return None
    
    def try_nytimes_transcript(self, title):
        """Try to find NYTimes podcast transcript"""
        # NYTimes transcripts are often on the episode page
        # Try to construct URL from title
        slug = title.lower().replace(' ', '-').replace(':', '').replace(',', '')
        slug = re.sub(r'[^\w\s-]', '', slug).strip()
        
        # Common NYTimes podcast URL patterns
        base_urls = [
            f"https://www.nytimes.com/2024/12/07/podcasts/{slug}.html",
            f"https://www.nytimes.com/2024/11/30/podcasts/{slug}.html",
            f"https://www.nytimes.com/2024/12/06/podcasts/{slug}.html",
        ]
        
        for url in base_urls:
            print(f"    Trying NYTimes URL: {url}")
            html = self.fetch_web_content(url)
            if html:
                transcript = self.extract_transcript_from_html(html, [".story-body-text", ".article-body"])
                if transcript:
                    return transcript
        
        return None

    def try_this_american_life_transcript(self, title):
        """Try to find This American Life transcript"""
        # TAL has episode numbers in titles, extract them
        episode_match = re.search(r'(\d+):', title)
        if episode_match:
            episode_num = episode_match.group(1)
            url = f"https://www.thisamericanlife.org/{episode_num}/transcript"
            print(f"    Trying TAL URL: {url}")
            
            html = self.fetch_web_content(url)
            if html:
                transcript = self.extract_transcript_from_html(html, [".content", ".radio-dialtone", ".transcript", ".body"])
                if transcript:
                    return transcript
        
        return None

    def try_lex_fridman_transcript(self, title):
        """Try to find Lex Fridman transcript"""
        # Lex Fridman podcasts often have episode numbers
        episode_match = re.search(r'#(\d+)', title)
        if episode_match:
            episode_num = episode_match.group(1)
            # Try YouTube auto-generated transcript approach
            # Note: This would need YouTube API or transcript extraction
            print(f"    Lex Fridman #{episode_num} - transcript extraction not implemented")
        return None

    def try_acquired_transcript(self, title):
        """Try to find Acquired podcast transcript"""
        # Acquired sometimes has transcripts on their website
        slug = title.lower().replace(' ', '-').replace(':', '').replace(',', '')
        slug = re.sub(r'[^\w\s-]', '', slug).strip()
        
        url = f"https://www.acquired.fm/{slug}"
        print(f"    Trying Acquired URL: {url}")
        
        html = self.fetch_web_content(url)
        if html:
            transcript = self.extract_transcript_from_html(html, [".transcript-content", ".post-content"])
            if transcript:
                return transcript
        
        return None
    
    def find_transcripts_for_unprocessed(self, limit=5):
        """Find transcripts for unprocessed episodes"""
        with sqlite3.connect("data/atlas.db") as conn:
            # Get unprocessed episodes
            episodes = conn.execute("""
                SELECT id, podcast_name, title, audio_url 
                FROM podcast_episodes 
                WHERE processed = 0 
                ORDER BY id DESC
                LIMIT ?
            """, (limit,)).fetchall()
            
            print(f"Found {len(episodes)} unprocessed episodes")
            success_count = 0
            
            for episode_id, podcast_name, title, audio_url in episodes:
                print(f"\nProcessing: {podcast_name} - {title[:60]}...")
                
                transcript = None
                
                # Try podcast-specific strategies
                if "EconTalk" in podcast_name:
                    transcript = self.try_econtalk_transcript(title)
                elif "Hard Fork" in podcast_name or "Ezra Klein" in podcast_name:
                    transcript = self.try_nytimes_transcript(title)
                elif "This American Life" in podcast_name:
                    transcript = self.try_this_american_life_transcript(title)
                elif "Lex Fridman" in podcast_name:
                    transcript = self.try_lex_fridman_transcript(title)
                elif "Acquired" in podcast_name:
                    transcript = self.try_acquired_transcript(title)
                elif "Stratechery" in podcast_name:
                    # Stratechery often doesn't have transcripts, skip for now
                    print("    Stratechery - transcripts not typically available")
                elif "Knowledge Project" in podcast_name:
                    print("    Knowledge Project - transcript strategy not yet implemented")
                elif "Sharp Tech" in podcast_name:
                    print("    Sharp Tech - transcript strategy not yet implemented") 
                else:
                    print(f"    No strategy for podcast: {podcast_name}")
                
                if transcript:
                    # Save transcript to database
                    conn.execute("""
                        INSERT OR REPLACE INTO content 
                        (title, content, content_type, url, created_at)
                        VALUES (?, ?, 'podcast_transcript', ?, CURRENT_TIMESTAMP)
                    """, (f"[TRANSCRIPT] {title}", transcript, audio_url))
                    
                    success_count += 1
                    print(f"    ✓ Found transcript: {len(transcript)} characters")
                else:
                    print("    ✗ No transcript found")
                
                # Mark episode as processed regardless
                conn.execute("""
                    UPDATE podcast_episodes 
                    SET processed = 1 
                    WHERE id = ?
                """, (episode_id,))
                
                # Rate limiting
                time.sleep(2)
            
            conn.commit()
            print(f"\nResults: {success_count}/{len(episodes)} transcripts found")
            return success_count

def main():
    """Run transcript discovery"""
    print("🎙️ Starting transcript discovery...")
    
    finder = RealTranscriptFinder()
    count = finder.find_transcripts_for_unprocessed(limit=10)
    
    if count > 0:
        print(f"\n✅ Success! Found {count} new transcripts")
        print("   Access them at: http://localhost:8000/api/v1/transcripts/discovery")
    else:
        print(f"\n❌ No transcripts found today")
        print("   This could mean:")
        print("   - Podcast sources don't publish transcripts")
        print("   - URL patterns have changed")
        print("   - Network/access issues")

if __name__ == "__main__":
    main()