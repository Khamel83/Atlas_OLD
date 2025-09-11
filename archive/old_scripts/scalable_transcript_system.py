#!/usr/bin/env python3
"""
Scalable Podcast Transcript Discovery System

Automatically discovers transcript sources for ANY podcast, not just hardcoded ones.
Works for 35 podcasts now, will work for 50, 100, or 1000 podcasts later.

Strategy:
1. Auto-detect podcast network/publisher from RSS/website
2. Apply network-specific transcript discovery patterns  
3. Build and cache transcript source mapping dynamically
4. Fallback to universal transcript aggregators
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import json
import time
from urllib.parse import urljoin, urlparse
import csv
from pathlib import Path

class ScalableTranscriptDiscoverer:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        # Cache file for discovered sources
        self.cache_file = Path("podcast_sources_cache.json")
        self.load_cache()
        
        # Network patterns for auto-detection
        self.network_patterns = {
            "NPR": {
                "domains": ["npr.org", "thisamericanlife.org"],
                "selectors": [".transcript", ".storytext", ".story-text"],
                "min_length": 1000
            },
            "Slate": {
                "domains": ["slate.com"],
                "selectors": [".article-body", ".post-content"],
                "min_length": 800
            },
            "NYTimes": {
                "domains": ["nytimes.com"],
                "selectors": [".story-body-text", ".article-body"],
                "min_length": 1200
            },
            "WSJ": {
                "domains": ["wsj.com"],
                "selectors": [".article-body", ".wsj-article-body"],
                "min_length": 1000
            },
            "Vox/Verge": {
                "domains": ["theverge.com", "vox.com"],
                "selectors": [".article-body", ".entry-content"],
                "min_length": 1000
            },
            "TheRinger": {
                "domains": ["theringer.com"],
                "selectors": [".article-content", ".post-content"],
                "min_length": 800
            },
            "Gimlet/Spotify": {
                "domains": ["gimletmedia.com", "spotify.com"],
                "selectors": [".transcript", ".episode-transcript"],
                "min_length": 1000
            },
            "WNYC": {
                "domains": ["wnyc.org", "radiolab.org"],
                "selectors": [".transcript-content", ".story-body"],
                "min_length": 1000
            }
        }
        
        # Universal fallback services
        self.universal_fallbacks = [
            "https://www.happyscribe.com/",
            "https://otter.ai/",
            "https://rev.com/",
            "https://sonix.ai/"
        ]
    
    def load_cache(self):
        """Load cached podcast source discoveries"""
        if self.cache_file.exists():
            with open(self.cache_file, 'r') as f:
                self.source_cache = json.load(f)
        else:
            self.source_cache = {}
    
    def save_cache(self):
        """Save discovered sources to cache"""
        with open(self.cache_file, 'w') as f:
            json.dump(self.source_cache, f, indent=2)
    
    def auto_detect_network(self, rss_url):
        """Auto-detect podcast network from RSS URL"""
        if not rss_url:
            return None
            
        domain = urlparse(rss_url).netloc.lower()
        
        for network, config in self.network_patterns.items():
            if any(net_domain in domain for net_domain in config["domains"]):
                return network
        
        return None
    
    def discover_transcript_source(self, podcast_name, rss_url):
        """Discover transcript source for any podcast"""
        
        # Check cache first
        cache_key = f"{podcast_name}_{rss_url}"
        if cache_key in self.source_cache:
            return self.source_cache[cache_key]
        
        # Auto-detect network
        network = self.auto_detect_network(rss_url)
        if network:
            source_info = {
                "network": network,
                "config": self.network_patterns[network],
                "discovered": True
            }
            self.source_cache[cache_key] = source_info
            self.save_cache()
            return source_info
        
        # Try to discover from RSS feed
        source_info = self.discover_from_rss(rss_url)
        if source_info:
            self.source_cache[cache_key] = source_info
            self.save_cache()
            return source_info
        
        # Generic website discovery
        source_info = self.discover_generic_patterns(podcast_name, rss_url)
        if source_info:
            self.source_cache[cache_key] = source_info
            self.save_cache()
            return source_info
        
        return None
    
    def discover_from_rss(self, rss_url):
        """Try to discover transcript sources from RSS feed"""
        try:
            response = self.session.get(rss_url, timeout=10)
            response.raise_for_status()
            
            # Parse RSS for transcript links
            from xml.etree import ElementTree as ET
            root = ET.fromstring(response.content)
            
            # Look for transcript links in RSS
            transcript_links = []
            for item in root.findall('.//item')[:5]:  # Check first 5 episodes
                # Check for transcript links
                for link_elem in item.findall('.//link'):
                    link = link_elem.text
                    if link and ('transcript' in link.lower() or 'show-notes' in link.lower()):
                        transcript_links.append(link)
                
                # Check episode website links
                for link_elem in item.findall('.//link'):
                    if link_elem.text:
                        transcript_links.append(link_elem.text)
            
            if transcript_links:
                # Test first link to see what network it belongs to
                test_link = transcript_links[0]
                network = self.auto_detect_network(test_link)
                
                return {
                    "network": network or "Generic",
                    "sample_links": transcript_links[:3],
                    "discovered": True,
                    "source": "RSS"
                }
        
        except Exception as e:
            print(f"  RSS discovery failed: {e}")
        
        return None
    
    def discover_generic_patterns(self, podcast_name, rss_url):
        """Generic pattern discovery for unknown podcasts"""
        
        # Common transcript URL patterns
        base_patterns = [
            "transcripts.{domain}",
            "{domain}/transcripts",
            "{domain}/episodes/transcript",
            "{domain}/podcast/transcript"
        ]
        
        # Extract domain from RSS
        if rss_url:
            domain = urlparse(rss_url).netloc.replace('www.', '').replace('feeds.', '')
            
            return {
                "network": "Generic",
                "patterns": [p.format(domain=domain) for p in base_patterns],
                "discovered": False,
                "needs_testing": True
            }
        
        return None
    
    def scrape_with_network_config(self, url, network_config):
        """Scrape transcript using network-specific configuration"""
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try network-specific selectors
            for selector in network_config["selectors"]:
                elements = soup.select(selector)
                for element in elements:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) >= network_config["min_length"]:
                        return text
            
            # Fallback to generic large text blocks
            all_divs = soup.find_all(['div', 'article', 'section'])
            for div in all_divs:
                text = div.get_text(separator=' ', strip=True)
                if len(text) >= network_config["min_length"] * 2:  # Higher bar for generic
                    return text
        
        except Exception as e:
            print(f"  Scraping error: {e}")
        
        return None
    
    def get_transcript_for_episode(self, podcast_name, episode_title, episode_url, rss_url):
        """Get transcript using scalable discovery"""
        
        # Discover source for this podcast
        source_info = self.discover_transcript_source(podcast_name, rss_url)
        
        if not source_info:
            return None
        
        # Use discovered network configuration
        if source_info.get("network") in self.network_patterns:
            network_config = self.network_patterns[source_info["network"]]
            return self.scrape_with_network_config(episode_url or rss_url, network_config)
        
        # Generic scraping approach
        return self.scrape_generic_transcript(episode_url or rss_url)
    
    def scrape_generic_transcript(self, url):
        """Generic transcript scraping"""
        if not url:
            return None
            
        try:
            response = self.session.get(url, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Universal transcript indicators
            transcript_selectors = [
                '.transcript', '.episode-transcript', '.show-transcript',
                '.article-body', '.post-content', '.entry-content',
                '.episode-content', '.story-body', '.show-notes'
            ]
            
            for selector in transcript_selectors:
                elements = soup.select(selector)
                for element in elements:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) > 800:
                        return text
        
        except Exception as e:
            print(f"  Generic scraping error: {e}")
        
        return None

def process_all_podcasts():
    """Process ALL podcasts in the system scalably"""
    discoverer = ScalableTranscriptDiscoverer()
    
    # Get all podcasts from CSV
    podcasts_data = []
    with open('config/podcasts_prioritized_updated.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['Podcast Name'].strip()
            rss = row['RSS_URL'].strip()
            if name and rss and rss != '0':
                podcasts_data.append((name, rss))
    
    print(f"Discovering transcript sources for {len(podcasts_data)} podcasts...")
    
    # Discover sources for all podcasts
    for podcast_name, rss_url in podcasts_data:
        print(f"Discovering: {podcast_name}")
        source_info = discoverer.discover_transcript_source(podcast_name, rss_url)
        if source_info:
            network = source_info.get("network", "Unknown")
            print(f"  ✓ Network: {network}")
        else:
            print(f"  ✗ No source discovered")
    
    print(f"\nSource discovery complete. Cache saved to {discoverer.cache_file}")
    
    # Now process episodes using discovered sources
    with sqlite3.connect("data/atlas.db") as conn:
        episodes = conn.execute("""
            SELECT id, title, podcast_name, audio_url
            FROM podcast_episodes
            WHERE processed = 0 
            LIMIT 50
        """).fetchall()
        
        success_count = 0
        
        # Get RSS URLs from cache
        rss_lookup = {}
        for name, rss in podcasts_data:
            rss_lookup[name] = rss
        
        for episode_id, title, podcast, audio_url in episodes:
            print(f"Processing: {podcast} - {title[:30]}...")
            
            rss_url = rss_lookup.get(podcast, "")
            transcript = discoverer.get_transcript_for_episode(podcast, title, audio_url, rss_url)
            
            if transcript:
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_transcript', CURRENT_TIMESTAMP)
                """, (f"[TRANSCRIPT] {title}", transcript))
                
                success_count += 1
                print(f"  ✓ Transcript: {len(transcript)} chars")
            else:
                print("  → No transcript found")
            
            # Mark as processed
            conn.execute("""
                UPDATE podcast_episodes 
                SET processed = 1 
                WHERE id = ?
            """, (episode_id,))
        
        conn.commit()
        print(f"\nProcessed {len(episodes)} episodes, found {success_count} transcripts")

if __name__ == "__main__":
    process_all_podcasts()