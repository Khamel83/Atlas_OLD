#!/usr/bin/env python3
"""
Simple Transcript Checker - Actually works

Tests real episodes to see where transcripts exist.
No complex systems, just direct checking.
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
import re

def check_econtalk_transcript(episode_title):
    """Check EconTalk - they have excellent transcripts"""
    try:
        # EconTalk episode URLs are predictable
        title_slug = episode_title.lower().replace(' ', '-').replace('(', '').replace(')', '')
        title_slug = re.sub(r'[^a-z0-9-]', '', title_slug)
        
        # Try the episode page
        url = f"https://www.econtalk.org/{title_slug}/"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for transcript content
            transcript_section = soup.find('div', class_=re.compile(r'transcript', re.I))
            if transcript_section:
                return transcript_section.get_text(strip=True)
            
            # Look for large text content (full episode transcripts)
            content_divs = soup.find_all(['div', 'article'], class_=re.compile(r'content|entry|post', re.I))
            for div in content_divs:
                text = div.get_text(strip=True)
                if len(text) > 5000:  # Substantial transcript
                    return text
        
    except Exception as e:
        print(f"EconTalk check failed: {e}")
    
    return None

def check_slate_transcript(podcast_name, episode_title):
    """Check Slate podcasts - they often have article versions"""
    try:
        # Slate converts many episodes to articles
        search_url = f"https://slate.com/search?q={episode_title}"
        response = requests.get(search_url, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for article links
            article_links = soup.find_all('a', href=re.compile(r'/podcasts/|/articles/'))
            for link in article_links[:3]:  # Check top 3 results
                article_url = 'https://slate.com' + link['href']
                article_response = requests.get(article_url, timeout=10)
                
                if article_response.status_code == 200:
                    article_soup = BeautifulSoup(article_response.content, 'html.parser')
                    article_content = article_soup.find(['div', 'article'], class_=re.compile(r'article-body|post-content'))
                    
                    if article_content:
                        text = article_content.get_text(strip=True)
                        if len(text) > 2000:  # Substantial content
                            return text
    
    except Exception as e:
        print(f"Slate check failed: {e}")
    
    return None

def check_nyt_transcript(podcast_name, episode_title):
    """Check NYTimes podcasts - professional transcripts"""
    try:
        # NYTimes often has full transcripts
        if "hard fork" in podcast_name.lower():
            search_terms = episode_title.replace(' ', '+')
            search_url = f"https://www.nytimes.com/search?query=hard+fork+{search_terms}"
            
            response = requests.get(search_url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Look for article links
                article_links = soup.find_all('a', href=re.compile(r'/\d{4}/\d{2}/\d{2}/'))
                for link in article_links[:2]:
                    article_url = 'https://www.nytimes.com' + link['href']
                    article_response = requests.get(article_url, timeout=10)
                    
                    if article_response.status_code == 200:
                        article_soup = BeautifulSoup(article_response.content, 'html.parser')
                        content = article_soup.find(['div', 'section'], class_=re.compile(r'story-body|article-body'))
                        
                        if content:
                            text = content.get_text(strip=True)
                            if len(text) > 3000:
                                return text
    
    except Exception as e:
        print(f"NYT check failed: {e}")
    
    return None

def actually_find_transcripts():
    """Actually find transcripts instead of building systems"""
    
    with sqlite3.connect("data/atlas.db") as conn:
        # Get unprocessed episodes from podcasts we know have transcripts
        episodes = conn.execute("""
            SELECT id, podcast_name, title, audio_url 
            FROM podcast_episodes 
            WHERE processed = 0 
            AND (
                podcast_name LIKE '%EconTalk%' OR
                podcast_name LIKE '%Slate%' OR  
                podcast_name LIKE '%Hard Fork%' OR
                podcast_name LIKE '%Ezra Klein%'
            )
            LIMIT 20
        """).fetchall()
        
        if not episodes:
            print("No episodes from transcript-heavy podcasts found")
            return
        
        found_count = 0
        
        for episode_id, podcast_name, title, audio_url in episodes:
            print(f"Checking: {podcast_name} - {title[:40]}...")
            
            transcript = None
            
            # Route to appropriate checker
            if "econtalk" in podcast_name.lower():
                transcript = check_econtalk_transcript(title)
            elif "slate" in podcast_name.lower():
                transcript = check_slate_transcript(podcast_name, title)  
            elif "hard fork" in podcast_name.lower() or "ezra klein" in podcast_name.lower():
                transcript = check_nyt_transcript(podcast_name, title)
            
            if transcript:
                # Found real transcript!
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, created_at)
                    VALUES (?, ?, 'podcast_transcript', CURRENT_TIMESTAMP)
                """, (f"[TRANSCRIPT] {title}", transcript))
                
                found_count += 1
                print(f"  ✓ FOUND TRANSCRIPT: {len(transcript)} chars")
            else:
                print(f"  ✗ No transcript found")
            
            # Mark as processed
            conn.execute("UPDATE podcast_episodes SET processed = 1 WHERE id = ?", (episode_id,))
        
        conn.commit()
        print(f"\nActual results: {found_count} transcripts found out of {len(episodes)} episodes")

if __name__ == "__main__":
    actually_find_transcripts()