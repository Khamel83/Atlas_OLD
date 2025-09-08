#!/usr/bin/env python3
"""Process ALL podcasts from the CSV - no more selective processing"""

import requests
from bs4 import BeautifulSoup
import re
import sqlite3
from datetime import datetime
from pathlib import Path
import csv
import xml.etree.ElementTree as ET
import time
from concurrent.futures import ThreadPoolExecutor
import json

# Load RSS feeds from CSV
def load_rss_feeds_from_csv():
    feeds = {}
    try:
        with open('podcast_rss_feeds.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    name = row[0].strip()
                    url = row[1].strip()
                    if name and url:
                        feeds[name] = url
    except Exception as e:
        print(f"⚠️  CSV RSS load error: {e}")
    
    return feeds

# Load CSV priorities
def load_podcast_priorities():
    podcasts = {}
    try:
        with open('config/podcasts_prioritized_updated.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('Exclude', '1') == '0':  # Only non-excluded
                    name = row['Podcast Name'].strip()
                    podcasts[name] = {
                        'count': int(row.get('Count', 0)),
                        'future': row.get('Future', '0') == '1',
                        'transcript_only': row.get('Trasncript_Only', '0') == '1',
                        'category': row.get('Category', 'Other')
                    }
    except Exception as e:
        print(f"⚠️  CSV load error: {e}")
    
    return podcasts

def get_rss_episodes(rss_url, limit=10):
    """Get recent episodes from RSS"""
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    try:
        response = session.get(rss_url, timeout=15)
        response.raise_for_status()
        
        root = ET.fromstring(response.content)
        episodes = []
        
        for item in root.findall('.//item')[:limit]:
            title_elem = item.find('title')
            if title_elem is not None and title_elem.text:
                episodes.append({'title': title_elem.text.strip()})
        
        return episodes
    except Exception as e:
        return []

def transcript_exists(title, podcast_name):
    """Check if already in database"""
    db_path = Path.home() / "dev" / "atlas" / "atlas.db"
    conn = sqlite3.connect(db_path)
    
    result = conn.execute("""
        SELECT 1 FROM content 
        WHERE title LIKE ? AND content_type = 'transcript' 
        LIMIT 1
    """, (f"%{title[:50]}%",)).fetchone()
    
    conn.close()
    return result is not None

def add_transcript(title, content, url, podcast_name):
    """Add to database"""
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

# Transcript extraction strategies
def try_lex_fridman(episodes, podcast_name):
    """Lex Fridman pattern"""
    found = 0
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
    
    for episode in episodes:
        title = episode['title']
        if transcript_exists(title, podcast_name):
            continue
            
        guest_match = re.search(r'#\d+\s*[-–]\s*([^:]+)', title)
        if not guest_match:
            continue
        
        guest_name = guest_match.group(1).strip()
        slug = re.sub(r'[^\w\s-]', '', guest_name.lower())
        slug = re.sub(r'[-\s]+', '-', slug).strip('-')
        
        url = f"https://lexfridman.com/{slug}-transcript"
        
        try:
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                content = soup.get_text(strip=True)
                
                if content and len(content) > 5000:
                    add_transcript(title, content, url, podcast_name)
                    found += 1
                    print(f"      ✅ {title[:60]}...")
        except:
            pass
        
        time.sleep(0.2)
    
    return found

def try_this_american_life(episodes, podcast_name):
    """This American Life pattern"""
    found = 0
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
    
    for episode in episodes:
        title = episode['title']
        if transcript_exists(title, podcast_name):
            continue
            
        ep_match = re.search(r'(\d+):', title)
        if not ep_match:
            continue
        
        ep_num = ep_match.group(1)
        url = f"https://www.thisamericanlife.org/{ep_num}/transcript"
        
        try:
            response = session.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                content_div = soup.find('div', class_='transcript-section') or soup.find('main')
                
                if content_div:
                    content = content_div.get_text(strip=True)
                    if len(content) > 2000:
                        add_transcript(title, content, url, podcast_name)
                        found += 1
                        print(f"      ✅ {title[:60]}...")
        except:
            pass
        
        time.sleep(0.3)
    
    return found

def try_generic_transcript_search(episodes, podcast_name, rss_url):
    """Generic transcript discovery"""
    found = 0
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
    
    # Try to determine website from RSS URL
    website = None
    if 'npr.org' in rss_url:
        website = 'npr.org'
    elif 'nytimes.com' in rss_url or 'simplecast.com' in rss_url:
        # NYTimes podcasts (Hard Fork, Ezra Klein)
        website = 'nytimes'
    elif 'econtalk' in rss_url:
        website = 'econtalk'
    elif 'megaphone.fm' in rss_url:
        # Slate podcasts, Vox podcasts
        if 'slate' in podcast_name.lower():
            website = 'slate'
        elif 'vox' in podcast_name.lower() or 'today' in podcast_name.lower():
            website = 'vox'
    
    # Try website-specific patterns
    if website == 'econtalk':
        for episode in episodes[:3]:
            title = episode['title']
            if transcript_exists(title, podcast_name):
                continue
                
            slug = re.sub(r'[^\w\s-]', '', title.lower())
            slug = re.sub(r'[-\s]+', '-', slug).strip('-')[:50]
            
            for test_url in [f"https://www.econtalk.org/{slug}/", f"https://www.econtalk.org/podcast/{slug}/"]:
                try:
                    response = session.get(test_url, timeout=8)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        transcript_div = soup.find('div', class_='transcript')
                        
                        if transcript_div:
                            content = transcript_div.get_text(strip=True)
                            if len(content) > 2000:
                                add_transcript(title, content, test_url, podcast_name)
                                found += 1
                                print(f"      ✅ {title[:60]}...")
                                break
                except:
                    continue
                    
    elif website == 'npr':
        # NPR transcripts are usually available
        for episode in episodes[:5]:
            title = episode['title']
            if transcript_exists(title, podcast_name):
                continue
            
            # Try NPR transcript patterns
            slug = re.sub(r'[^\w\s-]', '', title.lower())
            slug = re.sub(r'[-\s]+', '-', slug).strip('-')[:40]
            
            test_urls = [
                f"https://www.npr.org/transcripts/{slug}",
                f"https://www.npr.org/{slug}/transcript",
            ]
            
            for test_url in test_urls:
                try:
                    response = session.get(test_url, timeout=8)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        content = soup.get_text(strip=True)
                        
                        if len(content) > 3000:
                            add_transcript(title, content, test_url, podcast_name)
                            found += 1
                            print(f"      ✅ {title[:60]}...")
                            break
                except:
                    continue
    elif website == 'nytimes':
        for episode in episodes[:5]: # Limit to recent episodes for testing
            title = episode['title']
            if transcript_exists(title, podcast_name):
                continue
            
            # Try to construct a plausible URL for the episode page
            # This is a heuristic and might need adjustment
            slug = re.sub(r'[^\\w\\s-]', '', title.lower())
            slug = re.sub(r'[-\\s]+', '-', slug).strip('-')
            
            # Assuming the episode URL is the primary source for the transcript
            # This might need to be more dynamic based on actual NYT podcast URLs
            # For now, we'll try to use the RSS feed URL's domain and append a slug
            # This is a placeholder and needs refinement based on actual NYT URL patterns
            # Given the 403, I cannot reliably construct the URL.
            # I will try to use the podcast_name to construct a base URL and then search for the title.
            
            # For now, I will make a very general attempt to find content on the RSS feed URL itself
            # or a derived URL. This is unlikely, or a generic NYT transcript page.
            # This part is highly speculative due to the 403 error.
            
            # Placeholder for NYTimes transcript extraction
            # This needs to be refined once direct web access is possible.
            # For now, I will just print a message indicating this limitation.
            print(f"      ⚠️  Cannot fetch NYTimes transcripts due to 403 Forbidden error. Skipping {title}")
            continue
    
    return found

# Main processing
def main():
    print("🚀 Processing ALL podcasts from your priority list...")
    
    # Load data
    feeds = load_rss_feeds_from_csv()
    priorities = load_podcast_priorities()
    
    print(f"📊 Found {len(priorities)} podcasts to process (Exclude=0)")
    print(f"📡 Have RSS feeds for {len(feeds)} podcasts")
    
    # Get starting count
    db_path = Path.home() / "dev" / "atlas" / "atlas.db"
    conn = sqlite3.connect(db_path)
    start_count = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'transcript'").fetchone()[0]
    conn.close()
    
    print(f"📝 Starting with {start_count} transcripts")
    
    total_found = 0
    processed_count = 0
    
    # Process each podcast
    for podcast_name, info in priorities.items():
        processed_count += 1
        print(f"\n📻 {processed_count}/{len(priorities)} - {podcast_name} ({info['category']})")
        
        # Get RSS URL
        rss_url = feeds.get(podcast_name)
        if not rss_url:
            print(f"      ⚠️  No RSS URL found")
            continue
        
        # Get episodes
        episodes = get_rss_episodes(rss_url, limit=min(10, info['count'] if info['count'] > 0 else 5))
        if not episodes:
            print(f"      ⚠️  No episodes found")
            continue
        
        print(f"      📻 Got {len(episodes)} episodes, trying transcript extraction...")
        
        # Apply appropriate strategy
        found = 0
        if podcast_name == "Lex Fridman Podcast":
            found = try_lex_fridman(episodes, podcast_name)
        elif podcast_name == "This American Life":
            found = try_this_american_life(episodes, podcast_name)
        else:
            # Generic approach
            found = try_generic_transcript_search(episodes, podcast_name, rss_url)
        
        if found > 0:
            print(f"      🎉 Found {found} transcripts!")
            total_found += found
        else:
            print(f"      😕 No transcripts found")
    
    # Final results
    conn = sqlite3.connect(db_path)
    end_count = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'transcript'").fetchone()[0]
    conn.close()
    
    print(f"\n📈 FINAL RESULTS:")
    print(f"   📝 New transcripts found: {total_found}")
    print(f"   📊 Total transcripts: {start_count} → {end_count}")
    print(f"   🎯 Podcasts processed: {processed_count}")
    
    if total_found > 0:
        print("\n✅ Successfully scaled up transcript collection across ALL your podcasts!")

if __name__ == "__main__":
    main()
