#!/usr/bin/env python3
"""
Targeted Transcript Finder
Focus on specific podcasts that we know have transcripts
"""

import sqlite3
from comprehensive_transcript_finder import ComprehensiveTranscriptFinder

def process_specific_podcasts():
    """Process specific podcasts that we know have transcripts"""
    
    finder = ComprehensiveTranscriptFinder()
    
    # Target podcasts with working strategies
    target_podcasts = [
        "Lex Fridman Podcast",
        "This American Life", 
        "EconTalk"
    ]
    
    total_found = 0
    
    with sqlite3.connect("data/atlas.db") as conn:
        for podcast_name in target_podcasts:
            print(f"\n🎯 Processing {podcast_name}...")
            
            # Get unprocessed episodes for this specific podcast
            episodes = conn.execute("""
                SELECT id, podcast_name, title, audio_url 
                FROM podcast_episodes 
                WHERE podcast_name LIKE ? AND processed = 0 
                ORDER BY id DESC
                LIMIT 5
            """, (f"%{podcast_name}%",)).fetchall()
            
            print(f"Found {len(episodes)} unprocessed {podcast_name} episodes")
            
            success_count = 0
            
            for episode_id, full_podcast_name, title, audio_url in episodes:
                print(f"\nProcessing: {title[:60]}...")
                
                transcript = None
                
                # Apply the right strategy
                if "Lex Fridman" in full_podcast_name:
                    transcript = finder.try_lex_fridman_transcript(title)
                elif "This American Life" in full_podcast_name:
                    transcript = finder.try_this_american_life_transcript(title)
                elif "EconTalk" in full_podcast_name:
                    transcript = finder.try_econtalk_transcript(title)
                
                if transcript:
                    # Save transcript to database
                    conn.execute("""
                        INSERT OR REPLACE INTO content 
                        (title, content, content_type, url, created_at)
                        VALUES (?, ?, 'podcast_transcript', ?, CURRENT_TIMESTAMP)
                    """, (f"[TRANSCRIPT] {title}", transcript, audio_url))
                    
                    success_count += 1
                    total_found += 1
                    print(f"    ✅ Found transcript: {len(transcript)} characters")
                else:
                    print("    ❌ No transcript found")
                
                # Mark episode as processed
                conn.execute("""
                    UPDATE podcast_episodes 
                    SET processed = 1 
                    WHERE id = ?
                """, (episode_id,))
            
            conn.commit()
            print(f"{podcast_name} results: {success_count}/{len(episodes)} transcripts found")
    
    return total_found

def main():
    print("🚀 Targeted transcript processing for podcasts with known transcript sources...")
    
    total = process_specific_podcasts()
    
    if total > 0:
        print(f"\n🎉 SUCCESS! Found {total} new transcripts today")
        print("   Check them at: http://localhost:8000/api/v1/transcripts/discovery")
        
        # Show updated stats
        with sqlite3.connect("data/atlas.db") as conn:
            count = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'podcast_transcript'").fetchone()[0]
            print(f"   Total transcripts in database: {count}")
    else:
        print(f"\n⚠️  No new transcripts found")
        print("   Either all episodes are processed or transcript sources have changed")

if __name__ == "__main__":
    main()