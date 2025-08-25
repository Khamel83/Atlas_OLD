#!/usr/bin/env python3
"""
Atlas Mac Mini Client

Polls Atlas for transcription jobs and executes them using local resources
(Whisper, yt-dlp, etc). Designed to run on Mac Mini for heavy processing tasks.
"""

import requests
import json
import time
import logging
import subprocess
import tempfile
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional

class AtlasWorkerClient:
    def __init__(self, 
                 worker_id: str = None,
                 atlas_url: str = "http://192.168.1.100:8000",
                 capabilities: List[str] = None,
                 poll_interval: int = 30):
        """
        Initialize Atlas Worker Client
        
        Args:
            worker_id: Unique worker identifier (defaults to hostname-mac)
            atlas_url: Atlas server URL 
            capabilities: List of job types this worker can handle
            poll_interval: Job polling interval in seconds
        """
        self.worker_id = worker_id or f"{platform.node()}-mac"
        self.atlas_url = atlas_url.rstrip('/')
        self.base_url = f"{self.atlas_url}/api/v1/worker"
        self.poll_interval = poll_interval
        self.running = False
        
        # Setup logging first
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('AtlasWorker')
        
        # Default capabilities based on available tools
        self.capabilities = capabilities or self._detect_capabilities()
        
    def _detect_capabilities(self) -> List[str]:
        """Detect available transcription capabilities"""
        caps = []
        
        # Check for whisper
        if self._command_exists('whisper'):
            caps.extend(['transcribe_youtube', 'transcribe_podcast', 'transcribe_url'])
            self.logger.info("✅ Whisper detected - transcription capabilities enabled")
        
        # Check for yt-dlp  
        if self._command_exists('yt-dlp'):
            caps.extend(['download_youtube'])
            self.logger.info("✅ yt-dlp detected - YouTube download capability enabled")
            
        # Check for ffmpeg
        if self._command_exists('ffmpeg'):
            caps.extend(['convert_audio'])
            self.logger.info("✅ ffmpeg detected - audio conversion capability enabled")
            
        if not caps:
            self.logger.warning("⚠️ No transcription tools detected - limited capabilities")
            caps = ['basic_processing']
            
        return caps
        
    def _command_exists(self, command: str) -> bool:
        """Check if a command exists in PATH"""
        try:
            subprocess.run([command, '--help'], capture_output=True, check=False)
            return True
        except FileNotFoundError:
            return False
            
    def register(self) -> bool:
        """Register this worker with Atlas"""
        try:
            registration_data = {
                "worker_id": self.worker_id,
                "capabilities": self.capabilities,
                "platform": "mac",
                "whisper_available": 'whisper' in str(subprocess.run(['which', 'whisper'], capture_output=True).stdout),
                "ytdlp_available": 'yt-dlp' in str(subprocess.run(['which', 'yt-dlp'], capture_output=True).stdout),
                "metadata": {
                    "hostname": platform.node(),
                    "python_version": sys.version,
                    "started_at": datetime.now(timezone.utc).isoformat()
                }
            }
            
            response = requests.post(
                f"{self.base_url}/register", 
                json=registration_data,
                timeout=10
            )
            response.raise_for_status()
            
            result = response.json()
            self.logger.info(f"✅ Registration successful: {result.get('message')}")
            return True
            
        except requests.RequestException as e:
            self.logger.error(f"❌ Registration failed: {e}")
            return False
        except Exception as e:
            self.logger.error(f"❌ Unexpected registration error: {e}")
            return False
            
    def get_jobs(self) -> List[Dict[str, Any]]:
        """Get available jobs from Atlas"""
        try:
            params = {
                "worker_id": self.worker_id,
                "capabilities": ",".join(self.capabilities)
            }
            
            response = requests.get(
                f"{self.base_url}/jobs",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            result = response.json()
            jobs = result.get("jobs", [])
            
            if jobs:
                self.logger.info(f"📥 Received {len(jobs)} jobs")
            else:
                self.logger.debug("📭 No jobs available")
                
            return jobs
            
        except requests.RequestException as e:
            self.logger.error(f"❌ Failed to get jobs: {e}")
            return []
        except Exception as e:
            self.logger.error(f"❌ Unexpected error getting jobs: {e}")
            return []
            
    def submit_result(self, job_id: str, status: str, result: Dict[str, Any]) -> bool:
        """Submit job result back to Atlas"""
        try:
            result_data = {
                "job_id": job_id,
                "worker_id": self.worker_id,
                "status": status,
                "result": result,
                "timestamp": time.time()
            }
            
            response = requests.post(
                f"{self.base_url}/results",
                json=result_data,
                timeout=30
            )
            response.raise_for_status()
            
            response_data = response.json()
            self.logger.info(f"✅ Result submitted: {response_data.get('message')}")
            return True
            
        except requests.RequestException as e:
            self.logger.error(f"❌ Failed to submit result: {e}")
            return False
        except Exception as e:
            self.logger.error(f"❌ Unexpected error submitting result: {e}")
            return False
            
    def execute_job(self, job: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a transcription job"""
        job_id = job.get('id')
        job_type = job.get('type')
        job_data = job.get('data', {})
        
        self.logger.info(f"🔄 Executing job {job_id}: {job_type}")
        
        try:
            if job_type == 'transcribe_youtube':
                return self._transcribe_youtube(job_data)
            elif job_type == 'transcribe_podcast':
                return self._transcribe_podcast(job_data)
            elif job_type == 'transcribe_url':
                return self._transcribe_url(job_data)
            else:
                return {
                    'error': f"Unsupported job type: {job_type}",
                    'status': 'failed'
                }
                
        except Exception as e:
            self.logger.error(f"❌ Job execution failed: {e}")
            return {
                'error': str(e),
                'status': 'failed'
            }
            
    def _transcribe_youtube(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Transcribe YouTube video using yt-dlp + Whisper"""
        url = data.get('url')
        title = data.get('title', 'Unknown')
        
        if not url:
            return {'error': 'No URL provided', 'status': 'failed'}
            
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                # Download audio using yt-dlp
                self.logger.info(f"📥 Downloading audio from {url}")
                audio_path = os.path.join(temp_dir, "audio.%(ext)s")
                
                yt_cmd = [
                    'yt-dlp',
                    '--extract-audio',
                    '--audio-format', 'wav',
                    '--output', audio_path,
                    url
                ]
                
                result = subprocess.run(yt_cmd, capture_output=True, text=True, timeout=300)
                if result.returncode != 0:
                    return {
                        'error': f"yt-dlp failed: {result.stderr}",
                        'status': 'failed'
                    }
                
                # Find the downloaded audio file
                audio_files = list(Path(temp_dir).glob("audio.*"))
                if not audio_files:
                    return {'error': 'Audio download failed', 'status': 'failed'}
                    
                audio_file = audio_files[0]
                
                # Transcribe using Whisper
                self.logger.info(f"🎯 Transcribing audio: {audio_file}")
                whisper_cmd = [
                    'whisper',
                    str(audio_file),
                    '--output_format', 'txt',
                    '--output_dir', temp_dir
                ]
                
                result = subprocess.run(whisper_cmd, capture_output=True, text=True, timeout=600)
                if result.returncode != 0:
                    return {
                        'error': f"Whisper failed: {result.stderr}",
                        'status': 'failed'
                    }
                
                # Read transcript
                transcript_files = list(Path(temp_dir).glob("*.txt"))
                if not transcript_files:
                    return {'error': 'Transcript not generated', 'status': 'failed'}
                    
                transcript_path = transcript_files[0]
                with open(transcript_path, 'r', encoding='utf-8') as f:
                    transcript = f.read().strip()
                
                if not transcript:
                    return {'error': 'Empty transcript generated', 'status': 'failed'}
                
                self.logger.info(f"✅ Transcription complete: {len(transcript)} characters")
                
                return {
                    'transcript': transcript,
                    'filename': f"{title}_transcript.txt",
                    'source_url': url,
                    'title': title,
                    'length': len(transcript.split()),
                    'status': 'completed'
                }
                
            except subprocess.TimeoutExpired:
                return {'error': 'Transcription timeout', 'status': 'failed'}
            except Exception as e:
                return {'error': str(e), 'status': 'failed'}
                
    def _transcribe_podcast(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Transcribe podcast episode"""
        # Similar to YouTube transcription but for audio files
        url = data.get('url')
        title = data.get('title', 'Unknown')
        
        if not url:
            return {'error': 'No URL provided', 'status': 'failed'}
            
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                # Download audio file
                self.logger.info(f"📥 Downloading audio from {url}")
                audio_path = os.path.join(temp_dir, "audio.mp3")
                
                download_cmd = ['curl', '-L', '-o', audio_path, url]
                result = subprocess.run(download_cmd, capture_output=True, timeout=300)
                
                if result.returncode != 0:
                    return {'error': 'Audio download failed', 'status': 'failed'}
                
                # Transcribe using Whisper
                self.logger.info(f"🎯 Transcribing podcast: {title}")
                whisper_cmd = [
                    'whisper',
                    audio_path,
                    '--output_format', 'txt',
                    '--output_dir', temp_dir
                ]
                
                result = subprocess.run(whisper_cmd, capture_output=True, text=True, timeout=600)
                if result.returncode != 0:
                    return {
                        'error': f"Whisper failed: {result.stderr}",
                        'status': 'failed'
                    }
                
                # Read transcript
                transcript_files = list(Path(temp_dir).glob("*.txt"))
                if not transcript_files:
                    return {'error': 'Transcript not generated', 'status': 'failed'}
                    
                transcript_path = transcript_files[0]
                with open(transcript_path, 'r', encoding='utf-8') as f:
                    transcript = f.read().strip()
                
                self.logger.info(f"✅ Podcast transcription complete: {len(transcript)} characters")
                
                return {
                    'transcript': transcript,
                    'filename': f"{title}_transcript.txt",
                    'source_url': url,
                    'title': title,
                    'length': len(transcript.split()),
                    'status': 'completed'
                }
                
            except Exception as e:
                return {'error': str(e), 'status': 'failed'}
                
    def _transcribe_url(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Transcribe generic audio/video URL"""
        # For now, treat as YouTube transcription
        return self._transcribe_youtube(data)
        
    def run_once(self) -> bool:
        """Run one polling cycle"""
        try:
            # Get available jobs
            jobs = self.get_jobs()
            
            if not jobs:
                return True
                
            # Process each job
            for job in jobs:
                job_id = job.get('id')
                self.logger.info(f"🔄 Processing job {job_id}")
                
                # Execute the job
                result = self.execute_job(job)
                status = result.get('status', 'completed')
                
                # Submit result back to Atlas
                success = self.submit_result(job_id, status, result)
                
                if success:
                    self.logger.info(f"✅ Job {job_id} completed successfully")
                else:
                    self.logger.error(f"❌ Failed to submit result for job {job_id}")
                    
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Polling cycle failed: {e}")
            return False
            
    def run(self):
        """Start the main worker loop"""
        self.logger.info(f"🚀 Starting Atlas Worker: {self.worker_id}")
        self.logger.info(f"📡 Atlas URL: {self.atlas_url}")
        self.logger.info(f"🛠️ Capabilities: {', '.join(self.capabilities)}")
        
        # Register with Atlas
        if not self.register():
            self.logger.error("❌ Failed to register with Atlas - exiting")
            return
            
        self.running = True
        
        try:
            while self.running:
                self.logger.debug(f"🔍 Polling for jobs...")
                success = self.run_once()
                
                if not success:
                    self.logger.warning("⚠️ Polling cycle failed, continuing...")
                
                # Sleep until next poll
                time.sleep(self.poll_interval)
                
        except KeyboardInterrupt:
            self.logger.info("🛑 Received interrupt signal")
        except Exception as e:
            self.logger.error(f"❌ Fatal error: {e}")
        finally:
            self.running = False
            self.logger.info("🏁 Worker stopped")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Atlas Mac Mini Worker Client')
    parser.add_argument('--worker-id', help='Worker ID (defaults to hostname-mac)')
    parser.add_argument('--atlas-url', default='http://localhost:8000', 
                       help='Atlas server URL (default: http://localhost:8000)')
    parser.add_argument('--poll-interval', type=int, default=30,
                       help='Polling interval in seconds (default: 30)')
    parser.add_argument('--capabilities', nargs='*',
                       help='Override detected capabilities')
    parser.add_argument('--test', action='store_true',
                       help='Run a single polling cycle and exit')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger('AtlasWorker').setLevel(logging.DEBUG)
    
    # Create worker client
    client = AtlasWorkerClient(
        worker_id=args.worker_id,
        atlas_url=args.atlas_url,
        capabilities=args.capabilities,
        poll_interval=args.poll_interval
    )
    
    if args.test:
        # Test mode - single cycle
        print("🧪 Test mode - running single polling cycle")
        success = client.register()
        if success:
            client.run_once()
        else:
            print("❌ Registration failed")
            sys.exit(1)
    else:
        # Normal mode - continuous polling
        client.run()


if __name__ == '__main__':
    main()