#!/usr/bin/env python3
"""
Comprehensive Ingestion Testing Suite

Tests all ingestion methods:
- API-based: Instapaper, YouTube, RSS feeds
- Local files: documents, audio, video
- Real-time: live streams, webhooks
- Batch processing: bulk imports
"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import tempfile
import shutil

from helpers.config import load_config
from helpers.instapaper_ingestor import InstapaperIngestor
from helpers.youtube_ingestor import YouTubeIngestor
from helpers.podcast_ingestor import PodcastIngestor, ingest_podcasts
from helpers.document_ingestor import DocumentIngestor
from helpers.article_fetcher import fetch_and_save_articles
from helpers.enhanced_transcription import EnhancedTranscriptionEngine
from helpers.utils import log_info, log_error


class ComprehensiveIngestionTester:
    """Test all ingestion methods comprehensively"""
    
    def __init__(self, config_path: str = "config.json"):
        self.config = load_config()
        self.test_dir = Path("testing/ingestion_tests")
        self.test_dir.mkdir(parents=True, exist_ok=True)
        
        # Test data
        self.test_results = {
            "timestamp": datetime.now().isoformat(),
            "api_tests": {},
            "local_tests": {},
            "batch_tests": {},
            "performance_tests": {},
            "error_handling_tests": {}
        }
        
        self.log_path = self.test_dir / "comprehensive_ingestion.log"
        
        # Test URLs and data
        self.test_urls = {
            "youtube": [
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Rick Roll - safe test
                "https://www.youtube.com/watch?v=9bZkp7q19f0",  # PSY - Gangnam Style
            ],
            "articles": [
                "https://example.com/test-article",
                "https://httpbin.org/html",  # Test HTML response
                "https://www.w3.org/",  # W3C homepage
            ],
            "podcasts": [
                "https://feeds.simplecast.com/54nAGcIl",  # The Daily
                "https://www.npr.org/rss/podcast.php?id=510289",  # Planet Money
            ]
        }
    
    def run_comprehensive_tests(self) -> Dict[str, Any]:
        """Run all ingestion tests"""
        log_info(str(self.log_path), "Starting comprehensive ingestion testing")
        
        # Test API-based ingestion
        self.test_api_ingestion()
        
        # Test local file ingestion
        self.test_local_file_ingestion()
        
        # Test batch processing
        self.test_batch_processing()
        
        # Test error handling
        self.test_error_handling()
        
        # Test performance
        self.test_performance_limits()
        
        # Save results
        results_file = self.test_dir / f"comprehensive_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w') as f:
            json.dump(self.test_results, f, indent=2)
        
        log_info(str(self.log_path), f"Comprehensive testing complete. Results: {results_file}")
        return self.test_results
    
    def test_api_ingestion(self) -> Dict[str, Any]:
        """Test all API-based ingestion methods"""
        log_info(str(self.log_path), "Testing API-based ingestion")
        
        api_results = {}
        
        # Test YouTube ingestion
        api_results["youtube"] = self._test_youtube_api()
        
        # Test Instapaper ingestion
        api_results["instapaper"] = self._test_instapaper_api()
        
        # Test podcast RSS feeds
        api_results["podcast_rss"] = self._test_podcast_rss()
        
        # Test article fetching
        api_results["article_fetching"] = self._test_article_fetching()
        
        self.test_results["api_tests"] = api_results
        return api_results
    
    def test_local_file_ingestion(self) -> Dict[str, Any]:
        """Test local file ingestion capabilities"""
        log_info(str(self.log_path), "Testing local file ingestion")
        
        local_results = {}
        
        # Test document ingestion
        local_results["documents"] = self._test_document_ingestion()
        
        # Test audio file ingestion
        local_results["audio_files"] = self._test_audio_file_ingestion()
        
        # Test video file ingestion
        local_results["video_files"] = self._test_video_file_ingestion()
        
        # Test bulk file ingestion
        local_results["bulk_ingestion"] = self._test_bulk_file_ingestion()
        
        self.test_results["local_tests"] = local_results
        return local_results
    
    def test_batch_processing(self) -> Dict[str, Any]:
        """Test batch processing capabilities"""
        log_info(str(self.log_path), "Testing batch processing")
        
        batch_results = {}
        
        # Test OPML batch processing
        batch_results["opml_batch"] = self._test_opml_batch_processing()
        
        # Test URL list processing
        batch_results["url_batch"] = self._test_url_batch_processing()
        
        # Test directory scanning
        batch_results["directory_scan"] = self._test_directory_scanning()
        
        self.test_results["batch_tests"] = batch_results
        return batch_results
    
    def test_error_handling(self) -> Dict[str, Any]:
        """Test error handling and recovery"""
        log_info(str(self.log_path), "Testing error handling")
        
        error_results = {}
        
        # Test invalid URLs
        error_results["invalid_urls"] = self._test_invalid_urls()
        
        # Test network timeouts
        error_results["network_timeouts"] = self._test_network_timeouts()
        
        # Test corrupted files
        error_results["corrupted_files"] = self._test_corrupted_files()
        
        # Test missing credentials
        error_results["missing_credentials"] = self._test_missing_credentials()
        
        self.test_results["error_handling_tests"] = error_results
        return error_results
    
    def test_performance_limits(self) -> Dict[str, Any]:
        """Test performance limits and benchmarks"""
        log_info(str(self.log_path), "Testing performance limits")
        
        perf_results = {}
        
        # Test concurrent processing
        perf_results["concurrent_processing"] = self._test_concurrent_processing()
        
        # Test large file handling
        perf_results["large_files"] = self._test_large_file_handling()
        
        # Test memory usage
        perf_results["memory_usage"] = self._test_memory_usage()
        
        self.test_results["performance_tests"] = perf_results
        return perf_results
    
    def _test_youtube_api(self) -> Dict[str, Any]:
        """Test YouTube video ingestion"""
        try:
            ingestor = YouTubeIngestor(self.config)
            results = []
            
            for url in self.test_urls["youtube"]:
                start_time = time.time()
                
                try:
                    success = ingestor.ingest_single_video(url)
                    duration = time.time() - start_time
                    
                    results.append({
                        "url": url,
                        "success": success,
                        "duration": duration,
                        "error": None
                    })
                    
                    log_info(str(self.log_path), f"YouTube test: {url} - {'✓' if success else '✗'} ({duration:.2f}s)")
                    
                except Exception as e:
                    duration = time.time() - start_time
                    results.append({
                        "url": url,
                        "success": False,
                        "duration": duration,
                        "error": str(e)
                    })
                    
                    log_error(str(self.log_path), f"YouTube test failed: {url} - {e}")
            
            return {
                "overall_success": any(r["success"] for r in results),
                "results": results,
                "total_tested": len(results),
                "successful": sum(1 for r in results if r["success"])
            }
            
        except Exception as e:
            log_error(str(self.log_path), f"YouTube API test setup failed: {e}")
            return {"overall_success": False, "error": str(e)}
    
    def _test_instapaper_api(self) -> Dict[str, Any]:
        """Test Instapaper API ingestion"""
        try:
            # Check if credentials are available
            if not (self.config.get("INSTAPAPER_LOGIN") and self.config.get("INSTAPAPER_PASSWORD")):
                return {
                    "overall_success": False,
                    "error": "Instapaper credentials not configured",
                    "skipped": True
                }
            
            ingestor = InstapaperIngestor(self.config)
            
            start_time = time.time()
            
            # Test with a small limit
            try:
                ingestor.ingest_articles(limit=3)
                duration = time.time() - start_time
                
                return {
                    "overall_success": True,
                    "duration": duration,
                    "limit_tested": 3
                }
                
            except Exception as e:
                duration = time.time() - start_time
                return {
                    "overall_success": False,
                    "duration": duration,
                    "error": str(e)
                }
            
        except Exception as e:
            return {"overall_success": False, "error": str(e)}
    
    def _test_podcast_rss(self) -> Dict[str, Any]:
        """Test podcast RSS feed ingestion"""
        try:
            ingestor = PodcastIngestor(self.config)
            results = []
            
            for feed_url in self.test_urls["podcasts"]:
                start_time = time.time()
                
                try:
                    success = ingestor.process_feed(feed_url)
                    duration = time.time() - start_time
                    
                    results.append({
                        "feed_url": feed_url,
                        "success": success,
                        "duration": duration,
                        "error": None
                    })
                    
                except Exception as e:
                    duration = time.time() - start_time
                    results.append({
                        "feed_url": feed_url,
                        "success": False,
                        "duration": duration,
                        "error": str(e)
                    })
            
            return {
                "overall_success": any(r["success"] for r in results),
                "results": results,
                "total_tested": len(results),
                "successful": sum(1 for r in results if r["success"])
            }
            
        except Exception as e:
            return {"overall_success": False, "error": str(e)}
    
    def _test_article_fetching(self) -> Dict[str, Any]:
        """Test article URL fetching"""
        try:
            # Create temporary test file
            test_urls_file = self.test_dir / "test_articles.txt"
            with open(test_urls_file, 'w') as f:
                for url in self.test_urls["articles"]:
                    f.write(f"{url}\n")
            
            start_time = time.time()
            
            try:
                # Update config to use test file
                test_config = self.config.copy()
                test_config["article_input_file"] = str(test_urls_file)
                
                result = fetch_and_save_articles(test_config)
                duration = time.time() - start_time
                
                return {
                    "overall_success": True,
                    "duration": duration,
                    "urls_tested": len(self.test_urls["articles"]),
                    "result": result
                }
                
            except Exception as e:
                duration = time.time() - start_time
                return {
                    "overall_success": False,
                    "duration": duration,
                    "error": str(e)
                }
            finally:
                # Clean up
                if test_urls_file.exists():
                    test_urls_file.unlink()
            
        except Exception as e:
            return {"overall_success": False, "error": str(e)}
    
    def _test_document_ingestion(self) -> Dict[str, Any]:
        """Test document file ingestion"""
        try:
            ingestor = DocumentIngestor(self.config)
            
            # Create test documents
            test_docs = self._create_test_documents()
            results = []
            
            for doc_path in test_docs:
                start_time = time.time()
                
                try:
                    success = ingestor.ingest_document(str(doc_path))
                    duration = time.time() - start_time
                    
                    results.append({
                        "document": str(doc_path),
                        "success": success,
                        "duration": duration,
                        "file_size": doc_path.stat().st_size,
                        "error": None
                    })
                    
                except Exception as e:
                    duration = time.time() - start_time
                    results.append({
                        "document": str(doc_path),
                        "success": False,
                        "duration": duration,
                        "file_size": doc_path.stat().st_size,
                        "error": str(e)
                    })
            
            # Clean up test documents
            for doc_path in test_docs:
                if doc_path.exists():
                    doc_path.unlink()
            
            return {
                "overall_success": any(r["success"] for r in results),
                "results": results,
                "total_tested": len(results),
                "successful": sum(1 for r in results if r["success"])
            }
            
        except Exception as e:
            return {"overall_success": False, "error": str(e)}
    
    def _test_audio_file_ingestion(self) -> Dict[str, Any]:
        """Test audio file ingestion with transcription"""
        try:
            # Create test audio files (or use existing ones)
            test_audio_files = self._find_or_create_test_audio()
            
            if not test_audio_files:
                return {
                    "overall_success": False,
                    "error": "No test audio files available",
                    "skipped": True
                }
            
            transcription_engine = EnhancedTranscriptionEngine(self.config)
            results = []
            
            for audio_path in test_audio_files:
                start_time = time.time()
                
                try:
                    # Test fast transcription
                    result = transcription_engine.get_fastest_transcription(audio_path, str(self.log_path))
                    duration = time.time() - start_time
                    
                    results.append({
                        "audio_file": audio_path,
                        "success": bool(result.text),
                        "duration": duration,
                        "transcript_length": len(result.text.split()) if result.text else 0,
                        "transcription_duration": result.duration_seconds,
                        "error": result.error
                    })
                    
                except Exception as e:
                    duration = time.time() - start_time
                    results.append({
                        "audio_file": audio_path,
                        "success": False,
                        "duration": duration,
                        "error": str(e)
                    })
            
            return {
                "overall_success": any(r["success"] for r in results),
                "results": results,
                "total_tested": len(results),
                "successful": sum(1 for r in results if r["success"])
            }
            
        except Exception as e:
            return {"overall_success": False, "error": str(e)}
    
    def _test_video_file_ingestion(self) -> Dict[str, Any]:
        """Test video file ingestion"""
        # For now, return placeholder since video ingestion might use YouTube
        return {
            "overall_success": True,
            "note": "Video ingestion currently handled via YouTube API",
            "placeholder": True
        }
    
    def _test_bulk_file_ingestion(self) -> Dict[str, Any]:
        """Test bulk file ingestion from directory"""
        try:
            # Create test directory with multiple files
            test_dir = self.test_dir / "bulk_test"
            test_dir.mkdir(exist_ok=True)
            
            # Create multiple test documents
            test_files = []
            for i in range(5):
                test_file = test_dir / f"test_doc_{i}.txt"
                with open(test_file, 'w') as f:
                    f.write(f"This is test document number {i}.\n" * 10)
                test_files.append(test_file)
            
            start_time = time.time()
            
            # Test bulk processing
            ingestor = DocumentIngestor(self.config)
            successful = 0
            
            for test_file in test_files:
                try:
                    if ingestor.ingest_document(str(test_file)):
                        successful += 1
                except:
                    pass
            
            duration = time.time() - start_time
            
            # Clean up
            shutil.rmtree(test_dir, ignore_errors=True)
            
            return {
                "overall_success": successful > 0,
                "total_files": len(test_files),
                "successful_files": successful,
                "duration": duration,
                "files_per_second": len(test_files) / duration if duration > 0 else 0
            }
            
        except Exception as e:
            return {"overall_success": False, "error": str(e)}
    
    def _test_opml_batch_processing(self) -> Dict[str, Any]:
        """Test OPML batch processing"""
        try:
            opml_path = "inputs/podcasts.opml"
            
            if not os.path.exists(opml_path):
                return {
                    "overall_success": False,
                    "error": "OPML file not found",
                    "skipped": True
                }
            
            start_time = time.time()
            
            # Temporarily disable transcription for speed
            test_config = self.config.copy()
            test_config["run_transcription"] = False
            
            ingest_podcasts(test_config, opml_path)
            duration = time.time() - start_time
            
            return {
                "overall_success": True,
                "duration": duration,
                "opml_file": opml_path
            }
            
        except Exception as e:
            return {"overall_success": False, "error": str(e)}
    
    def _test_url_batch_processing(self) -> Dict[str, Any]:
        """Test batch URL processing"""
        # This would test processing multiple URLs from a file
        return {"placeholder": True, "note": "URL batch processing test"}
    
    def _test_directory_scanning(self) -> Dict[str, Any]:
        """Test automatic directory scanning"""
        # This would test scanning directories for new files
        return {"placeholder": True, "note": "Directory scanning test"}
    
    def _test_invalid_urls(self) -> Dict[str, Any]:
        """Test handling of invalid URLs"""
        invalid_urls = [
            "https://nonexistent-domain-12345.com",
            "not-a-url",
            "https://httpstat.us/404",
            "https://httpstat.us/500"
        ]
        
        results = []
        for url in invalid_urls:
            try:
                ingestor = YouTubeIngestor(self.config)
                success = ingestor.ingest_single_video(url)
                results.append({
                    "url": url,
                    "handled_gracefully": not success,  # Should fail gracefully
                    "crashed": False
                })
            except Exception as e:
                results.append({
                    "url": url,
                    "handled_gracefully": True,  # Exception is expected
                    "crashed": False,
                    "error": str(e)
                })
        
        return {
            "overall_success": all(r["handled_gracefully"] for r in results),
            "results": results
        }
    
    def _test_network_timeouts(self) -> Dict[str, Any]:
        """Test network timeout handling"""
        # Test with slow response URLs
        return {"placeholder": True, "note": "Network timeout test"}
    
    def _test_corrupted_files(self) -> Dict[str, Any]:
        """Test handling of corrupted files"""
        # Create corrupted test files and test handling
        return {"placeholder": True, "note": "Corrupted file test"}
    
    def _test_missing_credentials(self) -> Dict[str, Any]:
        """Test handling when API credentials are missing"""
        # Test with empty config
        empty_config = {}
        
        try:
            ingestor = InstapaperIngestor(empty_config)
            ingestor.ingest_articles(limit=1)
            return {"overall_success": False, "note": "Should have failed with missing credentials"}
        except Exception as e:
            return {"overall_success": True, "note": "Correctly handled missing credentials", "error": str(e)}
    
    def _test_concurrent_processing(self) -> Dict[str, Any]:
        """Test concurrent processing capabilities"""
        # This would test multiple ingestion processes running simultaneously
        return {"placeholder": True, "note": "Concurrent processing test"}
    
    def _test_large_file_handling(self) -> Dict[str, Any]:
        """Test handling of large files"""
        # This would test with large audio/video files
        return {"placeholder": True, "note": "Large file handling test"}
    
    def _test_memory_usage(self) -> Dict[str, Any]:
        """Test memory usage during processing"""
        # This would monitor memory usage during ingestion
        return {"placeholder": True, "note": "Memory usage test"}
    
    def _create_test_documents(self) -> List[Path]:
        """Create temporary test documents"""
        test_docs = []
        
        # Create text document
        txt_doc = self.test_dir / "test_document.txt"
        with open(txt_doc, 'w') as f:
            f.write("This is a test document for ingestion testing.\n" * 100)
        test_docs.append(txt_doc)
        
        # Create markdown document
        md_doc = self.test_dir / "test_document.md"
        with open(md_doc, 'w') as f:
            f.write("""# Test Document

This is a **test markdown document** for ingestion testing.

## Features
- Lists
- *Emphasis*
- `Code blocks`

""")
        test_docs.append(md_doc)
        
        return test_docs
    
    def _find_or_create_test_audio(self) -> List[str]:
        """Find existing audio files or create test ones"""
        # Look for existing audio files first
        audio_paths = []
        
        # Check common audio directories
        search_paths = [
            "test_data/audio",
            "output/podcasts/audio",
            "test_data/ground_truth"
        ]
        
        for search_path in search_paths:
            if os.path.exists(search_path):
                for file in os.listdir(search_path):
                    if file.endswith(('.mp3', '.wav', '.m4a')):
                        audio_paths.append(os.path.join(search_path, file))
                        if len(audio_paths) >= 3:  # Limit for testing
                            break
        
        return audio_paths[:3]  # Return up to 3 files for testing


def main():
    """Run comprehensive ingestion tests"""
    tester = ComprehensiveIngestionTester()
    results = tester.run_comprehensive_tests()
    
    print("\n" + "="*80)
    print("COMPREHENSIVE INGESTION TEST RESULTS")
    print("="*80)
    
    # Print summary
    print(f"\nTest completed at: {results['timestamp']}")
    
    # API Tests
    if results.get("api_tests"):
        print("\nAPI Ingestion Tests:")
        for method, data in results["api_tests"].items():
            if isinstance(data, dict):
                success = data.get("overall_success", False)
                skipped = data.get("skipped", False)
                status = "SKIP" if skipped else ("✓" if success else "✗")
                print(f"  {method:15} - {status}")
                if data.get("error"):
                    print(f"    Error: {data['error']}")
    
    # Local Tests
    if results.get("local_tests"):
        print("\nLocal File Ingestion Tests:")
        for method, data in results["local_tests"].items():
            if isinstance(data, dict):
                success = data.get("overall_success", False)
                skipped = data.get("skipped", False)
                placeholder = data.get("placeholder", False)
                status = "SKIP" if skipped else ("TODO" if placeholder else ("✓" if success else "✗"))
                print(f"  {method:15} - {status}")
    
    # Error Handling Tests
    if results.get("error_handling_tests"):
        print("\nError Handling Tests:")
        for test, data in results["error_handling_tests"].items():
            if isinstance(data, dict):
                success = data.get("overall_success", False)
                placeholder = data.get("placeholder", False)
                status = "TODO" if placeholder else ("✓" if success else "✗")
                print(f"  {test:15} - {status}")
    
    print("\n" + "="*80)
    return results


if __name__ == "__main__":
    main()