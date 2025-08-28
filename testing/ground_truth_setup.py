#!/usr/bin/env python3
"""
Ground Truth Testing Setup

Creates test datasets with known transcripts for fidelity testing.
Downloads sample podcasts with official transcripts where available.
"""

import os
import json
import requests
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from helpers.bulletproof_process_manager import create_managed_process

from helpers.utils import log_info, log_error


class GroundTruthSetup:
    """Setup ground truth test data for transcription fidelity testing"""
    
    def __init__(self):
        self.test_data_dir = Path("test_data/ground_truth")
        self.test_data_dir.mkdir(parents=True, exist_ok=True)
        
        # Known podcasts with official transcripts
        self.known_transcribed_podcasts = [
            {
                "name": "TED Radio Hour",
                "feed": "https://feeds.npr.org/510298/podcast.xml",
                "official_transcripts": True,
                "sample_episodes": [
                    {
                        "title": "The Power of Design",
                        "audio_url": "https://play.podtrac.com/npr-510298/edge1.pod.npr.org/anon.npr-podcasts/podcast/510298/1196934896/npr_1196934896.mp3",
                        "transcript_url": "https://www.npr.org/transcripts/1196934896"
                    }
                ]
            },
            {
                "name": "This American Life",
                "feed": "https://feeds.thisamericanlife.org/talpodcast",
                "official_transcripts": True,
                "sample_episodes": []
            }
        ]
        
        # Sample audio files for testing (CC licensed)
        self.sample_audio_files = [
            {
                "name": "librivox_sample",
                "url": "https://archive.org/download/rip_van_winkle_librivox/rip_van_winkle_01_irving.mp3",
                "transcript": """Once upon a time, in a small Dutch village in the mountains, there lived a simple man named Rip Van Winkle. He was a kind man, well-liked by his neighbors, though perhaps a bit too fond of avoiding work around his own home.""",
                "source": "LibriVox public domain recording"
            }
        ]
        
        # YouTube videos with accurate auto-generated captions
        self.youtube_test_videos = [
            {
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "title": "Rick Astley - Never Gonna Give You Up",
                "has_captions": True
            }
        ]
    
    def setup_all_test_data(self) -> Dict[str, Any]:
        """Setup comprehensive test data for fidelity testing"""
        results = {
            "sample_audio": [],
            "podcast_episodes": [],
            "youtube_videos": [],
            "synthetic_audio": []
        }
        
        log_info("ground_truth.log", "Setting up ground truth test data")
        
        # Download sample audio files
        for sample in self.sample_audio_files:
            result = self._download_sample_audio(sample)
            if result:
                results["sample_audio"].append(result)
        
        # Setup podcast test episodes
        for podcast in self.known_transcribed_podcasts:
            for episode in podcast.get("sample_episodes", []):
                result = self._setup_podcast_episode(episode)
                if result:
                    results["podcast_episodes"].append(result)
        
        # Create synthetic test audio
        synthetic = self._create_synthetic_test_audio()
        if synthetic:
            results["synthetic_audio"].append(synthetic)
        
        # Save test data manifest
        manifest_path = self.test_data_dir / "test_manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        log_info("ground_truth.log", f"Test data setup complete. Manifest saved to {manifest_path}")
        return results
    
    def _download_sample_audio(self, sample: Dict[str, str]) -> Optional[Dict[str, str]]:
        """Download a sample audio file with known transcript"""
        try:
            audio_path = self.test_data_dir / f"{sample['name']}.mp3"
            transcript_path = self.test_data_dir / f"{sample['name']}.txt"
            
            # Skip if already exists
            if audio_path.exists() and transcript_path.exists():
                log_info("ground_truth.log", f"Sample {sample['name']} already exists")
                return {
                    "name": sample["name"],
                    "audio_path": str(audio_path),
                    "transcript_path": str(transcript_path),
                    "source": sample.get("source", "unknown")
                }
            
            # Download audio
            log_info("ground_truth.log", f"Downloading {sample['name']}...")
            response = requests.get(sample["url"], stream=True, timeout=30)
            response.raise_for_status()
            
            with open(audio_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Save transcript
            with open(transcript_path, 'w') as f:
                f.write(sample["transcript"])
            
            log_info("ground_truth.log", f"Successfully downloaded {sample['name']}")
            
            return {
                "name": sample["name"],
                "audio_path": str(audio_path),
                "transcript_path": str(transcript_path),
                "source": sample.get("source", "unknown")
            }
            
        except Exception as e:
            log_error("ground_truth.log", f"Failed to download {sample['name']}: {e}")
            return None
    
    def _setup_podcast_episode(self, episode: Dict[str, str]) -> Optional[Dict[str, str]]:
        """Setup a podcast episode with official transcript"""
        try:
            name = episode["title"].replace(" ", "_").lower()
            audio_path = self.test_data_dir / f"podcast_{name}.mp3"
            transcript_path = self.test_data_dir / f"podcast_{name}.txt"
            
            # Skip if already exists
            if audio_path.exists() and transcript_path.exists():
                return {
                    "name": name,
                    "audio_path": str(audio_path),
                    "transcript_path": str(transcript_path),
                    "source": "podcast_official"
                }
            
            # Download audio
            log_info("ground_truth.log", f"Downloading podcast episode: {episode['title']}")
            response = requests.get(episode["audio_url"], stream=True, timeout=60)
            response.raise_for_status()
            
            with open(audio_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Fetch official transcript
            if "transcript_url" in episode:
                transcript = self._fetch_official_transcript(episode["transcript_url"])
                if transcript:
                    with open(transcript_path, 'w') as f:
                        f.write(transcript)
                    
                    return {
                        "name": name,
                        "audio_path": str(audio_path),
                        "transcript_path": str(transcript_path),
                        "source": "podcast_official"
                    }
            
        except Exception as e:
            log_error("ground_truth.log", f"Failed to setup podcast episode {episode['title']}: {e}")
            return None
    
    def _fetch_official_transcript(self, transcript_url: str) -> Optional[str]:
        """Fetch official transcript from URL"""
        try:
            response = requests.get(transcript_url, timeout=30)
            response.raise_for_status()
            
            # Basic transcript extraction (would need to be customized per site)
            # This is a simplified version
            html_content = response.text
            
            # Look for common transcript patterns
            import re
            
            # NPR transcript pattern
            npr_pattern = r'<div class="transcript.*?">(.*?)</div>'
            matches = re.findall(npr_pattern, html_content, re.DOTALL)
            
            if matches:
                # Clean up HTML tags
                import html
                transcript = re.sub(r'<[^>]+>', '', matches[0])
                transcript = html.unescape(transcript)
                transcript = re.sub(r'\s+', ' ', transcript).strip()
                return transcript
            
            return None
            
        except Exception as e:
            log_error("ground_truth.log", f"Failed to fetch transcript from {transcript_url}: {e}")
            return None
    
    def _create_synthetic_test_audio(self) -> Optional[Dict[str, str]]:
        """Create synthetic test audio using text-to-speech"""
        try:
            # Check if we have TTS available
            import subprocess
            
            # Try using system TTS (macOS/Linux)
            test_text = """
            This is a synthetic test audio file created for transcription accuracy testing.
            It contains clear speech with proper pronunciation and punctuation.
            The purpose is to establish a baseline for transcription fidelity measurement.
            """
            
            audio_path = self.test_data_dir / "synthetic_test.wav"
            transcript_path = self.test_data_dir / "synthetic_test.txt"
            
            # Skip if already exists
            if audio_path.exists() and transcript_path.exists():
                return {
                    "name": "synthetic_test",
                    "audio_path": str(audio_path),
                    "transcript_path": str(transcript_path),
                    "source": "synthetic_tts"
                }
            
            # Try different TTS options
            tts_success = False
            
            # Option 1: macOS 'say' command
            try:
                process = create_managed_process([
                    "say", "-v", "Alex", "-o", str(audio_path), test_text
                ], "tts_say")
                stdout, stderr = process.communicate()
                if process.returncode != 0:
                    raise subprocess.CalledProcessError(process.returncode, process.args, output=stdout, stderr=stderr)
                tts_success = True
                log_info("ground_truth.log", "Created synthetic audio using macOS 'say'")
            except (subprocess.CalledProcessError, FileNotFoundError):
                pass
            
            # Option 2: espeak (Linux)
            if not tts_success:
                try:
                    process = create_managed_process([
                        "espeak", "-w", str(audio_path), test_text
                    ], "tts_espeak")
                    stdout, stderr = process.communicate()
                    if process.returncode != 0:
                        raise subprocess.CalledProcessError(process.returncode, process.args, output=stdout, stderr=stderr)
                    tts_success = True
                    log_info("ground_truth.log", "Created synthetic audio using espeak")
                except (subprocess.CalledProcessError, FileNotFoundError):
                    pass
            
            if tts_success:
                # Save the exact text
                with open(transcript_path, 'w') as f:
                    f.write(test_text.strip())
                
                return {
                    "name": "synthetic_test",
                    "audio_path": str(audio_path),
                    "transcript_path": str(transcript_path),
                    "source": "synthetic_tts"
                }
            
        except Exception as e:
            log_error("ground_truth.log", f"Failed to create synthetic audio: {e}")
        
        return None
    
    def get_test_files(self) -> List[Tuple[str, str]]:
        """Get list of (audio_path, transcript_path) pairs for testing"""
        manifest_path = self.test_data_dir / "test_manifest.json"
        
        if not manifest_path.exists():
            log_info("ground_truth.log", "No test manifest found, setting up test data...")
            self.setup_all_test_data()
        
        test_files = []
        
        try:
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)
            
            # Collect all test files
            for category in manifest.values():
                if isinstance(category, list):
                    for item in category:
                        if "audio_path" in item and "transcript_path" in item:
                            audio_path = item["audio_path"]
                            transcript_path = item["transcript_path"]
                            
                            if os.path.exists(audio_path) and os.path.exists(transcript_path):
                                test_files.append((audio_path, transcript_path))
        
        except Exception as e:
            log_error("ground_truth.log", f"Failed to load test manifest: {e}")
        
        return test_files
    
    def validate_test_data(self) -> Dict[str, Any]:
        """Validate that all test data is properly set up"""
        test_files = self.get_test_files()
        
        validation_results = {
            "total_files": len(test_files),
            "valid_files": 0,
            "invalid_files": [],
            "total_audio_duration": 0,
            "total_transcript_words": 0
        }
        
        for audio_path, transcript_path in test_files:
            try:
                # Check file sizes
                audio_size = os.path.getsize(audio_path)
                transcript_size = os.path.getsize(transcript_path)
                
                if audio_size > 0 and transcript_size > 0:
                    validation_results["valid_files"] += 1
                    
                    # Count words in transcript
                    with open(transcript_path, 'r') as f:
                        words = len(f.read().split())
                        validation_results["total_transcript_words"] += words
                else:
                    validation_results["invalid_files"].append({
                        "audio_path": audio_path,
                        "transcript_path": transcript_path,
                        "issue": "Empty files"
                    })
                    
            except Exception as e:
                validation_results["invalid_files"].append({
                    "audio_path": audio_path,
                    "transcript_path": transcript_path,
                    "issue": str(e)
                })
        
        log_info("ground_truth.log", f"Validation complete: {validation_results['valid_files']}/{validation_results['total_files']} files valid")
        
        return validation_results


def main():
    """Setup ground truth test data"""
    setup = GroundTruthSetup()
    
    print("Setting up ground truth test data...")
    results = setup.setup_all_test_data()
    
    print("\nValidating test data...")
    validation = setup.validate_test_data()
    
    print("\nSetup Results:")
    print(f"  Sample Audio Files: {len(results.get('sample_audio', []))}")
    print(f"  Podcast Episodes: {len(results.get('podcast_episodes', []))}")
    print(f"  Synthetic Audio: {len(results.get('synthetic_audio', []))}")
    
    print("\nValidation Results:")
    print(f"  Valid Files: {validation['valid_files']}/{validation['total_files']}")
    print(f"  Total Words: {validation['total_transcript_words']}")
    
    if validation["invalid_files"]:
        print(f"  Invalid Files: {len(validation['invalid_files'])}")
        for invalid in validation["invalid_files"]:
            print(f"    - {invalid['audio_path']}: {invalid['issue']}")
    
    return results, validation


if __name__ == "__main__":
    main()