#!/usr/bin/env python3
import feedparser
import sqlite3
import requests

# Simple RSS feed importer - run once to populate episodes
feeds = {
    "Acquired": "https://feeds.simplecast.com/7wT59F0l",
    "99% Invisible": "https://feeds.99percentinvisible.org/99percentinvisible",
    "This American Life": "https://feeds.thisamericanlife.org/talpodcast",
    "Radiolab": "https://feeds.feedburner.com/radiolab",
    "ATP": "https://atp.fm/rss"
}

def import_episodes():
    # Create table
    with sqlite3.connect("data/atlas.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS podcast_episodes (
                id INTEGER PRIMARY KEY,
                title TEXT,
                audio_url TEXT UNIQUE,
                podcast_name TEXT,
                processed BOOLEAN DEFAULT 0
            )
        """)
        
        total = 0
        for name, url in feeds.items():
            print(f"Importing {name}...")
            feed = feedparser.parse(url)
            
            for entry in feed.entries[:10]:  # Only 10 per podcast for testing
                audio_url = None
                if hasattr(entry, 'enclosures'):
                    for enc in entry.enclosures:
                        if 'audio' in enc.type:
                            audio_url = enc.href
                            break
                
                if audio_url:
                    try:
                        conn.execute("""
                            INSERT OR IGNORE INTO podcast_episodes 
                            (title, audio_url, podcast_name) 
                            VALUES (?, ?, ?)
                        """, (entry.title, audio_url, name))
                        total += 1
                    except:
                        pass
        
        conn.commit()
        print(f"Imported {total} episodes")

if __name__ == "__main__":
    import_episodes()