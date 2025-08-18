#!/usr/bin/env python3
"""
Simple Transcript Discovery - Run Weekly

Simple approach: 
1. Find podcasts that already have some transcripts
2. Check if those same sources have more episodes
3. Try common patterns for big transcript sites (Rev, Otter, etc.)
4. Save results and don't overthink it

Run this once a week, not constantly.
"""

import sys
sys.path.append('/home/ubuntu/dev/atlas')

import requests
import time
from urllib.parse import urlparse, urljoin
import re
from pathlib import Path
import json
from datetime import datetime
import sqlite3

from helpers.config import load_config

class SimpleTranscriptDiscovery:
    """Simple weekly transcript discovery"""
    
    def __init__(self):
        self.config = load_config()
        self.db_path = Path("data/podcasts/atlas_podcasts.db")
        self.results_file = Path("data/podcasts/weekly_transcript_check.json")
        self.results_file.parent.mkdir(parents=True, exist_ok=True)
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; Atlas-Pod/1.0)'
        })
    
    def run_weekly_check(self):
        """Run the weekly transcript discovery"""
        print("🔍 Starting weekly transcript discovery...")
        
        results = {
            'date': datetime.now().isoformat(),
            'podcasts_checked': 0,
            'new_transcripts_found': 0,
            'sources_discovered': []
        }
        
        # 1. Get podcasts that already have some transcripts
        podcasts_with_transcripts = self._get_podcasts_with_transcripts()
        print(f"📊 Found {len(podcasts_with_transcripts)} podcasts with existing transcripts")
        
        # 2. For each podcast, check their transcript sources for more episodes
        for podcast in podcasts_with_transcripts:
            print(f"\n🎙️ Checking: {podcast['title']}")
            
            new_count = self._check_podcast_sources(podcast)
            results['new_transcripts_found'] += new_count
            results['podcasts_checked'] += 1
            
            # Rate limiting
            time.sleep(2)
        
        # 3. Try common transcript sites for popular podcasts
        popular_podcasts = self._get_popular_podcasts()
        for podcast in popular_podcasts[:10]:  # Top 10 only
            print(f"\n🌟 Checking popular podcast: {podcast['title']}")
            
            new_count = self._try_common_sources(podcast)
            results['new_transcripts_found'] += new_count
            
            time.sleep(1)
        
        # Save results
        with open(self.results_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print("\n✅ Weekly check complete!")
        print(f"   📊 Checked {results['podcasts_checked']} podcasts")
        print(f"   🎯 Found {results['new_transcripts_found']} new transcripts")
        
        return results
    
    def _get_podcasts_with_transcripts(self):
        """Get podcasts that already have transcripts found"""
        podcasts = []
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get podcasts with at least one transcript
            cursor.execute("""
                SELECT DISTINCT p.id, p.name, p.rss_url, p.config
                FROM podcasts p
                JOIN episodes e ON p.id = e.podcast_id  
                WHERE e.transcript_status = 'found'
                OR e.transcript_url IS NOT NULL
                ORDER BY p.name
            """)
            
            for row in cursor.fetchall():
                podcast_id, name, rss_url, config_json = row
                config = json.loads(config_json) if config_json else {}
                
                podcasts.append({
                    'id': podcast_id,
                    'title': name,  # Use name as title
                    'rss_url': rss_url,
                    'config': config
                })
            
            conn.close()
            
        except Exception as e:
            print(f"Error getting podcasts with transcripts: {e}")
        
        return podcasts
    
    def _get_popular_podcasts(self):
        """Get popular podcasts (most episodes) to check"""
        podcasts = []
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get podcasts with most episodes
            cursor.execute("""
                SELECT p.id, p.name, p.rss_url, p.config, COUNT(e.id) as episode_count
                FROM podcasts p
                LEFT JOIN episodes e ON p.id = e.podcast_id
                GROUP BY p.id
                ORDER BY episode_count DESC
                LIMIT 20
            """)
            
            for row in cursor.fetchall():
                podcast_id, name, rss_url, config_json, episode_count = row
                config = json.loads(config_json) if config_json else {}
                
                podcasts.append({
                    'id': podcast_id,
                    'title': name,  # Use name as title
                    'rss_url': rss_url,
                    'config': config,
                    'episode_count': episode_count
                })
            
            conn.close()
            
        except Exception as e:
            print(f"Error getting popular podcasts: {e}")
        
        return podcasts
    
    def _check_podcast_sources(self, podcast):
        """Check known transcript sources for this podcast for more episodes"""
        new_transcripts = 0
        
        try:
            # Get existing transcript sources for this podcast
            sources = self._get_transcript_sources(podcast['id'])
            
            for source in sources:
                domain = urlparse(source).netloc
                print(f"   🔗 Checking source: {domain}")
                
                # Try to find more episodes on this source
                new_count = self._scan_source_for_episodes(source, podcast)
                new_transcripts += new_count
                
                if new_count > 0:
                    print(f"      ✅ Found {new_count} new transcripts")
        
        except Exception as e:
            print(f"   ❌ Error checking sources: {e}")
        
        return new_transcripts
    
    def _get_transcript_sources(self, podcast_id):
        """Get list of domains/URLs where we've found transcripts for this podcast"""
        sources = set()
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT transcript_url, metadata FROM episodes 
                WHERE podcast_id = ? 
                AND (transcript_status = 'found' OR transcript_url IS NOT NULL)
            """, (podcast_id,))
            
            for row in cursor.fetchall():
                transcript_url, metadata_json = row
                
                # Add direct transcript URL
                if transcript_url:
                    sources.add(transcript_url)
                
                # Add any metadata transcript links
                if metadata_json:
                    metadata = json.loads(metadata_json) if metadata_json else {}
                    transcript_links = metadata.get('transcript_links', [])
                    
                    for link in transcript_links:
                        if isinstance(link, str):
                            sources.add(link)
            
            conn.close()
            
        except Exception as e:
            print(f"Error getting transcript sources: {e}")
        
        return list(sources)
    
    def _scan_source_for_episodes(self, source_url, podcast):
        """Scan a known source for more episodes"""
        new_count = 0
        
        try:
            # Get the base domain/path
            parsed = urlparse(source_url)
            base_url = f"{parsed.scheme}://{parsed.netloc}"
            
            # Try common patterns for finding more episodes
            search_patterns = [
                f"{base_url}/search?q={self._slugify(podcast['title'])}",
                f"{base_url}/{self._slugify(podcast['title'])}",
                f"{base_url}/shows/{self._slugify(podcast['title'])}",
                f"{base_url}/podcast/{self._slugify(podcast['title'])}",
            ]
            
            for pattern in search_patterns:
                try:
                    response = self.session.get(pattern, timeout=10)
                    if response.status_code == 200:
                        # Look for episode links
                        episode_links = self._extract_episode_links(response.text, base_url)
                        
                        # Check which ones we don't have yet
                        for link in episode_links[:5]:  # Limit to avoid spam
                            if self._is_new_episode(link, podcast['id']):
                                print(f"      📝 New episode found: {link}")
                                new_count += 1
                                # TODO: Add to database
                        
                        if episode_links:
                            break  # Found the right pattern
                            
                except Exception:
                    continue
                    
        except Exception as e:
            print(f"Error scanning source {source_url}: {e}")
        
        return new_count
    
    def _try_common_sources(self, podcast):
        """Try common transcript sites for this podcast"""
        new_count = 0
        
        podcast_slug = self._slugify(podcast['title'])
        
        # Common transcript sites to check
        sites_to_try = [
            f"https://www.rev.com/transcript/{podcast_slug}",
            f"https://otter.ai/u/{podcast_slug}",
            f"https://podscripts.co/{podcast_slug}",
            f"https://transcripts.{podcast_slug}.com",
            f"https://{podcast_slug}.com/transcripts",
            f"https://{podcast_slug}.com/episodes",
        ]
        
        for site in sites_to_try:
            try:
                response = self.session.get(site, timeout=10)
                if response.status_code == 200:
                    print(f"   ✅ Found site: {site}")
                    
                    # Look for episode links
                    episode_links = self._extract_episode_links(response.text, site)
                    
                    for link in episode_links[:3]:  # Limit check
                        if self._looks_like_transcript(link):
                            print(f"      📝 Potential transcript: {link}")
                            new_count += 1
                            
            except Exception:
                continue
        
        return new_count
    
    def _extract_episode_links(self, html, base_url):
        """Extract episode links from HTML"""
        links = []
        
        try:
            from bs4 import BeautifulSoup
            import warnings
            from bs4 import XMLParsedAsHTMLWarning
            warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
            
            soup = BeautifulSoup(html, 'html.parser')
            
            # Look for links that might be episodes
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                text = link.get_text().lower()
                
                # Skip navigation links
                if any(skip in text for skip in ['home', 'about', 'contact', 'privacy']):
                    continue
                
                # Look for episode-like links
                if any(word in text for word in ['episode', 'transcript', 'show']) or \
                   any(word in href.lower() for word in ['episode', 'transcript', 'ep']):
                    
                    full_url = urljoin(base_url, href)
                    links.append(full_url)
            
        except ImportError:
            print("BeautifulSoup not available")
        except Exception as e:
            print(f"Error extracting links: {e}")
        
        return list(set(links))  # Remove duplicates
    
    def _looks_like_transcript(self, url):
        """Quick check if URL looks like it could have a transcript"""
        url_lower = url.lower()
        return any(word in url_lower for word in [
            'transcript', 'transcription', 'text', 'notes'
        ])
    
    def _is_new_episode(self, url, podcast_id):
        """Check if this episode URL is new to our database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT COUNT(*) FROM episodes 
                WHERE podcast_id = ? AND url = ?
            """, (podcast_id, url))
            
            count = cursor.fetchone()[0]
            conn.close()
            
            return count == 0
            
        except Exception as e:
            print(f"Error checking if episode is new: {e}")
            return False
    
    def _slugify(self, text):
        """Convert text to URL slug"""
        if not text:
            return ""
        
        # Basic slugification
        slug = re.sub(r'[^\w\s-]', '', text).strip().lower()
        slug = re.sub(r'[-\s]+', '-', slug)
        
        return slug

def main():
    """Run weekly transcript discovery"""
    discovery = SimpleTranscriptDiscovery()
    results = discovery.run_weekly_check()
    
    print("\n📊 Summary:")
    print(f"   Podcasts checked: {results['podcasts_checked']}")
    print(f"   New transcripts: {results['new_transcripts_found']}")

if __name__ == "__main__":
    main()