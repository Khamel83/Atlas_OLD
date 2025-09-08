#!/usr/bin/env python3
"""
Bulk Transcript Processor
Process ALL backlogged episodes immediately - thousands of them
"""

import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import concurrent.futures
import threading
import time

class BulkTranscriptProcessor:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        self.results_lock = threading.Lock()
        self.success_count = 0
        self.processed_count = 0
        
    def try_lex_fridman_transcript(self, title):
        """Lex Fridman transcript extraction"""
        guest_match = re.search(r'#\d+\s*[-–]\s*([^:]+)', title)
        if not guest_match:
            return None
            
        guest_name = guest_match.group(1).strip()
        slug = guest_name.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[-\s]+', '-', slug)
        slug = slug.strip('-')
        
        transcript_url = f"https://lexfridman.com/{slug}-transcript"
        
        try:
            response = self.session.get(transcript_url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                content_areas = soup.find_all(['div', 'article', 'main'])
                for area in content_areas:
                    text = area.get_text(separator=' ', strip=True)
                    if len(text) > 5000 and 'transcript' in text.lower():
                        return text
        except:
            pass
        return None
    
    def try_this_american_life_transcript(self, title):
        """This American Life transcript extraction"""
        episode_match = re.search(r'(\d+):', title)
        if episode_match:
            episode_num = episode_match.group(1)
            url = f"https://www.thisamericanlife.org/{episode_num}/transcript"
            
            try:
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    content_element = soup.select_one('.content')
                    if content_element:
                        text = content_element.get_text(separator=' ', strip=True)
                        if len(text) > 1000:
                            return text
            except:
                pass
        return None
    
    def process_episode_batch(self, episodes):
        """Process a batch of episodes"""
        batch_success = 0
        
        for episode_id, podcast_name, title, audio_url in episodes:
            transcript = None
            
            # Apply strategy based on podcast
            if "Lex Fridman" in podcast_name:
                transcript = self.try_lex_fridman_transcript(title)
            elif "This American Life" in podcast_name:
                transcript = self.try_this_american_life_transcript(title)
            
            # Save result
            with sqlite3.connect("data/atlas.db") as conn:
                if transcript:
                    conn.execute("""
                        INSERT OR REPLACE INTO content 
                        (title, content, content_type, url, created_at)
                        VALUES (?, ?, 'podcast_transcript', ?, CURRENT_TIMESTAMP)
                    """, (f"[TRANSCRIPT] {title}", transcript, audio_url))
                    batch_success += 1
                
                # Mark as processed
                conn.execute("UPDATE podcast_episodes SET processed = 1 WHERE id = ?", (episode_id,))
                conn.commit()
        
        with self.results_lock:
            self.success_count += batch_success
            self.processed_count += len(episodes)
        
        return batch_success

def process_all_backlogs():
    """Process ALL unprocessed episodes from transcript-enabled podcasts"""
    
    processor = BulkTranscriptProcessor()
    
    # Get ALL unprocessed episodes for transcript-enabled podcasts
    with sqlite3.connect("data/atlas.db") as conn:
        all_episodes = conn.execute("""
            SELECT id, podcast_name, title, audio_url 
            FROM podcast_episodes 
            WHERE processed = 0 
            AND (
                podcast_name LIKE '%Lex Fridman%' OR
                podcast_name LIKE '%This American Life%' OR
                podcast_name LIKE '%EconTalk%'
            )
            ORDER BY id DESC
        """).fetchall()
    
    print(f"🚀 Processing {len(all_episodes)} episodes from backlog...")
    
    if not all_episodes:
        print("✅ No episodes to process!")
        return 0
    
    # Split into batches for parallel processing
    batch_size = 20
    batches = [all_episodes[i:i + batch_size] for i in range(0, len(all_episodes), batch_size)]
    
    start_time = time.time()
    
    # Process batches in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(processor.process_episode_batch, batch) for batch in batches]
        
        # Show progress
        completed = 0
        for future in concurrent.futures.as_completed(futures):
            completed += 1
            print(f"📊 Progress: {completed}/{len(batches)} batches complete")
    
    end_time = time.time()
    
    print(f"\n🎉 BULK PROCESSING COMPLETE!")
    print(f"   Processed: {processor.processed_count} episodes")
    print(f"   Found transcripts: {processor.success_count}")
    print(f"   Time: {end_time - start_time:.1f} seconds")
    print(f"   Rate: {processor.processed_count / (end_time - start_time):.1f} episodes/second")
    
    return processor.success_count

def main():
    print("⚡ BULK TRANSCRIPT PROCESSING - Processing entire backlog NOW")
    
    count = process_all_backlogs()
    
    if count > 0:
        # Show final database stats
        with sqlite3.connect("data/atlas.db") as conn:
            total_transcripts = conn.execute("SELECT COUNT(*) FROM content WHERE content_type = 'podcast_transcript'").fetchone()[0]
            
        print(f"\n📈 FINAL RESULTS:")
        print(f"   Total transcripts in database: {total_transcripts}")
        print(f"   New transcripts added: {count}")
        print(f"   Search at: http://localhost:8000/api/v1/transcripts/discovery")
    
    print(f"\n✅ Backlog processing complete. System ready for daily incremental processing.")

if __name__ == "__main__":
    main()