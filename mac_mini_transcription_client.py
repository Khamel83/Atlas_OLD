#!/usr/bin/env python3
"""
Atlas-Controlled Mac Mini Worker Client
Polls Atlas for transcription jobs, executes them, reports results back
"""

import os
import time
import json
import subprocess
import requests
from pathlib import Path
import tempfile
import urllib.request

class AtlasWorkerClient:
    def __init__(self, atlas_url, api_key=None):
        self.atlas_url = atlas_url.rstrip('/')
        self.api_key = api_key
        self.processed_dir = Path.home() / "transcription_queue" / "processed"
        self.failed_dir = Path.home() / "transcription_queue" / "failed"
        
        # Create directories
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        self.failed_dir.mkdir(parents=True, exist_ok=True)
    
    def on_created(self, event):
        if event.is_directory:
            return
            
        file_path = Path(event.src_path)
        if file_path.suffix.lower() in ['.mp3', '.wav', '.m4a', '.mp4']:
            print(f"📁 New audio file detected: {file_path.name}")
            time.sleep(2)  # Wait for file to be fully written
            self.process_audio_file(file_path)
    
    def process_audio_file(self, audio_path):
        """Transcribe audio and send to Atlas"""
        try:
            print(f"🎙️ Transcribing: {audio_path.name}")
            transcript = self.transcribe_with_whisper(audio_path)
            
            if transcript:
                print(f"✅ Transcription complete ({len(transcript)} chars)")
                self.send_to_atlas(audio_path.name, transcript)
                
                # Move to processed
                processed_path = self.processed_dir / audio_path.name
                audio_path.rename(processed_path)
                print(f"📦 Moved to processed: {processed_path}")
            else:
                raise Exception("Empty transcript")
                
        except Exception as e:
            print(f"❌ Failed to process {audio_path.name}: {e}")
            # Move to failed
            failed_path = self.failed_dir / audio_path.name
            audio_path.rename(failed_path)
    
    def transcribe_with_whisper(self, audio_path):
        """Use local whisper.cpp for transcription"""
        try:
            result = subprocess.run([
                'whisper',
                str(audio_path),
                '--language', 'en',
                '--model', 'base',
                '--output_format', 'txt',
                '--output_dir', '/tmp'
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode != 0:
                raise Exception(f"Whisper failed: {result.stderr}")
            
            # Read transcript file
            transcript_file = Path('/tmp') / f"{audio_path.stem}.txt"
            if transcript_file.exists():
                transcript = transcript_file.read_text().strip()
                transcript_file.unlink()  # Clean up
                return transcript
            else:
                raise Exception("Transcript file not found")
                
        except subprocess.TimeoutExpired:
            raise Exception("Transcription timed out (5min)")
        except Exception as e:
            raise Exception(f"Whisper error: {e}")
    
    def send_to_atlas(self, filename, transcript):
        """Send transcript to Atlas API"""
        payload = {
            'filename': filename,
            'transcript': transcript,
            'source': 'mac_mini_client',
            'timestamp': time.time()
        }
        
        headers = {'Content-Type': 'application/json'}
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'
        
        try:
            response = requests.post(
                f"{self.atlas_url}/api/v1/transcriptions",
                json=payload,
                headers=headers,
                timeout=30
            )
            
            if response.status_code == 200:
                print(f"🚀 Sent to Atlas successfully")
            else:
                raise Exception(f"Atlas API error: {response.status_code} - {response.text}")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {e}")

def main():
    # Configuration
    ATLAS_URL = os.getenv('ATLAS_URL', 'http://localhost:8000')
    API_KEY = os.getenv('ATLAS_API_KEY')  # Optional
    WATCH_DIR = Path.home() / "transcription_queue" / "incoming"
    
    # Create watch directory
    WATCH_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"🎯 Mac Mini Transcription Client Starting")
    print(f"📁 Watching: {WATCH_DIR}")
    print(f"🌐 Atlas URL: {ATLAS_URL}")
    print(f"🔑 API Key: {'Set' if API_KEY else 'None'}")
    print(f"📋 Usage: Drop audio files into {WATCH_DIR}")
    print(f"⚡ Auto-transcribes and sends to Atlas")
    print("=" * 60)
    
    # Set up file watcher
    event_handler = TranscriptionHandler(ATLAS_URL, API_KEY)
    observer = Observer()
    observer.schedule(event_handler, str(WATCH_DIR), recursive=False)
    
    try:
        observer.start()
        print("🔄 Monitoring for audio files... (Ctrl+C to stop)")
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n⏹️ Stopping transcription client...")
        observer.stop()
    
    observer.join()
    print("✅ Client stopped")

if __name__ == "__main__":
    main()