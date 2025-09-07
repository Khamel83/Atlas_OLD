#!/usr/bin/env python3
import sqlite3
import time
import sys

def process_episodes():
    """Simple processing - just mark episodes as processed"""
    with sqlite3.connect("data/atlas.db") as conn:
        # Get unprocessed episodes
        episodes = conn.execute("""
            SELECT id, title, podcast_name 
            FROM podcast_episodes 
            WHERE processed = 0 
            LIMIT 5
        """).fetchall()
        
        if not episodes:
            print("No episodes to process")
            return False
        
        for episode_id, title, podcast in episodes:
            print(f"Processing: {title[:50]}...")
            
            # Simulate processing - add to main content table
            conn.execute("""
                INSERT OR REPLACE INTO content 
                (title, content, content_type, created_at)
                VALUES (?, ?, 'podcast_episode', CURRENT_TIMESTAMP)
            """, (f"[PODCAST] {title}", f"Transcript for {title} from {podcast}"))
            
            # Mark as processed
            conn.execute("""
                UPDATE podcast_episodes 
                SET processed = 1 
                WHERE id = ?
            """, (episode_id,))
        
        conn.commit()
        print(f"Processed {len(episodes)} episodes")
        return True

def run_continuous():
    """Run processor every 30 seconds"""
    print("Starting simple continuous processor...")
    
    try:
        while True:
            if process_episodes():
                print("Work done, sleeping 30 seconds...")
            else:
                print("No work, sleeping 30 seconds...")
            
            time.sleep(30)
    except KeyboardInterrupt:
        print("Stopping processor")

if __name__ == "__main__":
    if "--continuous" in sys.argv:
        run_continuous()
    else:
        process_episodes()