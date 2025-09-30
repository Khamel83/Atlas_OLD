#!/usr/bin/env python3
"""
Tyler Cowen Podcast Accuracy Test

Test whisper_tiny transcription accuracy against human-generated transcript
for the Nate Silver episode of Conversations with Tyler.
"""

import os
import time
import json
from pathlib import Path
from typing import Dict, Any, Optional
import requests
import difflib
from datetime import datetime

from helpers.config import load_config
from helpers.enhanced_transcription import EnhancedTranscriptionEngine, WhisperModel
from helpers.utils import log_info, log_error


class TylerCowenAccuracyTester:
    """Test transcription accuracy against human reference"""

    def __init__(self):
        self.config = load_config()
        self.test_dir = Path("testing/podcast_tests")
        self.test_dir.mkdir(parents=True, exist_ok=True)
        self.log_path = self.test_dir / "tyler_cowen_accuracy.log"
        self.transcription_engine = EnhancedTranscriptionEngine(self.config)

    def test_episode_accuracy(self, audio_url: str, reference_transcript_path: str) -> Dict[str, Any]:
        """Test a single episode against reference transcript"""
        log_info(str(self.log_path), "Starting Tyler Cowen episode accuracy test")

        results = {
            "timestamp": datetime.now().isoformat(),
            "audio_url": audio_url,
            "reference_transcript_path": reference_transcript_path,
            "download_success": False,
            "transcription_success": False,
            "whisper_tiny_results": {},
            "accuracy_metrics": {},
            "error": None
        }

        try:
            # Download episode
            audio_path = self._download_episode(audio_url)
            if not audio_path:
                results["error"] = "Failed to download audio"
                return results

            results["download_success"] = True
            results["file_size_mb"] = os.path.getsize(audio_path) / (1024 * 1024)

            # Load reference transcript
            reference_text = self._load_reference_transcript(reference_transcript_path)
            if not reference_text:
                results["error"] = "Failed to load reference transcript"
                return results

            # Run whisper tiny transcription
            whisper_results = self._transcribe_with_tiny(audio_path)
            results["whisper_tiny_results"] = whisper_results

            if whisper_results.get("success"):
                results["transcription_success"] = True

                # Compare transcriptions
                accuracy_metrics = self._compare_transcripts(
                    reference_text,
                    whisper_results["transcript"]
                )
                results["accuracy_metrics"] = accuracy_metrics

                log_info(str(self.log_path), f"Word accuracy: {accuracy_metrics.get('word_accuracy', 0):.2%}")

            # Clean up
            if os.path.exists(audio_path):
                os.remove(audio_path)

        except Exception as e:
            log_error(str(self.log_path), f"Test failed: {e}")
            results["error"] = str(e)

        return results

    def _download_episode(self, audio_url: str, max_size_mb: int = 100) -> Optional[str]:
        """Download episode audio for testing"""
        try:
            audio_path = self.test_dir / "tyler_cowen_test_episode.mp3"

            log_info(str(self.log_path), f"Downloading audio from: {audio_url}")
            response = requests.get(audio_url, stream=True, timeout=60)
            response.raise_for_status()

            # Check size
            content_length = response.headers.get('content-length')
            if content_length:
                size_mb = int(content_length) / (1024 * 1024)
                if size_mb > max_size_mb:
                    log_error(str(self.log_path), f"Episode too large ({size_mb:.1f}MB)")
                    return None

            # Download
            downloaded_size = 0
            max_bytes = max_size_mb * 1024 * 1024

            with open(audio_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if downloaded_size + len(chunk) > max_bytes:
                        break
                    f.write(chunk)
                    downloaded_size += len(chunk)

            log_info(str(self.log_path), f"Downloaded {downloaded_size / (1024*1024):.1f}MB")
            return str(audio_path)

        except Exception as e:
            log_error(str(self.log_path), f"Download failed: {e}")
            return None

    def _load_reference_transcript(self, transcript_path: str) -> Optional[str]:
        """Load reference transcript from file"""
        try:
            with open(transcript_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()

            log_info(str(self.log_path), f"Loaded reference transcript: {len(content)} characters")
            return content

        except Exception as e:
            log_error(str(self.log_path), f"Failed to load reference transcript: {e}")
            return None

    def _transcribe_with_tiny(self, audio_path: str) -> Dict[str, Any]:
        """Transcribe using whisper tiny model"""
        log_info(str(self.log_path), "Running Whisper tiny transcription...")

        try:
            start_time = time.time()
            result = self.transcription_engine.transcribe_whisper_local(
                audio_path, WhisperModel.TINY.value, str(self.log_path)
            )
            duration = time.time() - start_time

            return {
                "success": not bool(result.error),
                "transcript": result.text,
                "word_count": result.word_count,
                "duration_seconds": result.duration_seconds,
                "processing_time_seconds": duration,
                "words_per_second": result.word_count / result.duration_seconds if result.duration_seconds > 0 else 0,
                "realtime_factor": result.duration_seconds / duration if duration > 0 else 0,
                "error": result.error
            }

        except Exception as e:
            log_error(str(self.log_path), f"Whisper tiny failed: {e}")
            return {"success": False, "error": str(e)}

    def _compare_transcripts(self, reference: str, ai_transcript: str) -> Dict[str, Any]:
        """Compare AI transcript against human reference"""

        # Normalize text for comparison
        ref_words = self._normalize_text(reference).split()
        ai_words = self._normalize_text(ai_transcript).split()

        # Word-level accuracy using difflib
        sequence_matcher = difflib.SequenceMatcher(None, ref_words, ai_words)
        matching_blocks = sequence_matcher.get_matching_blocks()

        # Calculate matches
        total_ref_words = len(ref_words)
        total_ai_words = len(ai_words)
        matched_words = sum(block.size for block in matching_blocks)

        # Accuracy metrics
        word_accuracy = matched_words / total_ref_words if total_ref_words > 0 else 0
        precision = matched_words / total_ai_words if total_ai_words > 0 else 0
        recall = matched_words / total_ref_words if total_ref_words > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        # Character-level similarity
        char_similarity = difflib.SequenceMatcher(None, reference.lower(), ai_transcript.lower()).ratio()

        # Length comparison
        length_ratio = len(ai_transcript) / len(reference) if len(reference) > 0 else 0

        return {
            "reference_word_count": total_ref_words,
            "ai_word_count": total_ai_words,
            "matched_words": matched_words,
            "word_accuracy": word_accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1_score,
            "character_similarity": char_similarity,
            "length_ratio": length_ratio,
            "reference_length": len(reference),
            "ai_length": len(ai_transcript)
        }

    def _normalize_text(self, text: str) -> str:
        """Normalize text for comparison"""
        import re

        # Convert to lowercase
        text = text.lower()

        # Remove extra whitespace
        text = ' '.join(text.split())

        # Remove common punctuation (but keep apostrophes for contractions)
        text = re.sub(r'[^\w\s\']', ' ', text)

        # Remove extra spaces
        text = ' '.join(text.split())

        return text


def test_with_manual_transcript():
    """Test with manually provided audio URL and transcript"""
    tester = TylerCowenAccuracyTester()

    # You can replace these with actual URLs/files
    audio_url = input("Enter podcast audio URL (or press Enter to skip): ").strip()
    if not audio_url:
        print("No audio URL provided. Creating example transcript file...")

        # Create example reference transcript
        example_transcript = """
TYLER COWEN: Today I'm here with Nate Silver, who is a statistician, writer, and poker player.
His latest book is "On the Edge: The Art of Risking Everything." Nate, welcome.

NATE SILVER: Thanks for having me, Tyler.

TYLER COWEN: How has your thinking about risk evolved over time?

NATE SILVER: I think one thing that's changed is I've become more comfortable with uncertainty...
        """.strip()

        ref_path = Path("testing/podcast_tests/example_reference.txt")
        with open(ref_path, 'w') as f:
            f.write(example_transcript)

        print(f"Created example reference transcript at: {ref_path}")
        print("To run a real test, provide an audio URL and reference transcript file.")
        return

    ref_path = input("Enter path to reference transcript file: ").strip()
    if not ref_path or not os.path.exists(ref_path):
        print("Reference transcript file not found")
        return

    print("\nRunning accuracy test...")
    results = tester.test_episode_accuracy(audio_url, ref_path)

    # Save results
    results_file = Path("testing/podcast_tests") / f"tyler_cowen_accuracy_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    # Print results
    print("\n" + "="*60)
    print("TYLER COWEN ACCURACY TEST RESULTS")
    print("="*60)

    if results.get("error"):
        print(f"❌ Test failed: {results['error']}")
        return

    if results.get("download_success"):
        print(f"✅ Audio downloaded: {results.get('file_size_mb', 0):.1f}MB")

    if results.get("transcription_success"):
        tiny_results = results.get("whisper_tiny_results", {})
        print(f"✅ Transcription completed in {tiny_results.get('processing_time_seconds', 0):.1f}s")
        print(f"   Words generated: {tiny_results.get('word_count', 0)}")
        print(f"   Processing speed: {tiny_results.get('realtime_factor', 0):.1f}x realtime")

        accuracy = results.get("accuracy_metrics", {})
        if accuracy:
            print("\n📊 Accuracy Metrics:")
            print(f"   Word accuracy: {accuracy.get('word_accuracy', 0):.2%}")
            print(f"   Precision: {accuracy.get('precision', 0):.2%}")
            print(f"   Recall: {accuracy.get('recall', 0):.2%}")
            print(f"   F1 Score: {accuracy.get('f1_score', 0):.2%}")
            print(f"   Character similarity: {accuracy.get('character_similarity', 0):.2%}")
            print(f"   Length ratio (AI/Human): {accuracy.get('length_ratio', 0):.2f}")

            print("\n📏 Length Comparison:")
            print(f"   Reference: {accuracy.get('reference_word_count', 0)} words")
            print(f"   AI Generated: {accuracy.get('ai_word_count', 0)} words")
            print(f"   Matched words: {accuracy.get('matched_words', 0)}")

    print(f"\nFull results saved to: {results_file}")


if __name__ == "__main__":
    test_with_manual_transcript()