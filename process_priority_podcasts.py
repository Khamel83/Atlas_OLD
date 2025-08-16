#!/usr/bin/env python3
"""
Process priority podcasts from configuration CSV
"""

import csv
import sys
import os
from datetime import datetime

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from helpers.podcast_ingestor import PodcastIngestor
from helpers.config import load_config
from helpers.utils import log_info

def load_podcast_config(csv_path):
    """Load podcast configuration from CSV"""
    podcasts = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row['Exclude']) == 0 and int(row['Count']) > 0:
                podcasts.append({
                    'name': row['Podcast Name'],
                    'category': row['Category'],
                    'count': int(row['Count']),
                    'transcript_only': int(row['Transcript_Only']) == 1,
                    'future': int(row['Future']) == 1
                })
    return podcasts

def get_podcast_feeds():
    """Map podcast names to RSS feed URLs"""
    # High-priority feeds with known URLs
    feeds = {
        'Conversations with Tyler': 'https://feeds.soundcloud.com/users/soundcloud:users:264034133/sounds.rss',
        'Acquired': 'https://feeds.megaphone.fm/acquired',
        'ACQ2 by Acquired': 'https://feeds.megaphone.fm/acq2',
        'Hard Fork': 'https://feeds.simplecast.com/KqTCbOXZ',
        'The Ezra Klein Show': 'https://feeds.simplecast.com/82FI35Px',
        'Planet Money': 'https://feeds.npr.org/510289/podcast.xml',
        'Radiolab': 'https://feeds.wnyc.org/radiolab',
        'Sharp Tech with Ben Thompson': 'https://feeds.stratechery.com/sharp-tech',
        'Stratechery': 'https://feeds.stratechery.com/stratechery',
        'The Knowledge Project with Shane Parrish': 'https://feeds.simplecast.com/4T39_jAj',
        'The Rewatchables': 'https://feeds.megaphone.fm/the-rewatchables',
        'EconTalk': 'https://files.libertyfund.org/econtalk/EconTalk.xml',
        'Dithering': 'https://dithering.fm/rss',
        'The Recipe with Kenji and Deb': 'https://feeds.simplecast.com/Dt6cjbql',
        'Against the Rules with Michael Lewis': 'https://feeds.megaphone.fm/against-the-rules',
        'Asianometry': 'https://feeds.buzzsprout.com/1513303.rss',
        'Dwarkesh Podcast': 'https://feeds.transistor.fm/the-lunar-society',
        'Land of the Giants': 'https://feeds.megaphone.fm/land-of-the-giants',
        'Revisionist History': 'https://feeds.megaphone.fm/revisionist-history',
        'The Trojan Horse Affair': 'https://feeds.simplecast.com/8PyWLWQW'
    }
    return feeds

def main():
    print("🎧 Processing Priority Podcasts")
    print("=" * 40)
    
    # Load configuration
    config = load_config()
    
    # Load podcast priorities
    podcast_config = load_podcast_config('/home/ubuntu/dev/atlas/podcast_config.csv')
    feed_urls = get_podcast_feeds()
    
    # Filter for high-priority podcasts with known feeds
    priority_podcasts = [p for p in podcast_config if p['name'] in feed_urls and p['count'] >= 100]
    priority_podcasts.sort(key=lambda x: x['count'], reverse=True)
    
    print(f"📊 Found {len(priority_podcasts)} high-priority podcasts")
    print()
    
    for i, podcast in enumerate(priority_podcasts[:5], 1):  # Process top 5
        print(f"[{i}/5] Processing: {podcast['name']}")
        print(f"   Category: {podcast['category']}")
        print(f"   Target episodes: {podcast['count']}")
        print(f"   Transcript only: {podcast['transcript_only']}")
        
        feed_url = feed_urls[podcast['name']]
        print(f"   Feed: {feed_url}")
        
        try:
            # Initialize ingestor
            ingestor = PodcastIngestor(config)
            
            # Process the feed
            success = ingestor.process_feed(feed_url)
            
            if success:
                print(f"   ✅ SUCCESS")
            else:
                print(f"   ❌ FAILED")
                
        except Exception as e:
            print(f"   ❌ ERROR: {e}")
        
        print()
    
    print("🎯 Podcast processing complete!")
    print(f"💡 Next: Check output/ directory for processed episodes")

if __name__ == "__main__":
    main()