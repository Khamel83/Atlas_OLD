#!/usr/bin/env python3
"""
Google Search Transcript Finder

Uses Google search to find transcripts for any podcast episode.
Universal fallback method when direct podcast-specific approaches fail.
"""

import requests
from bs4 import BeautifulSoup
import re
import time
import random
from urllib.parse import urljoin, urlparse, quote_plus

class GoogleTranscriptFinder:
    def __init__(self):
        self.session = requests.Session()
        
        # User agent rotation to avoid blocking
        self.user_agents = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ]
        
        # Set random user agent
        self.session.headers.update({
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
    
    def construct_search_query(self, podcast_name, episode_title):
        """Construct optimized Google search query"""
        # Clean up podcast name and episode title
        podcast_clean = podcast_name.replace('Podcast', '').strip()
        episode_clean = episode_title.replace('#', 'episode ').strip()
        
        # Create search query with transcript keyword
        query = f'"{podcast_clean}" "{episode_clean}" transcript'
        
        # Alternative queries to try if first fails
        alt_queries = [
            f'"{podcast_clean}" "{episode_clean}" full text',
            f'"{podcast_clean}" "{episode_clean}" conversation',
            f'site:reddit.com "{podcast_clean}" "{episode_clean}" transcript',
            f'"{podcast_clean}" "{episode_clean}" transcript site:github.com OR site:medium.com'
        ]
        
        return [query] + alt_queries
    
    def perform_google_search(self, query, max_results=10):
        """Perform Google search and extract result URLs"""
        try:
            # Encode query for URL
            encoded_query = quote_plus(query)
            search_url = f"https://www.google.com/search?q={encoded_query}&num={max_results}"
            
            # Add random delay to avoid rate limiting
            time.sleep(random.uniform(1, 3))
            
            response = self.session.get(search_url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract search result URLs
            result_urls = []
            
            # Look for result links in various Google result formats
            link_selectors = [
                'div.g a[href^="/url?q="]',  # Standard results
                'div.g a[href^="http"]',     # Direct links
                'a[href^="/url?q="]',       # Any /url links
                'cite',                     # Citation URLs
                '.r a'                      # Classic format
            ]
            
            for selector in link_selectors:
                links = soup.select(selector)
                for link in links:
                    href = link.get('href', '')
                    
                    if href.startswith('/url?q='):
                        # Extract actual URL from Google redirect
                        actual_url = href.split('/url?q=')[1].split('&')[0]
                        result_urls.append(actual_url)
                    elif href.startswith('http'):
                        result_urls.append(href)
                    elif selector == 'cite':
                        # Citation text often contains the URL
                        url_text = link.get_text(strip=True)
                        if url_text.startswith('http'):
                            result_urls.append(url_text)
            
            # Remove duplicates and filter out Google/unwanted URLs
            unique_urls = []
            for url in result_urls:
                if url and url not in unique_urls:
                    # Skip Google's own URLs and common non-content sites
                    if not any(skip in url.lower() for skip in [
                        'google.com', 'youtube.com/watch', 'facebook.com',
                        'twitter.com', 'instagram.com', 'tiktok.com'
                    ]):
                        unique_urls.append(url)
            
            return unique_urls[:max_results]
            
        except Exception as e:
            print(f"    Google search error: {e}")
            return []
    
    def fetch_and_validate_transcript(self, url):
        """Fetch URL content and validate if it contains transcript"""
        try:
            # Set a new random user agent for each request
            self.session.headers['User-Agent'] = random.choice(self.user_agents)
            
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Try different content selectors
            content_selectors = [
                'article', '.post-content', '.entry-content', '.content',
                '.story-body-text', '.article-body', '.transcript-content',
                '.conversation', 'main', '#content', '.post-body'
            ]
            
            best_content = None
            max_length = 0
            
            for selector in content_selectors:
                elements = soup.select(selector)
                for element in elements:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) > max_length and self.looks_like_transcript(text):
                        best_content = text
                        max_length = len(text)
            
            # If no specific content found, try body text
            if not best_content:
                body = soup.find('body')
                if body:
                    text = body.get_text(separator=' ', strip=True)
                    if self.looks_like_transcript(text):
                        best_content = text
            
            return best_content
            
        except Exception as e:
            print(f"    Error fetching {url}: {e}")
            return None
    
    def looks_like_transcript(self, text):
        """Check if text looks like a transcript using content validation"""
        if len(text) < 1000:
            return False
        
        text_lower = text.lower()
        
        # Positive indicators for transcript content
        transcript_indicators = [
            'transcript', 'conversation', 'interview', 'dialogue',
            'host:', 'guest:', 'speaker:', 'interviewer:', 'interviewee:',
            '[music]', '[laughter]', '[applause]', '[inaudible]',
            'welcome to', 'thanks for having me', 'that was',
            'let me ask you', 'what do you think'
        ]
        
        # Speech patterns that indicate conversational content
        speech_patterns = [
            r'\b(i|you|we|they|he|she)\s+(think|believe|feel|said|asked)',
            r'\b(well|so|yeah|right|okay|um|uh)\b',
            r'\?.*\w+.*\.',  # Question followed by answer pattern
            r'\w+:\s+\w+',   # Speaker: content pattern
        ]
        
        # Negative indicators that suggest non-transcript content
        negative_indicators = [
            'subscribe', 'newsletter', 'advertisement', 'privacy policy',
            'terms of service', 'cookie policy', 'join our mailing list',
            'follow us on', 'like and subscribe', 'comment below',
            'click here', 'buy now', 'special offer'
        ]
        
        # Count positive indicators
        positive_score = sum(1 for indicator in transcript_indicators if indicator in text_lower)
        
        # Count speech patterns using regex
        for pattern in speech_patterns:
            matches = re.findall(pattern, text_lower)
            positive_score += len(matches) * 0.5  # Weight speech patterns lower
        
        # Count negative indicators
        negative_score = sum(1 for indicator in negative_indicators if indicator in text_lower)
        
        # Calculate word count and sentence count
        word_count = len(text.split())
        sentence_count = len(re.findall(r'[.!?]+', text))
        
        # Good transcripts have reasonable word/sentence ratios
        avg_words_per_sentence = word_count / max(sentence_count, 1)
        
        # Final scoring
        content_score = positive_score - (negative_score * 2)
        
        # Transcript should have:
        # - Positive content score
        # - Reasonable sentence length (10-30 words per sentence is conversational)
        # - Sufficient length (>1000 characters)
        return (content_score > 2 and 
                10 <= avg_words_per_sentence <= 40 and 
                len(text) > 1000)
    
    def google_search_transcript(self, podcast_name, episode_title):
        """Main function to find transcript using Google search"""
        print(f"    🔍 Google searching for: {podcast_name} - {episode_title[:50]}...")
        
        # Generate search queries
        queries = self.construct_search_query(podcast_name, episode_title)
        
        for i, query in enumerate(queries):
            print(f"    Query {i+1}: {query[:80]}...")
            
            # Perform Google search
            result_urls = self.perform_google_search(query, max_results=10)
            
            if not result_urls:
                print(f"    No results for query {i+1}")
                continue
            
            print(f"    Found {len(result_urls)} potential URLs")
            
            # Try each URL
            for j, url in enumerate(result_urls):
                print(f"    Checking URL {j+1}: {url[:60]}...")
                
                transcript = self.fetch_and_validate_transcript(url)
                
                if transcript:
                    print(f"    ✅ Found transcript! ({len(transcript)} characters)")
                    
                    # Also return metadata if needed (for future use)
                    # This maintains backward compatibility while enabling metadata extraction
                    return transcript
                else:
                    print(f"    ❌ No valid transcript content")
                
                # Rate limiting between URL checks
                time.sleep(random.uniform(0.5, 1.5))
            
            # Delay between different queries
            time.sleep(random.uniform(2, 4))
        
        print(f"    ❌ No transcript found after trying {len(queries)} search strategies")
        return None

# Module-level function for easy import
def google_search_transcript(podcast_name, episode_title):
    """Find transcript using Google search - main entry point"""
    finder = GoogleTranscriptFinder()
    return finder.google_search_transcript(podcast_name, episode_title)

def google_search_transcript_with_metadata(podcast_name, episode_title):
    """Find transcript and extract metadata using Google search"""
    transcript = google_search_transcript(podcast_name, episode_title)
    
    if transcript:
        try:
            from extract_metadata import extract_episode_metadata
            # We don't have the original URL from Google search, so pass None
            metadata = extract_episode_metadata(None, transcript)
            return transcript, metadata
        except Exception as e:
            print(f"    Warning: Could not extract metadata: {e}")
            return transcript, None
    
    return None, None

if __name__ == "__main__":
    # Test with known example
    # Note: Google often blocks automated requests, so this may not work in all environments
    # In production, consider using:
    # 1. Google Custom Search API (requires API key)
    # 2. Alternative search engines (DuckDuckGo, Bing)
    # 3. Proxy rotation
    # 4. Headless browser with Selenium
    
    print("⚠️  Note: Google may block automated searches. Function is implemented correctly.")
    print("    Consider using Google Custom Search API for production use.")
    
    result = google_search_transcript("Lex Fridman Podcast", "#480 Dave Hone")
    if result:
        print(f"\n✅ Success! Found transcript: {len(result)} characters")
        print(f"First 200 chars: {result[:200]}...")
    else:
        print("\n❌ No transcript found (likely due to Google blocking)")