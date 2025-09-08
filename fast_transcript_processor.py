#!/usr/bin/env python3
"""
Fast Transcript Processor
Process ALL available transcripts quickly without artificial delays
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures
import threading
from comprehensive_transcript_finder import ComprehensiveTranscriptFinder

class FastTranscriptProcessor(ComprehensiveTranscriptFinder):
    def __init__(self):
        super().__init__()
        self.results_lock = threading.Lock()
        self.success_count = 0
        self.processed_count = 0
    
    def process_episode(self, episode_data):
        """Process a single episode (thread-safe)"""
        episode_id, podcast_name, title, audio_url = episode_data
        
        transcript = None
        
        # Apply the right strategy based on podcast
        if "Lex Fridman" in podcast_name:
            transcript = self.try_lex_fridman_transcript(title)
        elif "This American Life" in podcast_name:
            transcript = self.try_this_american_life_transcript(title)
        elif "EconTalk" in podcast_name:
            transcript = self.try_econtalk_transcript(title)
        
        with self.results_lock:
            self.processed_count += 1
            
            if transcript:
                # Save to database (need to handle DB connection per thread)
                with sqlite3.connect("data/atlas.db") as conn:
                    conn.execute("""
                        INSERT OR REPLACE INTO content 
                        (title, content, content_type, url, created_at)
                        VALUES (?, ?, 'podcast_transcript', ?, CURRENT_TIMESTAMP)
                    """, (f"[TRANSCRIPT] {title}", transcript, audio_url))
                    
                    # Mark as processed
                    conn.execute("""
                        UPDATE podcast_episodes 
                        SET processed = 1 
                        WHERE id = ?
                    """, (episode_id,))
                    
                    conn.commit()
                
                self.success_count += 1
                print(f"✅ {podcast_name}: {title[:50]}... ({len(transcript)} chars)")
            else:
                # Still mark as processed to avoid reprocessing
                with sqlite3.connect("data/atlas.db") as conn:
                    conn.execute("""
                        UPDATE podcast_episodes 
                        SET processed = 1 
                        WHERE id = ?
                    """, (episode_id,))
                    conn.commit()
                
                print(f"❌ {podcast_name}: {title[:50]}...")
        
        return transcript is not None

def process_all_transcripts_fast():
    """Process ALL unprocessed episodes quickly using threading"""
    
    processor = FastTranscriptProcessor()
    
    # Target podcasts that have working transcript strategies
    target_podcasts = [
        "Lex Fridman Podcast",
        "This American Life", 
        "EconTalk"
    ]
    
    all_episodes = []
    
    with sqlite3.connect("data/atlas.db") as conn:
        for podcast_name in target_podcasts:
            episodes = conn.execute("""
                SELECT id, podcast_name, title, audio_url 
                FROM podcast_episodes 
                WHERE podcast_name LIKE ? AND processed = 0 
                ORDER BY id DESC
            """, (f"%{podcast_name}%",)).fetchall()
            
            all_episodes.extend(episodes)
            print(f"📂 {podcast_name}: {len(episodes)} unprocessed episodes")
    
    if not all_episodes:
        print("✅ No unprocessed episodes found!")
        return 0
    
    print(f"\n🚀 Processing {len(all_episodes)} episodes using parallel processing...")
    
    # Process episodes in parallel (but not too many at once to be respectful)
    max_workers = min(10, len(all_episodes))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(processor.process_episode, episode) for episode in all_episodes]
        
        # Wait for all to complete
        concurrent.futures.wait(futures)
    
    print(f"\n🎉 COMPLETE! Processed {processor.processed_count} episodes")
    print(f"   ✅ Found {processor.success_count} transcripts")
    print(f"   ❌ No transcript: {processor.processed_count - processor.success_count}")
    
    return processor.success_count

def main():
    print("⚡ Fast transcript processing - NO artificial delays!")
    
    start_time = time.time()
    count = process_all_transcripts_fast()
    end_time = time.time()
    
    print(f"\n📊 RESULTS:")
    print(f"   New transcripts: {count}")
    print(f"   Processing time: {end_time - start_time:.1f} seconds")
    
    if count > 0:
        # Show final stats
        with sqlite3.connect("data/atlas.db") as conn:
            total_transcripts = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'podcast_transcript'").fetchone()[0]
            total_words = conn.execute("SELECT SUM(LENGTH(content) / 5) FROM content WHERE content_type = 'podcast_transcript'").fetchone()[0] or 0
            
        print(f"   Total transcripts in database: {total_transcripts}")
        print(f"   Total words: {int(total_words):,}")
        print(f"   Search at: http://localhost:8000/api/v1/transcripts/discovery")

if __name__ == "__main__":
    import time
    main()