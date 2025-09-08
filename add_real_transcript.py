#!/usr/bin/env python3
"""Add transcript to the actual working Atlas database"""

import requests
from bs4 import BeautifulSoup
import re
import sqlite3
from datetime import datetime
from pathlib import Path

def extract_lex_transcript(title):
    """Extract transcript using our proven pattern"""
    guest_match = re.search(r'#\d+\s*[-–]\s*([^:]+)', title)
    if not guest_match:
        return None
    
    guest_name = guest_match.group(1).strip()
    slug = re.sub(r'[^\w\s-]', '', guest_name.lower())
    slug = re.sub(r'[-\s]+', '-', slug).strip('-')
    
    transcript_url = f"https://lexfridman.com/{slug}-transcript"
    print(f"🔍 Fetching: {transcript_url}")
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    try:
        response = session.get(transcript_url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Get main content 
            content = soup.get_text(strip=True)
            
            if content and len(content) > 5000:
                print(f"✅ Found transcript: {len(content):,} characters")
                return content, transcript_url
                
    except Exception as e:
        print(f"❌ Error: {e}")
    
    return None

# Test with Dave Hone (we know this works)
episode_title = "#480 – Dave Hone: T-Rex, Dinosaurs, Extinction, Evolution, and Jurassic Park"

print("🎯 Adding transcript to working Atlas database...")
result = extract_lex_transcript(episode_title)

if result:
    content, url = result
    
    # Connect to actual Atlas database
    db_path = Path.home() / "dev" / "atlas" / "atlas.db"
    conn = sqlite3.connect(db_path)
    
    # Check if already exists
    existing = conn.execute("""
        SELECT id FROM content 
        WHERE title LIKE ? AND content_type = 'transcript'
    """, (f"%{episode_title}%",)).fetchone()
    
    if existing:
        print("⚠️  Transcript already exists in database")
    else:
        # Insert using actual schema
        conn.execute("""
            INSERT INTO content (
                title, url, content, content_type, metadata, 
                created_at, updated_at
            ) VALUES (?, ?, ?, 'transcript', ?, ?, ?)
        """, (
            f"[TRANSCRIPT] {episode_title}",
            url,
            content,
            f'{{"podcast": "Lex Fridman Podcast", "episode": "{episode_title}"}}',
            datetime.now().isoformat(),
            datetime.now().isoformat()
        ))
        conn.commit()
        print("✅ Added transcript to Atlas database!")
        
        # Get new stats
        total = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'transcript'").fetchone()[0]
        print(f"📊 Total transcripts now: {total}")
    
    conn.close()
else:
    print("❌ Failed to fetch transcript")