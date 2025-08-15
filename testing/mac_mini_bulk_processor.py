#!/usr/bin/env python3
"""
Mac Mini M4 Bulk Processing System

Optimized for Apple Silicon hardware with:
- Hardware-accelerated transcription
- Batch processing of entire podcast backlogs
- Smart ad detection and content filtering
- Integration with existing Atlas transcript lookup
- Efficient memory management
- Results packaging for VPS upload
"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import subprocess
import concurrent.futures
from dataclasses import dataclass
import sys

# Add current directory to path to import Atlas helpers
sys.path.insert(0, '.')

# Import Atlas components
try:
    from helpers.transcript_lookup import TranscriptLookup
    from helpers.enhanced_transcription import EnhancedTranscriptionEngine
    from helpers.config import load_config
    from helpers.podcast_ingestor import PodcastIngestor
    from helpers.utils import log_info, log_error
    import psutil
    import feedparser
    import requests
except ImportError as e:
    print(f"Install dependencies or run from Atlas root: {e}")
    print("Required: pip install psutil feedparser requests beautifulsoup4")


@dataclass
class BulkProcessingConfig:
    """Configuration for bulk processing"""
    max_concurrent_transcriptions: int = 4  # M4 can handle multiple
    use_coreml: bool = True  # Hardware acceleration
    skip_ads: bool = True
    ad_detection_threshold: float = 0.7
    output_base_dir: str = "bulk_output"
    max_episode_size_mb: int = 500  # M4 can handle larger files
    preferred_models: List[str] = None
    
    def __post_init__(self):
        if self.preferred_models is None:
            # Prioritize speed on M4 - can use larger models efficiently
            self.preferred_models = ["small", "medium", "large"]


class AdDetector:
    """Detect and mark advertisement segments in podcast audio"""
    
    def __init__(self):
        # Common ad indicators
        self.ad_keywords = [
            "sponsored by", "this episode is brought to you",
            "our sponsor", "ad break", "commercial break",
            "promo code", "discount code", "visit our website",
            "special offer", "limited time", "act now",
            "get your", "try free", "free trial",
            "mattress", "vpn", "meal kit", "underwear",
            "raycon", "skillshare", "brilliant", "audible",
            "squarespace", "nordvpn", "expressvpn"
        ]
        
        # Audio patterns that suggest ads
        self.ad_audio_patterns = {
            "music_change": "Sudden music/jingle change",
            "voice_change": "Different voice/narrator",
            "audio_quality_change": "Audio quality shift",
            "volume_spike": "Volume increase"
        }
    
    def detect_ad_segments(self, transcript: str, audio_path: str) -> List[Dict[str, Any]]:
        """Detect advertisement segments in transcript and audio"""
        ad_segments = []
        
        # Text-based detection
        lines = transcript.split('\n')
        current_segment = None
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            
            # Check for ad keywords
            for keyword in self.ad_keywords:
                if keyword in line_lower:
                    if current_segment is None:
                        current_segment = {
                            "start_line": max(0, i - 2),  # Include context
                            "type": "text_based",
                            "confidence": 0.8,
                            "trigger": keyword,
                            "content": []
                        }
                    
                    current_segment["content"].append(line)
                    
                    # Look ahead for end of ad
                    if any(end_phrase in line_lower for end_phrase in [
                        "back to", "now back to", "let's get back",
                        "returning to", "back to the show"
                    ]):
                        current_segment["end_line"] = i + 2
                        ad_segments.append(current_segment)
                        current_segment = None
                        break
        
        # Close any open segment
        if current_segment:
            current_segment["end_line"] = len(lines)
            ad_segments.append(current_segment)
        
        return ad_segments
    
    def create_ad_free_transcript(self, transcript: str, ad_segments: List[Dict[str, Any]]) -> str:
        """Create a transcript with ads removed or marked"""
        lines = transcript.split('\n')
        ad_free_lines = []
        
        for i, line in enumerate(lines):
            is_ad = False
            
            for segment in ad_segments:
                if segment["start_line"] <= i <= segment["end_line"]:
                    is_ad = True
                    break
            
            if not is_ad:
                ad_free_lines.append(line)
            elif i == (segment["start_line"] + segment["end_line"]) // 2:
                # Add a marker in the middle of the ad segment
                ad_free_lines.append(f"[AD SEGMENT REMOVED - {segment['trigger']}]")
        
        return '\n'.join(ad_free_lines)


class MacMiniOptimizer:
    """M4-specific optimizations for transcription"""
    
    def __init__(self):
        self.cpu_count = os.cpu_count()
        self.memory_gb = self._get_memory_gb()
        self.is_apple_silicon = self._detect_apple_silicon()
    
    def _get_memory_gb(self) -> int:
        """Get system memory in GB"""
        try:
            return int(psutil.virtual_memory().total / (1024**3))
        except:
            return 16  # Conservative default
    
    def _detect_apple_silicon(self) -> bool:
        """Detect if running on Apple Silicon"""
        try:
            result = subprocess.run(['uname', '-m'], capture_output=True, text=True)
            return 'arm64' in result.stdout
        except:
            return False
    
    def get_optimal_whisper_config(self, model_size: str) -> Dict[str, Any]:
        """Get M4-optimized Whisper configuration"""
        base_config = {
            "language": "en",
            "fp16": False,  # Better compatibility
            "device": "cpu",
            "threads": min(self.cpu_count, 8),  # Don't overwhelm system
        }
        
        if self.is_apple_silicon:
            # M4-specific optimizations
            base_config.update({
                "device": "mps",  # Metal Performance Shaders if available
                "fp16": True,     # M4 handles FP16 well
                "threads": self.cpu_count,  # Use all cores
            })
        
        # Model-specific settings
        model_configs = {
            "tiny": {"temperature": 0.0, "best_of": 1},
            "small": {"temperature": 0.0, "best_of": 1},
            "medium": {"temperature": 0.0, "best_of": 1},
            "large": {"temperature": 0.1, "best_of": 3},  # Higher quality for large
        }
        
        base_config.update(model_configs.get(model_size, {}))
        return base_config


class BulkPodcastProcessor:
    """Main bulk processing class optimized for Mac Mini M4"""
    
    def __init__(self, config: BulkProcessingConfig):
        self.config = config
        self.optimizer = MacMiniOptimizer()
        self.ad_detector = AdDetector() if config.skip_ads else None
        
        # Setup output directories
        self.output_dir = Path(config.output_base_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        self.transcripts_dir = self.output_dir / "transcripts"
        self.metadata_dir = self.output_dir / "metadata"
        self.audio_dir = self.output_dir / "audio"
        self.reports_dir = self.output_dir / "reports"
        
        for dir_path in [self.transcripts_dir, self.metadata_dir, self.audio_dir, self.reports_dir]:
            dir_path.mkdir(exist_ok=True)
        
        self.processing_stats = {
            "start_time": datetime.now(),
            "episodes_processed": 0,
            "total_audio_hours": 0,
            "transcription_time": 0,
            "ads_detected": 0,
            "errors": []
        }
    
    def process_opml_file(self, opml_path: str) -> Dict[str, Any]:
        """Process entire OPML file with bulk optimization"""
        print(f"🚀 Starting bulk processing of {opml_path} on Mac Mini M4")
        
        # Parse OPML
        feeds = self._parse_opml(opml_path)
        print(f"📻 Found {len(feeds)} podcast feeds")
        
        # Process feeds with optimized concurrency
        all_results = {}
        
        # Process feeds in batches to manage memory
        batch_size = 5  # Process 5 feeds at a time
        feed_batches = [feeds[i:i + batch_size] for i in range(0, len(feeds), batch_size)]
        
        for batch_num, feed_batch in enumerate(feed_batches, 1):
            print(f"\n📦 Processing batch {batch_num}/{len(feed_batches)}")
            
            batch_results = self._process_feed_batch(feed_batch)
            all_results.update(batch_results)
            
            # Memory cleanup between batches
            self._cleanup_temp_files()
        
        # Generate final report
        final_report = self._generate_final_report(all_results)
        
        print("\n🎉 Bulk processing complete!")
        print(f"📊 Processed {self.processing_stats['episodes_processed']} episodes")
        print(f"⏱️  Total time: {datetime.now() - self.processing_stats['start_time']}")
        
        return final_report
    
    def _parse_opml(self, opml_path: str) -> List[Tuple[str, str]]:
        """Parse OPML file and extract feed URLs"""
        try:
            import xml.etree.ElementTree as ET
            tree = ET.parse(opml_path)
            root = tree.getroot()
            
            feeds = []
            for outline in root.findall(".//outline[@type='rss']"):
                xml_url = outline.get('xmlUrl')
                title = outline.get('text', 'Unknown Feed')
                if xml_url:
                    feeds.append((xml_url, title))
            
            return feeds
        except Exception as e:
            print(f"❌ Error parsing OPML: {e}")
            return []
    
    def _process_feed_batch(self, feeds: List[Tuple[str, str]]) -> Dict[str, Any]:
        """Process a batch of feeds with optimal concurrency"""
        batch_results = {}
        
        # Use ThreadPoolExecutor for I/O operations (downloading)
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as io_executor:
            download_futures = {}
            
            for feed_url, feed_title in feeds:
                future = io_executor.submit(self._download_feed_episodes, feed_url, feed_title)
                download_futures[future] = (feed_url, feed_title)
            
            # Process downloads as they complete
            for future in concurrent.futures.as_completed(download_futures):
                feed_url, feed_title = download_futures[future]
                try:
                    episodes = future.result()
                    if episodes:
                        # Process transcriptions for this feed
                        feed_results = self._process_feed_transcriptions(feed_url, feed_title, episodes)
                        batch_results[feed_title] = feed_results
                except Exception as e:
                    print(f"❌ Error processing feed {feed_title}: {e}")
                    self.processing_stats["errors"].append(f"Feed {feed_title}: {e}")
        
        return batch_results
    
    def _download_feed_episodes(self, feed_url: str, feed_title: str, max_episodes: int = 10) -> List[Dict[str, Any]]:
        """Download episodes from a feed (limited for bulk processing)"""
        try:
            print(f"📥 Downloading episodes from {feed_title}")
            
            feed = feedparser.parse(feed_url)
            if not feed.entries:
                return []
            
            episodes = []
            
            # Limit episodes for bulk processing
            for entry in feed.entries[:max_episodes]:
                episode_data = self._download_single_episode(entry, feed_title)
                if episode_data:
                    episodes.append(episode_data)
            
            return episodes
            
        except Exception as e:
            print(f"❌ Error downloading from {feed_title}: {e}")
            return []
    
    def _download_single_episode(self, entry: Any, feed_title: str) -> Optional[Dict[str, Any]]:
        """Download a single episode"""
        title = entry.get("title", "Untitled Episode")
        
        # Extract audio URL
        audio_url = None
        if hasattr(entry, "enclosures") and entry.enclosures:
            audio_url = entry.enclosures[0].href
        elif hasattr(entry, "links") and entry.links:
            for link in entry.links:
                if link.get("type", "").startswith("audio"):
                    audio_url = link.get("href")
                    break
        
        if not audio_url:
            return None
        
        # Generate safe filename
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_title = safe_title[:50]  # Limit length
        
        audio_filename = f"{feed_title}_{safe_title}.mp3".replace(" ", "_")
        audio_path = self.audio_dir / audio_filename
        
        try:
            # Download with size limit
            response = requests.get(audio_url, stream=True, timeout=30)
            response.raise_for_status()
            
            # Check size
            content_length = response.headers.get('content-length')
            if content_length:
                size_mb = int(content_length) / (1024 * 1024)
                if size_mb > self.config.max_episode_size_mb:
                    print(f"⚠️  Skipping large episode: {title} ({size_mb:.1f}MB)")
                    return None
            
            # Download
            with open(audio_path, 'wb') as f:
                downloaded_size = 0
                max_bytes = self.config.max_episode_size_mb * 1024 * 1024
                
                for chunk in response.iter_content(chunk_size=8192):
                    if downloaded_size + len(chunk) > max_bytes:
                        print(f"⚠️  Size limit reached for: {title}")
                        break
                    f.write(chunk)
                    downloaded_size += len(chunk)
            
            return {
                "title": title,
                "audio_path": str(audio_path),
                "audio_url": audio_url,
                "size_mb": downloaded_size / (1024 * 1024),
                "feed_title": feed_title
            }
            
        except Exception as e:
            print(f"❌ Download failed for {title}: {e}")
            return None
    
    def _process_feed_transcriptions(self, feed_url: str, feed_title: str, episodes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Process transcriptions for all episodes in a feed"""
        print(f"🎤 Transcribing {len(episodes)} episodes from {feed_title}")
        
        feed_results = {
            "feed_url": feed_url,
            "episodes": {},
            "total_episodes": len(episodes),
            "successful_transcriptions": 0,
            "total_duration": 0
        }
        
        # Process transcriptions with limited concurrency
        with concurrent.futures.ProcessPoolExecutor(max_workers=self.config.max_concurrent_transcriptions) as executor:
            transcription_futures = {}
            
            for episode in episodes:
                for model in self.config.preferred_models:
                    future = executor.submit(self._transcribe_episode, episode, model)
                    transcription_futures[future] = (episode, model)
            
            # Collect results
            for future in concurrent.futures.as_completed(transcription_futures):
                episode, model = transcription_futures[future]
                try:
                    result = future.result()
                    if result["success"]:
                        episode_id = episode["title"]
                        if episode_id not in feed_results["episodes"]:
                            feed_results["episodes"][episode_id] = {}
                        
                        feed_results["episodes"][episode_id][model] = result
                        
                        if result["success"]:
                            feed_results["successful_transcriptions"] += 1
                            feed_results["total_duration"] += result.get("duration", 0)
                            
                except Exception as e:
                    print(f"❌ Transcription error: {e}")
        
        return feed_results
    
    def _transcribe_episode(self, episode: Dict[str, Any], model: str) -> Dict[str, Any]:
        """Transcribe a single episode with a specific model"""
        audio_path = episode["audio_path"]
        
        try:
            # Get M4-optimized config
            whisper_config = self.optimizer.get_optimal_whisper_config(model)
            
            # Setup output paths
            base_name = Path(audio_path).stem
            transcript_path = self.transcripts_dir / f"{base_name}_{model}.txt"
            
            # Skip if already exists
            if transcript_path.exists():
                with open(transcript_path, 'r') as f:
                    transcript_text = f.read()
                
                return {
                    "success": True,
                    "transcript": transcript_text,
                    "model": model,
                    "duration": 0,  # Cached
                    "cached": True
                }
            
            # Run Whisper transcription
            start_time = time.time()
            
            command = [
                "whisper",
                audio_path,
                "--model", model,
                "--output_format", "txt",
                "--output_dir", str(self.transcripts_dir),
                "--language", whisper_config["language"],
                "--threads", str(whisper_config["threads"])
            ]
            
            # Add M4-specific optimizations
            if whisper_config.get("fp16"):
                command.extend(["--fp16", "True"])
            
            result = subprocess.run(command, capture_output=True, text=True)
            duration = time.time() - start_time
            
            if result.returncode == 0:
                # Find generated transcript
                generated_file = self.transcripts_dir / f"{Path(audio_path).stem}.txt"
                if generated_file.exists():
                    transcript_text = generated_file.read_text()
                    
                    # Rename to model-specific name
                    generated_file.rename(transcript_path)
                    
                    # Process ads if enabled
                    if self.ad_detector:
                        ad_segments = self.ad_detector.detect_ad_segments(transcript_text, audio_path)
                        if ad_segments:
                            self.processing_stats["ads_detected"] += len(ad_segments)
                            transcript_text = self.ad_detector.create_ad_free_transcript(transcript_text, ad_segments)
                            
                            # Save ad-free version
                            ad_free_path = self.transcripts_dir / f"{base_name}_{model}_ad_free.txt"
                            ad_free_path.write_text(transcript_text)
                    
                    return {
                        "success": True,
                        "transcript": transcript_text,
                        "model": model,
                        "duration": duration,
                        "word_count": len(transcript_text.split()),
                        "cached": False
                    }
            
            return {
                "success": False,
                "error": result.stderr,
                "model": model,
                "duration": duration
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "model": model,
                "duration": 0
            }
    
    def _cleanup_temp_files(self):
        """Clean up temporary files between batches"""
        try:
            # Remove audio files to save space (keep transcripts)
            for audio_file in self.audio_dir.glob("*.mp3"):
                audio_file.unlink()
        except Exception as e:
            print(f"⚠️  Cleanup warning: {e}")
    
    def _generate_final_report(self, all_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive final report"""
        report = {
            "processing_stats": self.processing_stats,
            "feed_results": all_results,
            "performance_summary": {},
            "recommendations": {}
        }
        
        # Calculate performance metrics
        total_episodes = sum(feed["total_episodes"] for feed in all_results.values())
        successful_episodes = sum(feed["successful_transcriptions"] for feed in all_results.values())
        
        report["performance_summary"] = {
            "total_feeds": len(all_results),
            "total_episodes": total_episodes,
            "successful_episodes": successful_episodes,
            "success_rate": successful_episodes / total_episodes if total_episodes > 0 else 0,
            "ads_detected": self.processing_stats["ads_detected"],
            "processing_time_hours": (datetime.now() - self.processing_stats["start_time"]).total_seconds() / 3600
        }
        
        # Save detailed report
        report_file = self.reports_dir / f"bulk_processing_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"📊 Detailed report saved to: {report_file}")
        
        return report
    
    def package_for_upload(self) -> str:
        """Package results for VPS upload"""
        package_name = f"podcast_bulk_{datetime.now().strftime('%Y%m%d_%H%M%S')}.tar.gz"
        
        # Create tarball
        subprocess.run([
            "tar", "-czf", package_name,
            "-C", str(self.output_dir.parent),
            self.output_dir.name
        ])
        
        print(f"📦 Results packaged as: {package_name}")
        print(f"💾 Upload to VPS with: scp {package_name} user@vps:/path/to/atlas/")
        
        return package_name


def main():
    """Main bulk processing function for Mac Mini M4"""
    config = BulkProcessingConfig(
        max_concurrent_transcriptions=4,  # M4 can handle this
        skip_ads=True,
        preferred_models=["small", "medium"],  # Skip tiny for better quality
        max_episode_size_mb=200
    )
    
    processor = BulkPodcastProcessor(config)
    
    # Process the OPML file
    opml_path = input("Enter path to OPML file: ").strip()
    if not opml_path:
        opml_path = "podcasts.opml"  # Default
    
    if not os.path.exists(opml_path):
        print(f"❌ OPML file not found: {opml_path}")
        return
    
    # Run bulk processing
    results = processor.process_opml_file(opml_path)
    
    # Package for upload
    package_file = processor.package_for_upload()
    
    print("\n🎉 Bulk processing complete!")
    print("📊 Summary:")
    print(f"   Feeds: {results['performance_summary']['total_feeds']}")
    print(f"   Episodes: {results['performance_summary']['successful_episodes']}/{results['performance_summary']['total_episodes']}")
    print(f"   Success Rate: {results['performance_summary']['success_rate']:.1%}")
    print(f"   Ads Detected: {results['performance_summary']['ads_detected']}")
    print(f"   Processing Time: {results['performance_summary']['processing_time_hours']:.1f} hours")
    print(f"\n📦 Upload package: {package_file}")


if __name__ == "__main__":
    main()