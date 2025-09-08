#!/usr/bin/env python3
import feedparser
import sqlite3
import requests
import csv
import os

# Load ALL podcasts from prioritized CSV with RSS URLs
def load_all_feeds():
    feeds = {}
    csv_path = "config/podcasts_prioritized_updated.csv"
    
    if os.path.exists(csv_path):
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['Podcast Name'].strip('"')
                rss_url = row['RSS_URL'].strip()
                max_episodes = int(row['Count'])
                
                if rss_url and rss_url != '':
                    feeds[name] = {
                        'url': rss_url,
                        'max_episodes': max_episodes,
                        'category': row['Category']
                    }
                    print(f"Added: {name} ({max_episodes} episodes)")
        
        print(f"Loaded {len(feeds)} podcasts from CSV")
    else:
        print("CSV not found, using fallback feeds")
        feeds = {
            "Acquired": {"url": "https://feeds.transistor.fm/acquired", "max_episodes": 1000},
            "99% Invisible": {"url": "https://feeds.simplecast.com/BqbsxVfO", "max_episodes": 10},
            "This American Life": {"url": "https://www.thisamericanlife.org/podcast/rss.xml", "max_episodes": 100},
            "Radiolab": {"url": "https://feeds.simplecast.com/EmVW7VGp", "max_episodes": 100},
            "ATP": {"url": "https://cdn.atp.fm/rss/public?wtvryzdm", "max_episodes": 10}
        }
    
    return feeds

feeds = load_all_feeds()

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
        for name, feed_info in feeds.items():
            url = feed_info['url']
            max_eps = feed_info['max_episodes']
            
            print(f"Importing {name} (max: {max_eps})...")
            try:
                feed = feedparser.parse(url)
                
                if not feed.entries:
                    print(f"  No entries found for {name}")
                    continue
                
                imported = 0
                for entry in feed.entries[:max_eps]:
                    audio_url = None
                    if hasattr(entry, 'enclosures'):
                        for enc in entry.enclosures:
                            if hasattr(enc, 'type') and 'audio' in enc.type:
                                audio_url = enc.href
                                break
                    
                    if audio_url:
                        try:
                            conn.execute("""
                                INSERT OR IGNORE INTO podcast_episodes 
                                (title, audio_url, podcast_name) 
                                VALUES (?, ?, ?)
                            """, (entry.title, audio_url, name))
                            imported += 1
                        except Exception as e:
                            print(f"  Error inserting {entry.title}: {e}")
                
                total += imported
                print(f"  Imported {imported} episodes from {name}")
                
            except Exception as e:
                print(f"  Error importing {name}: {e}")
                continue
        
        conn.commit()
        print(f"Imported {total} episodes")

if __name__ == "__main__":
    import_episodes()