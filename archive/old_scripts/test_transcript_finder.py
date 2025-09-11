#!/usr/bin/env python3
"""
Test specific transcript finding for debugging
"""

import requests
from bs4 import BeautifulSoup
import re

def test_hard_fork_transcript():
    """Test finding Hard Fork transcript"""
    title = "Age-Gating the Internet + Cloudflare Takes On A.I. Scrapers + HatGPT"
    
    # Hard Fork is a NYTimes podcast
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    # Try different URL patterns for Hard Fork
    slug = title.lower().replace(' ', '-').replace(':', '').replace(',', '')
    slug = re.sub(r'[^\w\s-]', '', slug).strip()
    slug = slug.replace('--', '-')
    
    print(f"Title: {title}")
    print(f"Slug: {slug}")
    
    # Try various URL patterns
    test_urls = [
        f"https://www.nytimes.com/2024/12/07/podcasts/hard-fork/{slug}.html",
        f"https://www.nytimes.com/column/hard-fork",
        f"https://www.nytimes.com/podcasts/hard-fork",
        f"https://www.nytimes.com/2024/12/06/podcasts/hard-fork-{slug}.html",
    ]
    
    for url in test_urls:
        print(f"\nTrying: {url}")
        try:
            response = session.get(url, timeout=10)
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Look for transcript indicators
                text = soup.get_text().lower()
                if 'transcript' in text:
                    print("✓ Found 'transcript' in page text")
                    
                    # Look for specific transcript content
                    transcript_selectors = ['.story-body-text', '.article-body', '.transcript']
                    for selector in transcript_selectors:
                        elements = soup.select(selector)
                        for element in elements:
                            element_text = element.get_text(separator=' ', strip=True)
                            if len(element_text) > 500:
                                print(f"✓ Found substantial content ({len(element_text)} chars) with selector: {selector}")
                                return element_text[:200] + "..."
                else:
                    print("✗ No 'transcript' found in page text")
            
        except Exception as e:
            print(f"Error: {e}")
    
    return None

def test_this_american_life():
    """Test This American Life transcript"""
    title = "859: Chaos Graph"
    
    # Extract episode number
    episode_match = re.search(r'(\d+):', title)
    if episode_match:
        episode_num = episode_match.group(1)
        url = f"https://www.thisamericanlife.org/{episode_num}/transcript"
        
        print(f"\nTesting This American Life:")
        print(f"Title: {title}")
        print(f"Episode: {episode_num}")
        print(f"URL: {url}")
        
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        try:
            response = session.get(url, timeout=10)
            print(f"Status: {response.status_code}")
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Look for TAL transcript content
                selectors = ['.radio-dialtone', '.transcript', '.body', '.content']
                for selector in selectors:
                    elements = soup.select(selector)
                    for element in elements:
                        element_text = element.get_text(separator=' ', strip=True)
                        if len(element_text) > 500:
                            print(f"✓ Found transcript ({len(element_text)} chars) with selector: {selector}")
                            return element_text[:200] + "..."
                
                print("✗ No substantial transcript content found")
            else:
                print("✗ Page not found")
                
        except Exception as e:
            print(f"Error: {e}")
    
    return None

def main():
    print("🔍 Testing transcript discovery on specific episodes...\n")
    
    # Test Hard Fork
    hard_fork_result = test_hard_fork_transcript()
    if hard_fork_result:
        print(f"Hard Fork transcript preview: {hard_fork_result}")
    
    # Test This American Life
    tal_result = test_this_american_life()
    if tal_result:
        print(f"This American Life transcript preview: {tal_result}")
    
    if hard_fork_result or tal_result:
        print("\n✅ Found at least one transcript!")
    else:
        print("\n❌ No transcripts found in manual tests")

if __name__ == "__main__":
    main()