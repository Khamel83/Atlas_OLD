#!/usr/bin/env python3
"""
Atlas Resource Manager
Intelligent resource management and auto-scaling based on load patterns.
"""

import os
import sys
import time
import psutil
import shutil
import logging
import gc
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from threading import Lock

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers.queue_manager import get_queue_manager, get_queue_status
from helpers.metrics_collector import get_metrics_collector

@dataclass
class ResourceThresholds:
    """Resource threshold configuration"""
    memory_warning: float = 0.8  # 80%
    memory_critical: float = 0.9  # 90%
    disk_warning: float = 0.8    # 80%
    disk_critical: float = 0.9   # 90%
    cpu_warning: float = 4.0     # Load average
    cpu_critical: float = 6.0    # Load average
    max_workers: int = 5
    min_workers: int = 1

@dataclass
class WorkerScaleRule:
    """Worker scaling rules based on queue depth"""
    queue_depth_thresholds: List[int]  # Queue depths that trigger scaling
    worker_counts: List[int]           # Corresponding worker counts
    cooldown_seconds: int = 300        # 5 minute cooldown between scaling

class ResourceManager:
    """Intelligent resource management and auto-scaling system."""
    
    def __init__(self, config_path: str = "config/resource_config.json"):
        self.config_path = Path(config_path)
        self.thresholds = ResourceThresholds()
        self.metrics = get_metrics_collector()
        self.queue_manager = get_queue_manager()
        self._lock = Lock()
        
        # Worker scaling configuration
        self.worker_scale_rule = WorkerScaleRule(
            queue_depth_thresholds=[0, 5, 15, 30, 50],
            worker_counts=[1, 2, 3, 4, 5],
            cooldown_seconds=300
        )
        
        # State tracking
        self.last_scale_time = 0
        self.current_workers = 1
        self.resource_history = []
        self.setup_logging()
        
    def setup_logging(self):
        """Setup logging for resource manager."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        self.logger = logging.getLogger("resource_manager")
        self.logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(log_dir / "resource_manager.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def check_memory_pressure(self) -> Dict[str, Any]:
        """Check system memory pressure and recommend actions."""
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()
        
        pressure_info = {
            "memory_percent": memory.percent,
            "memory_available_gb": memory.available / (1024**3),
            "swap_percent": swap.percent,
            "pressure_level": "normal",
            "recommendations": []
        }
        
        if memory.percent > self.thresholds.memory_critical * 100:
            pressure_info["pressure_level"] = "critical"
            pressure_info["recommendations"].extend([
                "Emergency garbage collection",
                "Kill non-essential processes",
                "Scale down workers if possible"
            ])
        elif memory.percent > self.thresholds.memory_warning * 100:
            pressure_info["pressure_level"] = "warning"
            pressure_info["recommendations"].extend([
                "Trigger garbage collection",
                "Reduce worker count",
                "Clear caches"
            ])
        
        # Record metrics
        self.metrics.record_metric("atlas_memory_usage_bytes", memory.used)
        self.metrics.record_metric("atlas_memory_pressure", memory.percent / 100)
        
        return pressure_info
    
    def check_disk_space(self) -> Dict[str, Any]:
        """Check disk space and recommend cleanup actions."""
        data_dir = Path("data")
        logs_dir = Path("logs")
        
        total, used, free = shutil.disk_usage(".")
        disk_usage_percent = (used / total) * 100
        
        disk_info = {
            "disk_usage_percent": disk_usage_percent,
            "free_space_gb": free / (1024**3),
            "total_space_gb": total / (1024**3),
            "cleanup_level": "none",
            "recommendations": []
        }
        
        if disk_usage_percent > self.thresholds.disk_critical * 100:
            disk_info["cleanup_level"] = "emergency"
            disk_info["recommendations"].extend([
                "Emergency log cleanup",
                "Delete old backups",
                "Compress large data files",
                "Remove temporary files"
            ])
        elif disk_usage_percent > self.thresholds.disk_warning * 100:
            disk_info["cleanup_level"] = "routine"
            disk_info["recommendations"].extend([
                "Rotate old logs",
                "Clean up temp files",
                "Archive old data"
            ])
        
        # Check specific directories
        if data_dir.exists():
            data_size = sum(f.stat().st_size for f in data_dir.rglob('*') if f.is_file())
            disk_info["data_dir_gb"] = data_size / (1024**3)
        
        if logs_dir.exists():
            logs_size = sum(f.stat().st_size for f in logs_dir.rglob('*') if f.is_file())
            disk_info["logs_dir_gb"] = logs_size / (1024**3)
        
        # Record metrics
        self.metrics.record_metric("atlas_disk_free_bytes", free)
        self.metrics.record_metric("atlas_disk_usage_percent", disk_usage_percent / 100)
        
        return disk_info
    
    def check_cpu_load(self) -> Dict[str, Any]:
        """Check CPU load and detect sustained high usage."""
        load_avg = os.getloadavg()
        cpu_percent = psutil.cpu_percent(interval=1)
        
        cpu_info = {
            "load_1min": load_avg[0],
            "load_5min": load_avg[1], 
            "load_15min": load_avg[2],
            "cpu_percent": cpu_percent,
            "throttle_level": "none",
            "recommendations": []
        }
        
        if load_avg[1] > self.thresholds.cpu_critical:
            cpu_info["throttle_level"] = "critical"
            cpu_info["recommendations"].extend([
                "Emergency CPU throttling",
                "Kill high-CPU processes",
                "Reduce worker count"
            ])
        elif load_avg[1] > self.thresholds.cpu_warning:
            cpu_info["throttle_level"] = "warning"
            cpu_info["recommendations"].extend([
                "Apply CPU throttling",
                "Reduce concurrent operations",
                "Scale down if load persists"
            ])
        
        # Record metrics
        self.metrics.record_metric("atlas_cpu_load_1min", load_avg[0])
        self.metrics.record_metric("atlas_cpu_usage_percent", cpu_percent / 100)
        
        return cpu_info
    
    def calculate_optimal_workers(self) -> int:
        """Calculate optimal worker count based on queue depth and resources."""
        queue_status = get_queue_status()
        queue_depth = queue_status.get("queue_counts", {}).get("pending", 0)
        
        # Determine worker count based on queue depth
        optimal_workers = self.thresholds.min_workers
        for i, threshold in enumerate(self.worker_scale_rule.queue_depth_thresholds):
            if queue_depth >= threshold:
                optimal_workers = self.worker_scale_rule.worker_counts[i]
        
        # Adjust based on resource constraints
        memory_info = self.check_memory_pressure()
        cpu_info = self.check_cpu_load()
        
        # Reduce workers under resource pressure
        if memory_info["pressure_level"] == "critical" or cpu_info["throttle_level"] == "critical":
            optimal_workers = max(1, optimal_workers // 2)
        elif memory_info["pressure_level"] == "warning" or cpu_info["throttle_level"] == "warning":
            optimal_workers = max(1, optimal_workers - 1)
        
        # Ensure within bounds
        optimal_workers = max(self.thresholds.min_workers, 
                            min(self.thresholds.max_workers, optimal_workers))
        
        self.logger.info(f"Queue depth: {queue_depth}, Optimal workers: {optimal_workers}")
        return optimal_workers
    
    def should_scale_workers(self, target_workers: int) -> bool:
        """Determine if worker scaling should occur (respects cooldown)."""
        if target_workers == self.current_workers:
            return False
        
        # Check cooldown period
        time_since_last_scale = time.time() - self.last_scale_time
        if time_since_last_scale < self.worker_scale_rule.cooldown_seconds:
            return False
        
        return True
    
    def apply_emergency_resource_reclaim(self) -> Dict[str, Any]:
        """Apply emergency resource reclamation measures."""
        actions_taken = []
        
        # Force garbage collection
        collected = gc.collect()
        actions_taken.append(f"Garbage collection freed {collected} objects")
        
        # Check if we can reduce workers
        if self.current_workers > 1:
            actions_taken.append("Reducing worker count to minimum")
            # Note: Actual worker scaling would be handled by worker_scaler.py
        
        # Clear metrics cache if available
        if hasattr(self.metrics, 'clear_cache'):
            self.metrics.clear_cache()
            actions_taken.append("Cleared metrics cache")
        
        self.logger.warning(f"Emergency resource reclaim: {actions_taken}")
        return {
            "timestamp": datetime.now().isoformat(),
            "actions_taken": actions_taken,
            "trigger": "emergency_resource_pressure"
        }
    
    def get_resource_recommendations(self) -> Dict[str, Any]:
        """Get performance optimization recommendations."""
        memory_info = self.check_memory_pressure()
        disk_info = self.check_disk_space()
        cpu_info = self.check_cpu_load()
        optimal_workers = self.calculate_optimal_workers()
        
        recommendations = {
            "timestamp": datetime.now().isoformat(),
            "current_workers": self.current_workers,
            "optimal_workers": optimal_workers,
            "scaling_needed": optimal_workers != self.current_workers,
            "memory": memory_info,
            "disk": disk_info,
            "cpu": cpu_info,
            "immediate_actions": [],
            "long_term_optimizations": []
        }
        
        # Immediate actions
        if memory_info["pressure_level"] in ["warning", "critical"]:
            recommendations["immediate_actions"].extend(memory_info["recommendations"])
        
        if disk_info["cleanup_level"] != "none":
            recommendations["immediate_actions"].extend(disk_info["recommendations"])
        
        if cpu_info["throttle_level"] != "none":
            recommendations["immediate_actions"].extend(cpu_info["recommendations"])
        
        # Long-term optimizations
        if optimal_workers != self.current_workers:
            if optimal_workers > self.current_workers:
                recommendations["long_term_optimizations"].append(
                    f"Scale up workers from {self.current_workers} to {optimal_workers}"
                )
            else:
                recommendations["long_term_optimizations"].append(
                    f"Scale down workers from {self.current_workers} to {optimal_workers}"
                )
        
        # Historical pattern analysis
        if len(self.resource_history) >= 10:
            avg_memory = sum(h.get("memory_percent", 0) for h in self.resource_history[-10:]) / 10
            if avg_memory > 70:
                recommendations["long_term_optimizations"].append(
                    "Consider increasing system memory - consistently high usage"
                )
        
        return recommendations
    
    def monitor_resources(self) -> Dict[str, Any]:
        """Comprehensive resource monitoring with historical tracking."""
        with self._lock:
            current_state = {
                "timestamp": datetime.now().isoformat(),
                "memory": self.check_memory_pressure(),
                "disk": self.check_disk_space(),
                "cpu": self.check_cpu_load(),
                "workers": {
                    "current": self.current_workers,
                    "optimal": self.calculate_optimal_workers()
                }
            }
            
            # Add to history (keep last 100 entries)
            self.resource_history.append(current_state)
            if len(self.resource_history) > 100:
                self.resource_history.pop(0)
            
            # Check for emergency conditions
            emergency_needed = (
                current_state["memory"]["pressure_level"] == "critical" or
                current_state["disk"]["cleanup_level"] == "emergency" or
                current_state["cpu"]["throttle_level"] == "critical"
            )
            
            if emergency_needed:
                current_state["emergency_action"] = self.apply_emergency_resource_reclaim()
            
            return current_state

def get_resource_manager() -> ResourceManager:
    """Get singleton ResourceManager instance."""
    if not hasattr(get_resource_manager, '_instance'):
        get_resource_manager._instance = ResourceManager()
    return get_resource_manager._instance

def check_memory_pressure() -> Dict[str, Any]:
    """Convenience function to check memory pressure."""
    return get_resource_manager().check_memory_pressure()

def get_scaling_recommendation() -> Dict[str, Any]:
    """Get worker scaling recommendation."""
    rm = get_resource_manager()
    optimal = rm.calculate_optimal_workers()
    current = rm.current_workers
    
    return {
        "current_workers": current,
        "optimal_workers": optimal,
        "should_scale": rm.should_scale_workers(optimal),
        "scaling_direction": "up" if optimal > current else "down" if optimal < current else "none",
        "queue_status": get_queue_status()
    }

if __name__ == "__main__":
    rm = get_resource_manager()
    status = rm.monitor_resources()
    recommendations = rm.get_resource_recommendations()
    
    print("=== RESOURCE STATUS ===")
    print(f"Memory: {status['memory']['pressure_level']} ({status['memory']['memory_percent']:.1f}%)")
    print(f"Disk: {status['disk']['cleanup_level']} ({status['disk']['disk_usage_percent']:.1f}%)")
    print(f"CPU Load: {status['cpu']['throttle_level']} ({status['cpu']['load_5min']:.2f})")
    print(f"Workers: {status['workers']['current']} -> {status['workers']['optimal']}")
    
    if recommendations["immediate_actions"]:
        print("\n=== IMMEDIATE ACTIONS ===")
        for action in recommendations["immediate_actions"]:
            print(f"  • {action}")
    
    if recommendations["long_term_optimizations"]:
        print("\n=== OPTIMIZATION RECOMMENDATIONS ===")
        for opt in recommendations["long_term_optimizations"]:
            print(f"  • {opt}")