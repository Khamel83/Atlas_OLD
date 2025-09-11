#!/usr/bin/env python3
"""
Atlas Disk Cleanup
Automated disk space management and cleanup system.
"""

import os
import sys
import time
import gzip
import shutil
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers.resource_manager import get_resource_manager

@dataclass
class CleanupRule:
    """Disk cleanup rule configuration"""
    path: Path
    pattern: str
    max_age_days: int
    action: str  # delete, compress, archive
    size_threshold_mb: Optional[int] = None
    keep_count: Optional[int] = None

@dataclass
class CleanupResult:
    """Result of cleanup operation"""
    files_processed: int
    space_freed_mb: float
    errors: List[str]
    actions_taken: List[str]

class DiskCleanup:
    """Automated disk cleanup and space management."""
    
    def __init__(self):
        self.setup_logging()
        self.resource_manager = get_resource_manager()
        
        # Cleanup rules configuration
        self.cleanup_rules = self._get_default_cleanup_rules()
        self.cleanup_history: List[Dict[str, Any]] = []
        
        # Safety thresholds
        self.min_free_space_gb = 2.0  # Never go below 2GB free
        self.emergency_threshold = 0.95  # 95% disk usage triggers emergency cleanup
        
    def setup_logging(self):
        """Setup logging for disk cleanup."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        self.logger = logging.getLogger("disk_cleanup")
        self.logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(log_dir / "disk_cleanup.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def _get_default_cleanup_rules(self) -> List[CleanupRule]:
        """Get default cleanup rules for Atlas system."""
        base_path = Path(".")
        
        return [
            # Log files older than 30 days
            CleanupRule(
                path=base_path / "logs",
                pattern="*.log.*",
                max_age_days=30,
                action="delete"
            ),
            
            # Compress large log files older than 7 days
            CleanupRule(
                path=base_path / "logs", 
                pattern="*.log",
                max_age_days=7,
                action="compress",
                size_threshold_mb=10
            ),
            
            # Old backup files older than 60 days
            CleanupRule(
                path=base_path / "backups",
                pattern="*.bak",
                max_age_days=60,
                action="delete"
            ),
            
            # Keep only last 10 database backups
            CleanupRule(
                path=base_path / "data" / "backups",
                pattern="atlas_backup_*.db",
                max_age_days=0,  # Age doesn't matter, count-based
                action="delete",
                keep_count=10
            ),
            
            # Temporary files older than 1 day
            CleanupRule(
                path=base_path / "data",
                pattern="*.tmp",
                max_age_days=1,
                action="delete"
            ),
            
            # Old cache files older than 14 days
            CleanupRule(
                path=base_path / "data",
                pattern="cache_*",
                max_age_days=14,
                action="delete"
            ),
            
            # Memory leak reports older than 30 days
            CleanupRule(
                path=base_path / "logs",
                pattern="memory_leak_*.json",
                max_age_days=30,
                action="delete"
            ),
            
            # Old test artifacts
            CleanupRule(
                path=base_path / "test-artifacts",
                pattern="*",
                max_age_days=7,
                action="delete"
            ),
            
            # Large documents older than 90 days (archive)
            CleanupRule(
                path=base_path / "data" / "documents",
                pattern="*.md",
                max_age_days=90,
                action="compress",
                size_threshold_mb=1
            )
        ]
    
    def get_directory_size(self, path: Path) -> Tuple[int, float]:
        """Get directory size in bytes and MB."""
        total_size = 0
        file_count = 0
        
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    filepath = Path(dirpath) / filename
                    try:
                        total_size += filepath.stat().st_size
                        file_count += 1
                    except (OSError, FileNotFoundError):
                        continue
        except (OSError, PermissionError):
            pass
        
        return file_count, total_size / (1024 * 1024)  # MB
    
    def get_disk_usage(self, path: str = ".") -> Dict[str, float]:
        """Get disk usage information."""
        total, used, free = shutil.disk_usage(path)
        
        return {
            "total_gb": total / (1024**3),
            "used_gb": used / (1024**3),
            "free_gb": free / (1024**3),
            "usage_percent": (used / total) * 100
        }
    
    def compress_file(self, file_path: Path) -> bool:
        """Compress a file using gzip."""
        try:
            compressed_path = file_path.with_suffix(file_path.suffix + '.gz')
            
            with open(file_path, 'rb') as f_in:
                with gzip.open(compressed_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            # Remove original file
            file_path.unlink()
            self.logger.info(f"Compressed {file_path} -> {compressed_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to compress {file_path}: {e}")
            return False
    
    def apply_cleanup_rule(self, rule: CleanupRule) -> CleanupResult:
        """Apply a single cleanup rule."""
        result = CleanupResult(
            files_processed=0,
            space_freed_mb=0.0,
            errors=[],
            actions_taken=[]
        )
        
        if not rule.path.exists():
            return result
        
        try:
            # Find matching files
            if rule.pattern == "*":
                matching_files = list(rule.path.rglob("*"))
                matching_files = [f for f in matching_files if f.is_file()]
            else:
                matching_files = list(rule.path.glob(rule.pattern))
                # Also check subdirectories for recursive patterns
                if "**" not in rule.pattern:
                    matching_files.extend(list(rule.path.rglob(rule.pattern)))
            
            # Remove duplicates
            matching_files = list(set(matching_files))
            
            # Apply filters
            filtered_files = []
            
            for file_path in matching_files:
                try:
                    if not file_path.is_file():
                        continue
                    
                    file_stat = file_path.stat()
                    file_age = (datetime.now() - datetime.fromtimestamp(file_stat.st_mtime)).days
                    file_size_mb = file_stat.st_size / (1024 * 1024)
                    
                    # Age filter
                    if rule.max_age_days > 0 and file_age < rule.max_age_days:
                        continue
                    
                    # Size filter
                    if rule.size_threshold_mb and file_size_mb < rule.size_threshold_mb:
                        continue
                    
                    filtered_files.append((file_path, file_stat))
                    
                except (OSError, FileNotFoundError):
                    continue
            
            # Apply keep_count filter (keep newest files)
            if rule.keep_count is not None:
                filtered_files.sort(key=lambda x: x[1].st_mtime, reverse=True)
                filtered_files = filtered_files[rule.keep_count:]
            
            # Process files
            for file_path, file_stat in filtered_files:
                try:
                    file_size_mb = file_stat.st_size / (1024 * 1024)
                    
                    if rule.action == "delete":
                        file_path.unlink()
                        result.actions_taken.append(f"Deleted {file_path}")
                        result.space_freed_mb += file_size_mb
                        
                    elif rule.action == "compress":
                        if self.compress_file(file_path):
                            # Estimate compression savings (typical 70% reduction)
                            result.space_freed_mb += file_size_mb * 0.7
                            result.actions_taken.append(f"Compressed {file_path}")
                        else:
                            result.errors.append(f"Failed to compress {file_path}")
                    
                    elif rule.action == "archive":
                        # For now, just compress (could implement proper archiving later)
                        if self.compress_file(file_path):
                            result.space_freed_mb += file_size_mb * 0.7
                            result.actions_taken.append(f"Archived {file_path}")
                        else:
                            result.errors.append(f"Failed to archive {file_path}")
                    
                    result.files_processed += 1
                    
                except Exception as e:
                    result.errors.append(f"Error processing {file_path}: {e}")
        
        except Exception as e:
            result.errors.append(f"Error applying rule for {rule.path}: {e}")
        
        return result
    
    def routine_cleanup(self) -> Dict[str, Any]:
        """Perform routine cleanup based on configured rules."""
        cleanup_session = {
            "timestamp": datetime.now().isoformat(),
            "type": "routine",
            "disk_before": self.get_disk_usage(),
            "rules_applied": [],
            "total_files_processed": 0,
            "total_space_freed_mb": 0.0,
            "errors": []
        }
        
        self.logger.info("Starting routine cleanup...")
        
        for i, rule in enumerate(self.cleanup_rules):
            rule_result = self.apply_cleanup_rule(rule)
            
            rule_summary = {
                "rule_index": i,
                "path": str(rule.path),
                "pattern": rule.pattern,
                "action": rule.action,
                "files_processed": rule_result.files_processed,
                "space_freed_mb": rule_result.space_freed_mb,
                "actions_taken": rule_result.actions_taken,
                "errors": rule_result.errors
            }
            
            cleanup_session["rules_applied"].append(rule_summary)
            cleanup_session["total_files_processed"] += rule_result.files_processed
            cleanup_session["total_space_freed_mb"] += rule_result.space_freed_mb
            cleanup_session["errors"].extend(rule_result.errors)
        
        cleanup_session["disk_after"] = self.get_disk_usage()
        
        self.logger.info(f"Routine cleanup completed: "
                        f"{cleanup_session['total_files_processed']} files, "
                        f"{cleanup_session['total_space_freed_mb']:.1f}MB freed")
        
        return cleanup_session
    
    def emergency_cleanup(self) -> Dict[str, Any]:
        """Perform aggressive cleanup when disk space is critically low."""
        cleanup_session = {
            "timestamp": datetime.now().isoformat(),
            "type": "emergency",
            "disk_before": self.get_disk_usage(),
            "actions_taken": [],
            "total_space_freed_mb": 0.0,
            "errors": []
        }
        
        self.logger.warning("Starting emergency cleanup!")
        
        # Emergency actions (more aggressive than routine)
        emergency_actions = [
            # Delete all compressed logs older than 7 days
            ("logs/*.gz", 7, "delete"),
            # Delete all tmp files regardless of age
            ("data/*.tmp", 0, "delete"),
            ("*.tmp", 0, "delete"),
            # Delete old cache files
            ("data/cache_*", 1, "delete"),
            # Delete old memory leak reports
            ("logs/memory_leak_*.json", 7, "delete"),
            # Delete old test artifacts
            ("test-artifacts/*", 0, "delete"),
            # Delete old backup files
            ("backups/*.bak", 14, "delete"),
        ]
        
        for pattern, max_age_days, action in emergency_actions:
            try:
                # Find and process files
                if "/" in pattern:
                    base_path, file_pattern = pattern.rsplit("/", 1)
                    search_path = Path(base_path)
                else:
                    search_path = Path(".")
                    file_pattern = pattern
                
                if not search_path.exists():
                    continue
                
                matching_files = list(search_path.glob(file_pattern))
                
                for file_path in matching_files:
                    try:
                        if not file_path.is_file():
                            continue
                        
                        file_stat = file_path.stat()
                        file_age = (datetime.now() - datetime.fromtimestamp(file_stat.st_mtime)).days
                        
                        if max_age_days > 0 and file_age < max_age_days:
                            continue
                        
                        file_size_mb = file_stat.st_size / (1024 * 1024)
                        
                        if action == "delete":
                            file_path.unlink()
                            cleanup_session["actions_taken"].append(f"Emergency deleted {file_path}")
                            cleanup_session["total_space_freed_mb"] += file_size_mb
                    
                    except Exception as e:
                        cleanup_session["errors"].append(f"Error processing {file_path}: {e}")
            
            except Exception as e:
                cleanup_session["errors"].append(f"Error with pattern {pattern}: {e}")
        
        cleanup_session["disk_after"] = self.get_disk_usage()
        
        self.logger.warning(f"Emergency cleanup completed: "
                           f"{cleanup_session['total_space_freed_mb']:.1f}MB freed")
        
        return cleanup_session
    
    def auto_cleanup(self) -> Dict[str, Any]:
        """Automatic cleanup based on disk usage thresholds."""
        disk_usage = self.get_disk_usage()
        
        auto_cleanup_result = {
            "timestamp": datetime.now().isoformat(),
            "disk_usage": disk_usage,
            "cleanup_triggered": False,
            "cleanup_type": None,
            "cleanup_result": None
        }
        
        # Check if cleanup is needed
        if disk_usage["usage_percent"] >= self.emergency_threshold * 100:
            # Emergency cleanup
            auto_cleanup_result["cleanup_triggered"] = True
            auto_cleanup_result["cleanup_type"] = "emergency"
            auto_cleanup_result["cleanup_result"] = self.emergency_cleanup()
            
        elif disk_usage["usage_percent"] >= 80:  # Warning threshold
            # Routine cleanup
            auto_cleanup_result["cleanup_triggered"] = True
            auto_cleanup_result["cleanup_type"] = "routine"
            auto_cleanup_result["cleanup_result"] = self.routine_cleanup()
        
        # Record in history
        if auto_cleanup_result["cleanup_triggered"]:
            self.cleanup_history.append(auto_cleanup_result)
            
            # Keep only last 50 cleanup sessions
            if len(self.cleanup_history) > 50:
                self.cleanup_history.pop(0)
        
        return auto_cleanup_result
    
    def get_cleanup_status(self) -> Dict[str, Any]:
        """Get current cleanup status and recommendations."""
        disk_usage = self.get_disk_usage()
        
        # Calculate directory sizes
        directory_sizes = {}
        important_dirs = ["logs", "data", "backups", "test-artifacts"]
        
        for dir_name in important_dirs:
            dir_path = Path(dir_name)
            if dir_path.exists():
                file_count, size_mb = self.get_directory_size(dir_path)
                directory_sizes[dir_name] = {
                    "files": file_count,
                    "size_mb": size_mb
                }
        
        status = {
            "timestamp": datetime.now().isoformat(),
            "disk_usage": disk_usage,
            "directory_sizes": directory_sizes,
            "cleanup_recommendations": [],
            "recent_cleanups": self.cleanup_history[-5:] if self.cleanup_history else [],
            "next_cleanup_type": "none"
        }
        
        # Generate recommendations
        if disk_usage["usage_percent"] >= self.emergency_threshold * 100:
            status["next_cleanup_type"] = "emergency"
            status["cleanup_recommendations"].append("URGENT: Emergency cleanup needed")
        elif disk_usage["usage_percent"] >= 80:
            status["next_cleanup_type"] = "routine"
            status["cleanup_recommendations"].append("Routine cleanup recommended")
        
        # Check for large directories
        for dir_name, info in directory_sizes.items():
            if info["size_mb"] > 1000:  # > 1GB
                status["cleanup_recommendations"].append(
                    f"Large directory detected: {dir_name} ({info['size_mb']:.1f}MB)"
                )
        
        return status

def check_throttling():
    """Check if system should be throttled due to resource constraints."""
    resource_manager = get_resource_manager()
    resource_status = resource_manager.monitor_resources()
    
    throttle_needed = (
        resource_status["cpu"]["throttle_level"] in ["warning", "critical"] or
        resource_status["memory"]["pressure_level"] in ["warning", "critical"] or
        resource_status["disk"]["cleanup_level"] != "none"
    )
    
    return {
        "throttle_needed": throttle_needed,
        "resource_status": resource_status,
        "recommendations": resource_manager.get_resource_recommendations()
    }

if __name__ == "__main__":
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description="Atlas Disk Cleanup")
    parser.add_argument("--routine", action="store_true", help="Run routine cleanup")
    parser.add_argument("--emergency", action="store_true", help="Run emergency cleanup")
    parser.add_argument("--auto", action="store_true", help="Run automatic cleanup")
    parser.add_argument("--status", action="store_true", help="Show cleanup status")
    parser.add_argument("--monitor", action="store_true", help="Start monitoring mode")
    parser.add_argument("--interval", type=int, default=300, help="Monitoring interval in seconds")
    
    args = parser.parse_args()
    
    cleanup = DiskCleanup()
    
    if args.routine:
        result = cleanup.routine_cleanup()
        print(json.dumps(result, indent=2))
    elif args.emergency:
        result = cleanup.emergency_cleanup()
        print(json.dumps(result, indent=2))
    elif args.auto:
        result = cleanup.auto_cleanup()
        print(json.dumps(result, indent=2))
    elif args.status:
        status = cleanup.get_cleanup_status()
        print(json.dumps(status, indent=2))
    elif args.monitor:
        print(f"Starting disk cleanup monitoring (interval: {args.interval}s)")
        try:
            while True:
                result = cleanup.auto_cleanup()
                if result["cleanup_triggered"]:
                    print(f"Cleanup performed: {result['cleanup_type']}")
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("Monitoring stopped")
    else:
        # Default: show current status
        status = cleanup.get_cleanup_status()
        print("=== DISK CLEANUP STATUS ===")
        print(f"Disk usage: {status['disk_usage']['usage_percent']:.1f}%")
        print(f"Free space: {status['disk_usage']['free_gb']:.1f}GB")
        print(f"Next cleanup: {status['next_cleanup_type']}")
        
        if status["cleanup_recommendations"]:
            print("\nRecommendations:")
            for rec in status["cleanup_recommendations"]:
                print(f"  • {rec}")