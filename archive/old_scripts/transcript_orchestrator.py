#!/usr/bin/env python3
"""
Transcript Discovery Orchestrator

Main controller that tries all transcript sources in optimal order.
This is the unified entry point for finding transcripts from any podcast episode.
"""

import sqlite3
import time
import json
import re
import hashlib
from datetime import datetime, timedelta
from typing import Optional, Dict, Tuple

# Import all the transcript finding methods
try:
    from rss_transcript_extractor import extract_rss_transcripts, RSSTranscriptExtractor
except ImportError:
    extract_rss_transcripts = None
    
try:
    from transcript_google_search import google_search_transcript
except ImportError:
    google_search_transcript = None
    
try:
    from archive_transcript_search import search_archive_transcripts
except ImportError:
    search_archive_transcripts = None
    
try:
    from fixed_transcript_finder import RealTranscriptFinder
except ImportError:
    RealTranscriptFinder = None

try:
    from extract_metadata import extract_episode_metadata
except ImportError:
    extract_episode_metadata = None

try:
    from helpers.mac_mini_client import MacMiniClient
except ImportError:
    MacMiniClient = None

class TranscriptOrchestrator:
    def __init__(self, db_path="~/dev/atlas/atlas.db"):
        self.db_path = db_path.replace("~", "/home/ubuntu")
        
        # Initialize individual finders
        if RealTranscriptFinder:
            self.pattern_finder = RealTranscriptFinder()
        else:
            self.pattern_finder = None
        
        if extract_rss_transcripts:
            self.rss_extractor = RSSTranscriptExtractor()
        else:
            self.rss_extractor = None
        
        # Known RSS feeds for direct extraction
        self.known_rss_feeds = {
            'Lex Fridman': 'https://lexfridman.com/feed/podcast/',
            'This American Life': 'https://www.thisamericanlife.org/podcast/rss.xml',
            'Fresh Air': 'https://feeds.npr.org/381444908/podcast.xml',
            'RadioLab': 'https://feeds.wnyc.org/radiolab',
            'Hard Fork': 'https://rss.art19.com/the-ezra-klein-show'  # NYT shows often share feeds
        }
        
        # Mac Mini client for audio transcription fallback
        self.mac_mini_client = MacMiniClient() if MacMiniClient else None
        self.mac_mini_enabled = True  # Can be configured via .env
        
    def generate_cache_key(self, podcast_name: str, episode_title: str) -> str:
        """Generate a cache key for episode"""
        combined = f"{podcast_name}:{episode_title}".lower()
        return hashlib.md5(combined.encode()).hexdigest()
    
    def check_cache(self, podcast_name: str, episode_title: str) -> Optional[str]:
        """Check if we already have a transcript for this episode"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Look for existing transcript in content table
                cursor = conn.execute("""
                    SELECT content FROM content 
                    WHERE content_type = 'podcast_transcript' 
                    AND title LIKE ? 
                    ORDER BY created_at DESC 
                    LIMIT 1
                """, (f"%{episode_title}%",))
                
                result = cursor.fetchone()
                if result:
                    print(f"    ✅ Found cached transcript for {episode_title[:50]}...")
                    return result[0]
        except Exception as e:
            print(f"    ⚠️ Cache check failed: {e}")
        
        return None
    
    def record_attempt(self, podcast_name: str, episode_title: str, method: str, 
                      success: bool, error: str = None):
        """Record transcript discovery attempt in database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                # Update or insert into transcript_patterns table
                if success:
                    # Update success rate for this method
                    conn.execute("""
                        INSERT OR REPLACE INTO transcript_patterns 
                        (pattern_name, url_pattern, success_rate)
                        VALUES (?, ?, 
                            COALESCE((SELECT success_rate FROM transcript_patterns WHERE pattern_name = ?), 0) + 0.1
                        )
                    """, (method, f"{method}_pattern", method))
                else:
                    # Record failure but don't penalize success rate too heavily
                    conn.execute("""
                        INSERT OR IGNORE INTO transcript_patterns 
                        (pattern_name, url_pattern, success_rate)
                        VALUES (?, ?, 0.0)
                    """, (method, f"{method}_pattern"))
        except Exception as e:
            print(f"    ⚠️ Could not record attempt: {e}")
    
    def try_rss_extraction(self, podcast_name: str, episode_title: str) -> Tuple[Optional[str], Optional[str]]:
        """Try RSS feed extraction if we have a known RSS feed"""
        if not self.rss_extractor:
            print("DEBUG: Returning (None, None) because rss_extractor is None")
            return None, None
            
        # Check if we have a known RSS feed for this podcast
        rss_url = None
        for known_podcast, known_rss in self.known_rss_feeds.items():
            if known_podcast.lower() in podcast_name.lower():
                rss_url = known_rss
                break
        
        if not rss_url:
            print("DEBUG: Returning (None, None) because rss_url is None")
            return None, None
        
        try:
            print(f"    📡 Trying RSS extraction from {rss_url}...")
            all_episodes, episodes_with_transcripts = self.rss_extractor.extract_rss_transcripts(rss_url)
            
            # Find matching episode and return transcript if found
            for episode_data in episodes_with_transcripts:
                if self.episode_matches(episode_title, episode_data.get('title', '')):
                    transcript_text = episode_data.get('transcript', '')
                    if transcript_text:
                        print(f"    ✅ Found RSS transcript ({len(transcript_text)} chars)")
                        self.record_attempt(podcast_name, episode_title, 'rss_extraction', True)
                        return transcript_text, episode_data.get('title')
                        
            # No matching episode with transcript found
            print(f"    ❌ No matching episode found in RSS feed")
            self.record_attempt(podcast_name, episode_title, 'rss_extraction', False, "No matching episode")
            return None, None
            
        except Exception as e:
            print(f"    ❌ RSS extraction error: {e}")
            self.record_attempt(podcast_name, episode_title, 'rss_extraction', False, str(e))
            return None, None
    
    def try_pattern_matching(self, podcast_name: str, episode_title: str) -> Optional[str]:
        """Try known website patterns (Lex Fridman, This American Life, etc.)"""
        if not self.pattern_finder:
            return None
        
        try:
            print(f"    🎯 Trying pattern matching...")
            
            # Use the existing pattern finder logic
            transcript = None
            
            if "EconTalk" in podcast_name:
                transcript = self.pattern_finder.try_econtalk_transcript(episode_title)
            elif "Hard Fork" in podcast_name or "Ezra Klein" in podcast_name:
                transcript = self.pattern_finder.try_nytimes_transcript(episode_title)
            elif "This American Life" in podcast_name:
                transcript = self.pattern_finder.try_this_american_life_transcript(episode_title)
            elif "Lex Fridman" in podcast_name:
                transcript = self.pattern_finder.try_lex_fridman_transcript(episode_title)
            elif "Acquired" in podcast_name:
                transcript = self.pattern_finder.try_acquired_transcript(episode_title)
            
            if transcript:
                self.record_attempt(podcast_name, episode_title, 'pattern_matching', True)
                return transcript
            else:
                self.record_attempt(podcast_name, episode_title, 'pattern_matching', False)
                return None
                
        except Exception as e:
            print(f"    ❌ Pattern matching error: {e}")
            self.record_attempt(podcast_name, episode_title, 'pattern_matching', False, str(e))
            return None
    
    def try_google_search(self, podcast_name: str, episode_title: str) -> Optional[str]:
        """Try Google search fallback"""
        if not google_search_transcript:
            return None
        
        try:
            print(f"    🔍 Trying Google search...")
            transcript = google_search_transcript(podcast_name, episode_title)
            
            if transcript:
                self.record_attempt(podcast_name, episode_title, 'google_search', True)
                return transcript
            else:
                self.record_attempt(podcast_name, episode_title, 'google_search', False)
                return None
                
        except Exception as e:
            print(f"    ❌ Google search error: {e}")
            self.record_attempt(podcast_name, episode_title, 'google_search', False, str(e))
            return None
    
    def try_archive_search(self, podcast_name: str, episode_title: str) -> Optional[str]:
        """Try Internet Archive search"""
        if not search_archive_transcripts:
            return None
        
        try:
            print(f"    🏛️ Trying Internet Archive...")
            transcript = search_archive_transcripts(podcast_name, episode_title)
            
            if transcript:
                self.record_attempt(podcast_name, episode_title, 'archive_search', True)
                return transcript
            else:
                self.record_attempt(podcast_name, episode_title, 'archive_search', False)
                return None
                
        except Exception as e:
            print(f"    ❌ Archive search error: {e}")
            self.record_attempt(podcast_name, episode_title, 'archive_search', False, str(e))
            return None
    
    def try_nytimes_handler(self, podcast_name: str, episode_title: str, episode_url: Optional[str] = None) -> Optional[str]:
        """Handle NYTimes podcasts with 403 errors using specialized handler"""
        try:
            # Import the specialized handler
            from nytimes_transcript_handler import handle_403_error
            
            print(f"    🔧 Trying NYTimes 403 handler...")
            transcript = handle_403_error(podcast_name, episode_title, episode_url)
            
            if transcript:
                self.record_attempt(podcast_name, episode_title, "nytimes_handler", "success", transcript[:100])
                print(f"    ✅ NYTimes handler found transcript ({len(transcript)} chars)")
                return transcript
            else:
                self.record_attempt(podcast_name, episode_title, "nytimes_handler", "not_found", "")
                print(f"    ❌ NYTimes handler: transcript unavailable (marked in database)")
                
        except ImportError as e:
            print(f"    ⚠️ NYTimes handler not available: {e}")
        except Exception as e:
            print(f"    ❌ Error in NYTimes handler: {e}")
            self.record_attempt(podcast_name, episode_title, "nytimes_handler", "error", str(e))
            
        return None
    
    def try_mac_mini_transcription(self, podcast_name: str, episode_title: str, 
                                   audio_url: Optional[str] = None) -> Optional[str]:
        """Try Mac Mini audio transcription as final fallback"""
        if not self.mac_mini_client or not self.mac_mini_enabled or not audio_url:
            return None
        
        try:
            print(f"    🖥️ Trying Mac Mini transcription...")
            
            # Test Mac Mini connection first
            if not self.mac_mini_client.test_connection():
                print(f"    ⚠️ Mac Mini not available, skipping")
                self.record_attempt(podcast_name, episode_title, 'mac_mini_transcription', False, "Mac Mini not available")
                return None
            
            # Submit transcription task with timeout (10 minutes max)
            result = self.mac_mini_client.transcribe_audio(audio_url, quality="base", timeout=600)
            
            if result and result.get('success'):
                transcript = result.get('transcript', '')
                if transcript and len(transcript.strip()) > 100:  # Basic quality check
                    print(f"    ✅ Mac Mini transcription successful ({len(transcript)} chars)")
                    self.record_attempt(podcast_name, episode_title, 'mac_mini_transcription', True)
                    return transcript
                else:
                    print(f"    ❌ Mac Mini returned poor quality transcript")
                    self.record_attempt(podcast_name, episode_title, 'mac_mini_transcription', False, "Poor quality transcript")
                    return None
            else:
                error_msg = result.get('error', 'Unknown error') if result else 'No result returned'
                print(f"    ❌ Mac Mini transcription failed: {error_msg}")
                self.record_attempt(podcast_name, episode_title, 'mac_mini_transcription', False, error_msg)
                return None
                
        except Exception as e:
            print(f"    ❌ Mac Mini transcription error: {e}")
            self.record_attempt(podcast_name, episode_title, 'mac_mini_transcription', False, str(e))
            return None
    
    def episode_matches(self, episode_title1: str, episode_title2: str) -> bool:
        """Check if two episode titles match (fuzzy matching)"""
        # Simple fuzzy matching - check if key words match
        title1_words = set(re.findall(r'\w+', episode_title1.lower()))
        title2_words = set(re.findall(r'\w+', episode_title2.lower()))
        
        # Remove common words
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'episode', 'podcast'}
        title1_words -= common_words
        title2_words -= common_words
        
        if len(title1_words) == 0 or len(title2_words) == 0:
            return False
        
        # Calculate overlap
        overlap = len(title1_words & title2_words)
        total_unique = len(title1_words | title2_words)
        
        similarity = overlap / total_unique if total_unique > 0 else 0
        return similarity > 0.5  # 50% similarity threshold
    
    def store_transcript(self, podcast_name: str, episode_title: str, transcript: str, 
                        episode_url: Optional[str] = None):
        """Store discovered transcript in Atlas database"""
        try:
            # Extract metadata if possible
            metadata_json = None
            if extract_episode_metadata and episode_url:
                try:
                    metadata = extract_episode_metadata(episode_url, transcript)
                    metadata_json = json.dumps(metadata)
                except:
                    pass
            
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    INSERT OR REPLACE INTO content 
                    (title, content, content_type, url, metadata, created_at)
                    VALUES (?, ?, 'podcast_transcript', ?, ?, CURRENT_TIMESTAMP)
                """, (f"[TRANSCRIPT] {episode_title}", transcript, episode_url, metadata_json))
                
                print(f"    💾 Stored transcript in Atlas database")
                
        except Exception as e:
            print(f"    ⚠️ Could not store transcript: {e}")
    
    def find_transcript(self, podcast_name: str, episode_title: str, 
                       episode_url: Optional[str] = None) -> Optional[str]:
        """
        Main function to find transcript using all available methods
        
        Tries methods in optimal order:
        1. Cache check (fastest)
        2. RSS embedded links (most reliable)
        3. Known website patterns (fast and reliable)
        4. Google search (universal but blocked)
        5. Internet Archive (slow but comprehensive)
        6. NYTimes special handler (for 403 errors)
        7. Mac Mini audio transcription (final fallback)
        """
        
        print(f"🎙️ Finding transcript: {podcast_name} - {episode_title[:60]}...")
        
        # Method 1: Check cache first
        cached_transcript = self.check_cache(podcast_name, episode_title)
        if cached_transcript:
            return cached_transcript
        
        # Method 2: Try RSS extraction (most reliable if available)
        transcript, rss_episode_title = self.try_rss_extraction(podcast_name, episode_title)
        if transcript:
            self.store_transcript(podcast_name, rss_episode_title, transcript, episode_url)
            return transcript
        
        # Use the RSS-derived title for pattern matching if available, otherwise use original
        title_for_pattern_matching = rss_episode_title if rss_episode_title else episode_title

        # Method 3: Try known website patterns (fast and reliable)
        transcript = self.try_pattern_matching(podcast_name, title_for_pattern_matching)
        if transcript:
            self.store_transcript(podcast_name, episode_title, transcript, episode_url)
            return transcript
        
        # Method 4: Try Google search (universal but often blocked)
        transcript = self.try_google_search(podcast_name, episode_title)
        if transcript:
            self.store_transcript(podcast_name, episode_title, transcript, episode_url)
            return transcript
        
        # Method 5: Try Internet Archive (comprehensive but slow)
        transcript = self.try_archive_search(podcast_name, episode_title)
        if transcript:
            self.store_transcript(podcast_name, episode_title, transcript, episode_url)
            return transcript
        
        # Method 6: Handle 403 errors and NYTimes podcasts specially
        if any(nyt_podcast in podcast_name.lower() for nyt_podcast in ['hard fork', 'ezra klein', 'the daily', 'nytimes']):
            transcript = self.try_nytimes_handler(podcast_name, episode_title, episode_url)
            if transcript:
                self.store_transcript(podcast_name, episode_title, transcript, episode_url)
                return transcript
        
        # Method 7: Mac Mini audio transcription (final fallback)
        if episode_url:
            transcript = self.try_mac_mini_transcription(podcast_name, episode_title, episode_url)
            if transcript:
                # Store with Mac Mini attribution
                title_with_source = f"[TRANSCRIPT - Mac Mini] {episode_title}"
                self.store_transcript(podcast_name, title_with_source, transcript, episode_url)
                return transcript
        
        print(f"    ❌ No transcript found after trying all methods (including Mac Mini)")
        return None

# Module-level function for easy import
def find_transcript(podcast_name: str, episode_title: str, episode_url: Optional[str] = None) -> Optional[str]:
    """Find transcript using all available methods - main entry point"""
    orchestrator = TranscriptOrchestrator()
    return orchestrator.find_transcript(podcast_name, episode_title, episode_url)

if __name__ == "__main__":
    # Test with known working examples
    test_cases = [
        ("Lex Fridman Podcast", "#480 Dave Hone"),
        ("This American Life", "Episode 233: Starting From Scratch"),
        ("EconTalk", "Interview with economist"),
    ]
    
    for podcast_name, episode_title in test_cases:
        print(f"\n{'='*80}")
        print(f"Testing: {podcast_name} - {episode_title}")
        print('='*80)
        
        result = find_transcript(podcast_name, episode_title)
        
        if result:
            print(f"\n✅ SUCCESS! Found transcript: {len(result)} characters")
            print(f"First 200 chars: {result[:200]}...")
        else:
            print(f"\n❌ FAILED - No transcript found")
        
        print(f"\n{'='*80}")
        time.sleep(2)  # Rate limiting between tests