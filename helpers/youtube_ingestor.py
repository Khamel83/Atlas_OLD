import json
import os
import shutil
import subprocess
from datetime import datetime
from typing import Any, Dict, List, Optional

from pytube import YouTube
from youtube_transcript_api import (NoTranscriptFound, TranscriptsDisabled,
                                    YouTubeTranscriptApi)

from helpers.base_ingestor import BaseIngestor
from helpers.dedupe import link_uid
from helpers.metadata_manager import ContentType
from helpers.utils import (extract_video_id,
                           generate_markdown_summary, log_error, log_info)


def is_ytdlp_installed():
    """Check if yt-dlp is installed and available in the system's PATH."""
    return shutil.which("yt-dlp") is not None


class YouTubeIngestor(BaseIngestor):
    def get_content_type(self):
        return ContentType.YOUTUBE

    def get_module_name(self):
        return "youtube_ingestor"

    def fetch_content(self, source, metadata):
        return True, None

    def process_content(self, content, metadata):
        return True

    def __init__(self, config):
        super().__init__(config, ContentType.YOUTUBE, "youtube_ingestor")
        self.ytdlp_available = is_ytdlp_installed()

    def ingest_history(self, input_file: str = "inputs/youtube.txt"):
        if not self.ytdlp_available:
            log_info(
                self.log_path,
                "yt-dlp not found in PATH. Pytube fallback downloads will not be available.",
            )
        if not os.path.exists(input_file):
            log_error(self.log_path, f"YouTube input file not found: {input_file}")
            return
        with open(input_file, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
        for url in urls:
            self.ingest_single_video(url)
        log_info(self.log_path, "YouTube ingestion complete.")

    def ingest_single_video(self, url: str) -> bool:
        try:
            # Accept both raw video IDs and URLs
            if url.startswith("http"):
                video_id = extract_video_id(url)
                full_url = url
            else:
                video_id = url
                full_url = f"https://www.youtube.com/watch?v={video_id}"
            file_id = link_uid(full_url)
            
            # Initialize YouTube object for metadata extraction
            yt = YouTube(full_url)
            
            # COMPREHENSIVE METADATA EXTRACTION - Never lose any data!
            comprehensive_metadata = self._extract_all_youtube_metadata(yt, video_id, full_url)
            
            meta = self.create_metadata(
                source=full_url, 
                title=yt.title,
                type_specific=comprehensive_metadata["type_specific"]
            )
            meta.uid = file_id
            
            # Save raw YouTube API response for complete preservation
            self.save_raw_data(comprehensive_metadata["raw_youtube_data"], meta, "youtube_api")

            paths = self.path_manager.get_path_set(self.content_type, file_id)
            transcript_path = paths.get_path("transcript")
            meta_path = paths.get_path("metadata")
            if not video_id:
                meta["status"] = "error"
                meta["error"] = "Could not extract video ID"
                log_error(self.log_path, f"Could not extract video ID from {url}")
                with open(meta_path, "w", encoding="utf-8") as mf:
                    json.dump(meta, mf, indent=2)
                return False
            yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
            title = yt.title
            meta.title = title
            video_filename = f"{file_id}.mp4"
            video_path = self.path_manager.get_single_path(
                self.content_type, file_id, "video"
            )
            if not os.path.exists(video_path):
                log_info(self.log_path, f"Downloading: {title}")
                yt.streams.filter(progressive=True, file_extension="mp4").order_by(
                    "resolution"
                ).desc().first().download(
                    output_path=os.path.dirname(video_path), filename=video_filename
                )
                meta.status = "success"
            else:
                meta.status = "already_downloaded"
                # Fetch transcript if available
            try:
                log_info(self.log_path, f"Fetching transcript for: {title}")
                transcript = YouTubeTranscriptApi.get_transcript(video_id)
                transcript_text = "\n".join([x["text"] for x in transcript])
                with open(transcript_path, "w", encoding="utf-8") as tf:
                    tf.write(transcript_text)
                meta.transcript_path = transcript_path
                # Generate Markdown file first
                md_path = self.path_manager.get_single_path(
                    self.content_type, file_id, "markdown"
                )
                md = generate_markdown_summary(
                    title=title,
                    source=full_url,
                    date=meta.date,
                    tags=[],
                    notes=[],
                    content=transcript_text,
                )
                with open(md_path, "w", encoding="utf-8") as mdf:
                    mdf.write(md)
                meta.content_path = md_path
                # --- Run Evaluations ---
                if transcript_text:
                    self.run_evaluations(transcript_text, meta)
            except (TranscriptsDisabled, NoTranscriptFound):
                meta.transcript_path = None
                log_error(self.log_path, f"No transcript available for {title}")
            except Exception as e:
                self.handle_error(
                    f"Transcript fetch failed for {title}: {e}", source=full_url
                )
                meta.transcript_error = str(e)

        except Exception as e:
            self.handle_error(
                f"Error downloading {url}: {e}", source=full_url, should_retry=True
            )
            meta.set_error(str(e))
            if self.ytdlp_available:
                log_info(self.log_path, f"Trying yt-dlp fallback for {full_url}...")
                video_path = self.path_manager.get_single_path(
                    self.content_type, file_id, "video"
                )
                ytdlp_cmd = [
                    "yt-dlp",
                    f"https://www.youtube.com/watch?v={video_id}",
                    "-f",
                    "best[ext=mp4]",
                    "-o",
                    video_path,
                ]
                try:
                    result = subprocess.run(
                        ytdlp_cmd, capture_output=True, text=True, check=True
                    )
                    log_info(self.log_path, f"yt-dlp download succeeded for {video_id}")
                    meta.status = "success"
                    meta.type_specific["ytdlp_fallback"] = True
                    meta.type_specific["ytdlp_stdout"] = result.stdout
                    meta.type_specific["ytdlp_stderr"] = result.stderr
                except Exception as ytdlp_e:
                    self.handle_error(
                        f"yt-dlp download failed for {video_id}: {ytdlp_e}",
                        source=full_url,
                        should_retry=True,
                    )
                    meta.set_error(f"yt-dlp failed: {ytdlp_e}")
            else:
                log_error(
                    self.log_path,
                    f"Skipping yt-dlp fallback for {full_url} because it is not installed.",
                )
        finally:
            if meta_path:
                self.save_metadata(meta)
        return True
    
    def _extract_all_youtube_metadata(self, yt: YouTube, video_id: str, full_url: str) -> Dict[str, Any]:
        """
        Extract ALL available metadata from YouTube video.
        CORE PRINCIPLE: Never lose any data - capture everything!
        """
        
        # Raw YouTube object data preservation
        raw_youtube_data = {}
        try:
            # Extract all available pytube metadata
            raw_youtube_data = {
                "video_id": video_id,
                "title": getattr(yt, 'title', None),
                "description": getattr(yt, 'description', None),
                "length": getattr(yt, 'length', None),
                "views": getattr(yt, 'views', None),
                "rating": getattr(yt, 'rating', None),
                "age_restricted": getattr(yt, 'age_restricted', None),
                "video_id": getattr(yt, 'video_id', None),
                "watch_url": getattr(yt, 'watch_url', None),
                "embed_url": getattr(yt, 'embed_url', None),
                "thumbnail_url": getattr(yt, 'thumbnail_url', None),
                "publish_date": str(getattr(yt, 'publish_date', None)),
                "keywords": getattr(yt, 'keywords', []),
                "channel_url": getattr(yt, 'channel_url', None),
                "metadata": getattr(yt, 'metadata', None),
            }
            
            # Author/Channel information
            if hasattr(yt, 'author'):
                raw_youtube_data["author"] = yt.author
            if hasattr(yt, 'channel_id'):
                raw_youtube_data["channel_id"] = yt.channel_id
                
            # Stream information - preserve ALL available stream data
            if hasattr(yt, 'streams'):
                raw_youtube_data["available_streams"] = []
                for stream in yt.streams:
                    stream_info = {
                        "itag": getattr(stream, 'itag', None),
                        "mime_type": getattr(stream, 'mime_type', None),
                        "resolution": getattr(stream, 'resolution', None),
                        "fps": getattr(stream, 'fps', None),
                        "video_codec": getattr(stream, 'video_codec', None),
                        "audio_codec": getattr(stream, 'audio_codec', None),
                        "progressive": getattr(stream, 'is_progressive', None),
                        "adaptive": getattr(stream, 'is_adaptive', None),
                        "includes_audio_track": getattr(stream, 'includes_audio_track', None),
                        "includes_video_track": getattr(stream, 'includes_video_track', None),
                        "filesize": getattr(stream, 'filesize', None),
                        "bitrate": getattr(stream, 'bitrate', None)
                    }
                    raw_youtube_data["available_streams"].append(stream_info)
            
        except Exception as e:
            raw_youtube_data["extraction_error"] = str(e)
        
        # Structured YouTube metadata
        youtube_data = {
            # Core video information
            "video_id": video_id,
            "url": full_url,
            "title": getattr(yt, 'title', None),
            "description": getattr(yt, 'description', None),
            "duration_seconds": getattr(yt, 'length', None),
            "view_count": getattr(yt, 'views', None),
            "rating": getattr(yt, 'rating', None),
            "age_restricted": getattr(yt, 'age_restricted', False),
            
            # Publication information
            "publish_date": str(getattr(yt, 'publish_date', None)),
            "upload_date": str(getattr(yt, 'publish_date', None)),  # Same as publish_date for YouTube
            
            # Channel/Author information
            "channel_name": getattr(yt, 'author', None),
            "channel_id": getattr(yt, 'channel_id', None),
            "channel_url": getattr(yt, 'channel_url', None),
            
            # Content metadata
            "keywords": getattr(yt, 'keywords', []),
            "tags": getattr(yt, 'keywords', []),  # YouTube keywords are effectively tags
            "language": None,  # Could be extracted from description or other means
            
            # Media URLs
            "watch_url": getattr(yt, 'watch_url', full_url),
            "embed_url": getattr(yt, 'embed_url', None),
            "thumbnail_url": getattr(yt, 'thumbnail_url', None),
            
            # Calculated metadata
            "duration_formatted": self._format_duration(getattr(yt, 'length', 0)),
            "estimated_reading_time": self._estimate_transcript_reading_time(getattr(yt, 'length', 0)),
            
            # Technical information
            "stream_count": len(getattr(yt, 'streams', [])),
            "has_video": any(getattr(s, 'includes_video_track', False) for s in getattr(yt, 'streams', [])),
            "has_audio": any(getattr(s, 'includes_audio_track', False) for s in getattr(yt, 'streams', [])),
            "max_resolution": self._get_max_resolution(yt),
            "available_formats": self._get_available_formats(yt)
        }
        
        # Transcript metadata (to be filled later)
        transcript_metadata = {
            "transcript_available": False,
            "transcript_languages": [],
            "transcript_auto_generated": False,
            "transcript_length": 0
        }
        
        return {
            "type_specific": {
                "youtube": youtube_data,
                "transcript": transcript_metadata,
                "technical": {
                    "pytube_version": "unknown",  # Could get from pytube.__version__ if available
                    "extraction_method": "pytube",
                    "extraction_timestamp": datetime.now().isoformat(),
                    "user_agent": "pytube_default"
                },
                "raw_youtube_data": raw_youtube_data,
                "original_url": full_url
            }
        }
    
    def _format_duration(self, seconds: int) -> str:
        """Format duration in seconds to HH:MM:SS"""
        if not seconds:
            return "00:00:00"
        
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        else:
            return f"{minutes:02d}:{secs:02d}"
    
    def _estimate_transcript_reading_time(self, duration_seconds: int) -> int:
        """Estimate reading time for transcript (assuming 150 words per minute of video)"""
        if not duration_seconds:
            return 0
        
        # Rough estimate: 150 words per minute of video content
        estimated_words = (duration_seconds / 60) * 150
        # Reading speed: 200 words per minute
        reading_time_minutes = max(1, int(estimated_words / 200))
        return reading_time_minutes
    
    def _get_max_resolution(self, yt: YouTube) -> Optional[str]:
        """Get the maximum available resolution"""
        if not hasattr(yt, 'streams'):
            return None
        
        max_res = 0
        max_res_str = None
        
        for stream in yt.streams:
            if hasattr(stream, 'resolution') and stream.resolution:
                try:
                    # Extract numeric part of resolution (e.g., "720p" -> 720)
                    res_num = int(stream.resolution.replace('p', ''))
                    if res_num > max_res:
                        max_res = res_num
                        max_res_str = stream.resolution
                except (ValueError, AttributeError):
                    continue
        
        return max_res_str
    
    def _get_available_formats(self, yt: YouTube) -> List[str]:
        """Get list of available video/audio formats"""
        if not hasattr(yt, 'streams'):
            return []
        
        formats = set()
        for stream in yt.streams:
            if hasattr(stream, 'mime_type') and stream.mime_type:
                formats.add(stream.mime_type)
        
        return sorted(list(formats))


def ingest_youtube_history(config: dict, input_file: str = "inputs/youtube.txt"):
    ingestor = YouTubeIngestor(config)
    ingestor.ingest_history(input_file)


def ingest_youtube_video(url: str, config: Dict) -> bool:
    ingestor = YouTubeIngestor(config)
    return ingestor.ingest_single_video(url)
