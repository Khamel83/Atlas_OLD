#!/usr/bin/env python3
"""
Podcast Transcript Lookup System

This module implements the exact workflow you described:
1. Check existing transcript sources (RSS feeds, database)
2. Try YouTube fallback for missing transcripts
3. Try Google search as final fallback
4. Schedule retries for failures

Integrates with Atlas scheduler and numeric stage system.
"""

import logging
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

from helpers.database_config import get_database_connection
from helpers.youtube_podcast_fallback import YouTubePodcastFallback
from helpers.content_transactions import TransactionTimer

logger = logging.getLogger(__name__)

@dataclass
class PodcastEpisode:
    """Podcast episode data structure"""
    podcast_name: str
    episode_title: str
    episode_url: str
    audio_url: Optional[str] = None
    publish_date: Optional[str] = None
    duration: Optional[str] = None
    existing_transcript: Optional[str] = None

@dataclass
class TranscriptLookupResult:
    """Result of transcript lookup operation"""
    success: bool
    podcast_name: str
    episode_title: str
    transcript: Optional[str] = None
    source: Optional[str] = None
    fallback_used: bool = False
    error_message: Optional[str] = None
    retry_scheduled: bool = False
    processing_time: Optional[float] = None

class PodcastTranscriptLookup:
    """Main transcript lookup system for Atlas"""

    def __init__(self):
        self.youtube_fallback = YouTubePodcastFallback()
        self.conn = get_database_connection()

    def lookup_transcript(self, podcast_name: str, episode_title: str,
                         episode_url: str = None) -> TranscriptLookupResult:
        """
        Main transcript lookup method - implements your described workflow

        Args:
            podcast_name (str): Name of the podcast
            episode_title (str): Title of the episode
            episode_url (str): URL of the episode (optional)

        Returns:
            TranscriptLookupResult: Complete lookup result
        """
        start_time = datetime.now()

        try:
            logger.info(f"Starting transcript lookup for {podcast_name} - {episode_title}")

                # Step 1: Check existing sources (RSS feeds, database)
            existing_result = self._check_existing_sources(podcast_name, episode_title, episode_url)

                if existing_result.success:
                    timer.add_tags({
                        'podcast_name': podcast_name,
                        'episode_title': episode_title,
                        'source': existing_result.source,
                        'success': True,
                        'fallback_used': False
                    })
                    return existing_result

                # Step 2: Try YouTube fallback
                logger.info(f"Trying YouTube fallback for {podcast_name} - {episode_title}")
                youtube_result = self._try_youtube_fallback(podcast_name, episode_title)

                if youtube_result.success:
                    timer.add_tags({
                        'podcast_name': podcast_name,
                        'episode_title': episode_title,
                        'source': 'youtube',
                        'success': True,
                        'fallback_used': True
                    })
                    return youtube_result

                # Step 3: Try Google search fallback
                logger.info(f"Trying Google search fallback for {podcast_name} - {episode_title}")
                google_result = self._try_google_search_fallback(podcast_name, episode_title)

                if google_result.success:
                    timer.add_tags({
                        'podcast_name': podcast_name,
                        'episode_title': episode_title,
                        'source': 'google_search',
                        'success': True,
                        'fallback_used': True
                    })
                    return google_result

                # Step 4: All methods failed - schedule retry
                logger.warning(f"All transcript lookup methods failed for {podcast_name} - {episode_title}")
                retry_scheduled = self._schedule_retry(podcast_name, episode_title, episode_url)

                processing_time = (datetime.now() - start_time).total_seconds()

                timer.add_tags({
                    'podcast_name': podcast_name,
                    'episode_title': episode_title,
                    'success': False,
                    'fallback_used': False,
                    'retry_scheduled': retry_scheduled
                })
                timer.mark_failed(error="All lookup methods failed")

                return TranscriptLookupResult(
                    success=False,
                    podcast_name=podcast_name,
                    episode_title=episode_title,
                    error_message="All transcript lookup methods failed",
                    retry_scheduled=retry_scheduled,
                    processing_time=processing_time
                )

            except Exception as e:
                logger.error(f"Transcript lookup failed for {podcast_name} - {episode_title}: {e}")
                processing_time = (datetime.now() - start_time).total_seconds()

                timer.mark_failed(error=str(e))

                return TranscriptLookupResult(
                    success=False,
                    podcast_name=podcast_name,
                    episode_title=episode_title,
                    error_message=str(e),
                    processing_time=processing_time
                )

    def _check_existing_sources(self, podcast_name: str, episode_title: str,
                               episode_url: str = None) -> TranscriptLookupResult:
        """Check existing transcript sources (RSS feeds, database)"""

        try:
            # Check database first
            cursor = self.conn.cursor()

            # Look for existing transcripts
            query = """
                SELECT transcript, source, metadata
                FROM podcast_transcripts
                WHERE podcast_name = ? AND episode_title = ?
                ORDER BY created_at DESC
                LIMIT 1
            """

            cursor.execute(query, (podcast_name, episode_title))
            result = cursor.fetchone()

            if result and result[0]:  # transcript exists
                transcript, source, metadata_json = result

                # Parse metadata
                metadata = json.loads(metadata_json) if metadata_json else {}

                logger.info(f"Found existing transcript for {podcast_name} - {episode_title} from {source}")

                return TranscriptLookupResult(
                    success=True,
                    podcast_name=podcast_name,
                    episode_title=episode_title,
                    transcript=transcript,
                    source=source,
                    fallback_used=False
                )

            # Check if we have RSS feed content that might contain transcript
            rss_result = self._check_rss_feed_content(podcast_name, episode_title, episode_url)
            if rss_result.success:
                return rss_result

            return TranscriptLookupResult(
                success=False,
                podcast_name=podcast_name,
                episode_title=episode_title,
                error_message="No existing transcript found"
            )

        except Exception as e:
            logger.error(f"Failed to check existing sources: {e}")
            return TranscriptLookupResult(
                success=False,
                podcast_name=podcast_name,
                episode_title=episode_title,
                error_message=f"Database error: {str(e)}"
            )

    def _check_rss_feed_content(self, podcast_name: str, episode_title: str,
                              episode_url: str = None) -> TranscriptLookupResult:
        """Check RSS feed content for transcript"""

        try:
            # Look for RSS feed entries that might contain transcript data
            cursor = self.conn.cursor()

            query = """
                SELECT content, description, metadata
                FROM content
                WHERE content_type = 'podcast_episode'
                AND (title LIKE ? OR url = ?)
                LIMIT 1
            """

            search_title = f"%{episode_title}%"
            cursor.execute(query, (search_title, episode_url or ""))
            result = cursor.fetchone()

            if result:
                content, description, metadata_json = result

                # Combine content and description as potential transcript
                combined_text = f"{content or ''}\n\n{description or ''}".strip()

                if len(combined_text) > 100:  # Reasonable length for transcript
                    logger.info(f"Found RSS content for {podcast_name} - {episode_title}")

                    return TranscriptLookupResult(
                        success=True,
                        podcast_name=podcast_name,
                        episode_title=episode_title,
                        transcript=combined_text,
                        source="rss_feed",
                        fallback_used=False
                    )

            return TranscriptLookupResult(
                success=False,
                podcast_name=podcast_name,
                episode_title=episode_title,
                error_message="No RSS transcript found"
            )

        except Exception as e:
            logger.error(f"Failed to check RSS feed content: {e}")
            return TranscriptLookupResult(
                success=False,
                podcast_name=podcast_name,
                episode_title=episode_title,
                error_message=f"RSS check error: {str(e)}"
            )

    def _try_youtube_fallback(self, podcast_name: str, episode_title: str) -> TranscriptLookupResult:
        """Try YouTube as fallback source"""

        if not self.youtube_fallback.enabled:
            return TranscriptLookupResult(
                success=False,
                podcast_name=podcast_name,
                episode_title=episode_title,
                error_message="YouTube fallback not enabled"
            )

        try:
            # Use YouTube API to find and extract transcript
            result = self.youtube_fallback.get_podcast_transcript_fallback(podcast_name, episode_title)

            if result['success']:
                transcript = result.get('transcript')
                video_url = result.get('url')

                # Store the successful transcript
                self._store_transcript(podcast_name, episode_title, transcript, 'youtube', video_url)

                return TranscriptLookupResult(
                    success=True,
                    podcast_name=podcast_name,
                    episode_title=episode_title,
                    transcript=transcript,
                    source='youtube',
                    fallback_used=True
                )
            else:
                return TranscriptLookupResult(
                    success=False,
                    podcast_name=podcast_name,
                    episode_title=episode_title,
                    error_message=f"YouTube fallback failed: {result.get('error', 'Unknown error')}"
                )

        except Exception as e:
            logger.error(f"YouTube fallback failed: {e}")
            return TranscriptLookupResult(
                success=False,
                podcast_name=podcast_name,
                episode_title=episode_title,
                error_message=f"YouTube error: {str(e)}"
            )

    def _try_google_search_fallback(self, podcast_name: str, episode_title: str) -> TranscriptLookupResult:
        """Try Google search as final fallback"""

        try:
            # For now, implement a simple version
            # In the future, this could use the Google Search API

            search_query = f"{podcast_name} {episode_title} transcript"

            # TODO: Implement Google Search API integration
            # For now, return failure

            return TranscriptLookupResult(
                success=False,
                podcast_name=podcast_name,
                episode_title=episode_title,
                error_message="Google search fallback not yet implemented"
            )

        except Exception as e:
            logger.error(f"Google search fallback failed: {e}")
            return TranscriptLookupResult(
                success=False,
                podcast_name=podcast_name,
                episode_title=episode_title,
                error_message=f"Google search error: {str(e)}"
            )

    def _store_transcript(self, podcast_name: str, episode_title: str, transcript: str,
                          source: str, source_url: str = None):
        """Store successful transcript in database"""

        try:
            cursor = self.conn.cursor()

            # Create transcript table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS podcast_transcripts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    podcast_name TEXT NOT NULL,
                    episode_title TEXT NOT NULL,
                    transcript TEXT NOT NULL,
                    source TEXT NOT NULL,
                    source_url TEXT,
                    metadata TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    UNIQUE(podcast_name, episode_title, source)
                )
            """)

            # Prepare metadata
            metadata = {
                'source_url': source_url,
                'transcript_length': len(transcript),
                'word_count': len(transcript.split())
            }

            # Store transcript
            cursor.execute("""
                INSERT OR REPLACE INTO podcast_transcripts
                (podcast_name, episode_title, transcript, source, source_url, metadata, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                podcast_name,
                episode_title,
                transcript,
                source,
                source_url,
                json.dumps(metadata),
                datetime.now().isoformat(),
                datetime.now().isoformat()
            ))

            self.conn.commit()
            logger.info(f"Stored transcript for {podcast_name} - {episode_title} from {source}")

        except Exception as e:
            logger.error(f"Failed to store transcript: {e}")
            self.conn.rollback()

    def _schedule_retry(self, podcast_name: str, episode_title: str, episode_url: str = None) -> bool:
        """Schedule retry for failed transcript lookup"""

        try:
            cursor = self.conn.cursor()

            # Create retry table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transcript_lookup_retries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    podcast_name TEXT NOT NULL,
                    episode_title TEXT NOT NULL,
                    episode_url TEXT,
                    retry_count INTEGER DEFAULT 0,
                    next_retry_at TEXT NOT NULL,
                    last_attempt TEXT,
                    created_at TEXT NOT NULL
                )
            """)

            # Check if already scheduled
            cursor.execute("""
                SELECT COUNT(*) FROM transcript_lookup_retries
                WHERE podcast_name = ? AND episode_title = ?
                AND retry_count < 3
            """, (podcast_name, episode_title))

            if cursor.fetchone()[0] > 0:
                logger.info(f"Retry already scheduled for {podcast_name} - {episode_title}")
                return True

            # Schedule new retry
            next_retry = datetime.now() + timedelta(hours=24)  # Retry tomorrow

            cursor.execute("""
                INSERT INTO transcript_lookup_retries
                (podcast_name, episode_title, episode_url, retry_count, next_retry_at, last_attempt, created_at)
                VALUES (?, ?, ?, 0, ?, ?, ?)
            """, (
                podcast_name,
                episode_title,
                episode_url,
                next_retry.isoformat(),
                datetime.now().isoformat(),
                datetime.now().isoformat()
            ))

            self.conn.commit()
            logger.info(f"Scheduled retry for {podcast_name} - {episode_title}")
            return True

        except Exception as e:
            logger.error(f"Failed to schedule retry: {e}")
            self.conn.rollback()
            return False

    def process_pending_retries(self) -> Dict[str, Any]:
        """Process pending retry attempts"""

        try:
            cursor = self.conn.cursor()

            # Get retries that are due
            now = datetime.now().isoformat()
            cursor.execute("""
                SELECT podcast_name, episode_title, episode_url, retry_count
                FROM transcript_lookup_retries
                WHERE next_retry_at <= ? AND retry_count < 3
                ORDER BY next_retry_at ASC
                LIMIT 10
            """, (now,))

            pending_retries = cursor.fetchall()

            results = {
                'total_processed': 0,
                'successful': 0,
                'failed': 0,
                'details': []
            }

            for podcast_name, episode_title, episode_url, retry_count in pending_retries:
                logger.info(f"Processing retry {retry_count + 1} for {podcast_name} - {episode_title}")

                # Attempt lookup again
                result = self.lookup_transcript(podcast_name, episode_title, episode_url)

                if result.success:
                    # Remove from retry queue
                    cursor.execute("""
                        DELETE FROM transcript_lookup_retries
                        WHERE podcast_name = ? AND episode_title = ?
                    """, (podcast_name, episode_title))

                    results['successful'] += 1
                else:
                    # Update retry count and schedule next retry
                    next_retry = datetime.now() + timedelta(hours=24 * (retry_count + 2))
                    cursor.execute("""
                        UPDATE transcript_lookup_retries
                        SET retry_count = ?, next_retry_at = ?, last_attempt = ?
                        WHERE podcast_name = ? AND episode_title = ?
                    """, (retry_count + 1, next_retry.isoformat(), now, podcast_name, episode_title))

                    results['failed'] += 1

                results['total_processed'] += 1
                results['details'].append({
                    'podcast_name': podcast_name,
                    'episode_title': episode_title,
                    'success': result.success,
                    'source': result.source if result.success else None,
                    'error': result.error_message if not result.success else None
                })

            self.conn.commit()

            logger.info(f"Processed {results['total_processed']} retries: {results['successful']} successful, {results['failed']} failed")
            return results

        except Exception as e:
            logger.error(f"Failed to process retries: {e}")
            return {'total_processed': 0, 'successful': 0, 'failed': 0, 'error': str(e)}

    def get_lookup_statistics(self) -> Dict[str, Any]:
        """Get statistics about transcript lookup operations"""

        try:
            cursor = self.conn.cursor()

            # Get total podcasts in system
            cursor.execute("SELECT COUNT(DISTINCT podcast_name) FROM content WHERE content_type = 'podcast_episode'")
            total_podcasts = cursor.fetchone()[0] or 0

            # Get transcripts by source
            cursor.execute("""
                SELECT source, COUNT(*) as count
                FROM podcast_transcripts
                GROUP BY source
                ORDER BY count DESC
            """)
            transcripts_by_source = dict(cursor.fetchall())

            # Get pending retries
            cursor.execute("SELECT COUNT(*) FROM transcript_lookup_retries WHERE retry_count < 3")
            pending_retries = cursor.fetchone()[0] or 0

            return {
                'total_podcasts': total_podcasts,
                'transcripts_by_source': transcripts_by_source,
                'total_transcripts': sum(transcripts_by_source.values()),
                'pending_retries': pending_retries,
                'youtube_enabled': self.youtube_fallback.enabled
            }

        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
            return {'error': str(e)}

# Global instance for Atlas scheduler use
podcast_transcript_lookup = PodcastTranscriptLookup()

def lookup_podcast_transcript(podcast_name: str, episode_title: str, episode_url: str = None) -> TranscriptLookupResult:
    """Convenience function for Atlas integration"""
    return podcast_transcript_lookup.lookup_transcript(podcast_name, episode_title, episode_url)

def process_transcript_retries() -> Dict[str, Any]:
    """Convenience function for processing retries"""
    return podcast_transcript_lookup.process_pending_retries()

if __name__ == "__main__":
    # Test the podcast transcript lookup system
    print("🎙️ Podcast Transcript Lookup System Test")
    print("=" * 50)

    lookup = PodcastTranscriptLookup()

    # Test statistics
    stats = lookup.get_lookup_statistics()
    print(f"\n📊 System Statistics:")
    print(f"Total podcasts: {stats.get('total_podcasts', 0)}")
    print(f"Total transcripts: {stats.get('total_transcripts', 0)}")
    print(f"Transcripts by source: {stats.get('transcripts_by_source', {})}")
    print(f"Pending retries: {stats.get('pending_retries', 0)}")
    print(f"YouTube enabled: {stats.get('youtube_enabled', False)}")

    # Test lookup for a known podcast
    print(f"\n🔍 Testing transcript lookup...")
    test_result = lookup.lookup_transcript("Huberman Lab", "sleep")

    print(f"\n📋 Test Result:")
    print(f"Success: {test_result.success}")
    print(f"Source: {test_result.source}")
    print(f"Transcript length: {len(test_result.transcript) if test_result.transcript else 0}")
    print(f"Fallback used: {test_result.fallback_used}")
    print(f"Error: {test_result.error_message}")

    # Show integration info
    print(f"\n🔄 Atlas Integration:")
    print("This system integrates with Atlas scheduler:")
    print("- Call lookup_podcast_transcript() from stage 320")
    print("- Call process_transcript_retries() from daily scheduler")
    print("- All results tracked in transaction system")
    print("- YouTube fallback automatically attempted")