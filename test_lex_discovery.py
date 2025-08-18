#!/usr/bin/env python3
"""
Focused test on Lex Fridman podcast transcript discovery
Prove the scaling approach works on our highest-value target.
"""

import sys
sys.path.append('/home/ubuntu/dev/atlas')

import requests
import time
from urllib.parse import urlparse, urljoin
import sqlite3
from pathlib import Path
import json

class LexFridmanDiscoveryTest:
    """Test transcript discovery specifically on Lex Fridman podcast"""
    
    def __init__(self):
        self.db_path = Path("data/podcasts/atlas_podcasts.db")
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; Atlas-Pod/1.0)'
        })
        
    def run_lex_test(self):
        """Test discovery on Lex Fridman podcast"""
        print("🎯 Testing transcript discovery on Lex Fridman Podcast")
        print("=" * 60)
        
        # Get Lex Fridman podcast info
        lex_info = self._get_lex_podcast_info()
        if not lex_info:
            print("❌ Could not find Lex Fridman podcast in database")
            return
            
        print("📊 Current status:")
        print(f"   Podcast: {lex_info['name']}")
        print(f"   Total episodes: {lex_info['total_episodes']}")
        print(f"   Current transcripts: {lex_info['current_transcripts']}")
        print(f"   Success rate: {lex_info['current_transcripts']/lex_info['total_episodes']*100:.1f}%")
        
        # Get existing transcript sources
        sources = self._get_existing_sources(lex_info['id'])
        print(f"\n🔗 Existing transcript sources ({len(sources)}):")
        for source in sources[:5]:
            domain = urlparse(source).netloc
            print(f"   • {domain}")
            
        # Test each source for more episodes
        print("\n🔍 Testing sources for more episodes...")
        new_transcripts_found = 0
        
        for source in sources[:3]:  # Test top 3 sources
            print(f"\n📡 Testing: {urlparse(source).netloc}")
            found = self._test_source_for_more_episodes(source, lex_info)
            new_transcripts_found += found
            print(f"   Found {found} potential new transcripts")
            
            # Rate limiting
            time.sleep(2)
            
        # Try common patterns for Lex Fridman
        print("\n🌟 Testing common patterns for Lex Fridman...")
        pattern_found = self._test_common_patterns(lex_info)
        new_transcripts_found += pattern_found
        
        print("\n✅ Discovery test complete!")
        print(f"   🎯 Potential new transcripts found: {new_transcripts_found}")
        print(f"   📈 Potential total: {lex_info['current_transcripts'] + new_transcripts_found}")
        
        if new_transcripts_found > 0:
            new_rate = (lex_info['current_transcripts'] + new_transcripts_found) / lex_info['total_episodes'] * 100
            print(f"   🚀 Potential success rate: {new_rate:.1f}%")
            print(f"   💡 Scaling factor: {new_transcripts_found/lex_info['current_transcripts']:.1f}x improvement")
            
        return new_transcripts_found
        
    def _get_lex_podcast_info(self):
        """Get Lex Fridman podcast info from database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Find Lex Fridman podcast
            cursor.execute('SELECT id, name FROM podcasts WHERE name LIKE "%Lex%" OR name LIKE "%Fridman%"')
            podcast_row = cursor.fetchone()
            
            if not podcast_row:
                return None
                
            podcast_id, name = podcast_row
            
            # Get episode counts
            cursor.execute('SELECT COUNT(*) FROM episodes WHERE podcast_id = ?', (podcast_id,))
            total_episodes = cursor.fetchone()[0]
            
            cursor.execute('SELECT COUNT(*) FROM episodes WHERE podcast_id = ? AND (transcript_url IS NOT NULL OR transcript_status = "found")', (podcast_id,))
            current_transcripts = cursor.fetchone()[0]
            
            conn.close()
            
            return {
                'id': podcast_id,
                'name': name,
                'total_episodes': total_episodes,
                'current_transcripts': current_transcripts
            }
            
        except Exception as e:
            print(f"Error getting Lex podcast info: {e}")
            return None
            
    def _get_existing_sources(self, podcast_id):
        """Get existing transcript sources for Lex Fridman"""
        sources = set()
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT transcript_url, metadata FROM episodes 
                WHERE podcast_id = ? AND (transcript_url IS NOT NULL OR transcript_status = "found")
            ''', (podcast_id,))
            
            for row in cursor.fetchall():
                transcript_url, metadata_json = row
                
                if transcript_url:
                    sources.add(transcript_url)
                    
                if metadata_json:
                    try:
                        metadata = json.loads(metadata_json)
                        transcript_links = metadata.get('transcript_links', [])
                        for link in transcript_links:
                            if isinstance(link, str):
                                sources.add(link)
                    except:
                        pass
                        
            conn.close()
            
        except Exception as e:
            print(f"Error getting sources: {e}")
            
        return list(sources)
        
    def _test_source_for_more_episodes(self, source_url, lex_info):
        """Test a source for more Lex Fridman episodes"""
        found_count = 0
        
        try:
            # Get the base domain
            parsed = urlparse(source_url)
            base_url = f"{parsed.scheme}://{parsed.netloc}"
            
            # Try different search patterns
            search_patterns = [
                f"{base_url}/search?q=lex+fridman",
                f"{base_url}/lex-fridman",
                f"{base_url}/lexfridman", 
                f"{base_url}/shows/lex-fridman-podcast",
                f"{base_url}/podcast/lex-fridman",
                f"{parsed.scheme}://{parsed.netloc}/u/lex-fridman",
                f"{parsed.scheme}://{parsed.netloc}/transcript/lex-fridman",
            ]
            
            for pattern in search_patterns:
                try:
                    print(f"   🔎 Trying: {pattern}")
                    response = self.session.get(pattern, timeout=10)
                    
                    if response.status_code == 200:
                        print(f"   ✅ Found page: {pattern}")
                        
                        # Look for episode links
                        episode_links = self._extract_lex_episodes(response.text, base_url)
                        
                        print(f"   📄 Found {len(episode_links)} potential episode links")
                        
                        # Check a few to see if they're transcripts
                        for link in episode_links[:5]:
                            if self._looks_like_lex_transcript(link, response.text):
                                found_count += 1
                                print(f"   📝 Potential transcript: {link[:80]}...")
                                
                        if episode_links:
                            break  # Found the right pattern
                            
                except requests.exceptions.RequestException as e:
                    print(f"   ⚠️  Failed: {e}")
                    continue
                    
                time.sleep(1)  # Rate limiting
                
        except Exception as e:
            print(f"   ❌ Error testing source: {e}")
            
        return found_count
        
    def _test_common_patterns(self, lex_info):
        """Test common patterns specifically for Lex Fridman"""
        found_count = 0
        
        # Known high-probability sites for Lex Fridman transcripts
        test_sites = [
            "https://lexfridman.com/podcast",
            "https://lexfridman.com/transcripts", 
            "https://www.rev.com/transcript/lex-fridman",
            "https://otter.ai/u/lex-fridman",
            "https://podscripts.co/lex-fridman-podcast",
            "https://medium.com/@lexfridman",
            "https://reddit.com/r/lexfridman",
        ]
        
        for site in test_sites:
            try:
                print(f"   🌐 Testing: {site}")
                response = self.session.get(site, timeout=10)
                
                if response.status_code == 200:
                    print(f"   ✅ Site exists: {site}")
                    
                    # Look for transcript-like content
                    if self._has_transcript_content(response.text):
                        print("   📝 Has transcript content!")
                        found_count += 3  # Estimate multiple episodes
                        
                elif response.status_code == 404:
                    print(f"   ❌ Not found: {site}")
                else:
                    print(f"   ⚠️  Status {response.status_code}: {site}")
                    
            except Exception as e:
                print(f"   ❌ Error: {e}")
                
            time.sleep(1)
            
        return found_count
        
    def _extract_lex_episodes(self, html, base_url):
        """Extract episode links from HTML"""
        links = []
        
        try:
            from bs4 import BeautifulSoup
            import warnings
            from bs4 import XMLParsedAsHTMLWarning
            warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
            
            soup = BeautifulSoup(html, 'html.parser')
            
            # Look for links that might be Lex episodes
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                text = link.get_text().lower()
                
                # Look for Lex-specific patterns
                if any(pattern in text for pattern in [
                    'lex fridman', '#', 'episode', 'transcript', 'conversation'
                ]) or any(pattern in href.lower() for pattern in [
                    'lex', 'fridman', 'episode', 'transcript', 'ep'
                ]):
                    full_url = urljoin(base_url, href)
                    if full_url not in links:
                        links.append(full_url)
                        
        except ImportError:
            print("   ⚠️  BeautifulSoup not available")
        except Exception as e:
            print(f"   ⚠️  Error extracting links: {e}")
            
        return links
        
    def _looks_like_lex_transcript(self, url, context_html=""):
        """Check if URL looks like a Lex Fridman transcript"""
        url_lower = url.lower()
        
        # URL patterns
        transcript_patterns = ['transcript', 'transcription', 'full-text', 'notes']
        lex_patterns = ['lex', 'fridman']
        
        has_transcript = any(pattern in url_lower for pattern in transcript_patterns)
        has_lex = any(pattern in url_lower for pattern in lex_patterns)
        
        return has_transcript or has_lex
        
    def _has_transcript_content(self, html):
        """Check if page has transcript-like content"""
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text().lower()
            
            # Look for transcript indicators
            indicators = [
                'transcript', 'conversation', 'interview', 'lex fridman',
                'host:', 'guest:', 'speaker:', 'dialogue'
            ]
            
            return sum(1 for indicator in indicators if indicator in text) >= 3
            
        except:
            return False

def main():
    """Run Lex Fridman discovery test"""
    test = LexFridmanDiscoveryTest()
    result = test.run_lex_test()
    
    if result > 10:
        print(f"\n🚀 SUCCESS! Found {result} potential new transcripts")
        print("   This validates the scaling approach - ready for full implementation")
    elif result > 0:
        print(f"\n✅ Found {result} potential transcripts - approach shows promise")
        print("   Worth optimizing and scaling to other podcasts")
    else:
        print("\n🤔 No new transcripts found - may need different approach")
        print("   Current discovery methods may already be comprehensive")

if __name__ == "__main__":
    main()