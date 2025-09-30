#!/usr/bin/env python3
"""
Search Quality Analysis for Transcription Accuracy

Tests how different transcription accuracies affect search quality and retrieval.
Determines the minimum transcription quality needed for effective search.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import statistics

from helpers.config import load_config
from helpers.search_engine import SearchEngine
from helpers.utils import log_info, log_error


class SearchQualityAnalyzer:
    """Analyze search quality across different transcription accuracies"""

    def __init__(self):
        self.config = load_config()
        self.test_dir = Path("testing/search_quality")
        self.test_dir.mkdir(parents=True, exist_ok=True)

        self.log_path = self.test_dir / "search_quality.log"

        # Test queries categorized by difficulty
        self.test_queries = {
            "exact_phrases": [
                "artificial intelligence",
                "machine learning",
                "data science",
                "natural language processing",
                "deep learning"
            ],
            "technical_terms": [
                "neural networks",
                "transformer architecture",
                "gradient descent",
                "backpropagation",
                "convolutional neural network"
            ],
            "conceptual_queries": [
                "how AI works",
                "benefits of automation",
                "future of technology",
                "ethical implications",
                "societal impact"
            ],
            "partial_matches": [
                "AI revolution",
                "tech innovation",
                "digital transformation",
                "algorithmic bias",
                "human computer interaction"
            ]
        }

        # Search quality metrics
        self.quality_metrics = [
            "relevance_score",
            "result_count",
            "top_result_accuracy",
            "precision_at_5",
            "precision_at_10",
            "average_ranking"
        ]

        self.test_results = {
            "timestamp": datetime.now().isoformat(),
            "transcription_models_tested": [],
            "query_categories": list(self.test_queries.keys()),
            "search_results": {},
            "quality_analysis": {},
            "transcription_threshold_analysis": {},
            "recommendations": {}
        }

    def run_search_quality_analysis(self) -> Dict[str, Any]:
        """Run comprehensive search quality analysis"""
        log_info(str(self.log_path), "Starting search quality analysis")

        # Initialize search engine
        search_engine = SearchEngine(self.config)

        # Get test content with different transcription qualities
        test_content = self._prepare_test_content()

        if not test_content:
            log_error(str(self.log_path), "No test content available for search quality analysis")
            return self.test_results

        # Test each transcription quality level
        for quality_level, content_data in test_content.items():
            log_info(str(self.log_path), f"Testing search quality for: {quality_level}")

            # Index the content with this quality level
            self._index_test_content(search_engine, content_data, quality_level)

            # Run all test queries
            search_results = self._run_search_tests(search_engine, quality_level)
            self.test_results["search_results"][quality_level] = search_results

        # Analyze results
        self._analyze_search_quality()
        self._analyze_transcription_thresholds()
        self._generate_search_recommendations()

        # Save results
        results_file = self.test_dir / f"search_quality_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(results_file, 'w') as f:
            json.dump(self.test_results, f, indent=2)

        log_info(str(self.log_path), f"Search quality analysis complete. Results: {results_file}")
        return self.test_results

    def _prepare_test_content(self) -> Dict[str, List[Dict[str, Any]]]:
        """Prepare test content with different transcription quality levels"""
        log_info(str(self.log_path), "Preparing test content with varied transcription quality")

        # Look for existing transcribed content
        content_sources = [
            "output/podcasts/transcripts",
            "test_data/ground_truth",
            "output/youtube/transcripts"
        ]

        base_content = []
        for source_dir in content_sources:
            if os.path.exists(source_dir):
                for file in os.listdir(source_dir):
                    if file.endswith('.txt'):
                        file_path = os.path.join(source_dir, file)
                        try:
                            with open(file_path, 'r') as f:
                                content = f.read().strip()
                                if len(content) > 100:  # Minimum content length
                                    base_content.append({
                                        "id": file.replace('.txt', ''),
                                        "content": content,
                                        "source": source_dir,
                                        "word_count": len(content.split())
                                    })
                        except Exception as e:
                            log_error(str(self.log_path), f"Failed to read {file_path}: {e}")

        if not base_content:
            # Create synthetic test content if no real content available
            base_content = self._create_synthetic_test_content()

        # Generate different quality levels from base content
        quality_levels = {
            "perfect": base_content,  # Original content
            "high_quality": [],       # 95% accuracy simulation
            "medium_quality": [],     # 85% accuracy simulation
            "low_quality": [],        # 70% accuracy simulation
            "very_low_quality": []    # 50% accuracy simulation
        }

        # Simulate transcription errors for different quality levels
        for content_item in base_content:
            original_text = content_item["content"]

            # High quality (95% accuracy) - minor errors
            high_quality_text = self._simulate_transcription_errors(original_text, error_rate=0.05)
            quality_levels["high_quality"].append({
                **content_item,
                "content": high_quality_text,
                "quality_level": "high_quality",
                "simulated_accuracy": 0.95
            })

            # Medium quality (85% accuracy) - moderate errors
            medium_quality_text = self._simulate_transcription_errors(original_text, error_rate=0.15)
            quality_levels["medium_quality"].append({
                **content_item,
                "content": medium_quality_text,
                "quality_level": "medium_quality",
                "simulated_accuracy": 0.85
            })

            # Low quality (70% accuracy) - significant errors
            low_quality_text = self._simulate_transcription_errors(original_text, error_rate=0.30)
            quality_levels["low_quality"].append({
                **content_item,
                "content": low_quality_text,
                "quality_level": "low_quality",
                "simulated_accuracy": 0.70
            })

            # Very low quality (50% accuracy) - heavy errors
            very_low_quality_text = self._simulate_transcription_errors(original_text, error_rate=0.50)
            quality_levels["very_low_quality"].append({
                **content_item,
                "content": very_low_quality_text,
                "quality_level": "very_low_quality",
                "simulated_accuracy": 0.50
            })

        log_info(str(self.log_path), f"Prepared {len(base_content)} content items at {len(quality_levels)} quality levels")
        return quality_levels

    def _create_synthetic_test_content(self) -> List[Dict[str, Any]]:
        """Create synthetic test content for search testing"""
        synthetic_content = [
            {
                "id": "ai_overview",
                "content": """
                Artificial intelligence represents a revolutionary approach to problem solving and automation.
                Machine learning algorithms enable computers to learn from data without explicit programming.
                Deep learning neural networks have transformed natural language processing and computer vision.
                The future of AI includes advances in transformer architectures and large language models.
                Ethical considerations around algorithmic bias and fairness remain critical challenges.
                """,
                "source": "synthetic",
                "word_count": 53
            },
            {
                "id": "tech_innovation",
                "content": """
                Technology innovation drives digital transformation across industries and society.
                Automation and robotics are reshaping manufacturing and service sectors globally.
                Data science and analytics provide insights for better decision making processes.
                Cloud computing and distributed systems enable scalable applications and services.
                Cybersecurity measures protect against evolving threats in our connected world.
                """,
                "source": "synthetic",
                "word_count": 51
            },
            {
                "id": "human_computer_interaction",
                "content": """
                Human computer interaction focuses on designing intuitive and accessible interfaces.
                User experience research informs the development of user-friendly applications.
                Voice assistants and conversational AI improve natural communication with machines.
                Augmented reality and virtual reality create immersive digital experiences.
                Accessibility features ensure technology works for users with diverse abilities.
                """,
                "source": "synthetic",
                "word_count": 50
            }
        ]

        return synthetic_content

    def _simulate_transcription_errors(self, text: str, error_rate: float) -> str:
        """Simulate common transcription errors at a given error rate"""
        import random

        words = text.split()
        total_words = len(words)
        errors_to_introduce = int(total_words * error_rate)

        # Common transcription error patterns
        error_patterns = [
            # Homophones
            {"from": "there", "to": "their"},
            {"from": "to", "to": "too"},
            {"from": "your", "to": "you're"},
            {"from": "its", "to": "it's"},
            # Common mishearings
            {"from": "and", "to": "an"},
            {"from": "the", "to": "thee"},
            {"from": "a", "to": "uh"},
            # Technical term errors
            {"from": "neural", "to": "neural"},
            {"from": "algorithm", "to": "algorith"},
            {"from": "machine", "to": "machien"},
            # Missing words (represented as empty)
            {"from": "of", "to": ""},
            {"from": "in", "to": ""},
            {"from": "for", "to": ""},
        ]

        # Randomly introduce errors
        error_positions = random.sample(range(total_words), min(errors_to_introduce, total_words))

        for pos in error_positions:
            original_word = words[pos].lower()

            # Try to apply a pattern-based error
            error_applied = False
            for pattern in error_patterns:
                if pattern["from"] in original_word:
                    words[pos] = original_word.replace(pattern["from"], pattern["to"])
                    error_applied = True
                    break

            # If no pattern matched, introduce random character errors
            if not error_applied and len(words[pos]) > 2:
                word_chars = list(words[pos])
                # Random character substitution, deletion, or insertion
                error_type = random.choice(["substitute", "delete", "insert"])

                if error_type == "substitute" and len(word_chars) > 1:
                    char_pos = random.randint(0, len(word_chars) - 1)
                    word_chars[char_pos] = random.choice("abcdefghijklmnopqrstuvwxyz")
                elif error_type == "delete" and len(word_chars) > 2:
                    char_pos = random.randint(0, len(word_chars) - 1)
                    word_chars.pop(char_pos)
                elif error_type == "insert":
                    char_pos = random.randint(0, len(word_chars))
                    word_chars.insert(char_pos, random.choice("abcdefghijklmnopqrstuvwxyz"))

                words[pos] = "".join(word_chars)

        return " ".join(words)

    def _index_test_content(self, search_engine: SearchEngine, content_data: List[Dict[str, Any]], quality_level: str) -> None:
        """Index test content for search testing"""
        log_info(str(self.log_path), f"Indexing {len(content_data)} items for quality level: {quality_level}")

        # For this test, we'll simulate indexing by storing content
        # In a real implementation, this would add to the search index
        # For now, we'll store the content for manual search simulation

        index_file = self.test_dir / f"test_index_{quality_level}.json"
        with open(index_file, 'w') as f:
            json.dump(content_data, f, indent=2)

    def _run_search_tests(self, search_engine: SearchEngine, quality_level: str) -> Dict[str, Any]:
        """Run search tests for a specific quality level"""
        log_info(str(self.log_path), f"Running search tests for quality level: {quality_level}")

        results = {
            "quality_level": quality_level,
            "query_results": {},
            "performance_metrics": {}
        }

        # Load the indexed content for this quality level
        index_file = self.test_dir / f"test_index_{quality_level}.json"
        if not index_file.exists():
            return results

        with open(index_file, 'r') as f:
            indexed_content = json.load(f)

        # Test each query category
        for category, queries in self.test_queries.items():
            category_results = []

            for query in queries:
                query_result = self._test_single_query(query, indexed_content, category)
                category_results.append(query_result)

            results["query_results"][category] = category_results

        # Calculate performance metrics
        results["performance_metrics"] = self._calculate_search_metrics(results["query_results"])

        return results

    def _test_single_query(self, query: str, indexed_content: List[Dict[str, Any]], category: str) -> Dict[str, Any]:
        """Test a single search query against indexed content"""
        # Simple search implementation for testing
        # In production, this would use the actual search engine

        query_words = set(query.lower().split())
        matches = []

        for item in indexed_content:
            content_words = set(item["content"].lower().split())

            # Calculate relevance score based on word overlap
            overlap = len(query_words.intersection(content_words))
            total_query_words = len(query_words)

            if overlap > 0:
                relevance_score = overlap / total_query_words
                matches.append({
                    "item_id": item["id"],
                    "relevance_score": relevance_score,
                    "word_overlap": overlap,
                    "content_snippet": item["content"][:200] + "...",
                    "quality_level": item.get("quality_level", "unknown")
                })

        # Sort by relevance score
        matches.sort(key=lambda x: x["relevance_score"], reverse=True)

        return {
            "query": query,
            "category": category,
            "total_matches": len(matches),
            "top_matches": matches[:10],  # Top 10 results
            "has_relevant_results": len(matches) > 0,
            "top_relevance_score": matches[0]["relevance_score"] if matches else 0
        }

    def _calculate_search_metrics(self, query_results: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
        """Calculate search performance metrics"""
        metrics = {
            "overall_metrics": {},
            "category_metrics": {}
        }

        all_queries = []
        for category, results in query_results.items():
            all_queries.extend(results)

            # Category-specific metrics
            category_metrics = {
                "total_queries": len(results),
                "queries_with_results": sum(1 for r in results if r["has_relevant_results"]),
                "average_result_count": statistics.mean([r["total_matches"] for r in results]),
                "average_top_relevance": statistics.mean([r["top_relevance_score"] for r in results]),
                "success_rate": sum(1 for r in results if r["has_relevant_results"]) / len(results) if results else 0
            }

            metrics["category_metrics"][category] = category_metrics

        # Overall metrics
        if all_queries:
            metrics["overall_metrics"] = {
                "total_queries_tested": len(all_queries),
                "queries_with_results": sum(1 for r in all_queries if r["has_relevant_results"]),
                "overall_success_rate": sum(1 for r in all_queries if r["has_relevant_results"]) / len(all_queries),
                "average_result_count": statistics.mean([r["total_matches"] for r in all_queries]),
                "average_relevance_score": statistics.mean([r["top_relevance_score"] for r in all_queries])
            }

        return metrics

    def _analyze_search_quality(self) -> None:
        """Analyze search quality across different transcription levels"""
        log_info(str(self.log_path), "Analyzing search quality across transcription levels")

        quality_analysis = {}

        # Compare metrics across quality levels
        for quality_level, results in self.test_results["search_results"].items():
            if "performance_metrics" in results:
                overall_metrics = results["performance_metrics"].get("overall_metrics", {})

                quality_analysis[quality_level] = {
                    "success_rate": overall_metrics.get("overall_success_rate", 0),
                    "average_relevance": overall_metrics.get("average_relevance_score", 0),
                    "average_result_count": overall_metrics.get("average_result_count", 0),
                    "queries_tested": overall_metrics.get("total_queries_tested", 0)
                }

        # Calculate quality degradation
        if "perfect" in quality_analysis:
            perfect_success_rate = quality_analysis["perfect"]["success_rate"]
            perfect_relevance = quality_analysis["perfect"]["average_relevance"]

            for quality_level, metrics in quality_analysis.items():
                if quality_level != "perfect":
                    success_degradation = (perfect_success_rate - metrics["success_rate"]) / perfect_success_rate if perfect_success_rate > 0 else 0
                    relevance_degradation = (perfect_relevance - metrics["average_relevance"]) / perfect_relevance if perfect_relevance > 0 else 0

                    quality_analysis[quality_level]["success_degradation"] = success_degradation
                    quality_analysis[quality_level]["relevance_degradation"] = relevance_degradation

        self.test_results["quality_analysis"] = quality_analysis

    def _analyze_transcription_thresholds(self) -> None:
        """Analyze transcription accuracy thresholds for acceptable search quality"""
        log_info(str(self.log_path), "Analyzing transcription accuracy thresholds")

        quality_analysis = self.test_results.get("quality_analysis", {})

        # Define acceptable quality thresholds
        thresholds = {
            "excellent_search": 0.95,      # 95% of perfect performance
            "good_search": 0.85,           # 85% of perfect performance
            "acceptable_search": 0.70,     # 70% of perfect performance
            "poor_search": 0.50            # 50% of perfect performance
        }

        threshold_analysis = {}

        if "perfect" in quality_analysis:
            perfect_metrics = quality_analysis["perfect"]

            for threshold_name, threshold_value in thresholds.items():
                target_success_rate = perfect_metrics["success_rate"] * threshold_value
                target_relevance = perfect_metrics["average_relevance"] * threshold_value

                # Find quality levels that meet this threshold
                meeting_threshold = []
                for quality_level, metrics in quality_analysis.items():
                    if (metrics["success_rate"] >= target_success_rate and
                        metrics["average_relevance"] >= target_relevance):
                        meeting_threshold.append(quality_level)

                threshold_analysis[threshold_name] = {
                    "target_success_rate": target_success_rate,
                    "target_relevance": target_relevance,
                    "quality_levels_meeting_threshold": meeting_threshold,
                    "minimum_transcription_quality": self._get_minimum_quality_for_threshold(meeting_threshold)
                }

        self.test_results["transcription_threshold_analysis"] = threshold_analysis

    def _get_minimum_quality_for_threshold(self, quality_levels: List[str]) -> Optional[str]:
        """Get the minimum transcription quality that meets the threshold"""
        # Order from lowest to highest quality
        quality_order = ["very_low_quality", "low_quality", "medium_quality", "high_quality", "perfect"]

        for quality in quality_order:
            if quality in quality_levels:
                return quality

        return None

    def _generate_search_recommendations(self) -> None:
        """Generate recommendations based on search quality analysis"""
        recommendations = {
            "transcription_quality_recommendations": [],
            "search_optimization_recommendations": [],
            "use_case_specific_recommendations": {}
        }

        threshold_analysis = self.test_results.get("transcription_threshold_analysis", {})
        quality_analysis = self.test_results.get("quality_analysis", {})

        # Transcription quality recommendations
        if threshold_analysis:
            excellent_threshold = threshold_analysis.get("excellent_search", {})
            good_threshold = threshold_analysis.get("good_search", {})
            acceptable_threshold = threshold_analysis.get("acceptable_search", {})

            if excellent_threshold.get("minimum_transcription_quality"):
                recommendations["transcription_quality_recommendations"].append(
                    f"For excellent search quality, use {excellent_threshold['minimum_transcription_quality']} or better transcription"
                )

            if good_threshold.get("minimum_transcription_quality"):
                recommendations["transcription_quality_recommendations"].append(
                    f"For good search quality, minimum {good_threshold['minimum_transcription_quality']} transcription required"
                )

            if acceptable_threshold.get("minimum_transcription_quality"):
                recommendations["transcription_quality_recommendations"].append(
                    f"For acceptable search results, {acceptable_threshold['minimum_transcription_quality']} transcription is sufficient"
                )

        # Search optimization recommendations
        recommendations["search_optimization_recommendations"].extend([
            "Consider implementing fuzzy search for lower quality transcriptions",
            "Use synonym expansion to handle transcription errors",
            "Implement relevance boosting for exact phrase matches",
            "Consider hybrid search combining multiple quality levels"
        ])

        # Use case specific recommendations
        if quality_analysis:
            high_quality_success = quality_analysis.get("high_quality", {}).get("success_rate", 0)
            medium_quality_success = quality_analysis.get("medium_quality", {}).get("success_rate", 0)

            recommendations["use_case_specific_recommendations"] = {
                "bulk_processing": f"Medium quality transcription ({medium_quality_success:.1%} success rate) may be sufficient for bulk content processing",
                "precise_search": f"High quality transcription ({high_quality_success:.1%} success rate) recommended for precise search requirements",
                "cost_optimization": "Consider using faster/cheaper transcription for initial indexing, higher quality for important content",
                "real_time_search": "Balance transcription speed vs accuracy based on user expectations"
            }

        self.test_results["recommendations"] = recommendations


def main():
    """Run search quality analysis"""
    analyzer = SearchQualityAnalyzer()
    results = analyzer.run_search_quality_analysis()

    print("\n" + "="*80)
    print("SEARCH QUALITY ANALYSIS RESULTS")
    print("="*80)

    print(f"\nAnalysis completed at: {results['timestamp']}")

    # Quality analysis summary
    if results.get("quality_analysis"):
        print("\n📊 Search Performance by Transcription Quality:")
        print(f"{'Quality Level':<18} {'Success Rate':<12} {'Avg Relevance':<14} {'Degradation'}")
        print("-" * 70)

        for quality_level, metrics in results["quality_analysis"].items():
            success_rate = metrics.get("success_rate", 0) * 100
            avg_relevance = metrics.get("average_relevance", 0)
            degradation = metrics.get("success_degradation", 0) * 100

            degradation_str = f"-{degradation:.1f}%" if degradation > 0 else "baseline"

            print(f"{quality_level:<18} {success_rate:>8.1f}%    {avg_relevance:>8.3f}      {degradation_str}")

    # Threshold analysis
    if results.get("transcription_threshold_analysis"):
        print("\n🎯 Transcription Quality Thresholds:")
        for threshold_name, data in results["transcription_threshold_analysis"].items():
            min_quality = data.get("minimum_transcription_quality", "N/A")
            target_success = data.get("target_success_rate", 0) * 100
            print(f"  {threshold_name:18} - Minimum: {min_quality:15} (≥{target_success:.1f}% success)")

    # Recommendations
    if results.get("recommendations"):
        recs = results["recommendations"]

        print("\n💡 Transcription Quality Recommendations:")
        for rec in recs.get("transcription_quality_recommendations", []):
            print(f"  • {rec}")

        print("\n🔍 Search Optimization Recommendations:")
        for rec in recs.get("search_optimization_recommendations", []):
            print(f"  • {rec}")

        if recs.get("use_case_specific_recommendations"):
            print("\n🎯 Use Case Specific Recommendations:")
            for use_case, rec in recs["use_case_specific_recommendations"].items():
                print(f"  {use_case.replace('_', ' ').title()}: {rec}")

    print("\n" + "="*80)
    return results


if __name__ == "__main__":
    main()