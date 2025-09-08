#!/usr/bin/env python3
"""
Investigate Lex Fridman podcast transcript structure
"""

import requests
from bs4 import BeautifulSoup
import re

def check_lex_fridman_structure():
    """Check how Lex Fridman organizes transcripts"""
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    # Check the main podcast page
    main_url = "https://lexfridman.com/podcast"
    print(f"Checking: {main_url}")
    
    try:
        response = session.get(main_url, timeout=10)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for episode links
            links = soup.find_all('a', href=True)
            episode_links = []
            
            for link in links:
                href = link.get('href')
                if href and ('/podcast' in href or '#' in href):
                    episode_links.append(href)
            
            print(f"Found {len(episode_links)} potential episode links")
            
            # Try to find a specific episode pattern
            # Look for episode numbers
            for link in episode_links[:10]:
                if re.search(r'#?\d+', link):
                    print(f"Episode link pattern: {link}")
            
            # Try a few specific episode URLs
            test_episodes = ['450', '449', '448']
            
            for episode_num in test_episodes:
                episode_url = f"https://lexfridman.com/{episode_num}"
                print(f"\nTesting episode URL: {episode_url}")
                
                try:
                    ep_response = session.get(episode_url, timeout=10)
                    print(f"Status: {ep_response.status_code}")
                    
                    if ep_response.status_code == 200:
                        ep_soup = BeautifulSoup(ep_response.content, 'html.parser')
                        
                        # Look for transcript content
                        text = ep_soup.get_text().lower()
                        if 'transcript' in text:
                            print("✓ Found 'transcript' on episode page")
                            
                            # Look for substantial text content
                            content_areas = ep_soup.find_all(['div', 'article', 'section'])
                            for area in content_areas:
                                area_text = area.get_text(separator=' ', strip=True)
                                if len(area_text) > 5000:  # Substantial content
                                    print(f"✓ Found large content area: {len(area_text)} chars")
                                    print(f"Preview: {area_text[:200]}...")
                                    return episode_url, area_text[:1000]
                        
                        print("✗ No transcript found on this episode page")
                    
                except Exception as e:
                    print(f"Error accessing episode {episode_num}: {e}")
            
    except Exception as e:
        print(f"Error accessing main page: {e}")
    
    return None, None

def main():
    print("🔍 Investigating Lex Fridman transcript structure...\n")
    
    working_url, sample_content = check_lex_fridman_structure()
    
    if working_url:
        print(f"\n✅ Found working pattern!")
        print(f"URL: {working_url}")
        print(f"Sample content: {sample_content}")
    else:
        print(f"\n❌ Need to investigate further")

if __name__ == "__main__":
    main()