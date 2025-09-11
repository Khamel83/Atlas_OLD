#!/usr/bin/env python3
"""
Episode Metadata Extractor

Extracts episode metadata, show notes, and links alongside transcripts.
Designed to enhance transcript extraction with rich metadata capture.
"""

import requests
from bs4 import BeautifulSoup
import re
import json
from urllib.parse import urljoin, urlparse
from datetime import datetime
import time

class EpisodeMetadataExtractor:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Common advertising and affiliate keywords to filter out
        self.advertising_keywords = [
            'affiliate', 'promo', 'discount', 'coupon', 'sponsor', 'ad',
            'advertisement', 'referral', 'tracking', 'utm_', 'amazon.com/dp',
            'amzn.to', 'bit.ly', 'goo.gl', 'tinyurl', 'ow.ly',
            'audible.com', 'brilliantorg', 'squarespace', 'nordvpn',
            'expressvpn', 'skillshare', 'masterclass', 'bluehost'
        ]
    
    def fetch_episode_page(self, episode_url, timeout=15):
        """Fetch episode webpage content"""
        try:
            response = self.session.get(episode_url, timeout=timeout)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"    Error fetching episode page: {e}")
            return None
    
    def extract_links_from_text(self, text, base_url=None):
        """Extract hyperlinks from text content"""
        links = []
        
        # Find URLs in text using regex
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        found_urls = re.findall(url_pattern, text)
        
        for url in found_urls:
            if not self.is_advertising_link(url):
                links.append({
                    'url': url,
                    'type': 'direct_link',
                    'context': self.get_link_context(text, url)
                })
        
        return links
    
    def extract_links_from_html(self, soup, base_url=None):
        """Extract hyperlinks from HTML content"""
        links = []
        
        # Find all <a> tags with href
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            # Convert relative URLs to absolute
            if base_url and not href.startswith(('http://', 'https://', 'mailto:', 'tel:')):
                href = urljoin(base_url, href)
            
            if href.startswith(('http://', 'https://')) and not self.is_advertising_link(href):
                link_text = link.get_text(strip=True)
                
                links.append({
                    'url': href,
                    'text': link_text,
                    'type': 'html_link',
                    'context': self.get_html_link_context(link)
                })
        
        return links
    
    def is_advertising_link(self, url):
        """Check if URL appears to be advertising/affiliate link"""
        url_lower = url.lower()
        return any(keyword in url_lower for keyword in self.advertising_keywords)
    
    def get_link_context(self, text, url):
        """Get surrounding context for a link found in text"""
        # Find the position of the URL in text
        url_pos = text.find(url)
        if url_pos == -1:
            return ""
        
        # Get 100 characters before and after the URL
        start = max(0, url_pos - 100)
        end = min(len(text), url_pos + len(url) + 100)
        context = text[start:end].strip()
        
        return context
    
    def get_html_link_context(self, link_element):
        """Get context for HTML link element"""
        # Try to get parent paragraph or surrounding text
        parent = link_element.parent
        if parent:
            context = parent.get_text(strip=True)
            return context[:200]  # Limit context length
        return ""
    
    def extract_guest_names(self, text, title):
        """Extract guest names from title and content"""
        guests = []
        
        # Common patterns for guest identification
        guest_patterns = [
            r'with\s+([A-Z][a-z]+\s+[A-Z][a-z]+)',  # "with John Smith"
            r'guest:?\s+([A-Z][a-z]+\s+[A-Z][a-z]+)',  # "guest: John Smith"
            r'interviewing\s+([A-Z][a-z]+\s+[A-Z][a-z]+)',  # "interviewing John Smith"
            r'featuring\s+([A-Z][a-z]+\s+[A-Z][a-z]+)',  # "featuring John Smith"
            r'([A-Z][a-z]+\s+[A-Z][a-z]+)\s+joins',  # "John Smith joins"
        ]
        
        # Check title first
        for pattern in guest_patterns:
            matches = re.findall(pattern, title, re.IGNORECASE)
            guests.extend(matches)
        
        # Check transcript content (first 500 words to avoid false positives)
        content_start = text[:2000] if text else ""
        for pattern in guest_patterns:
            matches = re.findall(pattern, content_start, re.IGNORECASE)
            guests.extend(matches)
        
        # Remove duplicates and filter common false positives
        unique_guests = []
        false_positives = ['This American', 'New York', 'San Francisco', 'Los Angeles']
        
        for guest in guests:
            if guest not in unique_guests and guest not in false_positives:
                unique_guests.append(guest)
        
        return unique_guests
    
    def extract_duration_from_content(self, soup, text):
        """Extract episode duration from webpage or transcript"""
        duration_patterns = [
            r'duration:?\s*(\d+):(\d+):(\d+)',  # HH:MM:SS
            r'duration:?\s*(\d+):(\d+)',  # MM:SS
            r'length:?\s*(\d+)\s*minutes?',  # X minutes
            r'runtime:?\s*(\d+):(\d+)',  # MM:SS
        ]
        
        # Check meta tags first
        if soup:
            meta_duration = soup.find('meta', {'property': 'video:duration'})
            if meta_duration:
                return meta_duration.get('content')
            
            meta_duration = soup.find('meta', {'name': 'duration'})
            if meta_duration:
                return meta_duration.get('content')
        
        # Check text content
        search_text = (text[:1000] if text else "") + str(soup)[:1000] if soup else text[:1000] if text else ""
        
        for pattern in duration_patterns:
            match = re.search(pattern, search_text, re.IGNORECASE)
            if match:
                return match.group(0)
        
        return None
    
    def extract_publish_date(self, soup, text):
        """Extract episode publish date"""
        if not soup:
            return None
        
        # Check common meta tags for publication date
        date_selectors = [
            'meta[property="article:published_time"]',
            'meta[name="publish_date"]',
            'meta[name="date"]',
            'time[datetime]',
            '.published-date',
            '.episode-date',
            '.post-date'
        ]
        
        for selector in date_selectors:
            element = soup.select_one(selector)
            if element:
                date_value = element.get('content') or element.get('datetime') or element.get_text(strip=True)
                if date_value:
                    return date_value
        
        return None
    
    def extract_show_notes(self, soup, transcript_text):
        """Extract show notes/description from episode page"""
        if not soup:
            return None
        
        # Common selectors for show notes
        show_notes_selectors = [
            '.show-notes', '.episode-description', '.post-content',
            '.entry-content', '.episode-summary', '.description',
            '.content', 'article .content', '.episode-notes'
        ]
        
        best_notes = None
        max_length = 0
        
        for selector in show_notes_selectors:
            elements = soup.select(selector)
            for element in elements:
                text = element.get_text(separator=' ', strip=True)
                # Show notes should be substantial but not the full transcript
                if 100 < len(text) < 5000 and len(text) > max_length:
                    # Avoid selecting the transcript itself
                    if transcript_text and len(text) < len(transcript_text) * 0.8:
                        best_notes = text
                        max_length = len(text)
                    elif not transcript_text:
                        best_notes = text
                        max_length = len(text)
        
        return best_notes
    
    def extract_episode_metadata(self, episode_url, transcript_text=None):
        """Main function to extract episode metadata"""
        print(f"    📋 Extracting metadata from: {episode_url}")
        
        # Fetch episode page
        html_content = self.fetch_episode_page(episode_url)
        soup = BeautifulSoup(html_content, 'html.parser') if html_content else None
        
        metadata = {
            'episode_url': episode_url,
            'extracted_at': datetime.now().isoformat(),
            'links': [],
            'guests': [],
            'duration': None,
            'publish_date': None,
            'show_notes': None,
            'extraction_source': 'automated'
        }
        
        # Extract links from HTML
        if soup:
            html_links = self.extract_links_from_html(soup, episode_url)
            metadata['links'].extend(html_links)
        
        # Extract links from transcript text
        if transcript_text:
            text_links = self.extract_links_from_text(transcript_text, episode_url)
            metadata['links'].extend(text_links)
            
            # Extract guest names
            page_title = soup.find('title').get_text() if soup and soup.find('title') else ""
            metadata['guests'] = self.extract_guest_names(transcript_text, page_title)
        
        # Extract duration
        metadata['duration'] = self.extract_duration_from_content(soup, transcript_text)
        
        # Extract publish date
        metadata['publish_date'] = self.extract_publish_date(soup, transcript_text)
        
        # Extract show notes
        metadata['show_notes'] = self.extract_show_notes(soup, transcript_text)
        
        # Remove duplicate links
        seen_urls = set()
        unique_links = []
        for link in metadata['links']:
            if link['url'] not in seen_urls:
                seen_urls.add(link['url'])
                unique_links.append(link)
        metadata['links'] = unique_links
        
        print(f"    📋 Extracted: {len(metadata['links'])} links, {len(metadata['guests'])} guests")
        
        return metadata

# Module-level function for easy import
def extract_episode_metadata(episode_url, transcript_text=None):
    """Extract episode metadata - main entry point"""
    extractor = EpisodeMetadataExtractor()
    return extractor.extract_episode_metadata(episode_url, transcript_text)

if __name__ == "__main__":
    # Test with Lex Fridman episode
    test_url = "https://lexfridman.com/david-kipping/"
    test_transcript = "Sample transcript text with https://example.com reference link"
    
    result = extract_episode_metadata(test_url, test_transcript)
    print(json.dumps(result, indent=2))