"""
Atlas Stuck Items Monitor
Detects and alerts when content_metadata items don't have corresponding processing_queue records

Purpose: Prevent future occurrences of stuck documents by monitoring pipeline health
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
import aiosqlite

from modules.database import DatabaseManager

logger = logging.getLogger(__name__)

class StuckItemsMonitor:
    """Monitor for stuck items in content pipeline"""

    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.alert_threshold = 100  # Alert if more than 100 items stuck
        self.critical_threshold = 1000  # Critical if more than 1000 items stuck

    async def get_pipeline_health(self) -> Dict[str, Any]:
        """Get comprehensive pipeline health metrics"""
        logger.info("🔍 Checking pipeline health...")

        query = """
        SELECT
            'total_metadata' as metric,
            COUNT(*) as value
        FROM content_metadata
        UNION ALL
        SELECT
            'total_processing_queue' as metric,
            COUNT(*) as value
        FROM processing_queue
        UNION ALL
        SELECT
            'total_processed' as metric,
            COUNT(*) as value
        FROM processed_content
        UNION ALL
        SELECT
            'stuck_items' as metric,
            COUNT(*) as value
        FROM content_metadata cm
        WHERE cm.content_id NOT IN (
            SELECT DISTINCT content_id FROM processing_queue
        )
        UNION ALL
        SELECT
            'processing_success_rate' as metric,
            ROUND(
                (SELECT COUNT(*) FROM processed_content) * 100.0 /
                NULLIF((SELECT COUNT(*) FROM processing_queue WHERE status = 'completed'), 0), 2
            ) as value
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(query)
            results = await cursor.fetchall()

        metrics = {}
        for row in results:
            metric, value = row
            metrics[metric] = value

        return metrics

    async def get_stuck_items_analysis(self) -> Dict[str, Any]:
        """Analyze stuck items by source, type, and age"""
        logger.info("📊 Analyzing stuck items...")

        query = """
        SELECT
            source_name,
            content_type,
            COUNT(*) as count,
            MIN(created_at) as oldest,
            MAX(created_at) as newest,
            AVG(JULIANDAY('now') - JULIANDAY(created_at)) as avg_days_stuck
        FROM content_metadata
        WHERE content_id NOT IN (
            SELECT DISTINCT content_id FROM processing_queue
        )
        GROUP BY source_name, content_type
        ORDER BY count DESC
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(query)
            results = await cursor.fetchall()

        analysis = {
            'total_stuck': 0,
            'by_source': {},
            'by_type': {},
            'problem_areas': []
        }

        for row in results:
            source, content_type, count, oldest, newest, avg_days = row
            analysis['total_stuck'] += count

            # Track by source
            if source not in analysis['by_source']:
                analysis['by_source'][source] = {'total': 0, 'types': {}}
            analysis['by_source'][source]['total'] += count
            analysis['by_source'][source]['types'][content_type] = count

            # Track by type
            if content_type not in analysis['by_type']:
                analysis['by_type'][content_type] = {'total': 0, 'sources': {}}
            analysis['by_type'][content_type]['total'] += count
            analysis['by_type'][content_type]['sources'][source] = count

            # Identify problem areas (high count or old items)
            if count > 100 or (avg_days and avg_days > 7):
                analysis['problem_areas'].append({
                    'source': source,
                    'content_type': content_type,
                    'count': count,
                    'avg_days_stuck': round(avg_days or 0, 1),
                    'oldest': oldest,
                    'newest': newest
                })

        return analysis

    async def detect_stuck_items(self) -> Dict[str, Any]:
        """Detect stuck items and generate alerts"""
        logger.info("🚨 Detecting stuck items...")

        # Get pipeline health
        health_metrics = await self.get_pipeline_health()
        stuck_count = health_metrics.get('stuck_items', 0)

        # Analyze stuck items
        stuck_analysis = await self.get_stuck_items_analysis()

        # Generate alerts
        alerts = []
        alert_level = "healthy"

        if stuck_count >= self.critical_threshold:
            alert_level = "critical"
            alerts.append({
                'level': 'critical',
                'message': f'CRITICAL: {stuck_count} items stuck in pipeline',
                'action': 'Immediate investigation required'
            })
        elif stuck_count >= self.alert_threshold:
            alert_level = "warning"
            alerts.append({
                'level': 'warning',
                'message': f'WARNING: {stuck_count} items stuck in pipeline',
                'action': 'Monitor and investigate if trend continues'
            })

        # Check for specific problem areas
        for problem in stuck_analysis['problem_areas']:
            if problem['count'] > 500:
                alerts.append({
                    'level': 'warning',
                    'message': f"High concentration of stuck items: {problem['source']} - {problem['content_type']} ({problem['count']} items)",
                    'action': f"Investigate {problem['source']} processing pipeline"
                })

        # Check for recent stuck items (pipeline issue)
        recent_stuck_query = """
        SELECT COUNT(*) as count
        FROM content_metadata
        WHERE content_id NOT IN (
            SELECT DISTINCT content_id FROM processing_queue
        )
        AND created_at > datetime('now', '-1 hour')
        """

        async with aiosqlite.connect(self.db_manager.db_path) as db:
            cursor = await db.execute(recent_stuck_query)
            recent_results = await cursor.fetchall()

        recent_stuck = recent_results[0][0] if recent_results else 0

        if recent_stuck > 10:
            alerts.append({
                'level': 'critical',
                'message': f'PIPELINE ISSUE: {recent_stuck} items stuck in last hour',
                'action': 'Immediate pipeline investigation required'
            })

        return {
            'alert_level': alert_level,
            'stuck_count': stuck_count,
            'recent_stuck_1h': recent_stuck,
            'alerts': alerts,
            'analysis': stuck_analysis,
            'health_metrics': health_metrics,
            'timestamp': datetime.now().isoformat()
        }

    async def generate_health_report(self) -> Dict[str, Any]:
        """Generate comprehensive pipeline health report"""
        logger.info("📋 Generating pipeline health report...")

        # Get stuck items detection
        stuck_detection = await self.detect_stuck_items()

        # Calculate health score
        health_score = 100
        if stuck_detection['stuck_count'] > 0:
            # Deduct points based on stuck percentage
            total_metadata = stuck_detection['health_metrics'].get('total_metadata', 1)
            stuck_percentage = (stuck_detection['stuck_count'] / total_metadata) * 100
            health_score -= min(stuck_percentage * 2, 80)  # Max 80 point deduction

        # Determine status
        if health_score >= 90:
            status = "excellent"
            status_emoji = "🟢"
        elif health_score >= 75:
            status = "good"
            status_emoji = "🟡"
        elif health_score >= 50:
            status = "degraded"
            status_emoji = "🟠"
        else:
            status = "critical"
            status_emoji = "🔴"

        report = {
            'overall': {
                'health_score': round(health_score, 1),
                'status': status,
                'emoji': status_emoji,
                'timestamp': datetime.now().isoformat()
            },
            'stuck_items': stuck_detection,
            'recommendations': self._generate_recommendations(stuck_detection)
        }

        return report

    def _generate_recommendations(self, stuck_detection: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on stuck items analysis"""
        recommendations = []

        if stuck_detection['stuck_count'] == 0:
            recommendations.append("✅ Pipeline is healthy - no stuck items detected")
            return recommendations

        stuck_count = stuck_detection['stuck_count']
        analysis = stuck_detection['analysis']

        # High-level recommendations
        if stuck_count > 1000:
            recommendations.append("🚨 CRITICAL: Run document recovery immediately")
            recommendations.append("🔧 Investigate root cause of massive pipeline blockage")

        if stuck_count > 100:
            recommendations.append("⚠️ WARNING: Significant number of stuck items - investigate processing pipeline")

        # Specific source recommendations
        for source, data in analysis['by_source'].items():
            if data['total'] > 100:
                recommendations.append(f"🔍 Investigate {source} processing - {data['total']} items stuck")

        # Specific type recommendations
        for content_type, data in analysis['by_type'].items():
            if data['total'] > 100:
                recommendations.append(f"📋 Check {content_type} processing logic - {data['total']} items stuck")

        # Recent stuck items
        if stuck_detection['recent_stuck_1h'] > 0:
            recommendations.append("🆕 NEW ISSUE: Items getting stuck recently - check current pipeline health")

        # General recommendations
        if stuck_count > 0:
            recommendations.append("🔄 Schedule regular stuck items monitoring")
            recommendations.append("📊 Implement automated recovery for known good items")

        return recommendations

    async def setup_monitoring(self, check_interval_minutes: int = 30):
        """Setup continuous monitoring for stuck items"""
        logger.info(f"🔔 Setting up stuck items monitoring (check every {check_interval_minutes} minutes)...")

        while True:
            try:
                # Generate health report
                report = await self.generate_health_report()

                # Log status
                logger.info(f"📊 Pipeline Health Score: {report['overall']['health_score']}/100 "
                           f"({report['overall']['status'].upper()})")

                # Log alerts if any
                for alert in report['stuck_items']['alerts']:
                    logger.warning(f"🚨 {alert['level'].upper()}: {alert['message']}")

                # Log recommendations
                if report['stuck_items']['stuck_count'] > 0:
                    logger.info("💡 Recommendations:")
                    for rec in report['recommendations']:
                        logger.info(f"  {rec}")

                # Save report to database for historical tracking
                await self._save_health_report(report)

            except Exception as e:
                logger.error(f"❌ Error in stuck items monitoring: {e}")

            # Wait for next check
            await asyncio.sleep(check_interval_minutes * 60)

    async def _save_health_report(self, report: Dict[str, Any]):
        """Save health report to database for historical tracking"""
        try:
            # Skip database save for now - we don't have the health_reports table
            # Could implement table creation later if needed
            logger.debug("Health report saved to logs only")
        except Exception as e:
            logger.error(f"Error saving health report: {e}")

# Import json for _save_health_report
import json

async def get_stuck_items_monitor(db_manager: DatabaseManager) -> StuckItemsMonitor:
    """Factory function to get stuck items monitor"""
    return StuckItemsMonitor(db_manager)