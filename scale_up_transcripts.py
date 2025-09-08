#!/usr/bin/env python3
"""Scale up transcript discovery - find more from researched sources"""

import requests
from bs4 import BeautifulSoup
import re
import sqlite3
from datetime import datetime
from pathlib import Path
import json
import xml.etree.ElementTree as ET
import time

def get_rss_episodes(rss_url, limit=10):
    """Get recent episodes from RSS feed"""
    try:
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
        response = session.get(rss_url, timeout=15)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        episodes = []
        
        for item in root.findall('.//item')[:limit]:
            title_elem = item.find('title')
            if title_elem is not None and title_elem.text:
                episodes.append({
                    'title': title_elem.text.strip()
                })
        
        return episodes
        
    except Exception as e:
        print(f"      Error fetching RSS: {e}")
        return []

def try_this_american_life(episodes):
    """Try This American Life transcripts"""
    found = 0
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    for episode in episodes[:5]:  # Try 5
        title = episode['title']
        
        # Extract episode number
        ep_match = re.search(r'(\d+):', title)
        if not ep_match:
            continue
        
        ep_num = ep_match.group(1)
        transcript_url = f"https://www.thisamericanlife.org/{ep_num}/transcript"
        
        try:
            response = session.get(transcript_url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Look for transcript content
                transcript_content = soup.find('div', class_='transcript-section') or \
                                   soup.find('div', class_='transcript') or \
                                   soup.find('main')
                
                if transcript_content:
                    text = transcript_content.get_text(strip=True)
                    if len(text) > 2000:
                        # Check if exists
                        if not transcript_exists(title, "This American Life"):
                            add_to_database(title, text, transcript_url, "This American Life")
                            found += 1
                            print(f"      ✅ This American Life: {title[:60]}...")
                        
        except Exception as e:
            print(f"      ❌ TAL {title[:30]}: {e}")
            continue
    
    return found

def try_econtalk(episodes):
    """Try EconTalk transcripts"""
    found = 0
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    for episode in episodes[:3]:  # Try 3
        title = episode['title']
        
        if transcript_exists(title, "EconTalk"):
            continue
        
        # Try URL patterns
        title_slug = re.sub(r'[^\w\s-]', '', title.lower())
        title_slug = re.sub(r'[-\s]+', '-', title_slug).strip('-')[:50]  # Limit length
        
        test_urls = [
            f"https://www.econtalk.org/{title_slug}/",
            f"https://www.econtalk.org/podcast/{title_slug}/",
        ]
        
        for test_url in test_urls:
            try:
                response = session.get(test_url, timeout=8)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    transcript_div = soup.find('div', class_='transcript') or \
                                   soup.find('div', {'id': 'transcript'}) or \
                                   soup.find('section', class_='transcript')
                    
                    if transcript_div:
                        text = transcript_div.get_text(strip=True)
                        if len(text) > 2000:
                            add_to_database(title, text, test_url, "EconTalk")
                            found += 1
                            print(f"      ✅ EconTalk: {title[:60]}...")
                            break
                            
            except Exception:
                continue
                
        time.sleep(0.5)  # Brief pause
    
    return found

def try_more_lex_fridman():
    """Try more Lex Fridman episodes"""
    # Get Lex RSS and try more episodes
    rss_url = "https://lexfridman.com/feed/podcast/"
    episodes = get_rss_episodes(rss_url, limit=20)
    
    found = 0
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    for episode in episodes:
        title = episode['title']
        
        if transcript_exists(title, "Lex Fridman Podcast"):
            continue
            
        # Extract guest name
        guest_match = re.search(r'#\d+\s*[-–]\s*([^:]+)', title)
        if not guest_match:
            continue
        
        guest_name = guest_match.group(1).strip()
        slug = re.sub(r'[^\w\s-]', '', guest_name.lower())
        slug = re.sub(r'[-\s]+', '-', slug).strip('-')
        
        transcript_url = f"https://lexfridman.com/{slug}-transcript"
        
        try:
            response = session.get(transcript_url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                content = soup.get_text(strip=True)
                
                if content and len(content) > 5000:
                    add_to_database(title, content, transcript_url, "Lex Fridman Podcast")
                    found += 1
                    print(f"      ✅ Lex: {title[:60]}...")
                    
        except Exception as e:
            continue
        
        time.sleep(0.3)  # Brief pause
    
    return found

def transcript_exists(title, podcast_name):
    """Check if transcript already exists"""
    db_path = Path.home() / "dev" / "atlas" / "atlas.db"
    conn = sqlite3.connect(db_path)
    
    result = conn.execute("""
        SELECT 1 FROM content 
        WHERE title LIKE ? AND content_type = 'transcript' 
        LIMIT 1
    """, (f"%{title[:50]}%",)).fetchone()
    
    conn.close()
    return result is not None

def add_to_database(title, content, url, podcast_name):
    """Add transcript to Atlas database"""
    db_path = Path.home() / "dev" / "atlas" / "atlas.db"
    conn = sqlite3.connect(db_path)
    
    conn.execute("""
        INSERT INTO content (
            title, url, content, content_type, metadata, 
            created_at, updated_at
        ) VALUES (?, ?, ?, 'transcript', ?, ?, ?)
    """, (
        f"[TRANSCRIPT] {title}",
        url,
        content,
        f'{{"podcast": "{podcast_name}", "episode": "{title}"}}',
        datetime.now().isoformat(),
        datetime.now().isoformat()
    ))
    conn.commit()
    conn.close()

# Main execution
print("🚀 Scaling up transcript discovery...")

# Get starting count
db_path = Path.home() / "dev" / "atlas" / "atlas.db"
conn = sqlite3.connect(db_path)
start_count = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'transcript'").fetchone()[0]
conn.close()

print(f"📊 Starting with {start_count} transcripts")

# Try This American Life
print("\n🎙️ Trying This American Life...")
tal_episodes = get_rss_episodes("https://www.thisamericanlife.org/podcast/rss.xml", limit=10)
tal_found = try_this_american_life(tal_episodes)
print(f"   Found {tal_found} new This American Life transcripts")

# Try EconTalk
print("\n💰 Trying EconTalk...")
econ_episodes = get_rss_episodes("https://feeds.simplecast.com/wgl4xEgL", limit=8)
econ_found = try_econtalk(econ_episodes)
print(f"   Found {econ_found} new EconTalk transcripts")

# Try more Lex Fridman
print("\n🤖 Trying more Lex Fridman...")
lex_found = try_more_lex_fridman()
print(f"   Found {lex_found} new Lex Fridman transcripts")

# Final count
conn = sqlite3.connect(db_path)
end_count = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'transcript'").fetchone()[0]
conn.close()

total_found = tal_found + econ_found + lex_found
print(f"\n📈 RESULTS:")
print(f"   📝 New transcripts found: {total_found}")
print(f"   📊 Total transcripts: {start_count} → {end_count}")
print(f"   🎯 Success rate: {total_found}/{tal_episodes.__len__() + econ_episodes.__len__() + 20}")

if total_found > 0:
    print("\n✅ Transcript discovery scaled up successfully!")