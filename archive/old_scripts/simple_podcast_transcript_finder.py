#!/usr/bin/env python3
"""
Simple Podcast Transcript Finder

For each high-quality podcast, just search until we find ONE good transcript source.
Keep it simple and effective.
"""

import requests
import sqlite3
import json
import time
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def get_one_episode(feed_url):
    """Get just the most recent episode"""
    try:
        response = requests.get(feed_url, timeout=15)
        root = ET.fromstring(response.content)
        
        # Just get the first/most recent episode
        item = root.find('.//item')
        if item is not None:
            title_elem = item.find('title')
            link_elem = item.find('link')
            
            if title_elem is not None and link_elem is not None:
                return {
                    'title': title_elem.text,
                    'link': link_elem.text
                }
        return None
        
    except Exception as e:
        return None

def simple_transcript_search(url):
    """Simple transcript search - just look for text content"""
    try:
        session = requests.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0 (compatible)'})
        
        response = session.get(url, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove junk
        for tag in soup.find_all(['script', 'style', 'nav', 'aside', 'footer']):
            tag.decompose()
        
        # Try different content areas
        selectors = [
            '.transcript', '#transcript', 
            '.content', '.post-content', '.entry-content',
            'main', 'article', 'body'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                text = element.get_text(separator=' ', strip=True)
                # If we get substantial text, that's probably it
                if len(text) > 2000:
                    return text[:20000]  # Limit to 20K chars
        
        return None
        
    except Exception:
        return None

def save_transcript(episode, transcript_text, podcast_title):
    """Save one transcript to database"""
    try:
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        
        title = f"[TRANSCRIPT] {episode['title']}"
        content = f"Podcast: {podcast_title}\\n\\n{transcript_text}"
        
        cursor.execute("""
            INSERT OR IGNORE INTO content 
            (url, title, content, created_at)
            VALUES (?, ?, ?, ?)
        """, (
            episode['link'],
            title[:500],
            content,
            datetime.now().isoformat()
        ))
        
        conn.commit()
        conn.close()
        return True
        
    except Exception:
        return False

def main():
    """Simple: try each high-quality podcast until we get one transcript per podcast"""
    
    print("🎙️ SIMPLE PODCAST TRANSCRIPT FINDER")
    print("=" * 50)
    
    # Load analysis
    with open('podcast_transcript_analysis.json') as f:
        analysis = json.load(f)
    
    # Get all podcasts - high, medium, and even low confidence ones
    candidates = analysis['podcasts']
    
    print(f"📊 Found {len(candidates)} candidate podcasts")
    
    total_found = 0
    
    for i, podcast in enumerate(candidates, 1):
        title = podcast['title']
        feed_url = podcast['feed_url']
        
        print(f"\\n{i}. 🎙️ {title[:50]}...")
        
        # Get one recent episode
        episode = get_one_episode(feed_url)
        if not episode:
            print(f"   ❌ No episodes found")
            continue
        
        print(f"   📻 Trying: {episode['title'][:40]}...")
        
        # Try to find transcript
        transcript_text = simple_transcript_search(episode['link'])
        
        if transcript_text and len(transcript_text) > 1000:
            if save_transcript(episode, transcript_text, title):
                total_found += 1
                print(f"   ✅ SUCCESS! ({len(transcript_text)} chars)")
            else:
                print(f"   ❌ Save failed")
        else:
            print(f"   ⚠️  No substantial transcript found")
        
        time.sleep(2)  # Be nice to servers
        
        # Process more podcasts - aim for broader coverage
        if total_found >= 60:  # Higher limit for broader coverage
            print(f"\\n🎯 Found {total_found} transcripts - stopping here")
            break
    
    print(f"\\n🎉 SIMPLE SEARCH COMPLETE!")
    print(f"✅ New transcripts found: {total_found}")
    
    # Show final count
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM content WHERE title LIKE '%TRANSCRIPT%'")
    total_transcripts = cursor.fetchone()[0]
    conn.close()
    
    print(f"🎙️ Total transcripts in database: {total_transcripts}")
    
    return total_found > 0

if __name__ == "__main__":
    main()