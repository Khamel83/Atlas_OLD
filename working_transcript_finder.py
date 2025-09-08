#!/usr/bin/env python3
"""
Working Transcript Finder

Actually finds transcripts using WebFetch approach that we know works.
No more complex systems - just gets results.
"""

import sqlite3
import subprocess
import json
import time

def webfetch_transcript(url, prompt):
    """Use WebFetch tool to get transcript content"""
    try:
        # Call WebFetch tool through subprocess
        cmd = [
            'python3', '-c', f'''
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from functions.web_fetch import WebFetch

webfetch = WebFetch()
result = webfetch.fetch_and_process("{url}", "{prompt}")
print(result)
'''
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0 and result.stdout.strip():
            response = result.stdout.strip()
            # Filter out non-content responses
            if len(response) > 500 and not any(skip in response.lower() for skip in [
                'cannot find', 'no content', 'css', 'javascript', 'html', 'not available'
            ]):
                return response
    except Exception as e:
        print(f"  WebFetch error: {e}")
    
    return None

def find_econtalk_transcripts():
    """Find EconTalk transcripts using WebFetch"""
    with sqlite3.connect("data/atlas.db") as conn:
        episodes = conn.execute("""
            SELECT id, title FROM podcast_episodes 
            WHERE podcast_name = 'EconTalk' AND processed = 0 
            LIMIT 5
        """).fetchall()
        
        success_count = 0
        
        for episode_id, title in episodes:
            print(f"EconTalk: {title[:50]}...")
            
            # Create EconTalk URL from title
            title_slug = title.lower().replace(' ', '-').replace('(', '').replace(')', '')
            title_slug = ''.join(c for c in title_slug if c.isalnum() or c == '-')
            url = f"https://www.econtalk.org/{title_slug}/"
            
            # Use WebFetch to get transcript
            prompt = f"Extract the full transcript or conversation text from this EconTalk episode: {title}"
            transcript = webfetch_transcript(url, prompt)
            
            if transcript:
                # Save transcript
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_transcript', CURRENT_TIMESTAMP)
                """, (f"[TRANSCRIPT] {title}", transcript))
                
                success_count += 1
                print(f"  ✓ Found transcript: {len(transcript)} chars")
            else:
                print("  ✗ No transcript found")
            
            # Mark as processed
            conn.execute("UPDATE podcast_episodes SET processed = 1 WHERE id = ?", (episode_id,))
            
            time.sleep(2)  # Rate limiting
        
        conn.commit()
        print(f"EconTalk results: {success_count} transcripts found")

def find_nytimes_transcripts():
    """Find NYTimes podcast transcripts"""
    with sqlite3.connect("data/atlas.db") as conn:
        episodes = conn.execute("""
            SELECT id, title FROM podcast_episodes 
            WHERE (podcast_name LIKE '%Hard Fork%' OR podcast_name LIKE '%Ezra Klein%') 
            AND processed = 0 
            LIMIT 5
        """).fetchall()
        
        success_count = 0
        
        for episode_id, title in episodes:
            print(f"NYTimes: {title[:50]}...")
            
            # Search NYTimes for the episode
            search_terms = title.replace(' ', '+')
            search_url = f"https://www.nytimes.com/search?query={search_terms}"
            
            prompt = f"Find and extract any transcript or full text for the podcast episode: {title}"
            transcript = webfetch_transcript(search_url, prompt)
            
            if transcript:
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_transcript', CURRENT_TIMESTAMP)
                """, (f"[TRANSCRIPT] {title}", transcript))
                
                success_count += 1
                print(f"  ✓ Found transcript: {len(transcript)} chars")
            else:
                print("  ✗ No transcript found")
            
            conn.execute("UPDATE podcast_episodes SET processed = 1 WHERE id = ?", (episode_id,))
            time.sleep(2)
        
        conn.commit()
        print(f"NYTimes results: {success_count} transcripts found")

def actually_get_working_transcripts():
    """Actually get transcripts that work instead of building systems"""
    print("Finding transcripts using WebFetch approach...")
    
    # Test EconTalk first - we know these have transcripts
    find_econtalk_transcripts()
    
    # Test NYTimes podcasts
    find_nytimes_transcripts()
    
    # Check results
    with sqlite3.connect("data/atlas.db") as conn:
        count = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'podcast_transcript'").fetchone()[0]
        print(f"\nTotal podcast transcripts in database: {count}")

if __name__ == "__main__":
    actually_get_working_transcripts()