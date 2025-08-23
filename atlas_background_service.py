#!/usr/bin/env python3
"""
Atlas Background Service Manager

Provides comprehensive background service automation including:
- Content processing pipeline
- Search index maintenance  
- Analytics sync
- API server management
- Health monitoring
- Auto-restart capabilities
"""

import os
import sys
import json
import time
import logging
import psutil
import signal
import subprocess
import threading
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent))

from helpers.config import load_config

class AtlasServiceManager:
    """Comprehensive Atlas background service manager"""
    
    def __init__(self):
        """Initialize service manager"""
        self.config = load_config()
        self.services = {}
        self.running = False
        self.log_dir = Path("logs")
        self.log_dir.mkdir(exist_ok=True)
        self.pid_file = Path("atlas_service.pid")
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_dir / "atlas_service.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger("AtlasService")
        
    def start_api_server(self) -> bool:
        """Start the Atlas API server"""
        try:
            # Check if already running
            if self._is_port_in_use(8000):
                self.logger.info("API server already running on port 8000")
                return True
                
            # Start API server
            cmd = [
                sys.executable, "-m", "uvicorn", 
                "api.main:app", 
                "--host", "0.0.0.0", 
                "--port", "8000",
                "--log-level", "info"
            ]
            
            process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=Path(__file__).parent
            )
            
            # Give it time to start
            time.sleep(3)
            
            if process.poll() is None and self._is_port_in_use(8000):
                self.services["api_server"] = {
                    "process": process,
                    "pid": process.pid,
                    "start_time": datetime.now(),
                    "status": "running"
                }
                self.logger.info(f"API server started successfully (PID: {process.pid})")
                return True
            else:
                self.logger.error("Failed to start API server")
                return False
                
        except Exception as e:
            self.logger.error(f"Error starting API server: {e}")
            return False
    
    def start_background_tasks(self) -> bool:
        """Start background processing tasks"""
        try:
            # Start scheduler for background tasks
            scheduler_cmd = [
                sys.executable, "scripts/atlas_scheduler.py", "--start"
            ]
            
            scheduler_process = subprocess.Popen(
                scheduler_cmd,
                cwd=Path(__file__).parent,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            time.sleep(2)
            
            if scheduler_process.poll() is None:
                self.services["scheduler"] = {
                    "process": scheduler_process,
                    "pid": scheduler_process.pid,
                    "start_time": datetime.now(),
                    "status": "running"
                }
                self.logger.info(f"Background scheduler started (PID: {scheduler_process.pid})")
                return True
            else:
                self.logger.error("Failed to start background scheduler")
                return False
                
        except Exception as e:
            self.logger.error(f"Error starting background tasks: {e}")
            return False
    
    def _is_port_in_use(self, port: int) -> bool:
        """Check if a port is in use"""
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('localhost', port))
                return False
            except socket.error:
                return True
    
    def start_all_services(self) -> bool:
        """Start all Atlas services"""
        self.logger.info("Starting Atlas background services...")
        
        success = True
        
        # Start API server
        if not self.start_api_server():
            success = False
            
        # Start background tasks  
        if not self.start_background_tasks():
            success = False
            
        if success:
            self.running = True
            self._write_pid_file()
            self.logger.info("All Atlas services started successfully")
        else:
            self.logger.error("Some services failed to start")
            
        return success
    
    def stop_all_services(self) -> bool:
        """Stop all Atlas services"""
        self.logger.info("Stopping Atlas background services...")
        
        self.running = False
        success = True
        
        # Stop all tracked services
        for service_name, service_info in self.services.items():
            try:
                process = service_info["process"]
                if process.poll() is None:
                    process.terminate()
                    time.sleep(2)
                    if process.poll() is None:
                        process.kill()
                    self.logger.info(f"Stopped {service_name} (PID: {service_info['pid']})")
                service_info["status"] = "stopped"
            except Exception as e:
                self.logger.error(f"Error stopping {service_name}: {e}")
                success = False
        
        # Clean up PID file
        if self.pid_file.exists():
            self.pid_file.unlink()
            
        self.logger.info("Atlas services stopped")
        return success
    
    def get_service_status(self) -> Dict[str, Any]:
        """Get status of all services"""
        status = {
            "running": self.running,
            "services": {},
            "uptime": None,
            "health": "unknown"
        }
        
        # Update service statuses
        for service_name, service_info in self.services.items():
            try:
                process = service_info["process"]
                if process.poll() is None:
                    service_info["status"] = "running"
                    service_info["uptime"] = datetime.now() - service_info["start_time"]
                else:
                    service_info["status"] = "stopped"
                    
                status["services"][service_name] = {
                    "status": service_info["status"],
                    "pid": service_info["pid"],
                    "start_time": service_info["start_time"].isoformat(),
                    "uptime": str(service_info.get("uptime", "N/A"))
                }
            except Exception as e:
                status["services"][service_name] = {
                    "status": "error",
                    "error": str(e)
                }
        
        # Overall health check
        running_services = sum(1 for s in status["services"].values() if s.get("status") == "running")
        total_services = len(status["services"])
        
        if running_services == total_services and total_services > 0:
            status["health"] = "healthy"
        elif running_services > 0:
            status["health"] = "degraded"
        else:
            status["health"] = "unhealthy"
            
        return status
    
    def health_check(self) -> Dict[str, Any]:
        """Perform comprehensive health check"""
        health = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": "healthy",
            "checks": {}
        }
        
        # Check API server
        try:
            import requests
            response = requests.get("http://localhost:8000/api/v1/health", timeout=5)
            if response.status_code == 200:
                health["checks"]["api_server"] = {"status": "healthy", "response_time": response.elapsed.total_seconds()}
            else:
                health["checks"]["api_server"] = {"status": "unhealthy", "error": f"HTTP {response.status_code}"}
        except Exception as e:
            health["checks"]["api_server"] = {"status": "unhealthy", "error": str(e)}
        
        # Check search database
        try:
            import sqlite3
            conn = sqlite3.connect("data/enhanced_search.db")
            cursor = conn.execute("SELECT COUNT(*) FROM search_index")
            count = cursor.fetchone()[0]
            conn.close()
            health["checks"]["search_database"] = {"status": "healthy", "records": count}
        except Exception as e:
            health["checks"]["search_database"] = {"status": "unhealthy", "error": str(e)}
        
        # Check disk space
        try:
            disk_usage = psutil.disk_usage('/')
            free_gb = disk_usage.free / (1024**3)
            if free_gb > 1.0:  # More than 1GB free
                health["checks"]["disk_space"] = {"status": "healthy", "free_gb": round(free_gb, 2)}
            else:
                health["checks"]["disk_space"] = {"status": "warning", "free_gb": round(free_gb, 2)}
        except Exception as e:
            health["checks"]["disk_space"] = {"status": "error", "error": str(e)}
        
        # Overall status
        unhealthy_checks = [name for name, check in health["checks"].items() if check["status"] not in ["healthy", "warning"]]
        if unhealthy_checks:
            health["overall_status"] = "unhealthy"
            health["failed_checks"] = unhealthy_checks
        elif any(check["status"] == "warning" for check in health["checks"].values()):
            health["overall_status"] = "warning"
        
        return health
    
    def _write_pid_file(self):
        """Write PID file"""
        try:
            with open(self.pid_file, 'w') as f:
                f.write(str(os.getpid()))
        except Exception as e:
            self.logger.error(f"Error writing PID file: {e}")
    
    def monitor_loop(self):
        """Main monitoring loop"""
        self.logger.info("Starting Atlas service monitoring loop")
        
        while self.running:
            try:
                # Check service health
                status = self.get_service_status()
                
                # Restart failed services
                for service_name, service_info in status["services"].items():
                    if service_info["status"] not in ["running", "healthy"]:
                        self.logger.warning(f"Service {service_name} is {service_info['status']}, attempting restart")
                        self._restart_service(service_name)
                
                # Periodic health check
                if datetime.now().minute % 15 == 0:  # Every 15 minutes
                    health = self.health_check()
                    if health["overall_status"] != "healthy":
                        self.logger.warning(f"Health check failed: {health}")
                
                time.sleep(30)  # Check every 30 seconds
                
            except KeyboardInterrupt:
                self.logger.info("Received interrupt signal, shutting down...")
                break
            except Exception as e:
                self.logger.error(f"Error in monitoring loop: {e}")
                time.sleep(60)  # Wait longer on errors
        
        self.stop_all_services()
    
    def _restart_service(self, service_name: str):
        """Restart a specific service"""
        try:
            if service_name == "api_server":
                self.start_api_server()
            elif service_name == "scheduler":
                self.start_background_tasks()
            else:
                self.logger.warning(f"Don't know how to restart service: {service_name}")
        except Exception as e:
            self.logger.error(f"Error restarting {service_name}: {e}")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Atlas Background Service Manager")
    parser.add_argument("command", choices=["start", "stop", "status", "health", "restart"], help="Command to execute")
    parser.add_argument("--daemon", action="store_true", help="Run as daemon")
    
    args = parser.parse_args()
    
    service_manager = AtlasServiceManager()
    
    if args.command == "start":
        if service_manager.start_all_services():
            if args.daemon:
                try:
                    service_manager.monitor_loop()
                except KeyboardInterrupt:
                    print("\nShutting down...")
            else:
                print("✅ Atlas services started successfully")
                print("Use 'python atlas_background_service.py status' to check status")
        else:
            print("❌ Failed to start some services")
            sys.exit(1)
    
    elif args.command == "stop":
        if service_manager.stop_all_services():
            print("✅ Atlas services stopped successfully")
        else:
            print("❌ Error stopping some services")
            sys.exit(1)
    
    elif args.command == "status":
        status = service_manager.get_service_status()
        print("🔍 Atlas Service Status")
        print(f"Overall Health: {status['health']}")
        print(f"Running: {status['running']}")
        print("\nServices:")
        for name, info in status["services"].items():
            print(f"  {name}: {info['status']} (PID: {info.get('pid', 'N/A')})")
            if info.get("uptime"):
                print(f"    Uptime: {info['uptime']}")
    
    elif args.command == "health":
        health = service_manager.health_check()
        print("🏥 Atlas Health Check")
        print(f"Overall Status: {health['overall_status']}")
        print(f"Timestamp: {health['timestamp']}")
        print("\nChecks:")
        for name, check in health["checks"].items():
            status = check["status"]
            emoji = "✅" if status == "healthy" else "⚠️" if status == "warning" else "❌"
            print(f"  {emoji} {name}: {status}")
            if "error" in check:
                print(f"    Error: {check['error']}")
            if "records" in check:
                print(f"    Records: {check['records']}")
            if "free_gb" in check:
                print(f"    Free space: {check['free_gb']} GB")
    
    elif args.command == "restart":
        print("🔄 Restarting Atlas services...")
        service_manager.stop_all_services()
        time.sleep(2)
        if service_manager.start_all_services():
            print("✅ Atlas services restarted successfully")
        else:
            print("❌ Failed to restart services")
            sys.exit(1)

if __name__ == "__main__":
    main()