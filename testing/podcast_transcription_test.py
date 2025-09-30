#!/usr/bin/env python3
"""
Podcast Transcription Testing Suite

Fast podcast ingestion testing using whisper_tiny model.
Optimized for concept search and idea discovery on OCI infrastructure.
"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import xml.etree.ElementTree as ET
import statistics

from helpers.config import load_config
from helpers.enhanced_transcription import EnhancedTranscriptionEngine, WhisperModel
from helpers.utils import log_info, log_error
import feedparser


class PodcastTranscriptionTester:
    """Test podcast ingestion with whisper_tiny for fast concept extraction"""

    def __init__(self, opml_path: str = "inputs/podcasts.opml"):
        self.config = load_config()
        self.opml_path = opml_path
        self.test_dir = Path("testing/podcast_tests")
        self.test_dir.mkdir(parents=True, exist_ok=True)

        self.log_path = self.test_dir / "podcast_transcription.log"

        # Test results storage
        self.test_results = {
            "timestamp": datetime.now().isoformat(),
            "opml_file": opml_path,
            "feeds_tested": [],
            "transcription_comparison": {},
            "performance_analysis": {},
            "search_quality_analysis": {},
            "recommendations": {}
        }

        # Initialize transcription engine
        self.transcription_engine = EnhancedTranscriptionEngine(self.config)

    def run_comprehensive_podcast_test(self) -> Dict[str, Any]:
        """Run fast podcast transcription testing with whisper_tiny"""
        log_info(str(self.log_path), "Starting fast podcast transcription testing (whisper_tiny only)")

        # Parse OPML and get feeds
        feeds = self._parse_opml_feeds()
        if not feeds:
            log_error(str(self.log_path), "No feeds found in OPML file")
            return self.test_results

        log_info(str(self.log_path), f"Found {len(feeds)} podcast feeds")

        # Test each feed with limited episodes
        for feed_url, feed_title in feeds[:3]:  # Limit to first 3 feeds for testing
            log_info(str(self.log_path), f"Testing feed: {feed_title}")

            feed_results = self._test_podcast_feed(feed_url, feed_title)
            self.test_results["feeds_tested"].append(feed_results)

        # Analyze transcription performance across all tests
        self._analyze_transcription_performance()

        # Generate recommendations
        self._generate_recommendations()

        # Save results
        results_file = self.test_dir / f"podcast_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w') as f:
            json.dump(self.test_results, f, indent=2)

        log_info(str(self.log_path), f"Podcast testing complete. Results saved to {results_file}")
        return self.test_results

    def _parse_opml_feeds(self) -> List[Tuple[str, str]]:
        """Parse OPML file to extract podcast feeds"""
        if not os.path.exists(self.opml_path):
            log_error(str(self.log_path), f"OPML file not found: {self.opml_path}")
            return []

        try:
            tree = ET.parse(self.opml_path)
            root = tree.getroot()

            feeds = []
            for outline in root.findall(".//outline[@type='rss']"):
                xml_url = outline.get('xmlUrl')
                title = outline.get('text', 'Unknown Feed')
                if xml_url:
                    feeds.append((xml_url, title))

            log_info(str(self.log_path), f"Parsed {len(feeds)} feeds from OPML")
            return feeds

        except Exception as e:
            log_error(str(self.log_path), f"Failed to parse OPML file: {e}")
            return []

    def _test_podcast_feed(self, feed_url: str, feed_title: str) -> Dict[str, Any]:
        """Test a single podcast feed with multiple transcription methods"""
        log_info(str(self.log_path), f"Testing podcast feed: {feed_title}")

        feed_results = {
            "feed_url": feed_url,
            "feed_title": feed_title,
            "episodes_tested": [],
            "feed_parsing_success": False,
            "total_episodes_available": 0,
            "episodes_processed": 0
        }

        try:
            # Parse the feed
            feed = feedparser.parse(feed_url)

            if not feed.entries:
                log_error(str(self.log_path), f"No episodes found in feed: {feed_title}")
                return feed_results

            feed_results["feed_parsing_success"] = True
            feed_results["total_episodes_available"] = len(feed.entries)

            # Test first 2 episodes for comprehensive analysis
            episodes_to_test = feed.entries[:2]

            for i, episode in enumerate(episodes_to_test):
                log_info(str(self.log_path), f"Testing episode {i+1}: {episode.get('title', 'Untitled')}")

                episode_results = self._test_episode_transcription(episode, feed_title)
                if episode_results:
                    feed_results["episodes_tested"].append(episode_results)
                    feed_results["episodes_processed"] += 1

        except Exception as e:
            log_error(str(self.log_path), f"Failed to test feed {feed_title}: {e}")
            feed_results["error"] = str(e)

        return feed_results

    def _test_episode_transcription(self, episode: Any, feed_title: str) -> Optional[Dict[str, Any]]:
        """Test transcription of a single episode with multiple models"""
        title = episode.get("title", "Untitled Episode")

        # Extract audio URL
        audio_url = None
        if hasattr(episode, "enclosures") and episode.enclosures:
            audio_url = episode.enclosures[0].href
        elif hasattr(episode, "links") and episode.links:
            for link in episode.links:
                if link.get("type", "").startswith("audio"):
                    audio_url = link.get("href")
                    break

        if not audio_url:
            log_error(str(self.log_path), f"No audio URL found for episode: {title}")
            return None

        episode_results = {
            "title": title,
            "audio_url": audio_url,
            "download_success": False,
            "transcription_results": {},
            "transcription_comparison": {},
            "audio_duration_estimate": 0,
            "file_size_mb": 0
        }

        try:
            # Download episode (with size limit for testing)
            audio_path = self._download_episode_for_testing(audio_url, title, max_size_mb=50)
            if not audio_path:
                return episode_results

            episode_results["download_success"] = True
            episode_results["file_size_mb"] = os.path.getsize(audio_path) / (1024 * 1024)

            # Test with multiple transcription models
            transcription_results = self._test_all_transcription_models(audio_path)
            episode_results["transcription_results"] = transcription_results

            # Compare transcription quality if multiple succeeded
            if len(transcription_results) > 1:
                comparison = self._compare_transcriptions(transcription_results)
                episode_results["transcription_comparison"] = comparison

            # Clean up downloaded file
            if os.path.exists(audio_path):
                os.remove(audio_path)

        except Exception as e:
            log_error(str(self.log_path), f"Failed to test episode transcription: {e}")
            episode_results["error"] = str(e)

        return episode_results

    def _download_episode_for_testing(self, audio_url: str, title: str, max_size_mb: int = 50) -> Optional[str]:
        """Download episode audio for testing (with size limits)"""
        try:
            import requests

            # Sanitize filename
            safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            safe_title = safe_title[:50]  # Limit length

            audio_path = self.test_dir / f"temp_episode_{safe_title}.mp3"

            # Start download with streaming
            response = requests.get(audio_url, stream=True, timeout=30)
            response.raise_for_status()

            # Check content length
            content_length = response.headers.get('content-length')
            if content_length:
                size_mb = int(content_length) / (1024 * 1024)
                if size_mb > max_size_mb:
                    log_info(str(self.log_path), f"Episode too large ({size_mb:.1f}MB), skipping download")
                    return None

            # Download with size limit
            downloaded_size = 0
            max_bytes = max_size_mb * 1024 * 1024

            with open(audio_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if downloaded_size + len(chunk) > max_bytes:
                        log_info(str(self.log_path), f"Download size limit reached, truncating at {max_size_mb}MB")
                        break
                    f.write(chunk)
                    downloaded_size += len(chunk)

            if downloaded_size < 1024:  # Less than 1KB
                log_error(str(self.log_path), "Downloaded file too small, likely failed")
                if audio_path.exists():
                    audio_path.unlink()
                return None

            log_info(str(self.log_path), f"Downloaded {downloaded_size / (1024*1024):.1f}MB for testing")
            return str(audio_path)

        except Exception as e:
            log_error(str(self.log_path), f"Failed to download episode: {e}")
            return None

    def _test_all_transcription_models(self, audio_path: str) -> Dict[str, Any]:
        """Test whisper tiny model only (optimized for speed)"""
        results = {}

        # Use only whisper tiny for fast processing
        test_models = [WhisperModel.TINY]

        for model in test_models:
            model_name = f"whisper_{model.value}"
            log_info(str(self.log_path), f"Testing {model_name} model")

            try:
                start_time = time.time()
                result = self.transcription_engine.transcribe_whisper_local(
                    audio_path, model.value, str(self.log_path)
                )
                duration = time.time() - start_time

                results[model_name] = {
                    "success": not bool(result.error),
                    "transcript": result.text,
                    "word_count": result.word_count,
                    "duration_seconds": result.duration_seconds,
                    "total_time_seconds": duration,
                    "words_per_second": result.word_count / result.duration_seconds if result.duration_seconds > 0 else 0,
                    "realtime_factor": result.duration_seconds / duration if duration > 0 else 0,
                    "error": result.error
                }

                log_info(str(self.log_path), f"{model_name}: {result.word_count} words in {result.duration_seconds:.1f}s")

            except Exception as e:
                log_error(str(self.log_path), f"{model_name} failed: {e}")
                results[model_name] = {
                    "success": False,
                    "error": str(e),
                    "duration_seconds": 0,
                    "word_count": 0
                }

        # Skip API-based transcription - focusing on local models for OCI deployment

        return results

    def _compare_transcriptions(self, transcription_results: Dict[str, Any]) -> Dict[str, Any]:
        """Compare transcription results across different models"""
        successful_transcripts = {
            name: data for name, data in transcription_results.items()
            if data.get("success") and data.get("transcript")
        }

        if len(successful_transcripts) < 2:
            return {"note": "Insufficient successful transcriptions for comparison"}

        comparison = {
            "models_compared": list(successful_transcripts.keys()),
            "word_count_variation": {},
            "speed_comparison": {},
            "transcript_similarity": {}
        }

        # Word count analysis
        word_counts = [data["word_count"] for data in successful_transcripts.values()]
        comparison["word_count_variation"] = {
            "min": min(word_counts),
            "max": max(word_counts),
            "mean": statistics.mean(word_counts),
            "std_dev": statistics.stdev(word_counts) if len(word_counts) > 1 else 0,
            "coefficient_of_variation": statistics.stdev(word_counts) / statistics.mean(word_counts) if len(word_counts) > 1 and statistics.mean(word_counts) > 0 else 0
        }

        # Speed comparison
        speeds = {name: data.get("words_per_second", 0) for name, data in successful_transcripts.items()}
        comparison["speed_comparison"] = {
            "fastest_model": max(speeds, key=speeds.get),
            "slowest_model": min(speeds, key=speeds.get),
            "speed_ratios": speeds
        }

        # Basic transcript similarity (using first two transcripts)
        transcript_list = list(successful_transcripts.items())
        if len(transcript_list) >= 2:
            name1, data1 = transcript_list[0]
            name2, data2 = transcript_list[1]

            # Simple word overlap calculation
            words1 = set(data1["transcript"].lower().split())
            words2 = set(data2["transcript"].lower().split())

            overlap = len(words1.intersection(words2))
            union = len(words1.union(words2))
            similarity = overlap / union if union > 0 else 0

            comparison["transcript_similarity"] = {
                "models": [name1, name2],
                "word_overlap_ratio": similarity,
                "unique_words_model1": len(words1 - words2),
                "unique_words_model2": len(words2 - words1),
                "common_words": overlap
            }

        return comparison

    def _analyze_transcription_performance(self) -> None:
        """Analyze transcription performance across all tested episodes"""
        all_results = []

        for feed in self.test_results["feeds_tested"]:
            for episode in feed.get("episodes_tested", []):
                if episode.get("transcription_results"):
                    all_results.append(episode["transcription_results"])

        if not all_results:
            return

        # Aggregate performance metrics
        model_performance = {}

        for results in all_results:
            for model_name, data in results.items():
                if data.get("success"):
                    if model_name not in model_performance:
                        model_performance[model_name] = {
                            "success_count": 0,
                            "total_attempts": 0,
                            "speeds": [],
                            "word_counts": [],
                            "durations": []
                        }

                    perf = model_performance[model_name]
                    perf["success_count"] += 1
                    perf["total_attempts"] += 1

                    if data.get("words_per_second", 0) > 0:
                        perf["speeds"].append(data["words_per_second"])
                    if data.get("word_count", 0) > 0:
                        perf["word_counts"].append(data["word_count"])
                    if data.get("duration_seconds", 0) > 0:
                        perf["durations"].append(data["duration_seconds"])
                else:
                    if model_name not in model_performance:
                        model_performance[model_name] = {
                            "success_count": 0,
                            "total_attempts": 0,
                            "speeds": [],
                            "word_counts": [],
                            "durations": []
                        }
                    model_performance[model_name]["total_attempts"] += 1

        # Calculate statistics
        performance_summary = {}
        for model_name, perf in model_performance.items():
            summary = {
                "success_rate": perf["success_count"] / perf["total_attempts"] if perf["total_attempts"] > 0 else 0,
                "total_attempts": perf["total_attempts"],
                "successful_transcriptions": perf["success_count"]
            }

            if perf["speeds"]:
                summary["average_speed_words_per_sec"] = statistics.mean(perf["speeds"])
                summary["speed_std_dev"] = statistics.stdev(perf["speeds"]) if len(perf["speeds"]) > 1 else 0

            if perf["word_counts"]:
                summary["average_word_count"] = statistics.mean(perf["word_counts"])

            if perf["durations"]:
                summary["average_duration"] = statistics.mean(perf["durations"])

            performance_summary[model_name] = summary

        self.test_results["performance_analysis"] = performance_summary

    def _generate_recommendations(self) -> None:
        """Generate recommendations based on test results"""
        recommendations = {
            "speed_recommendations": {},
            "accuracy_recommendations": {},
            "general_recommendations": []
        }

        perf_analysis = self.test_results.get("performance_analysis", {})

        if perf_analysis:
            # Find fastest reliable model
            reliable_models = {
                name: data for name, data in perf_analysis.items()
                if data.get("success_rate", 0) >= 0.8  # 80% success rate threshold
            }

            if reliable_models:
                fastest_model = max(
                    reliable_models.items(),
                    key=lambda x: x[1].get("average_speed_words_per_sec", 0)
                )

                recommendations["speed_recommendations"]["fastest_reliable"] = {
                    "model": fastest_model[0],
                    "speed": fastest_model[1].get("average_speed_words_per_sec", 0),
                    "success_rate": fastest_model[1].get("success_rate", 0)
                }

            # Find most reliable model
            most_reliable = max(
                perf_analysis.items(),
                key=lambda x: x[1].get("success_rate", 0)
            )

            recommendations["accuracy_recommendations"]["most_reliable"] = {
                "model": most_reliable[0],
                "success_rate": most_reliable[1].get("success_rate", 0)
            }

        # General recommendations
        total_episodes_tested = sum(
            len(feed.get("episodes_tested", []))
            for feed in self.test_results["feeds_tested"]
        )

        if total_episodes_tested > 0:
            recommendations["general_recommendations"].extend([
                f"Successfully tested {total_episodes_tested} podcast episodes",
                "Consider using the fastest reliable model for bulk processing",
                "Use higher quality models for content that will be quoted or cited",
                "Monitor transcription accuracy vs speed tradeoffs for your use case"
            ])

        # Add specific model recommendations
        if "whisper_tiny" in perf_analysis and perf_analysis["whisper_tiny"].get("success_rate", 0) > 0.5:
            recommendations["general_recommendations"].extend([
                "Whisper tiny model excellent for concept search and idea discovery",
                "Fast processing suitable for OCI deployment and bulk podcast processing",
                "Adequate accuracy for finding topics, quotes, and key discussions"
            ])

        self.test_results["recommendations"] = recommendations


def main():
    """Run podcast transcription testing"""
    tester = PodcastTranscriptionTester()
    results = tester.run_comprehensive_podcast_test()

    print("\n" + "="*80)
    print("PODCAST TRANSCRIPTION TEST RESULTS")
    print("="*80)

    print(f"\nTest completed at: {results['timestamp']}")
    print(f"OPML file: {results['opml_file']}")

    # Feeds tested
    feeds_tested = results.get("feeds_tested", [])
    print(f"\nFeeds tested: {len(feeds_tested)}")

    for feed in feeds_tested:
        print(f"\n  📻 {feed['feed_title']}")
        print(f"     Episodes available: {feed.get('total_episodes_available', 0)}")
        print(f"     Episodes tested: {feed.get('episodes_processed', 0)}")

        for episode in feed.get("episodes_tested", []):
            print(f"     📝 {episode['title'][:50]}...")
            if episode.get("download_success"):
                print(f"        File size: {episode.get('file_size_mb', 0):.1f}MB")

                transcriptions = episode.get("transcription_results", {})
                successful = [name for name, data in transcriptions.items() if data.get("success")]
                print(f"        Successful transcriptions: {len(successful)}")

                if successful:
                    for model in successful:
                        data = transcriptions[model]
                        speed = data.get("words_per_second", 0)
                        words = data.get("word_count", 0)
                        print(f"          {model}: {words} words, {speed:.1f} words/sec")

    # Performance analysis
    if results.get("performance_analysis"):
        print("\n📊 Performance Analysis:")
        for model, perf in results["performance_analysis"].items():
            success_rate = perf.get("success_rate", 0) * 100
            avg_speed = perf.get("average_speed_words_per_sec", 0)
            print(f"  {model:15} - {success_rate:5.1f}% success, {avg_speed:6.1f} words/sec avg")

    # Recommendations
    if results.get("recommendations"):
        recs = results["recommendations"]
        print("\n💡 Recommendations:")

        if recs.get("speed_recommendations", {}).get("fastest_reliable"):
            fastest = recs["speed_recommendations"]["fastest_reliable"]
            print(f"  Fastest reliable: {fastest['model']} ({fastest['speed']:.1f} words/sec)")

        if recs.get("accuracy_recommendations", {}).get("most_reliable"):
            reliable = recs["accuracy_recommendations"]["most_reliable"]
            print(f"  Most reliable: {reliable['model']} ({reliable['success_rate']*100:.1f}% success)")

        for rec in recs.get("general_recommendations", []):
            print(f"  • {rec}")

    print("\n" + "="*80)
    return results


if __name__ == "__main__":
    main()