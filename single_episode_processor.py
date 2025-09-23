#!/usr/bin/env python3
"""
Process a single episode for the Atlas Manager
"""

import sys
import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import time

def process_episode(episode_id, episode_url, podcast_name):
    """Process a single episode and extract transcript"""
    try:
        # Connect to database
        conn = sqlite3.connect('data/atlas.db')
        cursor = conn.cursor()

        # Load sources cache
        sources_cache = {}
        try:
            with open('config/podcast_sources_cache.json', 'r') as f:
                sources_cache = json.load(f)
        except:
            pass

        # Setup session
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })

        # Fetch episode page
        response = session.get(episode_url, timeout=15)
        if response.status_code != 200:
            print(f"No transcript found (HTTP {response.status_code})")
            return False

        soup = BeautifulSoup(response.content, 'html.parser')

        # Try cached patterns first
        transcript = None
        for podcast_key, podcast_data in sources_cache.items():
            if podcast_name.lower() in podcast_key.lower():
                network_config = podcast_data.get('config', {})
                if 'selectors' in network_config:
                    for selector in network_config['selectors']:
                        element = soup.select_one(selector)
                        if element:
                            text = element.get_text(separator=' ', strip=True)
                            min_length = network_config.get('min_length', 1000)
                            if len(text) > min_length:
                                transcript = text
                                break
                if transcript:
                    break

        # Generic selectors if no cached patterns found
        if not transcript:
            selectors = ['.transcript', '#transcript', '.episode-transcript', '[class*="transcript"]']
            for selector in selectors:
                element = soup.select_one(selector)
                if element:
                    text = element.get_text(separator=' ', strip=True)
                    if len(text) > 1000 and 'transcript' in text.lower():
                        transcript = text
                        break

        if transcript:
            # Store transcript
            cursor.execute("""
                INSERT INTO content (title, url, content, content_type, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                f"[{podcast_name}] Episode {episode_id}",
                episode_url,
                transcript,
                'podcast_transcript',
                datetime.now().isoformat(),
                datetime.now().isoformat()
            ))
            conn.commit()
            print(f"Transcript found and stored ({len(transcript):,} chars)")
            return True
        else:
            print("No transcript found")
            return False

    except Exception as e:
        print(f"Error processing episode: {e}")
        return False
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 single_episode_processor.py <episode_id> <episode_url> <podcast_name>")
        sys.exit(1)

    episode_id = sys.argv[1]
    episode_url = sys.argv[2]
    podcast_name = sys.argv[3]

    process_episode(episode_id, episode_url, podcast_name)