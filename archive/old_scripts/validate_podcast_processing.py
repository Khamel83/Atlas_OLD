#!/usr/bin/env python3
"""
Validate Podcast Transcript Processing
"""

import sqlite3
import json
from collections import Counter

def validate_podcast_processing():
    """Check what we've accomplished with podcast transcripts"""
    
    print("🔍 PODCAST TRANSCRIPT PROCESSING VALIDATION")
    print("=" * 50)
    
    # Connect to database
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    
    # Get transcript count
    cursor.execute("SELECT COUNT(*) FROM content WHERE title LIKE '%TRANSCRIPT%'")
    total_transcripts = cursor.fetchone()[0]
    
    # Get sample transcripts
    cursor.execute("""
        SELECT title, LENGTH(content) as content_length, url 
        FROM content 
        WHERE title LIKE '%TRANSCRIPT%' 
        ORDER BY created_at DESC 
        LIMIT 20
    """)
    recent_transcripts = cursor.fetchall()
    
    print(f"📊 Total transcripts in database: {total_transcripts}")
    print(f"📈 Recent transcript samples:")
    
    for i, (title, length, url) in enumerate(recent_transcripts, 1):
        podcast_name = title.replace('[TRANSCRIPT] ', '')[:40]
        print(f"  {i:2}. {podcast_name:<40} ({length:,} chars)")
    
    # Check podcast sources
    cursor.execute("""
        SELECT content, COUNT(*) as count
        FROM content 
        WHERE title LIKE '%TRANSCRIPT%' 
        GROUP BY SUBSTR(content, 1, INSTR(content, '\n') - 1)
        ORDER BY count DESC
    """)
    
    podcast_sources = cursor.fetchall()
    print(f"\n📻 Unique podcast sources found: {len(podcast_sources)}")
    
    for source, count in podcast_sources[:10]:
        podcast_line = source.split('\n')[0] if '\n' in source else source
        podcast_name = podcast_line.replace('Podcast: ', '')[:35]
        print(f"  • {podcast_name:<35} ({count} episodes)")
    
    # Load original analysis to compare
    try:
        with open('podcast_transcript_analysis.json') as f:
            analysis = json.load(f)
        
        total_podcasts = len(analysis['podcasts'])
        processed_count = len(podcast_sources)
        
        print(f"\n📈 COVERAGE ANALYSIS:")
        print(f"  🎙️ Total podcasts subscribed: {total_podcasts}")
        print(f"  ✅ Podcasts with transcripts found: {processed_count}")
        print(f"  📊 Coverage rate: {(processed_count/total_podcasts)*100:.1f}%")
        
        if processed_count >= 30:
            print("  🎉 SUCCESS: Strong transcript collection!")
        elif processed_count >= 15:
            print("  ✅ GOOD: Decent transcript coverage")
        else:
            print("  ⚠️  PARTIAL: More work needed")
            
    except Exception as e:
        print(f"  ❌ Could not load original analysis: {e}")
    
    conn.close()
    return total_transcripts

if __name__ == "__main__":
    validate_podcast_processing()