#!/usr/bin/env python3
"""
Robust Atlas Service Manager
Handles all background services with auto-restart, health monitoring, and recovery
"""

import os
import sys
import time
import json
import psutil
import signal
import logging
import subprocess
import threading
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

class RobustAtlasManager:
    """Robust Atlas service manager with auto-recovery"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.services = {}
        self.running = False
        self.health_check_interval = 30  # seconds
        self.restart_attempts = {}
        self.max_restart_attempts = 3
        
        # Setup logging
        self.log_dir = self.base_dir / "logs" 
        self.log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - AtlasManager - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_dir / "atlas_manager.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def is_port_in_use(self, port: int) -> bool:
        """Check if a port is in use"""
        for conn in psutil.net_connections():
            if conn.laddr.port == port:
                return True
        return False
    
    def kill_process_on_port(self, port: int):
        """Kill process using a specific port"""
        for proc in psutil.process_iter(['pid', 'connections']):
            try:
                connections = proc.info['connections'] or []
                for conn in connections:
                    if conn.laddr.port == port:
                        self.logger.info(f"Killing process {proc.info['pid']} on port {port}")
                        proc.kill()
                        proc.wait(timeout=5)
                        return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                continue
        return False
    
    def start_api_server(self, port: int = 8001) -> bool:
        """Start FastAPI server with retry logic"""
        try:
            # Check if already running
            if self.is_port_in_use(port):
                self.logger.info(f"API server already running on port {port}")
                return True
            
            # Start API server
            api_dir = self.base_dir / "api"
            cmd = [sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", str(port)]
            
            self.logger.info(f"Starting API server on port {port}")
            process = subprocess.Popen(
                cmd,
                cwd=api_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                preexec_fn=os.setsid
            )
            
            # Wait a moment and check if it started
            time.sleep(3)
            if self.is_port_in_use(port):
                self.services['api_server'] = {
                    'process': process,
                    'port': port,
                    'started_at': datetime.now(),
                    'status': 'running'
                }
                self.logger.info(f"✅ API server started successfully on port {port}")
                return True
            else:
                self.logger.error("❌ API server failed to start")
                process.kill()
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to start API server: {e}")
            return False
    
    def start_background_processor(self) -> bool:
        """Start background content processing"""
        try:
            # Check if Atlas processing is working by running a quick test
            cmd = [sys.executable, "atlas_status.py"]
            result = subprocess.run(cmd, cwd=self.base_dir, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                self.logger.info("✅ Atlas core processing is operational")
                
                # Start a simple background processor
                processor_cmd = [sys.executable, "-c", """
import time
import sys
import subprocess
from pathlib import Path

# Background processing loop
while True:
    try:
        # Process articles every 30 minutes
        subprocess.run([sys.executable, 'run.py', '--articles'], timeout=300, capture_output=True)
        # Process podcasts every hour  
        subprocess.run([sys.executable, 'run.py', '--podcasts'], timeout=600, capture_output=True)
        # Sleep for 30 minutes
        time.sleep(1800)
    except Exception as e:
        print(f'Background processing error: {e}')
        time.sleep(300)  # Wait 5 minutes on error
"""]
                
                process = subprocess.Popen(
                    processor_cmd,
                    cwd=self.base_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    preexec_fn=os.setsid
                )
                
                self.services['background_processor'] = {
                    'process': process,
                    'started_at': datetime.now(),
                    'status': 'running'
                }
                self.logger.info("✅ Background processor started")
                return True
            else:
                self.logger.error("❌ Atlas core not responding")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to start background processor: {e}")
            return False
    
    def check_service_health(self) -> Dict[str, Any]:
        """Check health of all services"""
        health = {
            'timestamp': datetime.now().isoformat(),
            'overall_status': 'healthy',
            'services': {}
        }
        
        for service_name, service_info in self.services.items():
            try:
                process = service_info.get('process')
                if process and process.poll() is None:
                    # Process is running
                    health['services'][service_name] = {
                        'status': 'running',
                        'pid': process.pid,
                        'started_at': service_info.get('started_at', '').isoformat() if hasattr(service_info.get('started_at', ''), 'isoformat') else str(service_info.get('started_at', '')),
                        'uptime_seconds': (datetime.now() - service_info.get('started_at', datetime.now())).total_seconds()
                    }
                else:
                    # Process is dead
                    health['services'][service_name] = {
                        'status': 'dead',
                        'pid': None,
                        'started_at': None,
                        'uptime_seconds': 0
                    }
                    health['overall_status'] = 'unhealthy'
                    
            except Exception as e:
                health['services'][service_name] = {
                    'status': 'error',
                    'error': str(e)
                }
                health['overall_status'] = 'unhealthy'
        
        # Check API server port specifically
        if 'api_server' in self.services:
            port = self.services['api_server'].get('port', 8001)
            if not self.is_port_in_use(port):
                health['services']['api_server']['status'] = 'port_not_responding'
                health['overall_status'] = 'unhealthy'
        
        return health
    
    def restart_service(self, service_name: str) -> bool:
        """Restart a specific service"""
        self.logger.info(f"🔄 Restarting service: {service_name}")
        
        # Track restart attempts
        if service_name not in self.restart_attempts:
            self.restart_attempts[service_name] = 0
        
        self.restart_attempts[service_name] += 1
        
        if self.restart_attempts[service_name] > self.max_restart_attempts:
            self.logger.error(f"❌ Max restart attempts reached for {service_name}")
            return False
        
        # Stop service if running
        if service_name in self.services:
            try:
                process = self.services[service_name].get('process')
                if process and process.poll() is None:
                    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                    process.wait(timeout=10)
            except Exception as e:
                self.logger.warning(f"Error stopping {service_name}: {e}")
            
            del self.services[service_name]
        
        # Start service
        if service_name == 'api_server':
            return self.start_api_server()
        elif service_name == 'background_processor':
            return self.start_background_processor()
        else:
            self.logger.error(f"Unknown service: {service_name}")
            return False
    
    def health_monitor_loop(self):
        """Continuous health monitoring and auto-restart"""
        self.logger.info("🔍 Starting health monitor")
        
        while self.running:
            try:
                health = self.check_service_health()
                
                # Check each service and restart if needed
                for service_name, service_health in health['services'].items():
                    if service_health['status'] in ['dead', 'error', 'port_not_responding']:
                        self.logger.warning(f"⚠️ Service {service_name} is {service_health['status']}")
                        self.restart_service(service_name)
                
                # Reset restart attempts if all services are healthy
                if health['overall_status'] == 'healthy':
                    self.restart_attempts = {}
                
                # Log status periodically
                if datetime.now().minute % 15 == 0:  # Every 15 minutes
                    running_services = [name for name, info in health['services'].items() if info['status'] == 'running']
                    self.logger.info(f"📊 Services running: {', '.join(running_services)}")
                
                time.sleep(self.health_check_interval)
                
            except Exception as e:
                self.logger.error(f"Health monitor error: {e}")
                time.sleep(60)  # Wait longer on error
    
    def start_all_services(self):
        """Start all Atlas services"""
        self.logger.info("🚀 Starting Atlas services...")
        self.running = True
        
        success_count = 0
        
        # Start API server
        if self.start_api_server():
            success_count += 1
        
        # Start background processor
        if self.start_background_processor():
            success_count += 1
        
        if success_count > 0:
            self.logger.info(f"✅ Started {success_count} services successfully")
            
            # Start health monitoring in background thread
            monitor_thread = threading.Thread(target=self.health_monitor_loop, daemon=True)
            monitor_thread.start()
            
            return True
        else:
            self.logger.error("❌ Failed to start any services")
            return False
    
    def stop_all_services(self):
        """Stop all Atlas services"""
        self.logger.info("🛑 Stopping Atlas services...")
        self.running = False
        
        for service_name, service_info in self.services.items():
            try:
                process = service_info.get('process')
                if process and process.poll() is None:
                    self.logger.info(f"Stopping {service_name}...")
                    os.killpg(os.getpgid(process.pid), signal.SIGTERM)
                    process.wait(timeout=10)
            except Exception as e:
                self.logger.warning(f"Error stopping {service_name}: {e}")
        
        self.services.clear()
        self.logger.info("✅ All services stopped")
    
    def get_status(self) -> Dict[str, Any]:
        """Get comprehensive service status"""
        health = self.check_service_health()
        return {
            'running': self.running,
            'health': health,
            'restart_attempts': self.restart_attempts
        }

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Robust Atlas Service Manager')
    parser.add_argument('command', choices=['start', 'stop', 'restart', 'status', 'monitor'], 
                       help='Service command')
    parser.add_argument('--daemon', action='store_true', help='Run as daemon')
    
    args = parser.parse_args()
    
    manager = RobustAtlasManager()
    
    if args.command == 'start':
        if manager.start_all_services():
            print("✅ Atlas services started successfully")
            if not args.daemon:
                try:
                    print("Press Ctrl+C to stop services...")
                    while True:
                        time.sleep(1)
                except KeyboardInterrupt:
                    manager.stop_all_services()
        else:
            print("❌ Failed to start Atlas services")
            sys.exit(1)
    
    elif args.command == 'stop':
        manager.stop_all_services()
        print("✅ Atlas services stopped")
    
    elif args.command == 'restart':
        manager.stop_all_services()
        time.sleep(2)
        if manager.start_all_services():
            print("✅ Atlas services restarted successfully")
        else:
            print("❌ Failed to restart Atlas services")
            sys.exit(1)
    
    elif args.command == 'status':
        status = manager.get_status()
        print(f"🔍 Atlas Service Status")
        print(f"Running: {status['running']}")
        print(f"Overall Health: {status['health']['overall_status']}")
        print(f"\nServices:")
        for name, info in status['health']['services'].items():
            print(f"  {name}: {info['status']} (PID: {info.get('pid', 'N/A')})")
        
        if status['restart_attempts']:
            print(f"\nRestart Attempts: {status['restart_attempts']}")
    
    elif args.command == 'monitor':
        manager.start_all_services()
        print("🔍 Atlas monitoring started. Press Ctrl+C to stop.")
        try:
            while True:
                status = manager.get_status()
                print(f"\r{datetime.now().strftime('%H:%M:%S')} - Status: {status['health']['overall_status']}", end='', flush=True)
                time.sleep(5)
        except KeyboardInterrupt:
            manager.stop_all_services()

if __name__ == '__main__':
    main()