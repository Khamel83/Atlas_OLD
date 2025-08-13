#!/usr/bin/env python3
"""
Performance Benchmarking Suite

Comprehensive benchmarking of all ingestion components:
- Transcription speed across models and file sizes
- Network throughput for API-based ingestion
- Local file processing rates
- Memory and CPU usage patterns
- Scalability testing with concurrent operations
"""

import os
import json
import time
import psutil
import threading
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import statistics
import concurrent.futures
from dataclasses import dataclass

from helpers.config import load_config
from helpers.enhanced_transcription import EnhancedTranscriptionEngine, WhisperModel
from helpers.podcast_ingestor import PodcastIngestor
from helpers.youtube_ingestor import YouTubeIngestor
from helpers.document_ingestor import DocumentIngestor
from helpers.utils import log_info, log_error


@dataclass
class PerformanceMetrics:
    """Container for performance metrics"""
    start_time: float
    end_time: float
    duration: float
    cpu_usage_start: float
    cpu_usage_end: float
    memory_usage_start: float
    memory_usage_end: float
    peak_memory_usage: float
    items_processed: int
    bytes_processed: int
    success_rate: float
    errors: List[str]
    
    @property
    def items_per_second(self) -> float:
        return self.items_processed / self.duration if self.duration > 0 else 0
    
    @property
    def bytes_per_second(self) -> float:
        return self.bytes_processed / self.duration if self.duration > 0 else 0
    
    @property
    def mb_per_second(self) -> float:
        return self.bytes_per_second / (1024 * 1024)


class SystemMonitor:
    """Monitor system resources during operations"""
    
    def __init__(self):
        self.monitoring = False
        self.cpu_samples = []
        self.memory_samples = []
        self.start_time = 0
        
    def start_monitoring(self):
        """Start monitoring system resources"""
        self.monitoring = True
        self.cpu_samples = []
        self.memory_samples = []
        self.start_time = time.time()
        
        def monitor_loop():
            while self.monitoring:
                cpu_percent = psutil.cpu_percent(interval=0.1)
                memory_info = psutil.virtual_memory()
                
                self.cpu_samples.append({
                    'timestamp': time.time() - self.start_time,
                    'cpu_percent': cpu_percent
                })
                
                self.memory_samples.append({
                    'timestamp': time.time() - self.start_time,
                    'memory_used_mb': memory_info.used / (1024 * 1024),
                    'memory_percent': memory_info.percent
                })
                
                time.sleep(1)  # Sample every second
        
        self.monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        self.monitor_thread.start()
    
    def stop_monitoring(self) -> Dict[str, Any]:
        """Stop monitoring and return statistics"""
        self.monitoring = False
        
        if hasattr(self, 'monitor_thread'):
            self.monitor_thread.join(timeout=2)
        
        cpu_values = [s['cpu_percent'] for s in self.cpu_samples]
        memory_values = [s['memory_used_mb'] for s in self.memory_samples]
        
        return {
            'cpu_stats': {
                'avg': statistics.mean(cpu_values) if cpu_values else 0,
                'max': max(cpu_values) if cpu_values else 0,
                'min': min(cpu_values) if cpu_values else 0,
                'samples': len(cpu_values)
            },
            'memory_stats': {
                'avg_mb': statistics.mean(memory_values) if memory_values else 0,
                'max_mb': max(memory_values) if memory_values else 0,
                'min_mb': min(memory_values) if memory_values else 0,
                'samples': len(memory_values)
            },
            'raw_samples': {
                'cpu': self.cpu_samples,
                'memory': self.memory_samples
            }
        }


class PerformanceBenchmarker:
    """Comprehensive performance benchmarking system"""
    
    def __init__(self):
        self.config = load_config()
        self.test_dir = Path("testing/performance")
        self.test_dir.mkdir(parents=True, exist_ok=True)
        
        self.log_path = self.test_dir / "performance_benchmark.log"
        
        self.benchmark_results = {
            "timestamp": datetime.now().isoformat(),
            "system_info": self._get_system_info(),
            "transcription_benchmarks": {},
            "ingestion_benchmarks": {},
            "scalability_benchmarks": {},
            "resource_usage_analysis": {},
            "performance_recommendations": {}
        }
        
        self.transcription_engine = EnhancedTranscriptionEngine(self.config)
    
    def run_comprehensive_benchmarks(self) -> Dict[str, Any]:
        """Run all performance benchmarks"""
        log_info(str(self.log_path), "Starting comprehensive performance benchmarking")
        
        # Benchmark transcription performance
        self._benchmark_transcription_performance()
        
        # Benchmark ingestion methods
        self._benchmark_ingestion_methods()
        
        # Benchmark scalability
        self._benchmark_scalability()
        
        # Analyze resource usage patterns
        self._analyze_resource_usage()
        
        # Generate performance recommendations
        self._generate_performance_recommendations()
        
        # Save results
        results_file = self.test_dir / f"performance_benchmark_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w') as f:
            json.dump(self.benchmark_results, f, indent=2)
        
        log_info(str(self.log_path), f"Performance benchmarking complete. Results: {results_file}")
        return self.benchmark_results
    
    def _get_system_info(self) -> Dict[str, Any]:
        """Get system information for benchmark context"""
        try:
            return {
                "cpu_count": psutil.cpu_count(),
                "cpu_count_logical": psutil.cpu_count(logical=True),
                "memory_total_gb": psutil.virtual_memory().total / (1024**3),
                "disk_usage": {
                    "total_gb": psutil.disk_usage('/').total / (1024**3),
                    "free_gb": psutil.disk_usage('/').free / (1024**3)
                },
                "python_version": os.sys.version,
                "platform": os.name
            }
        except Exception as e:
            log_error(str(self.log_path), f"Failed to get system info: {e}")
            return {}
    
    def _benchmark_transcription_performance(self) -> None:
        """Benchmark transcription performance across models and file sizes"""
        log_info(str(self.log_path), "Benchmarking transcription performance")
        
        # Get test audio files of different sizes
        test_files = self._get_test_audio_files()
        
        if not test_files:
            log_error(str(self.log_path), "No test audio files available for transcription benchmarks")
            return
        
        transcription_results = {}
        
        # Test each model with each file size
        for model in [WhisperModel.TINY, WhisperModel.SMALL, WhisperModel.MEDIUM]:
            model_name = f"whisper_{model.value}"
            model_results = {}
            
            for file_path, file_info in test_files.items():
                log_info(str(self.log_path), f"Benchmarking {model_name} with {file_info['size_category']}")
                
                # Run benchmark with monitoring
                monitor = SystemMonitor()
                monitor.start_monitoring()
                
                start_time = time.time()
                start_memory = psutil.virtual_memory().used
                start_cpu = psutil.cpu_percent()
                
                try:
                    result = self.transcription_engine.transcribe_whisper_local(
                        file_path, model.value, str(self.log_path)
                    )
                    
                    end_time = time.time()
                    end_memory = psutil.virtual_memory().used
                    end_cpu = psutil.cpu_percent()
                    
                    system_stats = monitor.stop_monitoring()
                    
                    metrics = PerformanceMetrics(
                        start_time=start_time,
                        end_time=end_time,
                        duration=end_time - start_time,
                        cpu_usage_start=start_cpu,
                        cpu_usage_end=end_cpu,
                        memory_usage_start=start_memory / (1024**2),  # MB
                        memory_usage_end=end_memory / (1024**2),      # MB
                        peak_memory_usage=system_stats['memory_stats']['max_mb'],
                        items_processed=1,
                        bytes_processed=file_info['size_bytes'],
                        success_rate=1.0 if result.text else 0.0,
                        errors=[result.error] if result.error else []
                    )
                    
                    model_results[file_info['size_category']] = {
                        "file_size_mb": file_info['size_mb'],
                        "duration_seconds": metrics.duration,
                        "transcription_duration": result.duration_seconds,
                        "word_count": result.word_count,
                        "words_per_second": result.word_count / metrics.duration if metrics.duration > 0 else 0,
                        "mb_per_second": metrics.mb_per_second,
                        "realtime_factor": metrics.duration / file_info.get('audio_duration_estimate', metrics.duration),
                        "memory_usage": {
                            "start_mb": metrics.memory_usage_start,
                            "end_mb": metrics.memory_usage_end,
                            "peak_mb": metrics.peak_memory_usage,
                            "delta_mb": metrics.memory_usage_end - metrics.memory_usage_start
                        },
                        "cpu_usage": system_stats['cpu_stats'],
                        "success": metrics.success_rate > 0,
                        "errors": metrics.errors
                    }
                    
                except Exception as e:
                    monitor.stop_monitoring()
                    log_error(str(self.log_path), f"Transcription benchmark failed: {e}")
                    model_results[file_info['size_category']] = {
                        "error": str(e),
                        "success": False
                    }
            
            transcription_results[model_name] = model_results
        
        self.benchmark_results["transcription_benchmarks"] = transcription_results
    
    def _benchmark_ingestion_methods(self) -> None:
        """Benchmark different ingestion methods"""
        log_info(str(self.log_path), "Benchmarking ingestion methods")
        
        ingestion_results = {}
        
        # Benchmark podcast ingestion
        ingestion_results["podcast_ingestion"] = self._benchmark_podcast_ingestion()
        
        # Benchmark document ingestion
        ingestion_results["document_ingestion"] = self._benchmark_document_ingestion()
        
        # Benchmark YouTube ingestion (if available)
        ingestion_results["youtube_ingestion"] = self._benchmark_youtube_ingestion()
        
        self.benchmark_results["ingestion_benchmarks"] = ingestion_results
    
    def _benchmark_scalability(self) -> None:
        """Benchmark scalability with concurrent operations"""
        log_info(str(self.log_path), "Benchmarking scalability")
        
        scalability_results = {}
        
        # Test concurrent transcription
        scalability_results["concurrent_transcription"] = self._benchmark_concurrent_transcription()
        
        # Test concurrent ingestion
        scalability_results["concurrent_ingestion"] = self._benchmark_concurrent_ingestion()
        
        self.benchmark_results["scalability_benchmarks"] = scalability_results
    
    def _get_test_audio_files(self) -> Dict[str, Dict[str, Any]]:
        """Get test audio files categorized by size"""
        test_files = {}
        
        # Look for existing audio files
        audio_dirs = [
            "test_data/audio",
            "output/podcasts/audio",
            "test_data/ground_truth",
            "testing/temp"
        ]
        
        for audio_dir in audio_dirs:
            if os.path.exists(audio_dir):
                for file in os.listdir(audio_dir):
                    if file.endswith(('.mp3', '.wav', '.m4a')):
                        file_path = os.path.join(audio_dir, file)
                        file_size = os.path.getsize(file_path)
                        size_mb = file_size / (1024 * 1024)
                        
                        # Categorize by size
                        if size_mb < 5:
                            size_category = "small"
                        elif size_mb < 20:
                            size_category = "medium"
                        else:
                            size_category = "large"
                        
                        # Only keep one file per category for benchmarking
                        if size_category not in test_files:
                            test_files[file_path] = {
                                "size_bytes": file_size,
                                "size_mb": size_mb,
                                "size_category": size_category,
                                "audio_duration_estimate": size_mb * 60 / 1.5  # Rough estimate: 1.5MB per minute
                            }
        
        # If no files found, create minimal test files
        if not test_files:
            test_files = self._create_minimal_test_audio()
        
        return test_files
    
    def _create_minimal_test_audio(self) -> Dict[str, Dict[str, Any]]:
        """Create minimal test audio files for benchmarking"""
        # This would create small test audio files using TTS if available
        # For now, return empty dict if no audio files are available
        log_info(str(self.log_path), "No test audio files found, skipping audio benchmarks")
        return {}
    
    def _benchmark_podcast_ingestion(self) -> Dict[str, Any]:
        """Benchmark podcast ingestion performance"""
        try:
            monitor = SystemMonitor()
            monitor.start_monitoring()
            
            start_time = time.time()
            
            # Test with limited episodes for benchmarking
            ingestor = PodcastIngestor(self.config)
            
            # Use a known fast feed for testing
            test_feed = "https://feeds.simplecast.com/54nAGcIl"  # The Daily - usually fast
            
            success = ingestor.process_feed(test_feed)
            
            end_time = time.time()
            system_stats = monitor.stop_monitoring()
            
            return {
                "duration_seconds": end_time - start_time,
                "success": success,
                "system_stats": system_stats,
                "feed_tested": test_feed
            }
            
        except Exception as e:
            return {"error": str(e), "success": False}
    
    def _benchmark_document_ingestion(self) -> Dict[str, Any]:
        """Benchmark document ingestion performance"""
        try:
            # Create test documents of various sizes
            test_docs = self._create_test_documents_for_benchmark()
            
            if not test_docs:
                return {"error": "No test documents available", "success": False}
            
            ingestor = DocumentIngestor(self.config)
            results = []
            
            for doc_path, doc_info in test_docs.items():
                monitor = SystemMonitor()
                monitor.start_monitoring()
                
                start_time = time.time()
                
                try:
                    success = ingestor.ingest_document(doc_path)
                    end_time = time.time()
                    system_stats = monitor.stop_monitoring()
                    
                    results.append({
                        "document_size_mb": doc_info["size_mb"],
                        "duration_seconds": end_time - start_time,
                        "mb_per_second": doc_info["size_mb"] / (end_time - start_time) if end_time > start_time else 0,
                        "success": success,
                        "system_stats": system_stats
                    })
                    
                except Exception as e:
                    monitor.stop_monitoring()
                    results.append({
                        "document_size_mb": doc_info["size_mb"],
                        "error": str(e),
                        "success": False
                    })
                
                # Clean up test document
                if os.path.exists(doc_path):
                    os.remove(doc_path)
            
            return {
                "results": results,
                "total_documents": len(results),
                "successful_documents": sum(1 for r in results if r.get("success", False))
            }
            
        except Exception as e:
            return {"error": str(e), "success": False}
    
    def _benchmark_youtube_ingestion(self) -> Dict[str, Any]:
        """Benchmark YouTube ingestion performance"""
        try:
            monitor = SystemMonitor()
            monitor.start_monitoring()
            
            start_time = time.time()
            
            ingestor = YouTubeIngestor(self.config)
            
            # Use a short, safe video for testing
            test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            
            success = ingestor.ingest_single_video(test_url)
            
            end_time = time.time()
            system_stats = monitor.stop_monitoring()
            
            return {
                "duration_seconds": end_time - start_time,
                "success": success,
                "system_stats": system_stats,
                "video_tested": test_url
            }
            
        except Exception as e:
            return {"error": str(e), "success": False}
    
    def _benchmark_concurrent_transcription(self) -> Dict[str, Any]:
        """Benchmark concurrent transcription operations"""
        test_files = self._get_test_audio_files()
        
        if not test_files:
            return {"error": "No test audio files available", "success": False}
        
        # Test different concurrency levels
        concurrency_levels = [1, 2, 4]
        results = {}
        
        for concurrency in concurrency_levels:
            if concurrency > len(test_files):
                continue
                
            log_info(str(self.log_path), f"Testing concurrency level: {concurrency}")
            
            monitor = SystemMonitor()
            monitor.start_monitoring()
            
            start_time = time.time()
            
            # Run concurrent transcriptions
            with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
                futures = []
                file_list = list(test_files.items())[:concurrency]
                
                for file_path, file_info in file_list:
                    future = executor.submit(
                        self.transcription_engine.transcribe_whisper_local,
                        file_path, WhisperModel.TINY.value, str(self.log_path)
                    )
                    futures.append(future)
                
                # Wait for all to complete
                concurrent_results = []
                for future in concurrent.futures.as_completed(futures):
                    try:
                        result = future.result()
                        concurrent_results.append(result)
                    except Exception as e:
                        log_error(str(self.log_path), f"Concurrent transcription failed: {e}")
            
            end_time = time.time()
            system_stats = monitor.stop_monitoring()
            
            results[f"concurrency_{concurrency}"] = {
                "duration_seconds": end_time - start_time,
                "files_processed": len(concurrent_results),
                "successful_transcriptions": sum(1 for r in concurrent_results if r.text),
                "system_stats": system_stats,
                "average_cpu_usage": system_stats['cpu_stats']['avg'],
                "peak_memory_mb": system_stats['memory_stats']['max_mb']
            }
        
        return results
    
    def _benchmark_concurrent_ingestion(self) -> Dict[str, Any]:
        """Benchmark concurrent ingestion operations"""
        # This would test concurrent document/podcast ingestion
        # For now, return placeholder
        return {"note": "Concurrent ingestion benchmark placeholder"}
    
    def _create_test_documents_for_benchmark(self) -> Dict[str, Dict[str, Any]]:
        """Create test documents of various sizes for benchmarking"""
        test_docs = {}
        
        # Create documents of different sizes
        sizes = {
            "small": 1000,    # 1KB
            "medium": 100000, # 100KB
            "large": 1000000  # 1MB
        }
        
        for size_name, size_bytes in sizes.items():
            doc_path = self.test_dir / f"benchmark_doc_{size_name}.txt"
            
            # Create content of specified size
            content = "This is test content for benchmarking document ingestion performance. " * (size_bytes // 70)
            content = content[:size_bytes]  # Trim to exact size
            
            with open(doc_path, 'w') as f:
                f.write(content)
            
            test_docs[str(doc_path)] = {
                "size_bytes": size_bytes,
                "size_mb": size_bytes / (1024 * 1024),
                "size_category": size_name
            }
        
        return test_docs
    
    def _analyze_resource_usage(self) -> None:
        """Analyze resource usage patterns across benchmarks"""
        log_info(str(self.log_path), "Analyzing resource usage patterns")
        
        # Aggregate resource usage data from all benchmarks
        cpu_usage_data = []
        memory_usage_data = []
        
        # Collect from transcription benchmarks
        for model_data in self.benchmark_results.get("transcription_benchmarks", {}).values():
            for size_data in model_data.values():
                if isinstance(size_data, dict) and "cpu_usage" in size_data:
                    cpu_usage_data.append(size_data["cpu_usage"]["avg"])
                    memory_usage_data.append(size_data["memory_usage"]["peak_mb"])
        
        # Analyze patterns
        resource_analysis = {}
        
        if cpu_usage_data:
            resource_analysis["cpu_analysis"] = {
                "average_usage": statistics.mean(cpu_usage_data),
                "peak_usage": max(cpu_usage_data),
                "usage_variance": statistics.variance(cpu_usage_data) if len(cpu_usage_data) > 1 else 0
            }
        
        if memory_usage_data:
            resource_analysis["memory_analysis"] = {
                "average_peak_mb": statistics.mean(memory_usage_data),
                "maximum_peak_mb": max(memory_usage_data),
                "memory_variance": statistics.variance(memory_usage_data) if len(memory_usage_data) > 1 else 0
            }
        
        self.benchmark_results["resource_usage_analysis"] = resource_analysis
    
    def _generate_performance_recommendations(self) -> None:
        """Generate performance optimization recommendations"""
        recommendations = {
            "transcription_optimization": [],
            "resource_optimization": [],
            "scalability_recommendations": [],
            "general_recommendations": []
        }
        
        # Analyze transcription performance
        transcription_benchmarks = self.benchmark_results.get("transcription_benchmarks", {})
        
        if transcription_benchmarks:
            # Find fastest model
            model_speeds = {}
            for model, data in transcription_benchmarks.items():
                if isinstance(data, dict):
                    speeds = []
                    for size_data in data.values():
                        if isinstance(size_data, dict) and "words_per_second" in size_data:
                            speeds.append(size_data["words_per_second"])
                    if speeds:
                        model_speeds[model] = statistics.mean(speeds)
            
            if model_speeds:
                fastest_model = max(model_speeds, key=model_speeds.get)
                recommendations["transcription_optimization"].append(
                    f"Use {fastest_model} for fastest transcription ({model_speeds[fastest_model]:.1f} words/sec avg)"
                )
        
        # Resource usage recommendations
        resource_analysis = self.benchmark_results.get("resource_usage_analysis", {})
        
        if resource_analysis.get("cpu_analysis", {}).get("peak_usage", 0) > 90:
            recommendations["resource_optimization"].append(
                "High CPU usage detected - consider reducing concurrent operations"
            )
        
        if resource_analysis.get("memory_analysis", {}).get("maximum_peak_mb", 0) > 2000:  # 2GB
            recommendations["resource_optimization"].append(
                "High memory usage detected - consider processing smaller batches"
            )
        
        # General recommendations
        recommendations["general_recommendations"].extend([
            "Monitor system resources during bulk processing operations",
            "Consider batch processing for large volumes of content",
            "Use faster models for initial processing, higher quality for important content",
            "Implement queue-based processing for better resource management"
        ])
        
        self.benchmark_results["performance_recommendations"] = recommendations


def main():
    """Run performance benchmarking"""
    benchmarker = PerformanceBenchmarker()
    results = benchmarker.run_comprehensive_benchmarks()
    
    print("\n" + "="*80)
    print("PERFORMANCE BENCHMARK RESULTS")
    print("="*80)
    
    print(f"\nBenchmark completed at: {results['timestamp']}")
    
    # System info
    if results.get("system_info"):
        sys_info = results["system_info"]
        print(f"\nSystem Information:")
        print(f"  CPU Cores: {sys_info.get('cpu_count', 'N/A')} physical, {sys_info.get('cpu_count_logical', 'N/A')} logical")
        print(f"  Memory: {sys_info.get('memory_total_gb', 0):.1f} GB")
        print(f"  Disk Space: {sys_info.get('disk_usage', {}).get('free_gb', 0):.1f} GB free")
    
    # Transcription benchmarks
    if results.get("transcription_benchmarks"):
        print(f"\n⚡ Transcription Performance:")
        for model, data in results["transcription_benchmarks"].items():
            print(f"\n  {model}:")
            for size, metrics in data.items():
                if isinstance(metrics, dict) and "words_per_second" in metrics:
                    wps = metrics["words_per_second"]
                    duration = metrics["duration_seconds"]
                    mb_per_sec = metrics.get("mb_per_second", 0)
                    print(f"    {size:8} - {wps:6.1f} words/sec, {mb_per_sec:5.1f} MB/sec, {duration:5.1f}s total")
    
    # Resource usage analysis
    if results.get("resource_usage_analysis"):
        resource_analysis = results["resource_usage_analysis"]
        print(f"\n📊 Resource Usage Analysis:")
        
        if "cpu_analysis" in resource_analysis:
            cpu = resource_analysis["cpu_analysis"]
            print(f"  CPU Usage: {cpu.get('average_usage', 0):.1f}% avg, {cpu.get('peak_usage', 0):.1f}% peak")
        
        if "memory_analysis" in resource_analysis:
            memory = resource_analysis["memory_analysis"]
            print(f"  Memory Usage: {memory.get('average_peak_mb', 0):.1f} MB avg peak, {memory.get('maximum_peak_mb', 0):.1f} MB max")
    
    # Performance recommendations
    if results.get("performance_recommendations"):
        recs = results["performance_recommendations"]
        
        print(f"\n💡 Performance Recommendations:")
        
        for rec in recs.get("transcription_optimization", []):
            print(f"  🎤 {rec}")
        
        for rec in recs.get("resource_optimization", []):
            print(f"  💾 {rec}")
        
        for rec in recs.get("general_recommendations", []):
            print(f"  ⚙️  {rec}")
    
    print("\n" + "="*80)
    return results


if __name__ == "__main__":
    main()