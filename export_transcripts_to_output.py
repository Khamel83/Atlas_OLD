#!/usr/bin/env python3
"""Export discovered transcripts to output directory following user rules"""

import sqlite3
import json
import csv
from pathlib import Path
from datetime import datetime

def export_transcripts_by_rules():
    """Export transcripts to output/ following user preferences"""
    
    # Load user preferences
    prefs_file = Path("config/podcasts_prioritized.csv")
    podcast_rules = {}
    
    if prefs_file.exists():
        with open(prefs_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                podcast_name = row['Podcast Name'].strip('"')
                podcast_rules[podcast_name] = {
                    'count': int(row['Count']),
                    'transcript_only': bool(int(row['Transcript_Only'])),
                    'exclude': bool(int(row['Exclude']))
                }
    
    # Connect to podcast database
    db_path = Path("data/podcasts/atlas_podcasts.db")
    if not db_path.exists():
        print("❌ No podcast database found")
        return
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Get podcasts with transcript sources
    query = """
    SELECT DISTINCT p.name, p.rss_url,
           COUNT(DISTINCT e.id) as total_episodes,
           COUNT(DISTINCT ts.id) as episodes_with_transcripts
    FROM podcasts p 
    JOIN episodes e ON p.id = e.podcast_id 
    LEFT JOIN transcript_sources ts ON e.id = ts.episode_id
    GROUP BY p.id, p.name
    HAVING episodes_with_transcripts > 0
    ORDER BY episodes_with_transcripts DESC
    """
    
    results = cursor.execute(query).fetchall()
    
    print("📻 PODCASTS WITH AVAILABLE TRANSCRIPTS")
    print("=" * 60)
    
    output_dir = Path("output/podcasts")
    output_dir.mkdir(exist_ok=True)
    
    exported = 0
    
    for podcast_name, rss_url, total_episodes, transcript_episodes in results:
        
        print(f"\n🎙️  {podcast_name}")
        print(f"   Total episodes: {total_episodes}")
        print(f"   Episodes with transcripts: {transcript_episodes}")
        
        # Check user rules
        rules = None
        for rule_name, rule_data in podcast_rules.items():
            if rule_name.lower() in podcast_name.lower() or podcast_name.lower() in rule_name.lower():
                rules = rule_data
                break
        
        if rules:
            print(f"   User rules: {rules['count']} episodes, transcript_only: {rules['transcript_only']}")
            if rules['exclude']:
                print(f"   ❌ SKIPPED: User marked as excluded")
                continue
            
            max_episodes = min(rules['count'], transcript_episodes) if rules['count'] > 0 else transcript_episodes
        else:
            print(f"   ⚠️  No user rules found, using default (5 episodes)")
            max_episodes = min(5, transcript_episodes)
        
        # Get episodes with transcripts for this podcast
        episode_query = """
        SELECT e.title, e.url, e.publish_date, ts.url as transcript_url, ts.confidence
        FROM podcasts p 
        JOIN episodes e ON p.id = e.podcast_id 
        JOIN transcript_sources ts ON e.id = ts.episode_id
        WHERE p.name = ?
        ORDER BY e.publish_date DESC
        LIMIT ?
        """
        
        episodes = cursor.execute(episode_query, (podcast_name, max_episodes)).fetchall()
        
        print(f"   📄 Exporting {len(episodes)} episodes with transcripts")
        
        for i, (title, episode_url, publish_date, transcript_url, confidence) in enumerate(episodes):
            
            # Create output file
            safe_name = podcast_name.replace(" ", "_").replace("/", "_").lower()
            filename = f"{safe_name}_episode_{i+1:03d}.json"
            output_file = output_dir / filename
            
            episode_data = {
                "uid": f"podcast_{hash(episode_url) % 1000000:06d}",
                "podcast_name": podcast_name,
                "title": title,
                "episode_url": episode_url,
                "transcript_url": transcript_url,
                "transcript_confidence": confidence,
                "publish_date": publish_date,
                "status": "transcript_available",
                "transcript_text": "",  # Will be populated by fetching
                "created_at": datetime.now().isoformat(),
                "content_type": "podcast"
            }
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(episode_data, f, indent=2)
            
            exported += 1
    
    conn.close()
    
    print(f"\n✅ EXPORT COMPLETE")
    print(f"   Total episodes exported: {exported}")
    print(f"   Files created in: {output_dir}")
    
    return exported > 0

if __name__ == "__main__":
    export_transcripts_by_rules()