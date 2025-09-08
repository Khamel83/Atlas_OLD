#!/usr/bin/env python3
"""
Authenticated Transcript Finder
Uses NYTimes and Stratechery login credentials to access premium transcripts
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import re
import os
from urllib.parse import urljoin
from comprehensive_transcript_finder import ComprehensiveTranscriptFinder

class AuthenticatedTranscriptFinder(ComprehensiveTranscriptFinder):
    def __init__(self):
        super().__init__()
        
        # Load credentials from .env
        self.nytimes_email = os.getenv('NYTIMES_EMAIL', 'newyorktimes@khamel.com')
        self.nytimes_password = os.getenv('NYTIMES_PASSWORD', 'saucy-holly-abandon')
        self.stratechery_email = os.getenv('STRATECHERY_EMAIL', 'stratecheryUSC@khamel.com')
        
        # Session for authenticated requests
        self.auth_session = requests.Session()
        self.auth_session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
    
    def login_to_nytimes(self):
        """Login to NYTimes to access Hard Fork transcripts"""
        print("    Logging into NYTimes...")
        
        try:
            # Go to login page
            login_url = "https://myaccount.nytimes.com/auth/login"
            response = self.auth_session.get(login_url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Find login form
                form = soup.find('form')
                if form:
                    action = form.get('action', login_url)
                    
                    # Prepare login data
                    login_data = {
                        'username': self.nytimes_email,
                        'password': self.nytimes_password
                    }
                    
                    # Submit login
                    login_response = self.auth_session.post(action, data=login_data, timeout=10)
                    
                    if login_response.status_code in [200, 302]:
                        print("    ✓ NYTimes login successful")
                        return True
                    else:
                        print(f"    ✗ NYTimes login failed: {login_response.status_code}")
                        return False
        
        except Exception as e:
            print(f"    ✗ NYTimes login error: {e}")
        
        return False
    
    def try_hard_fork_transcript_authenticated(self, title):
        """Find Hard Fork transcript with NYTimes authentication"""
        
        # Login first
        if not self.login_to_nytimes():
            return None
        
        # Try to find the episode page
        # Hard Fork episodes are usually at nytimes.com/YYYY/MM/DD/podcasts/hard-fork-...
        
        # Create search query for the episode
        search_query = f"Hard Fork {title}"
        search_url = f"https://www.nytimes.com/search?query={search_query.replace(' ', '+')}"
        
        print(f"    Searching NYTimes for: {search_query}")
        
        try:
            search_response = self.auth_session.get(search_url, timeout=15)
            
            if search_response.status_code == 200:
                soup = BeautifulSoup(search_response.content, 'html.parser')
                
                # Look for Hard Fork episode links
                links = soup.find_all('a', href=True)
                
                for link in links:
                    href = link.get('href')
                    if href and 'hard-fork' in href.lower() and any(word.lower() in href.lower() for word in title.split()[:3]):
                        episode_url = urljoin("https://www.nytimes.com", href)
                        print(f"    Found episode URL: {episode_url}")
                        
                        # Try to get transcript from episode page
                        episode_response = self.auth_session.get(episode_url, timeout=15)
                        
                        if episode_response.status_code == 200:
                            episode_soup = BeautifulSoup(episode_response.content, 'html.parser')
                            
                            # Look for transcript content
                            transcript_selectors = [
                                '.story-body-text', '.article-body', '.transcript-content',
                                '[data-testid="body"]', '.StoryBodyCompanionColumn'
                            ]
                            
                            for selector in transcript_selectors:
                                elements = episode_soup.select(selector)
                                
                                for element in elements:
                                    text = element.get_text(separator=' ', strip=True)
                                    if len(text) > 2000 and ('transcript' in text.lower() or 'hard fork' in text.lower()):
                                        return text
            
        except Exception as e:
            print(f"    Error searching Hard Fork: {e}")
        
        return None
    
    def try_stratechery_transcript(self, title):
        """Find Stratechery transcript using email authentication"""
        print(f"    Trying Stratechery for: {title[:50]}...")
        
        # Stratechery uses email-based authentication
        # They send a magic link to the email
        
        # For now, let's try direct access to see if the content is available
        # Stratechery episodes are usually at stratechery.com/YYYY/episode-title/
        
        # Create slug from title
        slug = title.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[-\s]+', '-', slug)
        slug = slug.strip('-')
        
        # Try various URL patterns
        possible_urls = [
            f"https://stratechery.com/{slug}/",
            f"https://stratechery.com/2024/{slug}/",
            f"https://stratechery.com/2025/{slug}/"
        ]
        
        for url in possible_urls:
            print(f"    Trying Stratechery URL: {url}")
            
            try:
                response = self.auth_session.get(url, timeout=15)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Look for transcript or substantial content
                    content_selectors = ['.post-content', '.entry-content', 'article']
                    
                    for selector in content_selectors:
                        elements = soup.select(selector)
                        
                        for element in elements:
                            text = element.get_text(separator=' ', strip=True)
                            if len(text) > 1000:
                                return text
                
            except Exception as e:
                print(f"    Error accessing {url}: {e}")
        
        return None
    
    def process_premium_podcasts(self):
        """Process podcasts that require authentication"""
        
        target_podcasts = [
            ("Hard Fork", self.try_hard_fork_transcript_authenticated),
            ("The Ezra Klein Show", self.try_hard_fork_transcript_authenticated),  # Same NYTimes auth
            ("Stratechery", self.try_stratechery_transcript)
        ]
        
        total_found = 0
        
        with sqlite3.connect("data/atlas.db") as conn:
            for podcast_pattern, strategy_func in target_podcasts:
                print(f"\n🔐 Processing {podcast_pattern} (authenticated)...")
                
                # Get unprocessed episodes
                episodes = conn.execute("""
                    SELECT id, podcast_name, title, audio_url 
                    FROM podcast_episodes 
                    WHERE (podcast_name LIKE ? OR podcast_name LIKE ?) AND processed = 0 
                    ORDER BY id DESC
                    LIMIT 3
                """, (f"%{podcast_pattern}%", f"%{podcast_pattern.split()[0]}%")).fetchall()
                
                print(f"Found {len(episodes)} unprocessed episodes")
                
                success_count = 0
                
                for episode_id, full_podcast_name, title, audio_url in episodes:
                    print(f"\nProcessing: {title[:60]}...")
                    
                    transcript = strategy_func(title)
                    
                    if transcript:
                        # Save transcript to database
                        conn.execute("""
                            INSERT OR REPLACE INTO content 
                            (title, content, content_type, url, created_at)
                            VALUES (?, ?, 'podcast_transcript', ?, CURRENT_TIMESTAMP)
                        """, (f"[TRANSCRIPT] {title}", transcript, audio_url))
                        
                        success_count += 1
                        total_found += 1
                        print(f"    ✅ Found transcript: {len(transcript)} characters")
                    else:
                        print("    ❌ No transcript found")
                    
                    # Mark episode as processed
                    conn.execute("""
                        UPDATE podcast_episodes 
                        SET processed = 1 
                        WHERE id = ?
                    """, (episode_id,))
                    
                    time.sleep(3)  # Be respectful with authenticated requests
                
                conn.commit()
                print(f"{podcast_pattern} results: {success_count}/{len(episodes)} transcripts found")
        
        return total_found

def main():
    print("🔐 Starting authenticated transcript discovery...")
    
    finder = AuthenticatedTranscriptFinder()
    
    # First run regular transcript discovery
    print("📂 Running standard transcript discovery...")
    from targeted_transcript_finder import process_specific_podcasts
    standard_count = process_specific_podcasts()
    
    # Then run authenticated discovery
    print("\n🔐 Running authenticated transcript discovery...")
    auth_count = finder.process_premium_podcasts()
    
    total = standard_count + auth_count
    
    if total > 0:
        print(f"\n🎉 SUCCESS! Found {total} total transcripts today")
        print(f"   - Standard sources: {standard_count}")
        print(f"   - Authenticated sources: {auth_count}")
        print("   Check them at: http://localhost:8000/api/v1/transcripts/discovery")
        
        # Show updated stats
        with sqlite3.connect("data/atlas.db") as conn:
            count = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'podcast_transcript'").fetchone()[0]
            total_words = conn.execute("SELECT SUM(LENGTH(content) / 5) FROM content WHERE content_type = 'podcast_transcript'").fetchone()[0] or 0
            print(f"   Total transcripts in database: {count}")
            print(f"   Total words: {int(total_words):,}")
    else:
        print(f"\n⚠️  No new transcripts found this run")

if __name__ == "__main__":
    main()