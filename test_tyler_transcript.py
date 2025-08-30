#!/usr/bin/env python3
"""
Test Tyler Cowen transcript scraping
"""

import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

def scrape_tyler_transcript(episode_url):
    """Test scraping Tyler Cowen transcript"""
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    try:
        response = session.get(episode_url, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the main content area - Tyler's site uses .text-block
        content_area = soup.find('div', class_='text-block')
        if not content_area:
            content_area = soup.find('div', class_='entry-content')
        if not content_area:
            content_area = soup.find('article')
        if not content_area:
            content_area = soup.find('main')
        
        if content_area:
            # Remove non-transcript elements
            for elem in content_area.find_all(['script', 'style', 'aside', 'nav', 'header', 'footer']):
                elem.decompose()
            
            # Get title
            title_elem = soup.find('h1')
            title = title_elem.get_text().strip() if title_elem else "Tyler Cowen Episode"
            
            text = content_area.get_text(separator='\n', strip=True)
            
            print(f"Title: {title}")
            print(f"Content length: {len(text)}")
            print(f"Sample text: {text[:500]}...")
            
            # Basic checks for transcript quality
            if len(text) > 1000:
                if any(name in text.upper() for name in ['TYLER:', 'COWEN:', 'GUEST:']):
                    print("✅ Looks like a proper transcript")
                    return {
                        'title': title,
                        'content': text,
                        'url': episode_url
                    }
                else:
                    print("⚠️  Text found but doesn't look like transcript format")
            else:
                print("⚠️  Not enough text content")
        
        return None
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def save_to_atlas(transcript_data):
    """Save transcript to Atlas"""
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    
    title = f"[TRANSCRIPT] {transcript_data['title']}"
    content = f"Conversations with Tyler - {transcript_data['title']}\n\n{transcript_data['content']}"
    
    cursor.execute("""
        INSERT OR REPLACE INTO content 
        (url, title, content, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        transcript_data['url'],
        title,
        content[:10000],  # Limit content
        datetime.now().isoformat()
    ))
    
    conn.commit()
    conn.close()
    print("✅ Saved to Atlas database")

if __name__ == "__main__":
    print("🎙️ Testing Tyler Cowen transcript scraping")
    
    # Test with the Nate Silver episode
    test_url = "https://conversationswithtyler.com/episodes/nate-silver/"
    
    transcript = scrape_tyler_transcript(test_url)
    
    if transcript:
        print("\n🎉 Successfully extracted transcript!")
        save_to_atlas(transcript)
    else:
        print("\n❌ Failed to extract transcript")