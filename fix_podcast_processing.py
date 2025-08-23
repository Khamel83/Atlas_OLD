#!/usr/bin/env python3
"""Direct podcast processing using existing helpers"""

import sys
import json
import subprocess
from pathlib import Path

def process_priority_podcasts():
    """Process the highest priority podcasts directly"""
    
    # Your top priority podcasts with RSS URLs from the config
    priority_podcasts = [
        {
            "name": "Acquired", 
            "rss": "https://feeds.transistor.fm/acquired",
            "episodes": 100,  # Start with 100, not 1000
            "transcript_only": False
        },
        {
            "name": "Accidental Tech Podcast",
            "rss": "https://cdn.atp.fm/rss/public?wtvryzdm", 
            "episodes": 10,
            "transcript_only": False
        },
        {
            "name": "Conversations with Tyler",
            "rss": "https://cowenconvos.libsyn.com/rss",
            "episodes": 20,  # Start smaller
            "transcript_only": True
        },
        {
            "name": "Planet Money",
            "rss": "https://feeds.npr.org/510289/podcast.xml",
            "episodes": 20,
            "transcript_only": True
        },
        {
            "name": "Hard Fork", 
            "rss": "https://feeds.simplecast.com/l2i9YnTd",
            "episodes": 20,
            "transcript_only": True
        }
    ]
    
    print("🚀 PROCESSING PRIORITY PODCASTS")
    print("=" * 50)
    
    for podcast in priority_podcasts:
        print(f"\n🎙️  {podcast['name']}")
        print(f"   Episodes: {podcast['episodes']}")
        print(f"   Transcript only: {podcast['transcript_only']}")
        print(f"   RSS: {podcast['rss'][:50]}...")
        
        # Use the existing podcast transcript ingestor directly
        try:
            cmd = [
                sys.executable, 
                "helpers/podcast_transcript_ingestor.py",
                "--rss", podcast['rss'],
                "--max-episodes", str(podcast['episodes']),
                "--podcast-name", podcast['name']
            ]
            
            if podcast['transcript_only']:
                cmd.append("--transcript-only")
            
            print(f"   🚀 Starting processing...")
            
            result = subprocess.run(cmd, timeout=300, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"   ✅ SUCCESS: Processed {podcast['name']}")
                
                # Check what was actually created
                output_files = list(Path("output/podcasts").glob("*" + podcast['name'].replace(" ", "_").lower() + "*"))
                print(f"   📁 Created {len(output_files)} files")
                
            else:
                print(f"   ❌ ERROR: {result.stderr[:100] if result.stderr else result.stdout[:100]}")
                
        except subprocess.TimeoutExpired:
            print(f"   ⏱️  TIMEOUT: Took too long")
        except Exception as e:
            print(f"   ❌ EXCEPTION: {e}")

def main():
    process_priority_podcasts()

if __name__ == "__main__":
    main()