#!/usr/bin/env python3
"""
Unified Testing Dashboard

Central dashboard for running and monitoring all ingestion testing:
- Orchestrates all testing modules
- Provides real-time monitoring
- Generates comprehensive reports
- Tracks testing history and trends
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass

from helpers.config import load_config
from helpers.utils import log_info, log_error

# Import all testing modules
from testing.ingestion_prototype import IngestionPrototypeTester
from testing.comprehensive_ingestion_tests import ComprehensiveIngestionTester
from testing.podcast_transcription_test import PodcastTranscriptionTester
from testing.search_quality_analyzer import SearchQualityAnalyzer
from testing.performance_benchmarker import PerformanceBenchmarker
from testing.ground_truth_setup import GroundTruthSetup


@dataclass
class TestSuite:
    """Configuration for a test suite"""
    name: str
    description: str
    module_class: type
    priority: int
    estimated_duration_minutes: int
    dependencies: List[str]
    enabled: bool = True


class TestingDashboard:
    """Unified testing dashboard for comprehensive ingestion testing"""

    def __init__(self):
        self.config = load_config()
        self.dashboard_dir = Path("testing/dashboard")
        self.dashboard_dir.mkdir(parents=True, exist_ok=True)

        self.log_path = self.dashboard_dir / "dashboard.log"
        self.results_dir = self.dashboard_dir / "results"
        self.results_dir.mkdir(exist_ok=True)

        # Define available test suites
        self.test_suites = {
            "ground_truth_setup": TestSuite(
                name="Ground Truth Setup",
                description="Setup test data with known transcripts",
                module_class=GroundTruthSetup,
                priority=1,
                estimated_duration_minutes=10,
                dependencies=[]
            ),
            "ingestion_prototype": TestSuite(
                name="Ingestion Prototype",
                description="Core ingestion testing with multiple transcription models",
                module_class=IngestionPrototypeTester,
                priority=2,
                estimated_duration_minutes=30,
                dependencies=["ground_truth_setup"]
            ),
            "comprehensive_ingestion": TestSuite(
                name="Comprehensive Ingestion",
                description="Test all ingestion methods (API, local, batch)",
                module_class=ComprehensiveIngestionTester,
                priority=3,
                estimated_duration_minutes=20,
                dependencies=[]
            ),
            "podcast_transcription": TestSuite(
                name="Podcast Transcription",
                description="Podcast-specific transcription testing with OPML",
                module_class=PodcastTranscriptionTester,
                priority=4,
                estimated_duration_minutes=25,
                dependencies=[]
            ),
            "search_quality": TestSuite(
                name="Search Quality Analysis",
                description="Analyze search quality across transcription accuracies",
                module_class=SearchQualityAnalyzer,
                priority=5,
                estimated_duration_minutes=15,
                dependencies=["ingestion_prototype"]
            ),
            "performance_benchmark": TestSuite(
                name="Performance Benchmarking",
                description="Comprehensive performance and resource usage analysis",
                module_class=PerformanceBenchmarker,
                priority=6,
                estimated_duration_minutes=40,
                dependencies=[]
            )
        }

        # Dashboard state
        self.current_session = {
            "session_id": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "start_time": None,
            "end_time": None,
            "total_duration": 0,
            "tests_run": [],
            "results": {},
            "status": "ready"
        }

        # Load test history
        self.test_history = self._load_test_history()

    def run_full_test_suite(self, test_selection: Optional[List[str]] = None) -> Dict[str, Any]:
        """Run the complete test suite or selected tests"""
        log_info(str(self.log_path), "Starting unified testing dashboard")

        # Determine which tests to run
        if test_selection is None:
            tests_to_run = list(self.test_suites.keys())
        else:
            tests_to_run = [t for t in test_selection if t in self.test_suites]

        # Sort by priority and resolve dependencies
        tests_to_run = self._resolve_test_dependencies(tests_to_run)

        log_info(str(self.log_path), f"Running {len(tests_to_run)} test suites: {', '.join(tests_to_run)}")

        # Initialize session
        self.current_session["start_time"] = datetime.now()
        self.current_session["status"] = "running"
        self.current_session["tests_run"] = tests_to_run

        # Estimate total duration
        total_estimated_minutes = sum(
            self.test_suites[test_name].estimated_duration_minutes
            for test_name in tests_to_run
        )

        print("\n🚀 Starting Comprehensive Ingestion Testing")
        print(f"📊 Running {len(tests_to_run)} test suites")
        print(f"⏱️  Estimated duration: {total_estimated_minutes} minutes")
        print(f"📅 Session ID: {self.current_session['session_id']}")
        print("\n" + "="*80)

        # Run each test suite
        for i, test_name in enumerate(tests_to_run, 1):
            test_suite = self.test_suites[test_name]

            print(f"\n[{i}/{len(tests_to_run)}] Running: {test_suite.name}")
            print(f"Description: {test_suite.description}")
            print(f"Estimated time: {test_suite.estimated_duration_minutes} minutes")
            print("-" * 60)

            result = self._run_single_test_suite(test_name, test_suite)
            self.current_session["results"][test_name] = result

            # Show progress
            if result.get("success", False):
                print(f"✅ {test_suite.name} completed successfully")
            else:
                print(f"❌ {test_suite.name} failed: {result.get('error', 'Unknown error')}")

        # Finalize session
        self.current_session["end_time"] = datetime.now()
        self.current_session["total_duration"] = (
            self.current_session["end_time"] - self.current_session["start_time"]
        ).total_seconds() / 60  # minutes
        self.current_session["status"] = "completed"

        # Generate comprehensive report
        comprehensive_report = self._generate_comprehensive_report()

        # Save session results
        self._save_session_results()

        # Update test history
        self._update_test_history()

        print("\n" + "="*80)
        print("🎉 TESTING COMPLETE!")
        print(f"⏱️  Total duration: {self.current_session['total_duration']:.1f} minutes")
        print(f"📊 Results saved to: {self.results_dir}")
        print("="*80)

        return comprehensive_report

    def run_quick_test(self) -> Dict[str, Any]:
        """Run a quick subset of tests for faster feedback"""
        quick_tests = [
            "ground_truth_setup",
            "comprehensive_ingestion",
            "search_quality"
        ]

        print("🚀 Running Quick Test Suite...")
        return self.run_full_test_suite(quick_tests)

    def run_transcription_focus_test(self) -> Dict[str, Any]:
        """Run tests focused on transcription performance and quality"""
        transcription_tests = [
            "ground_truth_setup",
            "ingestion_prototype",
            "podcast_transcription",
            "performance_benchmark"
        ]

        print("🎤 Running Transcription-Focused Test Suite...")
        return self.run_full_test_suite(transcription_tests)

    def get_test_status(self) -> Dict[str, Any]:
        """Get current test status and progress"""
        return {
            "session": self.current_session,
            "available_suites": {
                name: {
                    "description": suite.description,
                    "estimated_minutes": suite.estimated_duration_minutes,
                    "enabled": suite.enabled,
                    "dependencies": suite.dependencies
                }
                for name, suite in self.test_suites.items()
            },
            "recent_history": self.test_history[-5:] if self.test_history else []
        }

    def generate_trend_analysis(self) -> Dict[str, Any]:
        """Generate trend analysis from test history"""
        if len(self.test_history) < 2:
            return {"note": "Insufficient history for trend analysis"}

        # Analyze trends over time
        trend_analysis = {
            "test_frequency": len(self.test_history),
            "date_range": {
                "earliest": self.test_history[0]["timestamp"],
                "latest": self.test_history[-1]["timestamp"]
            },
            "performance_trends": {},
            "success_rate_trends": {}
        }

        # Track performance improvements/degradations
        for test_name in self.test_suites.keys():
            test_results = []
            for session in self.test_history:
                if test_name in session.get("results", {}):
                    result = session["results"][test_name]
                    if result.get("success") and "duration" in result:
                        test_results.append({
                            "timestamp": session["timestamp"],
                            "duration": result["duration"],
                            "success": result["success"]
                        })

            if len(test_results) >= 2:
                # Calculate trend
                durations = [r["duration"] for r in test_results]
                recent_avg = sum(durations[-3:]) / len(durations[-3:])
                early_avg = sum(durations[:3]) / len(durations[:3])

                trend_analysis["performance_trends"][test_name] = {
                    "recent_avg_duration": recent_avg,
                    "early_avg_duration": early_avg,
                    "improvement_percent": ((early_avg - recent_avg) / early_avg * 100) if early_avg > 0 else 0,
                    "total_runs": len(test_results)
                }

        return trend_analysis

    def _resolve_test_dependencies(self, test_names: List[str]) -> List[str]:
        """Resolve test dependencies and return ordered list"""
        resolved = []
        remaining = test_names.copy()

        # Simple dependency resolution
        max_iterations = len(test_names) * 2  # Prevent infinite loops
        iteration = 0

        while remaining and iteration < max_iterations:
            iteration += 1
            made_progress = False

            for test_name in remaining.copy():
                test_suite = self.test_suites[test_name]
                dependencies = test_suite.dependencies

                # Check if all dependencies are satisfied
                if all(dep in resolved or dep not in test_names for dep in dependencies):
                    resolved.append(test_name)
                    remaining.remove(test_name)
                    made_progress = True

            if not made_progress:
                # Add remaining tests even if dependencies aren't met
                resolved.extend(remaining)
                break

        return resolved

    def _run_single_test_suite(self, test_name: str, test_suite: TestSuite) -> Dict[str, Any]:
        """Run a single test suite and return results"""
        start_time = time.time()

        try:
            # Initialize the test class
            if test_name == "ground_truth_setup":
                tester = test_suite.module_class()
                result = tester.setup_all_test_data()
                success = bool(result)
            elif test_name == "ingestion_prototype":
                tester = test_suite.module_class()
                result = tester.run_comprehensive_test_suite()
                success = bool(result)
            elif test_name == "comprehensive_ingestion":
                tester = test_suite.module_class()
                result = tester.run_comprehensive_tests()
                success = bool(result)
            elif test_name == "podcast_transcription":
                tester = test_suite.module_class()
                result = tester.run_comprehensive_podcast_test()
                success = bool(result)
            elif test_name == "search_quality":
                tester = test_suite.module_class()
                result = tester.run_search_quality_analysis()
                success = bool(result)
            elif test_name == "performance_benchmark":
                tester = test_suite.module_class()
                result = tester.run_comprehensive_benchmarks()
                success = bool(result)
            else:
                raise ValueError(f"Unknown test suite: {test_name}")

            duration = time.time() - start_time

            return {
                "success": success,
                "duration": duration,
                "result": result,
                "test_suite": test_suite.name
            }

        except Exception as e:
            duration = time.time() - start_time
            log_error(str(self.log_path), f"Test suite {test_name} failed: {e}")

            return {
                "success": False,
                "duration": duration,
                "error": str(e),
                "test_suite": test_suite.name
            }

    def _generate_comprehensive_report(self) -> Dict[str, Any]:
        """Generate comprehensive report from all test results"""
        report = {
            "session_info": {
                "session_id": self.current_session["session_id"],
                "start_time": self.current_session["start_time"].isoformat(),
                "end_time": self.current_session["end_time"].isoformat(),
                "total_duration_minutes": self.current_session["total_duration"],
                "tests_run": self.current_session["tests_run"]
            },
            "summary": {},
            "detailed_results": self.current_session["results"],
            "recommendations": {},
            "next_steps": []
        }

        # Generate summary
        total_tests = len(self.current_session["tests_run"])
        successful_tests = sum(
            1 for result in self.current_session["results"].values()
            if result.get("success", False)
        )

        report["summary"] = {
            "total_test_suites": total_tests,
            "successful_test_suites": successful_tests,
            "success_rate": successful_tests / total_tests if total_tests > 0 else 0,
            "total_duration_minutes": self.current_session["total_duration"]
        }

        # Extract key insights
        insights = self._extract_key_insights()
        report["key_insights"] = insights

        # Generate recommendations
        recommendations = self._generate_session_recommendations()
        report["recommendations"] = recommendations

        # Suggest next steps
        next_steps = self._suggest_next_steps()
        report["next_steps"] = next_steps

        return report

    def _extract_key_insights(self) -> Dict[str, Any]:
        """Extract key insights from test results"""
        insights = {
            "transcription_performance": {},
            "ingestion_capabilities": {},
            "search_quality": {},
            "system_performance": {}
        }

        # Extract transcription insights
        if "ingestion_prototype" in self.current_session["results"]:
            proto_result = self.current_session["results"]["ingestion_prototype"]
            if proto_result.get("success") and "result" in proto_result:
                transcription_tests = proto_result["result"].get("transcription_tests", {})
                if transcription_tests:
                    fastest_model = min(
                        transcription_tests.items(),
                        key=lambda x: x[1].get("duration_seconds", float('inf'))
                    )
                    insights["transcription_performance"]["fastest_model"] = {
                        "model": fastest_model[0],
                        "duration": fastest_model[1].get("duration_seconds", 0),
                        "words_per_second": fastest_model[1].get("words_per_second", 0)
                    }

        # Extract ingestion insights
        if "comprehensive_ingestion" in self.current_session["results"]:
            ingestion_result = self.current_session["results"]["comprehensive_ingestion"]
            if ingestion_result.get("success") and "result" in ingestion_result:
                api_tests = ingestion_result["result"].get("api_tests", {})
                successful_apis = [
                    name for name, data in api_tests.items()
                    if isinstance(data, dict) and data.get("overall_success", False)
                ]
                insights["ingestion_capabilities"]["working_apis"] = successful_apis

        return insights

    def _generate_session_recommendations(self) -> Dict[str, List[str]]:
        """Generate recommendations based on session results"""
        recommendations = {
            "immediate_actions": [],
            "optimization_opportunities": [],
            "infrastructure_improvements": []
        }

        # Check for failed tests
        failed_tests = [
            name for name, result in self.current_session["results"].items()
            if not result.get("success", False)
        ]

        if failed_tests:
            recommendations["immediate_actions"].append(
                f"Investigate failed tests: {', '.join(failed_tests)}"
            )

        # Performance recommendations
        if "performance_benchmark" in self.current_session["results"]:
            perf_result = self.current_session["results"]["performance_benchmark"]
            if perf_result.get("success"):
                recommendations["optimization_opportunities"].append(
                    "Review performance benchmark results for optimization opportunities"
                )

        # Infrastructure recommendations
        if len(self.current_session["tests_run"]) > 3:
            recommendations["infrastructure_improvements"].append(
                "Consider setting up continuous testing pipeline for regular validation"
            )

        return recommendations

    def _suggest_next_steps(self) -> List[str]:
        """Suggest next steps based on test results"""
        next_steps = []

        # Check if this was a first run
        if len(self.test_history) <= 1:
            next_steps.extend([
                "Review all test results and identify any configuration issues",
                "Set up regular testing schedule for ongoing validation",
                "Configure API keys for services you plan to use"
            ])

        # Check for missing data
        if "ground_truth_setup" in self.current_session["results"]:
            gt_result = self.current_session["results"]["ground_truth_setup"]
            if gt_result.get("success"):
                next_steps.append("Use ground truth data to validate transcription accuracy")

        # Performance optimization
        if self.current_session["total_duration"] > 60:  # More than 1 hour
            next_steps.append("Consider optimizing test suite for faster feedback cycles")

        # Production readiness
        success_rate = self.current_session.get("results", {})
        successful_count = sum(1 for r in success_rate.values() if r.get("success", False))
        total_count = len(success_rate)

        if total_count > 0 and successful_count / total_count > 0.8:
            next_steps.append("System appears ready for production testing with real data")
        else:
            next_steps.append("Address failing tests before proceeding to production")

        return next_steps

    def _save_session_results(self) -> None:
        """Save current session results"""
        session_file = self.results_dir / f"session_{self.current_session['session_id']}.json"

        # Serialize datetime objects
        session_data = self.current_session.copy()
        if session_data["start_time"]:
            session_data["start_time"] = session_data["start_time"].isoformat()
        if session_data["end_time"]:
            session_data["end_time"] = session_data["end_time"].isoformat()

        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2, default=str)

        log_info(str(self.log_path), f"Session results saved to {session_file}")

    def _load_test_history(self) -> List[Dict[str, Any]]:
        """Load test history from previous sessions"""
        history_file = self.dashboard_dir / "test_history.json"

        if history_file.exists():
            try:
                with open(history_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                log_error(str(self.log_path), f"Failed to load test history: {e}")

        return []

    def _update_test_history(self) -> None:
        """Update test history with current session"""
        # Add current session to history
        history_entry = {
            "session_id": self.current_session["session_id"],
            "timestamp": self.current_session["start_time"].isoformat(),
            "duration_minutes": self.current_session["total_duration"],
            "tests_run": self.current_session["tests_run"],
            "results": {
                name: {
                    "success": result.get("success", False),
                    "duration": result.get("duration", 0)
                }
                for name, result in self.current_session["results"].items()
            }
        }

        self.test_history.append(history_entry)

        # Keep only last 50 sessions
        self.test_history = self.test_history[-50:]

        # Save updated history
        history_file = self.dashboard_dir / "test_history.json"
        with open(history_file, 'w') as f:
            json.dump(self.test_history, f, indent=2)


def main():
    """Run the unified testing dashboard"""
    dashboard = TestingDashboard()

    # Show available options
    print("🧪 Atlas Ingestion Testing Dashboard")
    print("=" * 50)
    print("\nAvailable test modes:")
    print("1. Full Test Suite (comprehensive)")
    print("2. Quick Test (subset for fast feedback)")
    print("3. Transcription Focus (transcription-specific tests)")
    print("4. Show Status (current system status)")
    print("5. Show Trends (historical analysis)")

    choice = input("\nSelect test mode (1-5): ").strip()

    if choice == "1":
        results = dashboard.run_full_test_suite()
    elif choice == "2":
        results = dashboard.run_quick_test()
    elif choice == "3":
        results = dashboard.run_transcription_focus_test()
    elif choice == "4":
        status = dashboard.get_test_status()
        print(json.dumps(status, indent=2, default=str))
        return status
    elif choice == "5":
        trends = dashboard.generate_trend_analysis()
        print(json.dumps(trends, indent=2, default=str))
        return trends
    else:
        print("Running full test suite by default...")
        results = dashboard.run_full_test_suite()

    # Show summary
    if results:
        print("\n📊 FINAL SUMMARY")
        print(f"Session ID: {results['session_info']['session_id']}")
        print(f"Duration: {results['session_info']['total_duration_minutes']:.1f} minutes")
        print(f"Success Rate: {results['summary']['success_rate']:.1%}")

        if results.get("key_insights"):
            print("\n🔍 Key Insights:")
            insights = results["key_insights"]
            if "transcription_performance" in insights and insights["transcription_performance"]:
                fastest = insights["transcription_performance"].get("fastest_model", {})
                if fastest:
                    print(f"  Fastest transcription: {fastest['model']} ({fastest.get('words_per_second', 0):.1f} words/sec)")

        if results.get("next_steps"):
            print("\n📋 Recommended Next Steps:")
            for step in results["next_steps"]:
                print(f"  • {step}")

    return results


if __name__ == "__main__":
    main()