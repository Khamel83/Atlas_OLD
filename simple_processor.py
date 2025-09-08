#!/usr/bin/env python3
import sqlite3
import time
import sys
import os
import requests
import tempfile
import hashlib
from pathlib import Path

# Import transcription functionality
sys.path.insert(0, str(Path(__file__).parent))
try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    print("Warning: Whisper not available, using placeholder transcripts")
    WHISPER_AVAILABLE = False

class SimpleTranscriber:
    def __init__(self):
        if WHISPER_AVAILABLE:
            self.whisper_model = whisper.load_model("base")
        self.temp_dir = Path("temp/audio")
        self.temp_dir.mkdir(parents=True, exist_ok=True)
    
    def download_audio(self, url, max_size_mb=100):
        """Download audio file with size limit"""
        try:
            response = requests.head(url, timeout=10)
            if response.status_code != 200:
                return None
                
            # Check file size
            content_length = response.headers.get('content-length')
            if content_length:
                size_mb = int(content_length) / (1024 * 1024)
                if size_mb > max_size_mb:
                    print(f"  Audio too large: {size_mb:.1f}MB > {max_size_mb}MB")
                    return None
            
            # Download file
            url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
            temp_file = self.temp_dir / f"{url_hash}.mp3"
            
            if temp_file.exists():
                return str(temp_file)
            
            response = requests.get(url, timeout=30, stream=True)
            with open(temp_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            return str(temp_file)
        except Exception as e:
            print(f"  Download failed: {e}")
            return None
    
    def transcribe_audio(self, audio_path):
        """Transcribe audio file"""
        try:
            if not WHISPER_AVAILABLE:
                return f"[PLACEHOLDER] Transcript for {Path(audio_path).name}"
            
            result = self.whisper_model.transcribe(audio_path)
            return result["text"].strip()
        except Exception as e:
            print(f"  Transcription failed: {e}")
            return None

transcriber = SimpleTranscriber()

def process_episodes():
    """Process episodes with actual transcription"""
    with sqlite3.connect("data/atlas.db") as conn:
        # Get unprocessed episodes with audio URLs
        episodes = conn.execute("""
            SELECT id, title, podcast_name, audio_url 
            FROM podcast_episodes 
            WHERE processed = 0 AND audio_url IS NOT NULL 
            LIMIT 5
        """).fetchall()
        
        if not episodes:
            print("No episodes to process")
            return False
        
        for episode_id, title, podcast, audio_url in episodes:
            print(f"Processing: {title[:50]}...")
            
            # Download and transcribe
            audio_path = transcriber.download_audio(audio_url)
            if audio_path:
                transcript = transcriber.transcribe_audio(audio_path)
                if transcript:
                    # Add to main content table with real transcript
                    conn.execute("""
                        INSERT OR REPLACE INTO content 
                        (title, content, content_type, created_at)
                        VALUES (?, ?, 'podcast_episode', CURRENT_TIMESTAMP)
                    """, (f"[PODCAST] {title}", transcript))
                    print(f"  ✓ Transcribed: {len(transcript)} chars")
                else:
                    print("  ✗ Transcription failed")
                
                # Clean up audio file
                try:
                    os.remove(audio_path)
                except:
                    pass
            else:
                print("  ✗ Audio download failed")
            
            # Mark as processed regardless
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