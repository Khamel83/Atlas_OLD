#!/usr/bin/env python3
"""
RSS Transcript Extractor

Extracts transcript URLs directly from RSS feeds where podcasters embed them.
This is often the most reliable method since podcasters control their own feeds.
"""

import requests
import xml.etree.ElementTree as ET
import re
from urllib.parse import urljoin, urlparse
import time
from bs4 import BeautifulSoup
from typing import Optional, Dict, List, Tuple

class RSSTranscriptExtractor:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Atlas Podcast Transcript Extractor 1.0 (Python/requests)'
        })
        
        # Common transcript indicators in RSS feeds
        self.transcript_indicators = [
            'transcript', 'full text', 'show notes', 'full transcript',
            'episode transcript', 'conversation transcript', 'read the full',
            'complete transcript', 'written transcript'
        ]
        
        # Common URL patterns that indicate transcripts
        self.transcript_url_patterns = [
            r'transcript\.html?',
            r'full-text\.html?',
            r'/transcript/',
            r'/transcripts/',
            r'/episode-.*-transcript',
            r'\.transcript\.',
        ]
    
    def fetch_rss_feed(self, rss_url, timeout=30):
        """Fetch RSS feed XML content"""
        try:
            print(f"    📡 Fetching RSS feed: {rss_url}")
            response = self.session.get(rss_url, timeout=timeout)
            response.raise_for_status()
            
            # Ensure we got XML content
            content_type = response.headers.get('content-type', '')
            if 'xml' not in content_type.lower() and 'rss' not in content_type.lower():
                print(f"    ⚠️ Warning: Content type is {content_type}, may not be RSS")
            
            return response.text
        except Exception as e:
            print(f"    ❌ Error fetching RSS feed: {e}")
            return None
    
    def parse_rss_xml(self, xml_content):
        """Parse RSS XML and extract episode items"""
        try:
            root = ET.fromstring(xml_content)
            
            # Handle different RSS formats
            episodes = []
            
            # Standard RSS 2.0 format
            if root.tag == 'rss':
                channel = root.find('channel')
                if channel is not None:
                    items = channel.findall('item')
                    episodes.extend(items)
            
            # Atom format
            elif root.tag.endswith('feed'):
                entries = root.findall('.//{http://www.w3.org/2005/Atom}entry')
                episodes.extend(entries)
            
            # Try to find items regardless of namespace
            if not episodes:
                # Look for any element that might be an episode
                for elem in root.iter():
                    if elem.tag.endswith('item') or elem.tag.endswith('entry'):
                        episodes.append(elem)
            
            print(f"    📊 Found {len(episodes)} episodes in RSS feed")
            return episodes
            
        except ET.ParseError as e:
            print(f"    ❌ Error parsing RSS XML: {e}")
            return []
    
    def extract_text_from_html(self, html_content):
        """Extract plain text from HTML content for better searching"""
        if not html_content:
            return ""
        
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup.get_text(separator=' ', strip=True)
        except:
            # Fallback to regex if BeautifulSoup fails
            text = re.sub(r'<[^>]+>', ' ', html_content)
            return ' '.join(text.split())
    
    def find_transcript_urls_in_content(self, content_text, base_url=None):
        """Find transcript URLs in episode content"""
        transcript_urls = []
        
        if not content_text:
            return transcript_urls
        
        # Convert to lowercase for searching
        content_lower = content_text.lower()
        
        # Look for direct transcript URL patterns
        url_pattern = r'https?://[^\s<>"\']+(?:transcript|full-text|show-notes)[^\s<>"\']*'
        found_urls = re.findall(url_pattern, content_text, re.IGNORECASE)
        
        for url in found_urls:
            # Clean up the URL (remove trailing punctuation)
            url = re.sub(r'[.,;!?]+$', '', url)
            transcript_urls.append({
                'url': url,
                'type': 'direct_pattern',
                'confidence': 0.9
            })
        
        # Look for transcript indicators near URLs
        general_url_pattern = r'https?://[^\s<>"\']+[^\s<>"\']*'
        all_urls = re.findall(general_url_pattern, content_text)
        
        for url in all_urls:
            url = re.sub(r'[.,;!?]+$', '', url)
            
            # Check if transcript indicators appear near this URL
            url_position = content_lower.find(url.lower())
            if url_position != -1:
                # Get 200 characters before and after the URL
                context_start = max(0, url_position - 200)
                context_end = min(len(content_text), url_position + len(url) + 200)
                context = content_text[context_start:context_end].lower()
                
                # Check if transcript indicators are in the context
                transcript_score = 0
                for indicator in self.transcript_indicators:
                    if indicator in context:
                        transcript_score += 1
                
                if transcript_score > 0:
                    confidence = min(0.8, transcript_score * 0.2)
                    
                    # Avoid duplicates
                    if not any(existing['url'] == url for existing in transcript_urls):
                        transcript_urls.append({
                            'url': url,
                            'type': 'context_indicator',
                            'confidence': confidence
                        })
        
        return transcript_urls
    
    def extract_episode_info(self, episode_item):
        """Extract basic episode information from RSS item"""
        episode_info = {
            'title': '',
            'description': '',
            'link': '',
            'pub_date': '',
            'guid': ''
        }
        
        # Handle different XML namespaces and formats
        def get_text(elem, *tag_names):
            for tag_name in tag_names:
                # Try with different namespace prefixes
                for prefix in ['', '{http://www.w3.org/2005/Atom}']:
                    element = elem.find(f'{prefix}{tag_name}')
                    if element is not None:
                        return element.text or ''
            return ''
        
        def get_attr(elem, tag_name, attr_name):
            element = elem.find(tag_name)
            if element is not None:
                return element.get(attr_name, '')
            return ''
        
        # Extract title
        episode_info['title'] = get_text(episode_item, 'title')
        
        # Extract description (try multiple fields)
        description = (get_text(episode_item, 'description') or 
                      get_text(episode_item, 'summary') or
                      get_text(episode_item, 'content'))
        episode_info['description'] = description
        
        # Extract link
        episode_info['link'] = (get_text(episode_item, 'link') or
                               get_attr(episode_item, 'link', 'href'))
        
        # Extract publication date
        episode_info['pub_date'] = (get_text(episode_item, 'pubDate') or
                                   get_text(episode_item, 'published'))
        
        # Extract GUID
        episode_info['guid'] = get_text(episode_item, 'guid')
        
        return episode_info
    
    def extract_rss_transcripts(self, rss_url):
        """Main function to extract transcript URLs from RSS feed"""
        print(f"🎙️ Extracting transcript links from RSS feed...")
        
        # Fetch RSS feed
        xml_content = self.fetch_rss_feed(rss_url)
        if not xml_content:
            return [], []
        
        # Parse RSS XML
        episodes = self.parse_rss_xml(xml_content)
        if not episodes:
            return [], []
        
        # Extract transcript URLs from episodes
        episodes_with_transcripts = []
        all_processed_episodes = []
        
        for i, episode_item in enumerate(episodes):
            if i >= 50:  # Limit to first 50 episodes to avoid overwhelming
                break
            
            episode_info = self.extract_episode_info(episode_item)
            all_processed_episodes.append(episode_info)
            
            if not episode_info['title']:
                continue
                
            print(f"    📝 Checking episode: {episode_info['title'][:60]}...")
            
            # Search for transcript URLs in description
            description_text = self.extract_text_from_html(episode_info['description'])
            transcript_urls = self.find_transcript_urls_in_content(description_text, rss_url)
            
            if transcript_urls:
                episode_with_transcripts = episode_info.copy()
                episode_with_transcripts['transcript_urls'] = transcript_urls
                episode_with_transcripts['source_rss'] = rss_url
                
                episodes_with_transcripts.append(episode_with_transcripts)
                
                print(f"    ✅ Found {len(transcript_urls)} potential transcript URLs")
                for url_info in transcript_urls:
                    print(f"        📄 {url_info['url']} (confidence: {url_info['confidence']:.1f})")
            else:
                print(f"    ❌ No transcript URLs found")
            
            # Rate limiting
            time.sleep(0.1)
        
        total_found = len(episodes_with_transcripts)
        print(f"🎯 RSS extraction results: {total_found} episodes with transcript URLs found")
        
        return all_processed_episodes, episodes_with_transcripts

# Module-level function for easy import
def extract_rss_transcripts(rss_url):
    """Extract transcript URLs from RSS feed - main entry point"""
    extractor = RSSTranscriptExtractor()
    return extractor.extract_rss_transcripts(rss_url)

if __name__ == "__main__":
    # Test with This American Life RSS feed
    test_feeds = [
        "https://www.thisamericanlife.org/podcast/rss.xml",
        "https://feeds.megaphone.fm/lexfridman",
        "https://rss.art19.com/the-ezra-klein-show"
    ]
    
    for feed_url in test_feeds:
        print(f"\n{'='*60}")
        print(f"Testing RSS feed: {feed_url}")
        print('='*60)
        
        results = extract_rss_transcripts(feed_url)
        
        if results:
            print(f"\n✅ Success! Found transcript URLs in {len(results)} episodes")
            
            # Show first few results
            for i, episode in enumerate(results[:3]):
                print(f"\nEpisode {i+1}: {episode['title'][:50]}...")
                for url_info in episode['transcript_urls']:
                    print(f"  📄 {url_info['url']}")
        else:
            print(f"\n❌ No episodes with transcript URLs found")
        
        print(f"\n{'='*60}")
        time.sleep(2)  # Rate limiting between feeds