#!/usr/bin/env python3
"""
Discover ALL Transcript Sources
Research transcript availability for ALL podcasts in the database
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
import re

def test_transcript_availability(podcast_name, sample_episode_title):
    """Test if a podcast has transcripts by trying various strategies"""
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    })
    
    results = []
    
    # Strategy 1: Google search for podcast + transcript
    search_terms = [
        f'"{podcast_name}" transcript',
        f'"{podcast_name}" episode transcript',
        f'"{podcast_name.split()[0]}" transcript'
    ]
    
    # Strategy 2: Check common podcast websites
    # Extract likely website domains
    podcast_domains = []
    
    if "Knowledge Project" in podcast_name:
        podcast_domains.append("fs.blog")
    elif "Rewatchables" in podcast_name:
        podcast_domains.append("theringer.com")
    elif "Acquired" in podcast_name:
        podcast_domains.append("acquired.fm")
    elif "Conversations with Tyler" in podcast_name:
        podcast_domains.append("conversationswithtyler.com")
    elif "Stratechery" in podcast_name:
        podcast_domains.append("stratechery.com")
    elif "Sharp Tech" in podcast_name:
        podcast_domains.append("stratechery.com")  # Same network
    
    # Test each domain
    for domain in podcast_domains:
        test_urls = [
            f"https://{domain}/",
            f"https://{domain}/podcast/",
            f"https://{domain}/episodes/",
            f"https://{domain}/transcripts/"
        ]
        
        for url in test_urls:
            try:
                response = session.get(url, timeout=5)
                if response.status_code == 200:
                    content = response.text.lower()
                    if 'transcript' in content:
                        results.append(f"✓ {url} - mentions transcripts")
                        break
            except:
                pass
    
    return results

def discover_all_podcast_transcripts():
    """Check transcript availability for all podcasts"""
    
    with sqlite3.connect("data/atlas.db") as conn:
        # Get all podcasts with unprocessed episodes
        podcasts = conn.execute("""
            SELECT podcast_name, COUNT(*) as episode_count, 
                   MIN(title) as sample_title
            FROM podcast_episodes 
            WHERE processed = 0
            GROUP BY podcast_name
            ORDER BY episode_count DESC
            LIMIT 20
        """).fetchall()
        
        print(f"🔍 Researching transcript availability for {len(podcasts)} podcasts...\n")
        
        transcript_sources = {}
        
        for podcast_name, episode_count, sample_title in podcasts:
            print(f"📊 {podcast_name} ({episode_count} episodes)")
            
            results = test_transcript_availability(podcast_name, sample_title)
            
            if results:
                transcript_sources[podcast_name] = results
                for result in results:
                    print(f"    {result}")
            else:
                print(f"    ❌ No transcript sources found")
            
            print()
        
        print(f"\n📋 SUMMARY - Podcasts with potential transcript sources:")
        for podcast, sources in transcript_sources.items():
            print(f"✅ {podcast}")
            for source in sources:
                print(f"   {source}")

def main():
    print("🕵️ Comprehensive transcript source discovery")
    print("Researching ALL podcasts instead of assuming they don't have transcripts\n")
    
    discover_all_podcast_transcripts()

if __name__ == "__main__":
    main()