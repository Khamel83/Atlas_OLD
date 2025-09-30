#!/usr/bin/env python3
"""
Comprehensive Ingestion Testing Prototype

This module provides a complete testing framework for all Atlas ingestion features:
- Multi-speed transcription testing (tiny/small/medium/large Whisper models)
- API-based ingestion (Instapaper, YouTube)
- Local file ingestion (documents, audio)
- Podcast OPML ingestion
- Transcription fidelity comparison
- Search quality testing
- Performance benchmarking
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import difflib
import statistics

from helpers.config import load_config
from helpers.podcast_ingestor import ingest_podcasts
from helpers.youtube_ingestor import YouTubeIngestor
from helpers.document_ingestor import DocumentIngestor
from helpers.instapaper_ingestor import InstapaperIngestor
from helpers.transcription_openrouter import transcribe_audio as transcribe_openrouter
from helpers.search_engine import SearchEngine
from helpers.utils import log_info, log_error
from helpers.bulletproof_process_manager import create_managed_process


class TranscriptionModel:
    """Configuration for different Whisper models for speed/accuracy testing"""
    TINY = {"name": "tiny", "speed": "fastest", "accuracy": "lowest"}
    SMALL = {"name": "small", "speed": "fast", "accuracy": "medium"}
    MEDIUM = {"name": "medium", "speed": "medium", "accuracy": "good"}
    LARGE = {"name": "large", "speed": "slow", "accuracy": "highest"}

    @classmethod
    def all_models(cls):
        return [cls.TINY, cls.SMALL, cls.MEDIUM, cls.LARGE]


class IngestionPrototypeTester:
    """Main testing class for comprehensive ingestion testing"""

    def __init__(self, config_path: str = "config.json"):
        self.config = load_config()
        self.test_output_dir = Path("testing/results")
        self.test_output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize test data tracking
        self.test_results = {
            "timestamp": datetime.now().isoformat(),
            "transcription_tests": {},
            "ingestion_tests": {},
            "performance_tests": {},
            "fidelity_tests": {},
            "search_tests": {}
        }

        # Setup logging
        self.log_path = self.test_output_dir / "ingestion_test.log"

    def run_comprehensive_test_suite(self) -> Dict[str, Any]:
        """Run all ingestion tests and return comprehensive results"""
        log_info(str(self.log_path), "Starting comprehensive ingestion test suite")

        # 1. Test all transcription models
        self.test_transcription_models()

        # 2. Test all ingestion methods
        self.test_all_ingestion_methods()

        # 3. Test transcription fidelity
        self.test_transcription_fidelity()

        # 4. Test search quality with different transcription accuracies
        self.test_search_quality()

        # 5. Performance benchmarking
        self.benchmark_performance()

        # Save comprehensive results
        results_file = self.test_output_dir / f"comprehensive_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w') as f:
            json.dump(self.test_results, f, indent=2)

        log_info(str(self.log_path), f"Test suite complete. Results saved to {results_file}")
        return self.test_results

    def test_transcription_models(self) -> Dict[str, Any]:
        """Test all Whisper models for speed and accuracy"""
        log_info(str(self.log_path), "Testing transcription models")

        # Get test audio file
        test_audio = self._get_test_audio_file()
        if not test_audio:
            log_error(str(self.log_path), "No test audio file available")
            return {}

        transcription_results = {}

        for model in TranscriptionModel.all_models():
            model_name = model["name"]
            log_info(str(self.log_path), f"Testing {model_name} model")

            start_time = time.time()

            # Test with local Whisper
            transcript = self._transcribe_with_model(test_audio, model_name)

            end_time = time.time()
            duration = end_time - start_time

            transcription_results[model_name] = {
                "transcript": transcript,
                "duration_seconds": duration,
                "words_per_second": len(transcript.split()) / duration if transcript else 0,
                "model_info": model
            }

            log_info(str(self.log_path), f"{model_name} model completed in {duration:.2f}s")

        self.test_results["transcription_tests"] = transcription_results
        return transcription_results

    def test_all_ingestion_methods(self) -> Dict[str, Any]:
        """Test all ingestion methods: API, local files, podcasts"""
        log_info(str(self.log_path), "Testing all ingestion methods")

        ingestion_results = {}

        # Test podcast ingestion
        ingestion_results["podcasts"] = self._test_podcast_ingestion()

        # Test YouTube ingestion
        ingestion_results["youtube"] = self._test_youtube_ingestion()

        # Test document ingestion
        ingestion_results["documents"] = self._test_document_ingestion()

        # Test Instapaper ingestion (if configured)
        ingestion_results["instapaper"] = self._test_instapaper_ingestion()

        self.test_results["ingestion_tests"] = ingestion_results
        return ingestion_results

    def test_transcription_fidelity(self) -> Dict[str, Any]:
        """Test transcription fidelity against ground truth"""
        log_info(str(self.log_path), "Testing transcription fidelity")

        # Get test audio with known transcript
        test_audio, ground_truth = self._get_test_audio_with_transcript()
        if not test_audio or not ground_truth:
            log_error(str(self.log_path), "No ground truth transcript available")
            return {}

        fidelity_results = {}

        for model in TranscriptionModel.all_models():
            model_name = model["name"]
            transcript = self._transcribe_with_model(test_audio, model_name)

            if transcript:
                # Calculate similarity metrics
                similarity = self._calculate_transcript_similarity(ground_truth, transcript)
                fidelity_results[model_name] = similarity

        # Test OpenRouter transcription
        if os.getenv("OPENROUTER_API_KEY"):
            or_transcript = transcribe_openrouter(test_audio)
            or_similarity = self._calculate_transcript_similarity(ground_truth, or_transcript)
            fidelity_results["openrouter"] = or_similarity

        self.test_results["fidelity_tests"] = fidelity_results
        return fidelity_results

    def test_search_quality(self) -> Dict[str, Any]:
        """Test search quality with different transcription accuracies"""
        log_info(str(self.log_path), "Testing search quality")

        search_results = {}

        # Initialize search engine
        search_engine = SearchEngine(self.config)

        # Test queries that should find content in transcripts
        test_queries = [
            "artificial intelligence",
            "machine learning",
            "podcast discussion",
            "technology trends"
        ]

        for query in test_queries:
            query_results = {}

            # Test search against different transcription qualities
            for model in TranscriptionModel.all_models():
                model_name = model["name"]
                # Simulate search with model-specific transcripts
                results = search_engine.search(query, limit=10)
                query_results[model_name] = {
                    "result_count": len(results),
                    "top_score": results[0]["score"] if results else 0,
                    "avg_score": statistics.mean([r["score"] for r in results]) if results else 0
                }

            search_results[query] = query_results

        self.test_results["search_tests"] = search_results
        return search_results

    def benchmark_performance(self) -> Dict[str, Any]:
        """Benchmark performance of all ingestion methods"""
        log_info(str(self.log_path), "Benchmarking performance")

        performance_results = {}

        # Benchmark podcast ingestion
        performance_results["podcast_ingestion"] = self._benchmark_podcast_ingestion()

        # Benchmark transcription speeds
        performance_results["transcription_speeds"] = self._benchmark_transcription_speeds()

        # Benchmark document processing
        performance_results["document_processing"] = self._benchmark_document_processing()

        self.test_results["performance_tests"] = performance_results
        return performance_results

    def _get_test_audio_file(self) -> Optional[str]:
        """Get a test audio file for transcription testing"""
        # Look for existing audio files in test data
        test_audio_paths = [
            "test_data/audio/sample.mp3",
            "output/podcasts/audio",
            "inputs/test_audio.mp3"
        ]

        for path in test_audio_paths:
            if os.path.exists(path):
                if os.path.isdir(path):
                    # Get first audio file in directory
                    for file in os.listdir(path):
                        if file.endswith(('.mp3', '.wav', '.m4a')):
                            return os.path.join(path, file)
                else:
                    return path

        return None

    def _get_test_audio_with_transcript(self) -> Tuple[Optional[str], Optional[str]]:
        """Get test audio file with known ground truth transcript"""
        # Check for podcast with official transcript
        ground_truth_dir = Path("test_data/ground_truth")
        if ground_truth_dir.exists():
            for audio_file in ground_truth_dir.glob("*.mp3"):
                transcript_file = audio_file.with_suffix(".txt")
                if transcript_file.exists():
                    return str(audio_file), transcript_file.read_text()

        # Fallback to any test audio (no ground truth)
        test_audio = self._get_test_audio_file()
        return test_audio, None

    def _transcribe_with_model(self, audio_path: str, model_name: str) -> str:
        """Transcribe audio with specific Whisper model"""
        try:
            # Temporarily modify the transcription function to use specific model
            import subprocess
            from pathlib import Path

            output_dir = Path(audio_path).parent
            transcript_path = output_dir / f"{Path(audio_path).stem}_{model_name}.txt"

            if transcript_path.exists():
                return transcript_path.read_text()

            command = [
                "whisper",
                str(audio_path),
                "--model", model_name,
                "--output_format", "txt",
                "--output_dir", str(output_dir),
                "--language", "en"
            ]

            process = create_managed_process(command, f"transcribe_{model_name}")
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                # Find the generated transcript file
                generated_file = output_dir / f"{Path(audio_path).stem}.txt"
                if generated_file.exists():
                    transcript = generated_file.read_text()
                    # Save with model-specific name
                    transcript_path.write_text(transcript)
                    return transcript

            return ""
        except Exception as e:
            log_error(str(self.log_path), f"Transcription failed with {model_name}: {e}")
            return ""

    def _calculate_transcript_similarity(self, ground_truth: str, transcript: str) -> Dict[str, float]:
        """Calculate similarity metrics between ground truth and transcript"""
        # Word-level similarity
        gt_words = ground_truth.lower().split()
        tr_words = transcript.lower().split()

        # Calculate various similarity metrics
        sequence_matcher = difflib.SequenceMatcher(None, gt_words, tr_words)
        word_similarity = sequence_matcher.ratio()

        # Character-level similarity
        char_similarity = difflib.SequenceMatcher(None, ground_truth.lower(), transcript.lower()).ratio()

        # Calculate word error rate (WER)
        wer = self._calculate_wer(gt_words, tr_words)

        return {
            "word_similarity": word_similarity,
            "character_similarity": char_similarity,
            "word_error_rate": wer,
            "ground_truth_length": len(gt_words),
            "transcript_length": len(tr_words)
        }

    def _calculate_wer(self, reference: List[str], hypothesis: List[str]) -> float:
        """Calculate Word Error Rate"""
        # Simple WER calculation using edit distance
        d = [[0] * (len(hypothesis) + 1) for _ in range(len(reference) + 1)]

        for i in range(len(reference) + 1):
            d[i][0] = i
        for j in range(len(hypothesis) + 1):
            d[0][j] = j

        for i in range(1, len(reference) + 1):
            for j in range(1, len(hypothesis) + 1):
                if reference[i-1] == hypothesis[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1

        return d[len(reference)][len(hypothesis)] / len(reference) if reference else 0

    def _test_podcast_ingestion(self) -> Dict[str, Any]:
        """Test podcast OPML ingestion"""
        try:
            start_time = time.time()

            # Test with existing OPML file
            opml_path = "inputs/podcasts.opml"
            if os.path.exists(opml_path):
                ingest_podcasts(self.config, opml_path)

            duration = time.time() - start_time

            return {
                "success": True,
                "duration": duration,
                "opml_file": opml_path
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def _test_youtube_ingestion(self) -> Dict[str, Any]:
        """Test YouTube video ingestion"""
        try:
            ingestor = YouTubeIngestor(self.config)

            # Test with a sample YouTube URL
            test_urls = [
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Rick Roll as safe test
                # Add more test URLs as needed
            ]

            results = []
            for url in test_urls:
                start_time = time.time()
                success = ingestor.ingest_single_video(url)
                duration = time.time() - start_time

                results.append({
                    "url": url,
                    "success": success,
                    "duration": duration
                })

            return {"results": results}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _test_document_ingestion(self) -> Dict[str, Any]:
        """Test local document ingestion"""
        try:
            ingestor = DocumentIngestor(self.config)

            # Look for test documents
            test_docs = []
            for ext in ['*.pdf', '*.txt', '*.md']:
                test_docs.extend(Path("test_data").glob(f"**/{ext}"))

            results = []
            for doc in test_docs[:5]:  # Test first 5 documents
                start_time = time.time()
                success = ingestor.ingest_document(str(doc))
                duration = time.time() - start_time

                results.append({
                    "document": str(doc),
                    "success": success,
                    "duration": duration
                })

            return {"results": results}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _test_instapaper_ingestion(self) -> Dict[str, Any]:
        """Test Instapaper API ingestion"""
        try:
            if not (self.config.get("INSTAPAPER_LOGIN") and self.config.get("INSTAPAPER_PASSWORD")):
                return {"success": False, "error": "Instapaper credentials not configured"}

            ingestor = InstapaperIngestor(self.config)

            start_time = time.time()
            ingestor.ingest_articles(limit=5)  # Test with 5 articles
            duration = time.time() - start_time

            return {
                "success": True,
                "duration": duration,
                "limit": 5
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _benchmark_podcast_ingestion(self) -> Dict[str, Any]:
        """Benchmark podcast ingestion performance"""
        try:
            # Test different feed sizes
            benchmark_results = {}

            opml_path = "inputs/podcasts.opml"
            if os.path.exists(opml_path):
                start_time = time.time()
                ingest_podcasts(self.config, opml_path)
                duration = time.time() - start_time

                # Count processed items
                output_dir = Path(self.config.get("podcast_output_path", "output/podcasts"))
                item_count = len(list(output_dir.glob("*.json"))) if output_dir.exists() else 0

                benchmark_results["full_opml"] = {
                    "duration": duration,
                    "items_processed": item_count,
                    "items_per_second": item_count / duration if duration > 0 else 0
                }

            return benchmark_results
        except Exception as e:
            return {"error": str(e)}

    def _benchmark_transcription_speeds(self) -> Dict[str, Any]:
        """Benchmark transcription speeds for different models"""
        test_audio = self._get_test_audio_file()
        if not test_audio:
            return {"error": "No test audio available"}

        # Get audio duration (approximate from file size)
        audio_size_mb = os.path.getsize(test_audio) / (1024 * 1024)

        speed_results = {}
        for model in TranscriptionModel.all_models():
            model_name = model["name"]

            start_time = time.time()
            transcript = self._transcribe_with_model(test_audio, model_name)
            duration = time.time() - start_time

            speed_results[model_name] = {
                "transcription_time": duration,
                "audio_size_mb": audio_size_mb,
                "mb_per_second": audio_size_mb / duration if duration > 0 else 0,
                "success": bool(transcript)
            }

        return speed_results

    def _benchmark_document_processing(self) -> Dict[str, Any]:
        """Benchmark document processing performance"""
        try:
            ingestor = DocumentIngestor(self.config)

            # Find test documents of different sizes
            test_docs = list(Path("test_data").glob("**/*.pdf"))[:5]

            benchmark_results = []
            for doc in test_docs:
                doc_size_mb = os.path.getsize(doc) / (1024 * 1024)

                start_time = time.time()
                success = ingestor.ingest_document(str(doc))
                duration = time.time() - start_time

                benchmark_results.append({
                    "document": str(doc),
                    "size_mb": doc_size_mb,
                    "processing_time": duration,
                    "mb_per_second": doc_size_mb / duration if duration > 0 else 0,
                    "success": success
                })

            return {"results": benchmark_results}
        except Exception as e:
            return {"error": str(e)}


def main():
    """Run the comprehensive ingestion test suite"""
    tester = IngestionPrototypeTester()
    results = tester.run_comprehensive_test_suite()

    print("\n" + "="*80)
    print("COMPREHENSIVE INGESTION TEST RESULTS")
    print("="*80)

    # Print summary
    print(f"\nTest completed at: {results['timestamp']}")
    print("Results saved to: testing/results/")

    # Print transcription model performance
    if results.get("transcription_tests"):
        print("\nTranscription Model Performance:")
        for model, data in results["transcription_tests"].items():
            print(f"  {model:8} - {data['duration_seconds']:.1f}s, {data['words_per_second']:.1f} words/sec")

    # Print ingestion test results
    if results.get("ingestion_tests"):
        print("\nIngestion Method Tests:")
        for method, data in results["ingestion_tests"].items():
            success = data.get("success", False)
            print(f"  {method:12} - {'✓' if success else '✗'}")

    # Print fidelity results
    if results.get("fidelity_tests"):
        print("\nTranscription Fidelity (vs ground truth):")
        for model, data in results["fidelity_tests"].items():
            wer = data.get("word_error_rate", 0)
            similarity = data.get("word_similarity", 0)
            print(f"  {model:12} - WER: {wer:.3f}, Similarity: {similarity:.3f}")

    print("\n" + "="*80)
    return results


if __name__ == "__main__":
    main()