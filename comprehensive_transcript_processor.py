#!/usr/bin/env python3
"""
Comprehensive transcript processor using our research findings
Processes all available podcasts with their specific URL patterns and authentication
"""

import json
import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, quote
import hashlib
from datetime import datetime

class ComprehensiveTranscriptProcessor:
    def __init__(self, db_path="data/atlas.db"):
        self.db_path = db_path
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        # Load our research data
        with open('podcast_transcript_sources.json', 'r') as f:
            self.transcript_sources = json.load(f)
    
    def process_all_podcasts(self):
        """Process transcripts for all podcasts based on our research"""
        print("🚀 Starting comprehensive transcript processing...")
        
        # Get all episodes from database
        with sqlite3.connect(self.db_path) as conn:
            episodes = conn.execute("""
                SELECT id, podcast_name, title, url, published_date
                FROM podcast_episodes
                WHERE podcast_name IN ({})
                ORDER BY published_date DESC
            """.format(','.join(['?' for _ in self.transcript_sources.keys()]),),
            list(self.transcript_sources.keys())).fetchall()
        
        print(f"📊 Found {len(episodes)} episodes across {len(self.transcript_sources)} podcasts")
        
        # Group by podcast for processing
        by_podcast = {}
        for ep in episodes:
            podcast_name = ep[1]
            if podcast_name not in by_podcast:
                by_podcast[podcast_name] = []
            by_podcast[podcast_name].append(ep)
        
        results = {}
        total_found = 0
        
        # Process each podcast type
        for podcast_name, episodes in by_podcast.items():
            source_info = self.transcript_sources.get(podcast_name, {})
            status = source_info.get('status', 'UNKNOWN')
            
            print(f"\n🎙️ Processing {podcast_name} ({len(episodes)} episodes, status: {status})")
            
            if status == 'WORKING':
                found = self._process_working_podcast(podcast_name, episodes, source_info)
                results[podcast_name] = {'found': found, 'total': len(episodes)}
                total_found += found
            elif status == 'PAYWALL':
                found = self._process_paywall_podcast(podcast_name, episodes, source_info)
                results[podcast_name] = {'found': found, 'total': len(episodes)}
                total_found += found
            elif status == 'PARTIAL':
                found = self._process_partial_podcast(podcast_name, episodes, source_info)
                results[podcast_name] = {'found': found, 'total': len(episodes)}
                total_found += found
            else:
                print(f"   ⏸️  Skipping {status} podcast")
                results[podcast_name] = {'found': 0, 'total': len(episodes)}
        
        print(f"\n✅ Processing complete! Found {total_found} new transcripts")
        return results
    
    def _process_working_podcast(self, podcast_name, episodes, source_info):
        """Process podcasts with working transcript access"""
        found_count = 0
        
        if podcast_name == "Lex Fridman Podcast":
            found_count = self._process_lex_fridman(episodes)
        elif podcast_name == "This American Life":
            found_count = self._process_this_american_life(episodes)
        
        return found_count
    
    def _process_lex_fridman(self, episodes):
        """Process Lex Fridman transcripts using our discovered pattern"""
        found_count = 0
        
        # Process in batches for efficiency
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_episode = {}
            
            for episode in episodes[:50]:  # Process 50 at a time
                ep_id, podcast_name, title, url, pub_date = episode
                
                # Skip if we already have this transcript
                if self._has_transcript(ep_id):
                    continue
                
                future = executor.submit(self._fetch_lex_fridman_transcript, ep_id, title)
                future_to_episode[future] = episode
            
            for future in as_completed(future_to_episode):
                episode = future_to_episode[future]
                try:
                    transcript_text = future.result()
                    if transcript_text:
                        self._save_transcript(episode[0], transcript_text, f"lexfridman.com")
                        found_count += 1
                        print(f"   ✅ Found transcript for: {episode[2][:60]}...")
                except Exception as e:
                    print(f"   ❌ Failed {episode[2][:60]}: {e}")
        
        return found_count
    
    def _fetch_lex_fridman_transcript(self, episode_id, title):
        """Fetch Lex Fridman transcript using our pattern"""
        # Extract guest name from title
        guest_match = re.search(r'#\d+\s*[-–]\s*([^:]+)', title)
        if not guest_match:
            return None
        
        guest_name = guest_match.group(1).strip()
        # Create slug
        slug = re.sub(r'[^\w\s-]', '', guest_name.lower())
        slug = re.sub(r'[-\s]+', '-', slug).strip('-')
        
        transcript_url = f"https://lexfridman.com/{slug}-transcript"
        
        try:
            response = self.session.get(transcript_url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find transcript content
                transcript_div = soup.find('div', class_='transcript') or soup.find('div', {'id': 'transcript'})
                if transcript_div:
                    text = transcript_div.get_text(strip=True)
                    if len(text) > 1000:  # Must be substantial
                        return text
                
                # Fallback: look for any large text blocks
                content = soup.find('main') or soup.find('article') or soup.find('body')
                if content:
                    text = content.get_text(strip=True)
                    if len(text) > 5000:
                        return text
                        
        except Exception as e:
            print(f"      Error fetching {transcript_url}: {e}")
        
        return None
    
    def _process_this_american_life(self, episodes):
        """Process This American Life transcripts"""
        found_count = 0
        
        for episode in episodes[:20]:  # Process 20 at a time
            ep_id, podcast_name, title, url, pub_date = episode
            
            if self._has_transcript(ep_id):
                continue
            
            # Extract episode number from title
            ep_match = re.search(r'(\d+):', title)
            if not ep_match:
                continue
            
            ep_num = ep_match.group(1)
            transcript_url = f"https://www.thisamericanlife.org/{ep_num}/transcript"
            
            try:
                response = self.session.get(transcript_url, timeout=15)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Find transcript content
                    transcript_content = soup.find('div', class_='transcript-section')
                    if transcript_content:
                        text = transcript_content.get_text(strip=True)
                        if len(text) > 2000:
                            self._save_transcript(ep_id, text, transcript_url)
                            found_count += 1
                            print(f"   ✅ Found transcript for: {title[:60]}...")
                            
            except Exception as e:
                print(f"   ❌ Failed {title[:60]}: {e}")
        
        return found_count
    
    def _process_paywall_podcast(self, podcast_name, episodes, source_info):
        """Process podcasts behind paywalls (with auth)"""
        auth_type = source_info.get('auth_type')
        
        if auth_type == 'NYTIMES_LOGIN':
            return self._process_nytimes_podcasts(podcast_name, episodes)
        elif auth_type == 'STRATECHERY_EMAIL':
            return self._process_stratechery_podcasts(podcast_name, episodes)
        
        return 0
    
    def _process_nytimes_podcasts(self, podcast_name, episodes):
        """Process NYTimes podcasts (Hard Fork, Ezra Klein)"""
        # Would need to implement NYTimes authentication
        # For now, skip but log that we need credentials
        print(f"   🔐 {podcast_name} requires NYTimes authentication - skipping for now")
        return 0
    
    def _process_stratechery_podcasts(self, podcast_name, episodes):
        """Process Stratechery podcasts"""
        # Would need to implement Stratechery email authentication
        print(f"   🔐 {podcast_name} requires Stratechery authentication - skipping for now")
        return 0
    
    def _process_partial_podcast(self, podcast_name, episodes, source_info):
        """Process podcasts with partial transcript availability"""
        if podcast_name == "EconTalk":
            return self._process_econtalk(episodes)
        return 0
    
    def _process_econtalk(self, episodes):
        """Process EconTalk partial transcripts"""
        found_count = 0
        
        for episode in episodes[:10]:  # Test with 10
            ep_id, podcast_name, title, url, pub_date = episode
            
            if self._has_transcript(ep_id):
                continue
            
            # Try common EconTalk URL patterns
            title_slug = re.sub(r'[^\w\s-]', '', title.lower())
            title_slug = re.sub(r'[-\s]+', '-', title_slug).strip('-')
            
            potential_urls = [
                f"https://www.econtalk.org/{title_slug}/",
                f"https://www.econtalk.org/podcast/{title_slug}/",
            ]
            
            for test_url in potential_urls:
                try:
                    response = self.session.get(test_url, timeout=10)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        
                        # Look for transcript content
                        transcript_div = soup.find('div', class_='transcript') or \
                                       soup.find('div', {'id': 'transcript'})
                        
                        if transcript_div:
                            text = transcript_div.get_text(strip=True)
                            if len(text) > 2000:
                                self._save_transcript(ep_id, text, test_url)
                                found_count += 1
                                print(f"   ✅ Found EconTalk transcript: {title[:60]}...")
                                break
                                
                except Exception:
                    continue
        
        return found_count
    
    def _has_transcript(self, episode_id):
        """Check if we already have a transcript for this episode"""
        with sqlite3.connect(self.db_path) as conn:
            result = conn.execute("""
                SELECT 1 FROM content 
                WHERE source_episode_id = ? AND content_type = 'transcript'
            """, (episode_id,)).fetchone()
        return result is not None
    
    def _save_transcript(self, episode_id, transcript_text, source_url):
        """Save transcript to database"""
        content_id = hashlib.sha256(f"transcript_{episode_id}".encode()).hexdigest()[:16]
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT OR REPLACE INTO content (
                    id, title, content, content_type, source_episode_id, url, 
                    created_date, processed, word_count
                ) VALUES (?, ?, ?, 'transcript', ?, ?, ?, 1, ?)
            """, (
                content_id,
                f"Transcript for episode {episode_id}",
                transcript_text,
                episode_id,
                source_url,
                datetime.now().isoformat(),
                len(transcript_text.split())
            ))

def main():
    processor = ComprehensiveTranscriptProcessor()
    results = processor.process_all_podcasts()
    
    # Print summary
    print(f"\n📈 PROCESSING SUMMARY:")
    print(f"{'Podcast':<40} {'Found':<10} {'Total':<10} {'Rate':<10}")
    print("-" * 70)
    
    total_found = 0
    total_episodes = 0
    
    for podcast, stats in results.items():
        found = stats['found']
        total = stats['total']
        rate = f"{found/total*100:.1f}%" if total > 0 else "0%"
        
        print(f"{podcast[:39]:<40} {found:<10} {total:<10} {rate:<10}")
        total_found += found
        total_episodes += total
    
    print("-" * 70)
    overall_rate = f"{total_found/total_episodes*100:.1f}%" if total_episodes > 0 else "0%"
    print(f"{'TOTAL':<40} {total_found:<10} {total_episodes:<10} {overall_rate:<10}")

if __name__ == "__main__":
    main()