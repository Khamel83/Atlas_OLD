#!/usr/bin/env python3
"""
Podcast God - Query the exact podcast requirements from PODCAST_GOD.CSV
"""

import csv
import asyncio
from typing import List, Dict, Tuple

def load_podcast_god() -> List[Dict]:
    """Load PODCAST_GOD.CSV and return processed podcast list"""
    podcasts = []

    with open('PODCAST_GOD.CSV', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Exclude'] == '1':
                continue  # Skip excluded podcasts

            count = int(row['Count'])
            if count == 0:
                continue  # Skip podcasts with 0 count

            # Only include podcasts that should be processed
            if row['Future'] == '1':
                podcasts.append({
                    'category': row['Category'],
                    'name': row['Podcast Name'].strip('"'),
                    'count': count,
                    'transcript_only': row['Trasncript_Only'] == '1',
                    'exclude': row['Exclude'] == '1'
                })

    return podcasts

def ask_podcast_god() -> Tuple[int, List[Dict]]:
    """Ask Podcast God what to process"""
    podcasts = load_podcast_god()

    total_episodes = sum(p['count'] for p in podcasts)

    print("🎙️ PODCAST GOD HAS SPOKEN:")
    print(f"📊 Total podcasts to process: {len(podcasts)}")
    print(f"🎧 Total episodes needed: {total_episodes:,}")
    print()

    print("📋 BREAKDOWN BY CATEGORY:")
    categories = {}
    for podcast in podcasts:
        cat = podcast['category']
        if cat not in categories:
            categories[cat] = {'count': 0, 'episodes': 0, 'podcasts': []}
        categories[cat]['count'] += 1
        categories[cat]['episodes'] += podcast['count']
        categories[cat]['podcasts'].append(podcast)

    for cat, data in sorted(categories.items()):
        print(f"📂 {cat}:")
        print(f"   📚 {data['count']} podcasts, {data['episodes']:,} episodes")
        for podcast in sorted(data['podcasts'], key=lambda x: x['count'], reverse=True):
            transcript_note = " (transcripts only)" if podcast['transcript_only'] else ""
            print(f"   - {podcast['name']}: {podcast['count']:,} episodes{transcript_note}")
        print()

    print(f"🎯 TOP 10 PODCASTS BY EPISODE COUNT:")
    top_podcasts = sorted(podcasts, key=lambda x: x['count'], reverse=True)[:10]
    for i, podcast in enumerate(top_podcasts, 1):
        print(f"   {i}. {podcast['name']}: {podcast['count']:,} episodes")

    return total_episodes, podcasts

if __name__ == "__main__":
    ask_podcast_god()