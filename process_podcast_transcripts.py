#!/usr/bin/env python3
"""
Process High-Confidence Podcast Transcripts

Based on the podcast analysis, fetch transcripts from known sources:
- This American Life
- Conversations with Tyler  
- Planet Money
- The Indicator
- Lex Fridman Podcast
"""

import json
import requests
import sqlite3
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
import time
import xml.etree.ElementTree as ET

class PodcastTranscriptProcessor:
    """Process transcripts from high-confidence podcast sources"""
    
    def __init__(self):
        self.db_path = "atlas.db"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
    def get_feed_episodes(self, feed_url, limit=5):
        """Get recent episodes from RSS feed"""
        try:
            response = self.session.get(feed_url, timeout=30)
            response.raise_for_status()
            
            root = ET.fromstring(response.content)
            episodes = []
            
            for item in root.findall('.//item')[:limit]:
                title_elem = item.find('title')
                link_elem = item.find('link')
                description_elem = item.find('description')
                
                if title_elem is not None and link_elem is not None:
                    episodes.append({
                        'title': title_elem.text,
                        'link': link_elem.text,
                        'description': description_elem.text if description_elem is not None else ""
                    })
                    
            return episodes
            
        except Exception as e:
            print(f"❌ Error fetching feed {feed_url}: {e}")
            return []
    
    def scrape_this_american_life(self, episode_url):
        """Scrape This American Life transcript"""
        try:
            response = self.session.get(episode_url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for transcript link
            transcript_link = soup.find('a', href=lambda x: x and 'transcript' in x.lower())
            if transcript_link:
                transcript_url = transcript_link['href']
                if not transcript_url.startswith('http'):
                    transcript_url = f"https://www.thisamericanlife.org{transcript_url}"
                
                # Fetch transcript page
                transcript_response = self.session.get(transcript_url, timeout=30)
                transcript_soup = BeautifulSoup(transcript_response.content, 'html.parser')
                
                # Extract transcript text
                transcript_content = transcript_soup.find('div', class_='transcript')
                if transcript_content:
                    return {
                        'source': 'this-american-life',
                        'transcript': transcript_content.get_text(separator='\n', strip=True),
                        'url': transcript_url
                    }
            
            return None
            
        except Exception as e:
            print(f"❌ Error scraping TAL {episode_url}: {e}")
            return None
    
    def scrape_conversations_with_tyler(self, episode_url):
        """Scrape Conversations with Tyler transcript"""
        try:
            response = self.session.get(episode_url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Tyler Cowen's site usually has transcript in main content
            transcript_content = soup.find('div', class_='entry-content')
            if transcript_content:
                # Remove non-transcript elements
                for elem in transcript_content.find_all(['script', 'style', 'aside']):
                    elem.decompose()
                
                text = transcript_content.get_text(separator='\n', strip=True)
                
                # Basic check if this looks like a transcript
                if len(text) > 1000 and ('TYLER:' in text.upper() or 'COWEN:' in text.upper()):
                    return {
                        'source': 'conversations-with-tyler',
                        'transcript': text,
                        'url': episode_url
                    }
            
            return None
            
        except Exception as e:
            print(f"❌ Error scraping Tyler {episode_url}: {e}")
            return None
    
    def scrape_lex_fridman(self, episode_url):
        """Scrape Lex Fridman transcript - usually on lexfridman.com"""
        try:
            # Convert to lexfridman.com if it's not already
            if 'lexfridman.com' not in episode_url:
                # Try to extract episode number and convert
                import re
                episode_match = re.search(r'(\d+)', episode_url)
                if episode_match:
                    episode_num = episode_match.group(1)
                    episode_url = f"https://lexfridman.com/{episode_num}/"
            
            response = self.session.get(episode_url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for transcript section
            transcript_section = soup.find('section', id='transcript')
            if not transcript_section:
                transcript_section = soup.find('div', class_='transcript')
            
            if transcript_section:
                return {
                    'source': 'lex-fridman',
                    'transcript': transcript_section.get_text(separator='\n', strip=True),
                    'url': episode_url
                }
            
            return None
            
        except Exception as e:
            print(f"❌ Error scraping Lex {episode_url}: {e}")
            return None
    
    def save_transcript_to_atlas(self, episode, transcript_data):
        """Save transcript to Atlas database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            title = f"[TRANSCRIPT] {episode['title']}"
            content = f"Podcast: {episode['title']}\nSource: {transcript_data['source']}\n\n{transcript_data['transcript']}"
            url = transcript_data['url']
            
            cursor.execute("""
                INSERT OR REPLACE INTO content 
                (url, title, content, created_at)
                VALUES (?, ?, ?, ?)
            """, (
                url,
                title,
                content[:10000],  # Limit content size
                datetime.now().isoformat()
            ))
            
            conn.commit()
            conn.close()
            
            return True
            
        except Exception as e:
            print(f"❌ Error saving transcript: {e}")
            return False
    
    def process_podcast_source(self, podcast_name, feed_url, scraper_func):
        """Process a specific podcast source"""
        print(f"\n🎙️ Processing {podcast_name}...")
        
        # Get recent episodes
        episodes = self.get_feed_episodes(feed_url, limit=3)  # Process 3 recent episodes
        
        if not episodes:
            print(f"❌ No episodes found for {podcast_name}")
            return 0
        
        processed = 0
        
        for episode in episodes:
            print(f"  📄 Processing: {episode['title'][:60]}...")
            
            # Try to get transcript
            transcript_data = scraper_func(episode['link'])
            
            if transcript_data:
                if self.save_transcript_to_atlas(episode, transcript_data):
                    processed += 1
                    print(f"    ✅ Saved transcript")
                else:
                    print(f"    ❌ Failed to save")
            else:
                print(f"    ⚠️ No transcript found")
            
            time.sleep(2)  # Be respectful
        
        return processed

def main():
    """Process transcripts from high-confidence podcast sources"""
    
    print("🎙️ Atlas Podcast Transcript Processor")
    print("=" * 50)
    
    # Load the podcast analysis
    analysis_file = "podcast_transcript_analysis.json"
    if not Path(analysis_file).exists():
        print(f"❌ Run find_podcast_transcripts.py first")
        return False
    
    with open(analysis_file) as f:
        analysis = json.load(f)
    
    # Get high-confidence podcasts
    high_confidence = [p for p in analysis['podcasts'] if p['transcript_info']['confidence'] == 'high']
    
    processor = PodcastTranscriptProcessor()
    total_processed = 0
    
    # Map podcast sources to scrapers and feed URLs
    podcast_sources = {
        'this-american-life': {
            'name': 'This American Life',
            'feed': 'https://www.thisamericanlife.org/podcast/rss.xml',
            'scraper': processor.scrape_this_american_life
        },
        'conversations-with-tyler': {
            'name': 'Conversations with Tyler',
            'feed': 'https://cowenconvos.libsyn.com/rss',
            'scraper': processor.scrape_conversations_with_tyler  
        },
        'lex-fridman': {
            'name': 'Lex Fridman Podcast',
            'feed': 'https://lexfridman.com/feed/podcast/',
            'scraper': processor.scrape_lex_fridman
        },
        'planet-money': {
            'name': 'Planet Money',
            'feed': 'https://feeds.npr.org/510289/podcast.xml',
            'scraper': processor.scrape_this_american_life  # NPR uses similar structure
        },
        'the-indicator': {
            'name': 'The Indicator',
            'feed': 'https://feeds.npr.org/510325/podcast.xml', 
            'scraper': processor.scrape_this_american_life  # NPR uses similar structure
        }
    }
    
    # Process each high-confidence source
    for podcast in high_confidence:
        source = podcast['transcript_info']['source']
        
        if source in podcast_sources:
            source_info = podcast_sources[source]
            
            processed = processor.process_podcast_source(
                source_info['name'],
                source_info['feed'], 
                source_info['scraper']
            )
            
            total_processed += processed
            print(f"✅ {source_info['name']}: {processed} transcripts processed")
    
    print(f"\n🎉 TRANSCRIPT PROCESSING COMPLETE!")
    print(f"📊 Total transcripts added: {total_processed}")
    
    if total_processed > 0:
        print(f"🔍 Your Atlas now has podcast transcripts!")
        print(f"🧠 Try asking: 'What did Tyler Cowen say about economics?'")
        print(f"🎯 Or: 'Find insights from Lex Fridman interviews'")
    
    return total_processed > 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)