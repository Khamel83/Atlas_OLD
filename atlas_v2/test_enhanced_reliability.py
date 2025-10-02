#!/usr/bin/env python3
"""
Enhanced Atlas Reliability Test Suite

Tests the production-grade reliability features:
- Bulletproof duplicate prevention
- Intelligent queue management
- Error handling with circuit breakers
- Dead letter queue functionality
- Auto-fix capabilities
"""

import asyncio
import json
import logging
import time
from datetime import datetime
from typing import Dict, Any, List

from modules.enhanced_processor import get_enhanced_processor
from modules.database import DatabaseManager
from modules.config_manager import ConfigManager
from modules.intelligent_monitor import get_intelligent_monitor
from modules.enhanced_queue_manager import enqueue_url, get_queue_stats
from modules.dead_letter_queue import get_quarantine_stats

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnhancedReliabilityTester:
    """Comprehensive reliability testing for enhanced Atlas"""

    def __init__(self):
        self.test_results = {
            'duplicate_prevention': {'passed': 0, 'failed': 0, 'details': []},
            'queue_management': {'passed': 0, 'failed': 0, 'details': []},
            'error_handling': {'passed': 0, 'failed': 0, 'details': []},
            'dead_letter_queue': {'passed': 0, 'failed': 0, 'details': []},
            'intelligent_monitoring': {'passed': 0, 'failed': 0, 'details': []},
            'start_time': datetime.now()
        }

    async def run_all_tests(self) -> Dict[str, Any]:
        """Run comprehensive reliability test suite"""
        logger.info("🚀 Starting Enhanced Atlas Reliability Test Suite...")

        # Initialize components
        config_manager = ConfigManager()
        db_manager = DatabaseManager()
        await db_manager.initialize()

        try:
            # Test 1: Duplicate Prevention
            await self.test_duplicate_prevention(db_manager, config_manager)

            # Test 2: Queue Management
            await self.test_queue_management(db_manager, config_manager)

            # Test 3: Error Handling
            await self.test_error_handling(db_manager, config_manager)

            # Test 4: Dead Letter Queue
            await self.test_dead_letter_queue(db_manager, config_manager)

            # Test 5: Intelligent Monitoring
            await self.test_intelligent_monitoring(db_manager, config_manager)

        finally:
            await db_manager.close()

        # Generate final report
        return self.generate_final_report()

    async def test_duplicate_prevention(self, db_manager, config_manager):
        """Test bulletproof duplicate prevention"""
        logger.info("🧪 Testing Duplicate Prevention...")

        test_url = "https://example.com/duplicate-test-article"
        source_name = "Duplicate Test Source"

        try:
            # Test duplicate URL submission
            success1, msg1, content_id1 = await enqueue_url(
                url=test_url,
                source_name=source_name,
                content_type="article"
            )

            success2, msg2, content_id2 = await enqueue_url(
                url=test_url,
                source_name=source_name,
                content_type="article"
            )

            # Verify duplicate prevention worked
            if success1 and not success2 and "Duplicate" in msg2:
                self.test_results['duplicate_prevention']['passed'] += 1
                self.test_results['duplicate_prevention']['details'].append(
                    f"✅ Duplicate prevention: {msg2}"
                )
                logger.info("✅ Duplicate prevention working correctly")
            else:
                self.test_results['duplicate_prevention']['failed'] += 1
                self.test_results['duplicate_prevention']['details'].append(
                    f"❌ Duplicate prevention failed: success1={success1}, success2={success2}, msg2={msg2}"
                )
                logger.error("❌ Duplicate prevention test failed")

        except Exception as e:
            self.test_results['duplicate_prevention']['failed'] += 1
            self.test_results['duplicate_prevention']['details'].append(f"❌ Exception: {e}")
            logger.error(f"❌ Duplicate prevention test exception: {e}")

    async def test_queue_management(self, db_manager, config_manager):
        """Test intelligent queue management"""
        logger.info("🧪 Testing Queue Management...")

        try:
            # Get queue stats
            stats = await get_queue_stats()

            # Verify queue stats structure
            required_fields = ['pending_count', 'queue_health', 'backpressure_active']
            if all(field in stats for field in required_fields):
                self.test_results['queue_management']['passed'] += 1
                self.test_results['queue_management']['details'].append(
                    f"✅ Queue stats available: {stats['pending_count']} pending, health={stats['queue_health']}"
                )
                logger.info("✅ Queue management stats working correctly")
            else:
                self.test_results['queue_management']['failed'] += 1
                missing = [field for field in required_fields if field not in stats]
                self.test_results['queue_management']['details'].append(
                    f"❌ Missing queue stats fields: {missing}"
                )
                logger.error(f"❌ Queue management missing fields: {missing}")

        except Exception as e:
            self.test_results['queue_management']['failed'] += 1
            self.test_results['queue_management']['details'].append(f"❌ Exception: {e}")
            logger.error(f"❌ Queue management test exception: {e}")

    async def test_error_handling(self, db_manager, config_manager):
        """Test production-grade error handling"""
        logger.info("🧪 Testing Error Handling...")

        try:
            # Test with an invalid URL that should fail
            invalid_url = "file:///invalid/local/file.txt"

            success, msg, content_id = await enqueue_url(
                url=invalid_url,
                source_name="Error Test Source",
                content_type="article"
            )

            # Invalid URLs should be quarantined
            if not success and ("quarantined" in msg.lower() or "invalid" in msg.lower()):
                self.test_results['error_handling']['passed'] += 1
                self.test_results['error_handling']['details'].append(
                    f"✅ Error handling: Invalid URL properly quarantined - {msg}"
                )
                logger.info("✅ Error handling working correctly")
            else:
                self.test_results['error_handling']['failed'] += 1
                self.test_results['error_handling']['details'].append(
                    f"❌ Error handling failed: success={success}, msg={msg}"
                )
                logger.error("❌ Error handling test failed")

        except Exception as e:
            self.test_results['error_handling']['failed'] += 1
            self.test_results['error_handling']['details'].append(f"❌ Exception: {e}")
            logger.error(f"❌ Error handling test exception: {e}")

    async def test_dead_letter_queue(self, db_manager, config_manager):
        """Test dead letter queue functionality"""
        logger.info("🧪 Testing Dead Letter Queue...")

        try:
            # Get quarantine stats
            stats = await get_quarantine_stats(days_ago=7)

            # Verify DLQ stats structure
            if 'total_quarantined' in stats:
                self.test_results['dead_letter_queue']['passed'] += 1
                self.test_results['dead_letter_queue']['details'].append(
                    f"✅ Dead letter queue: {stats['total_quarantined']} items quarantined"
                )
                logger.info("✅ Dead letter queue working correctly")
            else:
                self.test_results['dead_letter_queue']['failed'] += 1
                self.test_results['dead_letter_queue']['details'].append(
                    "❌ Dead letter queue stats missing total_quarantined field"
                )
                logger.error("❌ Dead letter queue test failed")

        except Exception as e:
            self.test_results['dead_letter_queue']['failed'] += 1
            self.test_results['dead_letter_queue']['details'].append(f"❌ Exception: {e}")
            logger.error(f"❌ Dead letter queue test exception: {e}")

    async def test_intelligent_monitoring(self, db_manager, config_manager):
        """Test intelligent monitoring with auto-fix"""
        logger.info("🧪 Testing Intelligent Monitoring...")

        try:
            # Initialize intelligent monitor
            monitor = await get_intelligent_monitor(db_manager, config_manager)

            # Test health check
            health_result = await monitor.health_check_with_auto_fix()

            # Verify health check structure
            required_fields = ['status', 'timestamp', 'auto_fix_enabled']
            if all(field in health_result for field in required_fields):
                self.test_results['intelligent_monitoring']['passed'] += 1
                self.test_results['intelligent_monitoring']['details'].append(
                    f"✅ Intelligent monitoring: status={health_result['status']}, auto_fix={health_result['auto_fix_enabled']}"
                )
                logger.info("✅ Intelligent monitoring working correctly")
            else:
                self.test_results['intelligent_monitoring']['failed'] += 1
                missing = [field for field in required_fields if field not in health_result]
                self.test_results['intelligent_monitoring']['details'].append(
                    f"❌ Missing monitoring fields: {missing}"
                )
                logger.error(f"❌ Intelligent monitoring missing fields: {missing}")

            # Test monitoring stats
            stats = monitor.get_monitoring_stats()
            if 'uptime_hours' in stats and 'auto_fix_enabled' in stats:
                self.test_results['intelligent_monitoring']['passed'] += 1
                self.test_results['intelligent_monitoring']['details'].append(
                    f"✅ Monitoring stats: {stats['uptime_hours']:.1f}h uptime"
                )
                logger.info("✅ Monitoring stats working correctly")
            else:
                self.test_results['intelligent_monitoring']['failed'] += 1
                self.test_results['intelligent_monitoring']['details'].append(
                    "❌ Monitoring stats missing required fields"
                )
                logger.error("❌ Monitoring stats test failed")

        except Exception as e:
            self.test_results['intelligent_monitoring']['failed'] += 1
            self.test_results['intelligent_monitoring']['details'].append(f"❌ Exception: {e}")
            logger.error(f"❌ Intelligent monitoring test exception: {e}")

    def generate_final_report(self) -> Dict[str, Any]:
        """Generate comprehensive test report"""
        end_time = datetime.now()
        duration = (end_time - self.test_results['start_time']).total_seconds()

        # Calculate totals
        total_passed = sum(result['passed'] for result in self.test_results.values() if isinstance(result, dict))
        total_failed = sum(result['failed'] for result in self.test_results.values() if isinstance(result, dict))
        total_tests = total_passed + total_failed

        success_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0

        # Overall status
        if success_rate >= 90:
            overall_status = "EXCELLENT"
            status_emoji = "🎉"
        elif success_rate >= 80:
            overall_status = "GOOD"
            status_emoji = "✅"
        elif success_rate >= 70:
            overall_status = "ACCEPTABLE"
            status_emoji = "⚠️"
        else:
            overall_status = "NEEDS ATTENTION"
            status_emoji = "❌"

        report = {
            "summary": {
                "status": overall_status,
                "emoji": status_emoji,
                "total_tests": total_tests,
                "passed": total_passed,
                "failed": total_failed,
                "success_rate": round(success_rate, 2),
                "duration_seconds": round(duration, 1),
                "timestamp": end_time.isoformat()
            },
            "test_categories": {},
            "detailed_results": self.test_results
        }

        # Add category summaries
        for category, results in self.test_results.items():
            if isinstance(results, dict):
                passed = results.get('passed', 0)
                failed = results.get('failed', 0)
                total = passed + failed
                category_success = (passed / total * 100) if total > 0 else 0

                report["test_categories"][category] = {
                    "passed": passed,
                    "failed": failed,
                    "total": total,
                    "success_rate": round(category_success, 2),
                    "details": results.get('details', [])
                }

        return report

async def main():
    """Run the enhanced reliability test suite"""
    print("🚀 Enhanced Atlas Reliability Test Suite")
    print("=" * 50)

    tester = EnhancedReliabilityTester()
    report = await tester.run_all_tests()

    # Display results
    summary = report['summary']
    print(f"\n{summary['emoji']} TEST COMPLETE: {summary['status']}")
    print(f"📊 Results: {summary['passed']}/{summary['total_tests']} passed ({summary['success_rate']}%)")
    print(f"⏱️  Duration: {summary['duration_seconds']} seconds")

    print("\n📋 Category Results:")
    for category, results in report['test_categories'].items():
        status = "✅" if results['success_rate'] >= 80 else "⚠️" if results['success_rate'] >= 60 else "❌"
        print(f"{status} {category.replace('_', ' ').title()}: {results['passed']}/{results['total']} ({results['success_rate']}%)")

    # Show failures if any
    total_failed = summary['failed']
    if total_failed > 0:
        print(f"\n❌ Failed Tests ({total_failed}):")
        for category, results in report['test_categories'].items():
            if results['failed'] > 0:
                print(f"\n{category.replace('_', ' ').title()}:")
                for detail in results['details']:
                    if detail.startswith('❌'):
                        print(f"  {detail}")

    # Save report
    with open('enhanced_reliability_test_report.json', 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\n📄 Detailed report saved to: enhanced_reliability_test_report.json")

    # Return appropriate exit code
    if summary['success_rate'] >= 80:
        print("\n🎉 Enhanced Atlas reliability verification PASSED!")
        return 0
    else:
        print("\n❌ Enhanced Atlas reliability verification FAILED!")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)