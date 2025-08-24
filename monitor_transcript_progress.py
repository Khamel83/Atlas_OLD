#!/usr/bin/env python3
"""
Simple transcript progress monitor
Shows you exactly what transcript discovery is doing
"""

import json
from pathlib import Path
from datetime import datetime

def show_transcript_progress():
    print("🎯 ATLAS TRANSCRIPT DISCOVERY STATUS")
    print("=" * 50)
    
    # Check TranscriptManager state
    try:
        processed_file = Path("output/processed_transcripts.json")
        if processed_file.exists():
            with open(processed_file) as f:
                data = json.load(f)
                
            print(f"📊 Processed URLs: {data.get('total_processed', 0)}")
            print(f"📅 Last updated: {data.get('last_updated', 'Never')}")
        else:
            print("📊 No processed transcripts file found")
    except Exception as e:
        print(f"❌ Error reading processed state: {e}")
    
    # Check actual transcript files
    transcripts_dir = Path("output/transcripts")
    if transcripts_dir.exists():
        transcript_files = list(transcripts_dir.glob("*.json"))
        print(f"📄 Transcript files stored: {len(transcript_files)}")
        
        if transcript_files:
            print("\n📋 Recent transcripts:")
            for file in sorted(transcript_files, key=lambda x: x.stat().st_mtime, reverse=True)[:5]:
                try:
                    with open(file) as f:
                        data = json.load(f)
                    title = data.get('title', 'Unknown')[:50]
                    source = data.get('source', 'unknown')
                    print(f"   • {title}... ({source})")
                except:
                    print(f"   • {file.name} (corrupted)")
    else:
        print("📄 No transcripts directory found")
    
    # Check podcast episodes available for processing
    podcasts_dir = Path("output/podcasts")
    if podcasts_dir.exists():
        podcast_files = list(podcasts_dir.glob("*_rss_entry.json"))
        print(f"🎙️  Podcast episodes available: {len(podcast_files)}")
        
        # Count by potential transcript sources
        atp_episodes = sum(1 for f in podcast_files if "atp" in f.read_text().lower())
        print(f"   • ATP episodes: ~{atp_episodes}")
    else:
        print("🎙️  No podcast episodes directory found")
    
    print("\n🎯 TO RUN TRANSCRIPT DISCOVERY:")
    print("   python3 -c \"from helpers.transcript_manager import TranscriptManager; tm = TranscriptManager(); transcripts = tm.discover_transcripts('auto', limit=10); [tm.fetch_transcript(t) for t in transcripts]\"")

if __name__ == "__main__":
    show_transcript_progress()