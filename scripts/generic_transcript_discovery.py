#!/usr/bin/env python3
"""
Generic Podcast Transcript Discovery System
Works for ALL podcasts using learned patterns
"""

import sys
import os
sys.path.append('/home/ubuntu/dev/atlas')

import requests
import sqlite3
import time
import re
from urllib.parse import urlparse, urljoin
from collections import defaultdict
import json
from pathlib import Path

class GenericTranscriptDiscovery:
    """Generic discovery system that learns patterns from successful finds"""
    
    def __init__(self):
        self.db_path = Path("data/podcasts/atlas_podcasts.db")
        self.patterns_file = Path("data/podcasts/transcript_patterns.json")
        self.patterns_file.parent.mkdir(parents=True, exist_ok=True)
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; Atlas-Pod/1.0)'
        })
        
        # Load or create pattern database
        self.patterns = self._load_patterns()
    
    def discover_for_podcast(self, podcast_id, max_episodes=None):
        """Discover transcripts for a specific podcast using its learned patterns"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get podcast info
        cursor.execute("SELECT name FROM podcasts WHERE id = ?", (podcast_id,))
        podcast_name = cursor.fetchone()[0]
        
        print(f"🎙️ Discovering transcripts for: {podcast_name}")
        
        # Get known patterns for this podcast
        podcast_patterns = self.patterns.get(str(podcast_id), {})
        
        if not podcast_patterns.get('sources'):
            print("   ❌ No known patterns - learning from existing transcripts...")
            self._learn_patterns_for_podcast(podcast_id)
            podcast_patterns = self.patterns.get(str(podcast_id), {})
        
        # Get episodes without transcripts
        if max_episodes is None:
            cursor.execute("""
                SELECT id, title, url FROM episodes 
                WHERE podcast_id = ? 
                AND (transcript_status IS NULL OR transcript_status != 'found')
                AND transcript_url IS NULL
                ORDER BY id DESC
            """, (podcast_id,))
        else:
            cursor.execute("""
                SELECT id, title, url FROM episodes 
                WHERE podcast_id = ? 
                AND (transcript_status IS NULL OR transcript_status != 'found')
                AND transcript_url IS NULL
                ORDER BY id DESC
                LIMIT ?
            """, (podcast_id, max_episodes))
        
        episodes = cursor.fetchall()
        print(f"   📊 Testing {len(episodes)} episodes without transcripts")
        
        found_count = 0
        total_episodes = len(episodes)
        
        for i, (episode_id, title, episode_url) in enumerate(episodes, 1):
            print(f"   🔍 [{i}/{total_episodes}] {title[:50]}...")
            
            # Try each known source pattern
            for source_pattern in podcast_patterns.get('sources', []):
                transcript_url = self._try_pattern(source_pattern, title, episode_url)
                
                if transcript_url:
                    print(f"      ✅ [{found_count + 1}] Found: {transcript_url}")
                    
                    # Update database
                    cursor.execute("""
                        UPDATE episodes 
                        SET transcript_url = ?, transcript_status = 'found'
                        WHERE id = ?
                    """, (transcript_url, episode_id))
                    
                    found_count += 1
                    break  # Found one, move to next episode
            
            # Show progress every 50 episodes
            if i % 50 == 0:
                print(f"   📊 Progress: {i}/{total_episodes} episodes checked, {found_count} transcripts found")
            
            time.sleep(1)  # Rate limiting
        
        conn.commit()
        conn.close()
        
        print(f"   📊 Found {found_count} new transcripts")
        
        # Update success stats
        if str(podcast_id) in self.patterns:
            self.patterns[str(podcast_id)]['last_run'] = time.time()
            self.patterns[str(podcast_id)]['total_found'] = self.patterns[str(podcast_id)].get('total_found', 0) + found_count
        
        self._save_patterns()
        
        return found_count
    
    def discover_all_podcasts(self, max_per_podcast=None):
        """Run discovery on all podcasts with existing transcripts"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get podcasts that have at least one transcript
        cursor.execute("""
            SELECT DISTINCT p.id, p.name, COUNT(e.transcript_url) as transcript_count
            FROM podcasts p
            JOIN episodes e ON p.id = e.podcast_id  
            WHERE e.transcript_url IS NOT NULL
            GROUP BY p.id, p.name
            ORDER BY transcript_count DESC
        """)
        
        podcasts = cursor.fetchall()
        conn.close()
        
        print(f"🚀 Running discovery on {len(podcasts)} podcasts with existing transcripts")
        
        total_found = 0
        
        for podcast_id, podcast_name, existing_count in podcasts:
            print(f"\n📡 Processing: {podcast_name} ({existing_count} existing)")
            
            found = self.discover_for_podcast(podcast_id, max_per_podcast)
            total_found += found
            
            if found > 0:
                print(f"   ✨ Success! Found {found} additional transcripts")
        
        print(f"\n🎯 TOTAL RESULTS: {total_found} new transcripts discovered")
        
        return total_found
    
    def _learn_patterns_for_podcast(self, podcast_id):
        """Learn transcript URL patterns from existing successful finds"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get existing transcript URLs for this podcast
        cursor.execute("""
            SELECT transcript_url, title FROM episodes 
            WHERE podcast_id = ? AND transcript_url IS NOT NULL
        """, (podcast_id,))
        
        transcript_data = cursor.fetchall()
        conn.close()
        
        if not transcript_data:
            return
        
        # Analyze patterns
        sources = set()
        url_patterns = []
        
        for transcript_url, title in transcript_data:
            domain = urlparse(transcript_url).netloc
            sources.add(domain)
            
            # Extract URL pattern
            pattern = self._extract_url_pattern(transcript_url, title)
            if pattern:
                url_patterns.append(pattern)
        
        # Store learned patterns
        self.patterns[str(podcast_id)] = {
            'sources': list(sources),
            'url_patterns': url_patterns,
            'learned_from': len(transcript_data),
            'total_found': 0,
            'last_run': None
        }
        
        print(f"   📚 Learned {len(sources)} sources, {len(url_patterns)} patterns")
    
    def _extract_url_pattern(self, transcript_url, title):
        """Extract a reusable URL pattern from a successful transcript URL"""
        
        parsed = urlparse(transcript_url)
        base_url = f"{parsed.scheme}://{parsed.netloc}"
        
        # Common patterns to detect
        patterns = {
            'episode_slug': r'/([^/]+)/?$',  # Last part of URL
            'transcript_suffix': r'(.+)-transcript',
            'transcript_query': r'\?.*transcript',
            'transcript_hash': r'#transcript',
            'episode_id': r'/(\d+)/',
        }
        
        for pattern_name, regex in patterns.items():
            if re.search(regex, transcript_url):
                return {
                    'type': pattern_name,
                    'base_url': base_url,
                    'template': transcript_url,
                    'regex': regex
                }
        
        return {'type': 'direct', 'base_url': base_url, 'template': transcript_url}
    
    def _try_pattern(self, source_domain, title, episode_url):
        """Try to find transcript URL using learned patterns"""
        
        # Generate possible transcript URLs
        candidates = []
        
        # Pattern 1: {domain}/{guest-name}-transcript
        guest_name = self._extract_guest_name(title)
        if guest_name:
            candidates.append(f"https://{source_domain}/{guest_name}-transcript")
        
        # Pattern 2: {domain}/transcripts/{episode-slug}
        episode_slug = self._title_to_slug(title)
        candidates.extend([
            f"https://{source_domain}/transcripts/{episode_slug}",
            f"https://{source_domain}/transcript/{episode_slug}",
            f"https://{source_domain}/{episode_slug}#transcript",
            f"https://{source_domain}/{episode_slug}?transcript=1",
        ])
        
        # Pattern 3: Episode number based
        episode_number = self._extract_episode_number(title)
        if episode_number:
            candidates.extend([
                f"https://{source_domain}/transcripts/{episode_number}",
                f"https://{source_domain}/{episode_number}/transcript",
            ])
        
        # Test each candidate
        for candidate in candidates:
            try:
                response = self.session.get(candidate, timeout=10)
                if response.status_code == 200 and self._looks_like_transcript(response.text):
                    return candidate
            except:
                continue
        
        return None
    
    def _extract_guest_name(self, title):
        """Extract guest name from episode title"""
        # Remove episode number
        title = re.sub(r'^#?\d+\s*[-–—:]\s*', '', title)
        
        # Extract guest name (everything before first colon)
        guest = title.split(':')[0].split(',')[0].strip()
        
        # Convert to slug
        return self._title_to_slug(guest)
    
    def _extract_episode_number(self, title):
        """Extract episode number from title"""
        match = re.search(r'#?(\d+)', title)
        return match.group(1) if match else None
    
    def _title_to_slug(self, text):
        """Convert text to URL slug"""
        if not text:
            return ""
        
        slug = re.sub(r'[^\w\s-]', '', text).strip().lower()
        slug = re.sub(r'[-\s]+', '-', slug)
        return slug.strip('-')
    
    def _looks_like_transcript(self, html_content):
        """Quick check if content looks like a transcript"""
        content_lower = html_content.lower()
        
        # Check for transcript indicators
        indicators = ['transcript', 'speaker:', 'host:', 'guest:', '[music]', '[applause]']
        
        return any(indicator in content_lower for indicator in indicators)
    
    def _load_patterns(self):
        """Load learned patterns from file"""
        try:
            if self.patterns_file.exists():
                with open(self.patterns_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        
        return {}
    
    def _save_patterns(self):
        """Save learned patterns to file"""
        try:
            with open(self.patterns_file, 'w') as f:
                json.dump(self.patterns, f, indent=2)
        except Exception as e:
            print(f"Error saving patterns: {e}")

def main():
    """Run generic transcript discovery"""
    
    discovery = GenericTranscriptDiscovery()
    
    if len(sys.argv) > 1 and sys.argv[1] == '--single':
        # Test on single podcast
        podcast_id = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        found = discovery.discover_for_podcast(podcast_id)  # No episode limit for production
        print(f"Found {found} transcripts for podcast {podcast_id}")
    else:
        # Run on all podcasts
        total_found = discovery.discover_all_podcasts()  # No episode limit for production
        print(f"Total new transcripts discovered: {total_found}")

if __name__ == "__main__":
    main()