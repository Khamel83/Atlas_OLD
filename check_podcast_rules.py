#!/usr/bin/env python3
"""Check if Atlas is following user's specific podcast preferences"""

import csv
import json
from pathlib import Path

def check_podcast_preferences():
    """Check if podcast processing follows user rules"""
    
    # Load user preferences
    prefs_file = Path("config/podcasts_prioritized.csv")
    if not prefs_file.exists():
        print("❌ No podcast preferences file found")
        return
    
    podcast_rules = {}
    with open(prefs_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            podcast_name = row['Podcast Name']
            podcast_rules[podcast_name] = {
                'count': int(row['Count']),
                'future': bool(int(row['Future'])),
                'transcript_only': bool(int(row['Transcript_Only'])),
                'exclude': bool(int(row['Exclude'])),
                'category': row['Category']
            }
    
    print("📋 USER PODCAST PREFERENCES vs ATLAS PROCESSING")
    print("=" * 70)
    
    # Check what's actually been processed
    podcast_output = Path("output/podcasts")
    processed_podcasts = {}
    
    if podcast_output.exists():
        for json_file in podcast_output.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                podcast_title = data.get('podcast_title', 'Unknown')
                
                if podcast_title not in processed_podcasts:
                    processed_podcasts[podcast_title] = []
                processed_podcasts[podcast_title].append(data)
            except Exception:
                continue
    
    # Compare preferences vs reality
    for podcast_name, rules in podcast_rules.items():
        print(f"\n🎙️  {podcast_name}")
        print(f"   Category: {rules['category']}")
        print(f"   Target episodes: {rules['count']}")
        print(f"   Transcript only: {rules['transcript_only']}")
        print(f"   Future episodes: {rules['future']}")
        print(f"   Excluded: {rules['exclude']}")
        
        # Check actual processing
        episodes_found = 0
        transcripts_found = 0
        
        # Look for matching processed episodes
        for proc_name, episodes in processed_podcasts.items():
            if podcast_name.lower() in proc_name.lower() or proc_name.lower() in podcast_name.lower():
                episodes_found = len(episodes)
                for ep in episodes:
                    if ep.get('transcript_text') or ep.get('transcript_path'):
                        transcripts_found += 1
                break
        
        print(f"   ✅ Episodes processed: {episodes_found}")
        print(f"   ✅ Transcripts found: {transcripts_found}")
        
        # Check compliance
        if rules['exclude']:
            if episodes_found > 0:
                print(f"   ⚠️  WARNING: {episodes_found} episodes found but podcast marked as EXCLUDED")
            else:
                print(f"   ✅ CORRECT: Properly excluded")
        else:
            if rules['transcript_only'] and transcripts_found < episodes_found:
                print(f"   ⚠️  WARNING: Transcript-only rule not followed")
            
            if rules['count'] > 0 and episodes_found < min(10, rules['count']):
                print(f"   ⚠️  WARNING: Expected {rules['count']} episodes, found {episodes_found}")
            elif episodes_found > 0:
                print(f"   ✅ PROCESSING: Episodes being processed")
    
    # Show high priority podcasts that should have lots of content
    print(f"\n🔥 HIGH PRIORITY PODCASTS (should have most content):")
    high_priority = [(name, rules) for name, rules in podcast_rules.items() 
                    if rules['count'] >= 100 and not rules['exclude']]
    
    for podcast_name, rules in high_priority:
        episodes_count = 0
        for proc_name, episodes in processed_podcasts.items():
            if podcast_name.lower() in proc_name.lower():
                episodes_count = len(episodes)
                break
        print(f"   {podcast_name}: {episodes_count} episodes (target: {rules['count']})")
    
    # ATP special check (should have enhanced transcripts)
    print(f"\n🎯 SPECIAL CASES:")
    atp_found = any("atp" in name.lower() or "accidental tech" in name.lower() 
                   for name in processed_podcasts.keys())
    print(f"   ATP (Accidental Tech): {'✅ Found' if atp_found else '❌ Missing'}")
    
    if atp_found:
        print("   (Should have enhanced transcripts from catatp.fm)")
    
    print(f"\n📊 SUMMARY:")
    total_rules = len(podcast_rules)
    excluded_rules = len([r for r in podcast_rules.values() if r['exclude']])
    active_rules = total_rules - excluded_rules
    processed_count = len(processed_podcasts)
    
    print(f"   Total podcast rules: {total_rules}")
    print(f"   Active rules (not excluded): {active_rules}")  
    print(f"   Actually processed: {processed_count}")
    print(f"   Compliance rate: {(processed_count/max(1,active_rules))*100:.1f}%")

if __name__ == "__main__":
    check_podcast_preferences()