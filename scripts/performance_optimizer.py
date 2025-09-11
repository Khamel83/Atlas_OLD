#!/usr/bin/env python3
"""
Atlas Performance Optimizer
Analyzes system performance and provides optimization recommendations.
"""

import os
import sys
import time
import json
import psutil
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from collections import defaultdict

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers.resource_manager import get_resource_manager
from helpers.queue_manager import get_queue_status
from helpers.metrics_collector import get_metrics_collector
from scripts.worker_scaler import WorkerScaler
from scripts.disk_cleanup import DiskCleanup

@dataclass
class OptimizationRecommendation:
    """Performance optimization recommendation"""
    category: str
    priority: str  # high, medium, low
    title: str
    description: str
    impact: str
    effort: str  # low, medium, high
    actions: List[str]
    metrics: Dict[str, Any]

class PerformanceOptimizer:
    """System performance analysis and optimization recommendations."""
    
    def __init__(self):
        self.setup_logging()
        self.resource_manager = get_resource_manager()
        self.metrics = get_metrics_collector()
        self.worker_scaler = WorkerScaler()
        self.disk_cleanup = DiskCleanup()
        
        # Performance history
        self.performance_history: List[Dict[str, Any]] = []
        self.baseline_metrics: Optional[Dict[str, Any]] = None
        
    def setup_logging(self):
        """Setup logging for performance optimizer."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        self.logger = logging.getLogger("performance_optimizer")
        self.logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(log_dir / "performance_optimizer.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def collect_performance_metrics(self) -> Dict[str, Any]:
        """Collect comprehensive performance metrics."""
        # System metrics
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk_io = psutil.disk_io_counters()
        network_io = psutil.net_io_counters()
        load_avg = os.getloadavg()
        
        # Atlas-specific metrics
        queue_status = get_queue_status()
        worker_status = self.worker_scaler.get_worker_status()
        resource_status = self.resource_manager.monitor_resources()
        cleanup_status = self.disk_cleanup.get_cleanup_status()
        
        metrics = {
            "timestamp": datetime.now().isoformat(),
            
            # System performance
            "cpu": {
                "usage_percent": cpu_percent,
                "load_1min": load_avg[0],
                "load_5min": load_avg[1],
                "load_15min": load_avg[2],
                "core_count": psutil.cpu_count()
            },
            
            "memory": {
                "total_gb": memory.total / (1024**3),
                "used_gb": memory.used / (1024**3),
                "available_gb": memory.available / (1024**3),
                "usage_percent": memory.percent,
                "pressure_level": resource_status["memory"]["pressure_level"]
            },
            
            "disk": {
                "usage_percent": cleanup_status["disk_usage"]["usage_percent"],
                "free_gb": cleanup_status["disk_usage"]["free_gb"],
                "io_read_mb": disk_io.read_bytes / (1024**2) if disk_io else 0,
                "io_write_mb": disk_io.write_bytes / (1024**2) if disk_io else 0
            },
            
            "network": {
                "bytes_sent_mb": network_io.bytes_sent / (1024**2) if network_io else 0,
                "bytes_recv_mb": network_io.bytes_recv / (1024**2) if network_io else 0,
                "packets_sent": network_io.packets_sent if network_io else 0,
                "packets_recv": network_io.packets_recv if network_io else 0
            },
            
            # Atlas application metrics
            "queue": {
                "pending_tasks": queue_status.get("queue_counts", {}).get("pending", 0),
                "processing_tasks": queue_status.get("queue_counts", {}).get("processing", 0),
                "completed_tasks": queue_status.get("queue_counts", {}).get("completed", 0),
                "failed_tasks": queue_status.get("queue_counts", {}).get("failed", 0)
            },
            
            "workers": {
                "running_count": worker_status["running_workers"],
                "total_count": worker_status["total_workers"]
            },
            
            "process_count": len(psutil.pids()),
            "uptime_hours": (time.time() - psutil.boot_time()) / 3600
        }
        
        return metrics
    
    def analyze_cpu_performance(self, metrics: Dict[str, Any]) -> List[OptimizationRecommendation]:
        """Analyze CPU performance and generate recommendations."""
        recommendations = []
        cpu_data = metrics["cpu"]
        
        # High CPU usage
        if cpu_data["usage_percent"] > 80:
            recommendations.append(OptimizationRecommendation(
                category="cpu",
                priority="high",
                title="High CPU Usage Detected",
                description=f"CPU usage is at {cpu_data['usage_percent']:.1f}%, which may impact performance.",
                impact="System responsiveness may be degraded",
                effort="low",
                actions=[
                    "Reduce number of concurrent workers",
                    "Optimize CPU-intensive operations",
                    "Consider adding CPU throttling",
                    "Check for runaway processes"
                ],
                metrics={"cpu_usage": cpu_data["usage_percent"]}
            ))
        
        # High load average
        if cpu_data["load_5min"] > cpu_data["core_count"] * 2:
            recommendations.append(OptimizationRecommendation(
                category="cpu",
                priority="medium",
                title="High System Load",
                description=f"5-minute load average ({cpu_data['load_5min']:.2f}) is high for {cpu_data['core_count']} cores.",
                impact="System may be overloaded",
                effort="medium",
                actions=[
                    "Scale down concurrent operations",
                    "Implement load balancing",
                    "Add process prioritization",
                    "Consider upgrading hardware"
                ],
                metrics={"load_5min": cpu_data["load_5min"], "cores": cpu_data["core_count"]}
            ))
        
        return recommendations
    
    def analyze_memory_performance(self, metrics: Dict[str, Any]) -> List[OptimizationRecommendation]:
        """Analyze memory performance and generate recommendations."""
        recommendations = []
        memory_data = metrics["memory"]
        
        # High memory usage
        if memory_data["usage_percent"] > 85:
            recommendations.append(OptimizationRecommendation(
                category="memory",
                priority="high",
                title="High Memory Usage",
                description=f"Memory usage is at {memory_data['usage_percent']:.1f}%, approaching critical levels.",
                impact="Risk of out-of-memory errors and swap usage",
                effort="low",
                actions=[
                    "Trigger garbage collection",
                    "Reduce worker count",
                    "Clear application caches",
                    "Restart memory-intensive processes"
                ],
                metrics={"memory_usage": memory_data["usage_percent"]}
            ))
        
        # Memory pressure
        if memory_data["pressure_level"] in ["warning", "critical"]:
            recommendations.append(OptimizationRecommendation(
                category="memory",
                priority="high",
                title=f"Memory Pressure: {memory_data['pressure_level'].title()}",
                description="System is experiencing memory pressure.",
                impact="Performance degradation and potential instability",
                effort="medium",
                actions=[
                    "Implement memory monitoring",
                    "Optimize data structures",
                    "Add memory limits to processes",
                    "Consider memory upgrade"
                ],
                metrics={"pressure_level": memory_data["pressure_level"]}
            ))
        
        return recommendations
    
    def analyze_disk_performance(self, metrics: Dict[str, Any]) -> List[OptimizationRecommendation]:
        """Analyze disk performance and generate recommendations."""
        recommendations = []
        disk_data = metrics["disk"]
        
        # High disk usage
        if disk_data["usage_percent"] > 85:
            recommendations.append(OptimizationRecommendation(
                category="disk",
                priority="high",
                title="High Disk Usage",
                description=f"Disk usage is at {disk_data['usage_percent']:.1f}%, approaching capacity.",
                impact="Risk of disk full errors and performance degradation",
                effort="low",
                actions=[
                    "Run disk cleanup",
                    "Archive old files",
                    "Delete unnecessary files",
                    "Compress large files"
                ],
                metrics={"disk_usage": disk_data["usage_percent"]}
            ))
        
        # Low free space
        if disk_data["free_gb"] < 5:
            recommendations.append(OptimizationRecommendation(
                category="disk",
                priority="critical",
                title="Low Disk Space",
                description=f"Only {disk_data['free_gb']:.1f}GB free space remaining.",
                impact="System may become unstable or fail",
                effort="low",
                actions=[
                    "Emergency disk cleanup",
                    "Move files to external storage",
                    "Delete large unnecessary files",
                    "Add storage capacity"
                ],
                metrics={"free_space_gb": disk_data["free_gb"]}
            ))
        
        return recommendations
    
    def analyze_queue_performance(self, metrics: Dict[str, Any]) -> List[OptimizationRecommendation]:
        """Analyze queue performance and generate recommendations."""
        recommendations = []
        queue_data = metrics["queue"]
        worker_data = metrics["workers"]
        
        # Large queue backlog
        if queue_data["pending_tasks"] > 50:
            recommendations.append(OptimizationRecommendation(
                category="queue",
                priority="medium",
                title="Large Queue Backlog",
                description=f"{queue_data['pending_tasks']} tasks pending in queue.",
                impact="Increased processing latency",
                effort="low",
                actions=[
                    "Scale up workers",
                    "Optimize task processing",
                    "Implement task prioritization",
                    "Check for processing bottlenecks"
                ],
                metrics={"pending_tasks": queue_data["pending_tasks"]}
            ))
        
        # High failure rate
        total_tasks = sum([
            queue_data["completed_tasks"],
            queue_data["failed_tasks"],
            queue_data["processing_tasks"]
        ])
        
        if total_tasks > 0:
            failure_rate = queue_data["failed_tasks"] / total_tasks
            if failure_rate > 0.1:  # 10% failure rate
                recommendations.append(OptimizationRecommendation(
                    category="queue",
                    priority="high",
                    title="High Task Failure Rate",
                    description=f"Task failure rate is {failure_rate:.1%}.",
                    impact="Reduced system effectiveness and potential data loss",
                    effort="medium",
                    actions=[
                        "Investigate failure causes",
                        "Implement better error handling",
                        "Add retry mechanisms",
                        "Improve input validation"
                    ],
                    metrics={"failure_rate": failure_rate}
                ))
        
        # Worker utilization
        if worker_data["running_count"] == 0 and queue_data["pending_tasks"] > 0:
            recommendations.append(OptimizationRecommendation(
                category="workers",
                priority="critical",
                title="No Workers Running",
                description="No workers are running but tasks are pending.",
                impact="No task processing occurring",
                effort="low",
                actions=[
                    "Start worker processes",
                    "Check worker health",
                    "Restart worker scaling system",
                    "Investigate worker failures"
                ],
                metrics={"workers": worker_data["running_count"], "pending": queue_data["pending_tasks"]}
            ))
        
        return recommendations
    
    def analyze_historical_trends(self) -> List[OptimizationRecommendation]:
        """Analyze historical performance trends."""
        recommendations = []
        
        if len(self.performance_history) < 10:
            return recommendations
        
        # Calculate trends over last 10 measurements
        recent_history = self.performance_history[-10:]
        
        # CPU trend
        cpu_values = [h["cpu"]["usage_percent"] for h in recent_history]
        cpu_trend = (cpu_values[-1] - cpu_values[0]) / len(cpu_values)
        
        if cpu_trend > 5:  # CPU usage increasing
            recommendations.append(OptimizationRecommendation(
                category="trends",
                priority="medium",
                title="Increasing CPU Usage Trend",
                description=f"CPU usage has increased by {cpu_trend:.1f}% over recent measurements.",
                impact="System may be approaching CPU limits",
                effort="medium",
                actions=[
                    "Monitor CPU usage closely",
                    "Identify CPU-intensive operations",
                    "Plan for load reduction",
                    "Consider performance optimization"
                ],
                metrics={"cpu_trend": cpu_trend}
            ))
        
        # Memory trend
        memory_values = [h["memory"]["usage_percent"] for h in recent_history]
        memory_trend = (memory_values[-1] - memory_values[0]) / len(memory_values)
        
        if memory_trend > 3:  # Memory usage increasing
            recommendations.append(OptimizationRecommendation(
                category="trends",
                priority="medium",
                title="Increasing Memory Usage Trend",
                description=f"Memory usage has increased by {memory_trend:.1f}% over recent measurements.",
                impact="Potential memory leak or increasing load",
                effort="medium",
                actions=[
                    "Investigate memory leaks",
                    "Monitor memory usage patterns",
                    "Implement memory profiling",
                    "Plan for memory optimization"
                ],
                metrics={"memory_trend": memory_trend}
            ))
        
        return recommendations
    
    def generate_optimization_recommendations(self) -> Dict[str, Any]:
        """Generate comprehensive optimization recommendations."""
        # Collect current metrics
        current_metrics = self.collect_performance_metrics()
        
        # Add to history
        self.performance_history.append(current_metrics)
        if len(self.performance_history) > 100:
            self.performance_history.pop(0)
        
        # Analyze different aspects
        recommendations = []
        recommendations.extend(self.analyze_cpu_performance(current_metrics))
        recommendations.extend(self.analyze_memory_performance(current_metrics))
        recommendations.extend(self.analyze_disk_performance(current_metrics))
        recommendations.extend(self.analyze_queue_performance(current_metrics))
        recommendations.extend(self.analyze_historical_trends())
        
        # Sort by priority
        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        recommendations.sort(key=lambda r: priority_order.get(r.priority, 4))
        
        # Generate optimization report
        report = {
            "timestamp": datetime.now().isoformat(),
            "current_metrics": current_metrics,
            "recommendations": [
                {
                    "category": r.category,
                    "priority": r.priority,
                    "title": r.title,
                    "description": r.description,
                    "impact": r.impact,
                    "effort": r.effort,
                    "actions": r.actions,
                    "metrics": r.metrics
                }
                for r in recommendations
            ],
            "summary": {
                "total_recommendations": len(recommendations),
                "critical_count": len([r for r in recommendations if r.priority == "critical"]),
                "high_count": len([r for r in recommendations if r.priority == "high"]),
                "medium_count": len([r for r in recommendations if r.priority == "medium"]),
                "low_count": len([r for r in recommendations if r.priority == "low"])
            }
        }
        
        self.logger.info(f"Generated {len(recommendations)} optimization recommendations")
        return report
    
    def create_weekly_report(self) -> Dict[str, Any]:
        """Create comprehensive weekly performance report."""
        if not self.performance_history:
            return {"error": "No performance history available"}
        
        # Calculate averages over history
        cpu_avg = sum(h["cpu"]["usage_percent"] for h in self.performance_history) / len(self.performance_history)
        memory_avg = sum(h["memory"]["usage_percent"] for h in self.performance_history) / len(self.performance_history)
        queue_avg = sum(h["queue"]["pending_tasks"] for h in self.performance_history) / len(self.performance_history)
        
        # Find peaks
        cpu_peak = max(h["cpu"]["usage_percent"] for h in self.performance_history)
        memory_peak = max(h["memory"]["usage_percent"] for h in self.performance_history)
        queue_peak = max(h["queue"]["pending_tasks"] for h in self.performance_history)
        
        weekly_report = {
            "report_period": f"{datetime.now() - timedelta(days=7)} to {datetime.now()}",
            "generated_at": datetime.now().isoformat(),
            
            "performance_summary": {
                "cpu": {
                    "average_usage": cpu_avg,
                    "peak_usage": cpu_peak,
                    "status": "good" if cpu_avg < 70 else "warning" if cpu_avg < 85 else "critical"
                },
                "memory": {
                    "average_usage": memory_avg,
                    "peak_usage": memory_peak,
                    "status": "good" if memory_avg < 70 else "warning" if memory_avg < 85 else "critical"
                },
                "queue": {
                    "average_pending": queue_avg,
                    "peak_pending": queue_peak,
                    "status": "good" if queue_avg < 20 else "warning" if queue_avg < 50 else "critical"
                }
            },
            
            "optimization_opportunities": self.generate_optimization_recommendations()["recommendations"],
            
            "key_metrics": {
                "measurements_taken": len(self.performance_history),
                "uptime_hours": self.performance_history[-1]["uptime_hours"] if self.performance_history else 0,
                "process_count": self.performance_history[-1]["process_count"] if self.performance_history else 0
            }
        }
        
        return weekly_report

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Atlas Performance Optimizer")
    parser.add_argument("--analyze", action="store_true", help="Analyze current performance")
    parser.add_argument("--weekly", action="store_true", help="Generate weekly report")
    parser.add_argument("--monitor", action="store_true", help="Start monitoring mode")
    parser.add_argument("--interval", type=int, default=300, help="Monitoring interval in seconds")
    parser.add_argument("--output", type=str, help="Output file for reports")
    
    args = parser.parse_args()
    
    optimizer = PerformanceOptimizer()
    
    if args.analyze:
        report = optimizer.generate_optimization_recommendations()
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(report, f, indent=2)
            print(f"Analysis saved to {args.output}")
        else:
            print("=== PERFORMANCE ANALYSIS ===")
            print(f"Found {report['summary']['total_recommendations']} recommendations")
            
            for rec in report["recommendations"][:5]:  # Show top 5
                print(f"\n[{rec['priority'].upper()}] {rec['title']}")
                print(f"  {rec['description']}")
                print(f"  Actions: {', '.join(rec['actions'][:2])}")
    
    elif args.weekly:
        report = optimizer.create_weekly_report()
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(report, f, indent=2)
            print(f"Weekly report saved to {args.output}")
        else:
            print("=== WEEKLY PERFORMANCE REPORT ===")
            summary = report["performance_summary"]
            print(f"CPU: {summary['cpu']['average_usage']:.1f}% avg, {summary['cpu']['peak_usage']:.1f}% peak ({summary['cpu']['status']})")
            print(f"Memory: {summary['memory']['average_usage']:.1f}% avg, {summary['memory']['peak_usage']:.1f}% peak ({summary['memory']['status']})")
            print(f"Queue: {summary['queue']['average_pending']:.1f} avg, {summary['queue']['peak_pending']} peak ({summary['queue']['status']})")
    
    elif args.monitor:
        print(f"Starting performance monitoring (interval: {args.interval}s)")
        try:
            while True:
                report = optimizer.generate_optimization_recommendations()
                critical_count = report["summary"]["critical_count"]
                high_count = report["summary"]["high_count"]
                
                if critical_count > 0:
                    print(f"ALERT: {critical_count} critical performance issues detected!")
                elif high_count > 0:
                    print(f"Warning: {high_count} high-priority performance issues")
                else:
                    print("Performance status: OK")
                
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("Monitoring stopped")
    
    else:
        # Default: quick status
        metrics = optimizer.collect_performance_metrics()
        print("=== QUICK PERFORMANCE STATUS ===")
        print(f"CPU: {metrics['cpu']['usage_percent']:.1f}%")
        print(f"Memory: {metrics['memory']['usage_percent']:.1f}%")
        print(f"Disk: {metrics['disk']['usage_percent']:.1f}%")
        print(f"Queue: {metrics['queue']['pending_tasks']} pending")
        print(f"Workers: {metrics['workers']['running_count']} running")