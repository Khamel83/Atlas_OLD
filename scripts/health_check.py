#!/usr/bin/env python3

"""
Atlas Health Check Script
Comprehensive health monitoring for Atlas deployment
"""

import sys
import json
import time
import sqlite3
import requests
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional, Tuple

# Add the parent directory to the path to import Atlas modules
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from helpers.config import load_config
except ImportError:
    print("Warning: Could not import Atlas config module")
    load_config = None

class AtlasHealthChecker:
    """Comprehensive health checker for Atlas system"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path)
        self.results = {}
        
    def _load_config(self, config_path: Optional[str]) -> Dict:
        """Load Atlas configuration"""
        if load_config and not config_path:
            try:
                return load_config()
            except Exception as e:
                print(f"Warning: Could not load Atlas config: {e}")
        
        # Fallback to environment variables
        import os
        return {
            "atlas_host": os.getenv("ATLAS_HOST", "localhost"),
            "atlas_port": int(os.getenv("ATLAS_PORT", "5000")),
            "database_path": os.getenv("DATABASE_PATH", "data/atlas.db"),
            "data_directory": os.getenv("ATLAS_DATA_DIR", "data"),
            "export_directory": os.getenv("EXPORT_DIR", "exports"),
            "log_directory": os.getenv("LOG_DIR", "logs")
        }
    
    def check_api_health(self) -> Tuple[bool, Dict]:
        """Check Atlas API health"""
        try:
            host = self.config.get("atlas_host", "localhost")
            port = self.config.get("atlas_port", 5000)
            
            # Health endpoint
            health_url = f"http://{host}:{port}/api/capture/health"
            response = requests.get(health_url, timeout=10)
            
            if response.status_code == 200:
                health_data = response.json()
                return True, {
                    "status": "healthy",
                    "response_time": response.elapsed.total_seconds(),
                    "data": health_data
                }
            else:
                return False, {
                    "status": "unhealthy",
                    "status_code": response.status_code,
                    "error": response.text
                }
                
        except requests.RequestException as e:
            return False, {
                "status": "connection_failed",
                "error": str(e)
            }
        except Exception as e:
            return False, {
                "status": "error",
                "error": str(e)
            }
    
    def check_database_health(self) -> Tuple[bool, Dict]:
        """Check database connectivity and basic metrics"""
        try:
            db_path = self.config.get("database_path", "data/atlas.db")
            
            if not Path(db_path).exists():
                return False, {
                    "status": "database_not_found",
                    "path": db_path
                }
            
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check if main tables exist
            tables_check = {}
            expected_tables = ["episodes", "capture_queue", "export_history"]
            
            for table in expected_tables:
                try:
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    count = cursor.fetchone()[0]
                    tables_check[table] = {"exists": True, "count": count}
                except sqlite3.OperationalError:
                    tables_check[table] = {"exists": False, "count": 0}
            
            # Database size
            db_size = Path(db_path).stat().st_size
            
            # Recent activity check
            recent_activity = {}
            try:
                cursor.execute("""
                    SELECT COUNT(*) FROM capture_queue 
                    WHERE captured_at > datetime('now', '-24 hours')
                """)
                recent_activity["captures_24h"] = cursor.fetchone()[0]
            except:
                recent_activity["captures_24h"] = "unknown"
            
            conn.close()
            
            return True, {
                "status": "healthy",
                "path": db_path,
                "size_bytes": db_size,
                "tables": tables_check,
                "recent_activity": recent_activity
            }
            
        except Exception as e:
            return False, {
                "status": "error",
                "error": str(e)
            }
    
    def check_disk_space(self) -> Tuple[bool, Dict]:
        """Check available disk space"""
        try:
            import shutil
            
            # Check main data directory
            data_dir = self.config.get("data_directory", "data")
            if Path(data_dir).exists():
                total, used, free = shutil.disk_usage(data_dir)
                free_percent = (free / total) * 100
                
                return free_percent > 10, {  # Alert if less than 10% free
                    "status": "healthy" if free_percent > 10 else "low_space",
                    "total_gb": round(total / (1024**3), 2),
                    "used_gb": round(used / (1024**3), 2),
                    "free_gb": round(free / (1024**3), 2),
                    "free_percent": round(free_percent, 2)
                }
            else:
                return False, {
                    "status": "directory_not_found",
                    "path": data_dir
                }
                
        except Exception as e:
            return False, {
                "status": "error",
                "error": str(e)
            }
    
    def check_background_service(self) -> Tuple[bool, Dict]:
        """Check if background service is running"""
        try:
            import psutil
            
            # Look for Atlas background service process
            atlas_processes = []
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    cmdline = ' '.join(proc.info['cmdline'] or [])
                    if 'atlas_background_service' in cmdline:
                        atlas_processes.append({
                            'pid': proc.info['pid'],
                            'name': proc.info['name'],
                            'cmdline': cmdline
                        })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            if atlas_processes:
                return True, {
                    "status": "running",
                    "processes": atlas_processes
                }
            else:
                return False, {
                    "status": "not_running",
                    "processes": []
                }
                
        except ImportError:
            return None, {
                "status": "psutil_not_available",
                "message": "Install psutil for process monitoring"
            }
        except Exception as e:
            return False, {
                "status": "error",
                "error": str(e)
            }
    
    def check_log_files(self) -> Tuple[bool, Dict]:
        """Check log files for recent errors"""
        try:
            log_dir = Path(self.config.get("log_directory", "logs"))
            
            if not log_dir.exists():
                return False, {
                    "status": "log_directory_not_found",
                    "path": str(log_dir)
                }
            
            log_files = list(log_dir.glob("*.log"))
            if not log_files:
                return False, {
                    "status": "no_log_files",
                    "path": str(log_dir)
                }
            
            # Check most recent log file for errors
            recent_log = max(log_files, key=lambda x: x.stat().st_mtime)
            
            error_count = 0
            warning_count = 0
            recent_errors = []
            
            try:
                with open(recent_log, 'r') as f:
                    lines = f.readlines()
                    
                # Check last 100 lines for errors/warnings
                for line in lines[-100:]:
                    if 'ERROR' in line.upper():
                        error_count += 1
                        recent_errors.append(line.strip())
                    elif 'WARNING' in line.upper():
                        warning_count += 1
                
                return error_count == 0, {
                    "status": "healthy" if error_count == 0 else "errors_found",
                    "recent_log": str(recent_log),
                    "error_count": error_count,
                    "warning_count": warning_count,
                    "recent_errors": recent_errors[-5:]  # Last 5 errors
                }
                
            except Exception as e:
                return False, {
                    "status": "cannot_read_logs",
                    "error": str(e)
                }
                
        except Exception as e:
            return False, {
                "status": "error",
                "error": str(e)
            }
    
    def run_comprehensive_check(self) -> Dict:
        """Run all health checks"""
        checks = {
            "api": self.check_api_health(),
            "database": self.check_database_health(),
            "disk_space": self.check_disk_space(),
            "background_service": self.check_background_service(),
            "logs": self.check_log_files()
        }
        
        overall_health = True
        summary = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": "unknown",
            "checks": {}
        }
        
        for check_name, (status, details) in checks.items():
            summary["checks"][check_name] = {
                "healthy": status,
                "details": details
            }
            
            # Overall health is false if any critical check fails
            if status is False:
                overall_health = False
            elif status is None:  # Some checks return None for "unknown"
                pass  # Don't affect overall health
        
        summary["overall_status"] = "healthy" if overall_health else "unhealthy"
        
        return summary
    
    def generate_report(self, format_type: str = "text") -> str:
        """Generate health report in specified format"""
        health_data = self.run_comprehensive_check()
        
        if format_type == "json":
            return json.dumps(health_data, indent=2)
        
        elif format_type == "text":
            report = []
            report.append("=" * 50)
            report.append("ATLAS HEALTH CHECK REPORT")
            report.append("=" * 50)
            report.append(f"Timestamp: {health_data['timestamp']}")
            report.append(f"Overall Status: {health_data['overall_status'].upper()}")
            report.append("")
            
            for check_name, check_data in health_data["checks"].items():
                status_icon = "✅" if check_data["healthy"] else "❌" if check_data["healthy"] is False else "⚠️"
                report.append(f"{status_icon} {check_name.upper()}")
                
                # Add key details
                details = check_data["details"]
                if "status" in details:
                    report.append(f"   Status: {details['status']}")
                if "error" in details:
                    report.append(f"   Error: {details['error']}")
                if "response_time" in details:
                    report.append(f"   Response Time: {details['response_time']:.3f}s")
                if "free_percent" in details:
                    report.append(f"   Free Space: {details['free_percent']:.1f}%")
                if "processes" in details and details["processes"]:
                    report.append(f"   Running Processes: {len(details['processes'])}")
                
                report.append("")
            
            return "\n".join(report)
        
        else:
            raise ValueError(f"Unsupported format: {format_type}")

def main():
    parser = argparse.ArgumentParser(description="Atlas Health Check")
    parser.add_argument("--config", help="Path to config file")
    parser.add_argument("--format", choices=["text", "json"], default="text", 
                       help="Output format")
    parser.add_argument("--output", help="Output file (default: stdout)")
    parser.add_argument("--continuous", action="store_true", 
                       help="Run continuously with interval")
    parser.add_argument("--interval", type=int, default=60, 
                       help="Interval in seconds for continuous mode")
    
    args = parser.parse_args()
    
    checker = AtlasHealthChecker(args.config)
    
    if args.continuous:
        print(f"Running continuous health checks every {args.interval} seconds...")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                report = checker.generate_report(args.format)
                
                if args.output:
                    with open(args.output, 'w') as f:
                        f.write(report)
                    print(f"Health report written to {args.output}")
                else:
                    print(report)
                    print("-" * 50)
                
                time.sleep(args.interval)
                
        except KeyboardInterrupt:
            print("Health check stopped.")
    
    else:
        report = checker.generate_report(args.format)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Health report written to {args.output}")
        else:
            print(report)
        
        # Exit with non-zero code if unhealthy
        health_data = checker.run_comprehensive_check()
        if health_data["overall_status"] != "healthy":
            sys.exit(1)

if __name__ == "__main__":
    main()