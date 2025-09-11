#!/usr/bin/env python3
"""
Atlas Worker Scaler
Dynamic worker management based on queue depth and resource availability.
"""

import os
import sys
import time
import json
import signal
import logging
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers.resource_manager import get_resource_manager, get_scaling_recommendation
from helpers.queue_manager import get_queue_manager, get_queue_status
from helpers.bulletproof_process_manager import create_managed_process

@dataclass
class WorkerInstance:
    """Represents a worker instance"""
    pid: int
    worker_id: str
    worker_type: str
    started_at: datetime
    last_heartbeat: datetime
    status: str = "running"  # running, stopping, stopped

class WorkerScaler:
    """Dynamic worker scaling manager."""
    
    def __init__(self):
        self.setup_logging()
        self.resource_manager = get_resource_manager()
        self.queue_manager = get_queue_manager()
        
        # Worker tracking
        self.workers: Dict[str, WorkerInstance] = {}
        self.worker_registry_file = Path("data/worker_registry.json")
        self.scaling_history: List[Dict[str, Any]] = []
        
        # Configuration
        self.worker_script = "helpers/smart_transcription_pipeline.py"
        self.max_startup_time = 60  # seconds
        self.heartbeat_timeout = 300  # 5 minutes
        
        # Load existing workers
        self.load_worker_registry()
        
    def setup_logging(self):
        """Setup logging for worker scaler."""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        self.logger = logging.getLogger("worker_scaler")
        self.logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(log_dir / "worker_scaler.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def load_worker_registry(self):
        """Load worker registry from disk."""
        if self.worker_registry_file.exists():
            try:
                with open(self.worker_registry_file, 'r') as f:
                    data = json.load(f)
                
                for worker_data in data.get("workers", []):
                    worker = WorkerInstance(
                        pid=worker_data["pid"],
                        worker_id=worker_data["worker_id"],
                        worker_type=worker_data["worker_type"],
                        started_at=datetime.fromisoformat(worker_data["started_at"]),
                        last_heartbeat=datetime.fromisoformat(worker_data["last_heartbeat"]),
                        status=worker_data.get("status", "unknown")
                    )
                    self.workers[worker.worker_id] = worker
                    
                self.logger.info(f"Loaded {len(self.workers)} workers from registry")
            except Exception as e:
                self.logger.error(f"Failed to load worker registry: {e}")
    
    def save_worker_registry(self):
        """Save worker registry to disk."""
        try:
            self.worker_registry_file.parent.mkdir(exist_ok=True)
            
            data = {
                "updated_at": datetime.now().isoformat(),
                "workers": []
            }
            
            for worker in self.workers.values():
                data["workers"].append({
                    "pid": worker.pid,
                    "worker_id": worker.worker_id,
                    "worker_type": worker.worker_type,
                    "started_at": worker.started_at.isoformat(),
                    "last_heartbeat": worker.last_heartbeat.isoformat(),
                    "status": worker.status
                })
            
            with open(self.worker_registry_file, 'w') as f:
                json.dump(data, f, indent=2)
                
        except Exception as e:
            self.logger.error(f"Failed to save worker registry: {e}")
    
    def check_worker_health(self, worker: WorkerInstance) -> bool:
        """Check if worker process is healthy."""
        try:
            # Check if process exists
            os.kill(worker.pid, 0)
            
            # Check heartbeat timeout
            time_since_heartbeat = datetime.now() - worker.last_heartbeat
            if time_since_heartbeat.total_seconds() > self.heartbeat_timeout:
                self.logger.warning(f"Worker {worker.worker_id} heartbeat timeout")
                return False
            
            return True
        except OSError:
            # Process doesn't exist
            return False
    
    def cleanup_dead_workers(self):
        """Remove dead workers from registry."""
        dead_workers = []
        
        for worker_id, worker in self.workers.items():
            if not self.check_worker_health(worker):
                dead_workers.append(worker_id)
                self.logger.info(f"Removing dead worker {worker_id} (PID: {worker.pid})")
        
        for worker_id in dead_workers:
            del self.workers[worker_id]
        
        if dead_workers:
            self.save_worker_registry()
    
    def start_worker(self, worker_type: str = "transcript") -> Optional[WorkerInstance]:
        """Start a new worker instance."""
        worker_id = f"{worker_type}_{int(time.time())}_{len(self.workers)}"
        
        try:
            # Prepare worker command
            cmd = [
                sys.executable,
                self.worker_script,
                "--worker-id", worker_id,
                "--worker-type", worker_type
            ]
            
            # Start worker using bulletproof process manager
            process = create_managed_process(
                cmd,
                f"worker_{worker_id}",
                cwd=Path(__file__).parent.parent
            )
            
            if process and process.pid:
                worker = WorkerInstance(
                    pid=process.pid,
                    worker_id=worker_id,
                    worker_type=worker_type,
                    started_at=datetime.now(),
                    last_heartbeat=datetime.now()
                )
                
                self.workers[worker_id] = worker
                self.save_worker_registry()
                
                self.logger.info(f"Started worker {worker_id} (PID: {process.pid})")
                return worker
            else:
                self.logger.error(f"Failed to start worker {worker_id}")
                return None
                
        except Exception as e:
            self.logger.error(f"Exception starting worker: {e}")
            return None
    
    def stop_worker(self, worker_id: str, graceful: bool = True) -> bool:
        """Stop a worker instance."""
        if worker_id not in self.workers:
            self.logger.warning(f"Worker {worker_id} not found")
            return False
        
        worker = self.workers[worker_id]
        
        try:
            if graceful:
                # Send SIGTERM for graceful shutdown
                os.kill(worker.pid, signal.SIGTERM)
                self.logger.info(f"Sent SIGTERM to worker {worker_id}")
                
                # Wait up to 30 seconds for graceful shutdown
                for _ in range(30):
                    if not self.check_worker_health(worker):
                        break
                    time.sleep(1)
                
                # Force kill if still running
                if self.check_worker_health(worker):
                    os.kill(worker.pid, signal.SIGKILL)
                    self.logger.warning(f"Force killed worker {worker_id}")
            else:
                # Force kill immediately
                os.kill(worker.pid, signal.SIGKILL)
                self.logger.info(f"Force killed worker {worker_id}")
            
            # Remove from registry
            del self.workers[worker_id]
            self.save_worker_registry()
            return True
            
        except OSError as e:
            # Process might already be dead
            if e.errno == 3:  # No such process
                del self.workers[worker_id]
                self.save_worker_registry()
                return True
            else:
                self.logger.error(f"Error stopping worker {worker_id}: {e}")
                return False
    
    def scale_workers(self, target_count: int) -> Dict[str, Any]:
        """Scale workers to target count."""
        current_count = len([w for w in self.workers.values() if w.status == "running"])
        scale_action = {
            "timestamp": datetime.now().isoformat(),
            "current_count": current_count,
            "target_count": target_count,
            "scaling_direction": "none",
            "workers_started": [],
            "workers_stopped": [],
            "success": True
        }
        
        if target_count > current_count:
            # Scale up
            scale_action["scaling_direction"] = "up"
            workers_to_start = target_count - current_count
            
            for i in range(workers_to_start):
                worker = self.start_worker("transcript")
                if worker:
                    scale_action["workers_started"].append(worker.worker_id)
                else:
                    scale_action["success"] = False
                    break
        
        elif target_count < current_count:
            # Scale down
            scale_action["scaling_direction"] = "down"
            workers_to_stop = current_count - target_count
            
            # Stop oldest workers first
            running_workers = [
                w for w in self.workers.values() 
                if w.status == "running"
            ]
            running_workers.sort(key=lambda w: w.started_at)
            
            for i in range(min(workers_to_stop, len(running_workers))):
                worker = running_workers[i]
                if self.stop_worker(worker.worker_id):
                    scale_action["workers_stopped"].append(worker.worker_id)
                else:
                    scale_action["success"] = False
                    break
        
        # Record scaling action
        self.scaling_history.append(scale_action)
        
        # Keep only last 50 scaling actions
        if len(self.scaling_history) > 50:
            self.scaling_history.pop(0)
        
        self.logger.info(f"Scaling {scale_action['scaling_direction']}: "
                        f"{current_count} -> {target_count} workers")
        
        return scale_action
    
    def auto_scale(self) -> Dict[str, Any]:
        """Perform automatic scaling based on current conditions."""
        # Clean up dead workers first
        self.cleanup_dead_workers()
        
        # Get scaling recommendation
        recommendation = get_scaling_recommendation()
        
        auto_scale_result = {
            "timestamp": datetime.now().isoformat(),
            "recommendation": recommendation,
            "action_taken": None,
            "reason": ""
        }
        
        if recommendation["should_scale"]:
            target_workers = recommendation["optimal_workers"]
            
            # Perform scaling
            scale_result = self.scale_workers(target_workers)
            auto_scale_result["action_taken"] = scale_result
            auto_scale_result["reason"] = f"Queue depth and resource analysis"
            
        else:
            auto_scale_result["reason"] = "No scaling needed or in cooldown period"
        
        return auto_scale_result
    
    def get_worker_status(self) -> Dict[str, Any]:
        """Get comprehensive worker status."""
        self.cleanup_dead_workers()
        
        running_workers = [w for w in self.workers.values() if w.status == "running"]
        
        status = {
            "timestamp": datetime.now().isoformat(),
            "total_workers": len(self.workers),
            "running_workers": len(running_workers),
            "workers": {},
            "queue_status": get_queue_status(),
            "resource_status": self.resource_manager.monitor_resources(),
            "recent_scaling": self.scaling_history[-5:] if self.scaling_history else []
        }
        
        for worker in self.workers.values():
            status["workers"][worker.worker_id] = {
                "pid": worker.pid,
                "type": worker.worker_type,
                "started_at": worker.started_at.isoformat(),
                "last_heartbeat": worker.last_heartbeat.isoformat(),
                "status": worker.status,
                "uptime_minutes": (datetime.now() - worker.started_at).total_seconds() / 60
            }
        
        return status
    
    def monitor_and_scale(self, interval: int = 60):
        """Continuous monitoring and scaling loop."""
        self.logger.info(f"Starting worker scaler monitoring (interval: {interval}s)")
        
        try:
            while True:
                try:
                    # Perform auto-scaling check
                    result = self.auto_scale()
                    
                    if result["action_taken"]:
                        self.logger.info(f"Auto-scaling performed: {result['action_taken']['scaling_direction']}")
                    
                    # Wait for next interval
                    time.sleep(interval)
                    
                except KeyboardInterrupt:
                    self.logger.info("Received interrupt signal, shutting down...")
                    break
                except Exception as e:
                    self.logger.error(f"Error in monitoring loop: {e}")
                    time.sleep(interval)
        
        finally:
            self.logger.info("Worker scaler monitoring stopped")

def test_worker_scaling():
    """Test worker scaling functionality."""
    scaler = WorkerScaler()
    
    print("=== WORKER SCALING TEST ===")
    
    # Get initial status
    status = scaler.get_worker_status()
    print(f"Initial workers: {status['running_workers']}")
    
    # Test scaling up
    print("\nTesting scale up to 3 workers...")
    scale_result = scaler.scale_workers(3)
    print(f"Scale up result: {scale_result['success']}")
    print(f"Workers started: {scale_result['workers_started']}")
    
    time.sleep(5)  # Give workers time to start
    
    # Check status
    status = scaler.get_worker_status()
    print(f"Current workers: {status['running_workers']}")
    
    # Test scaling down
    print("\nTesting scale down to 1 worker...")
    scale_result = scaler.scale_workers(1)
    print(f"Scale down result: {scale_result['success']}")
    print(f"Workers stopped: {scale_result['workers_stopped']}")
    
    time.sleep(2)
    
    # Final status
    status = scaler.get_worker_status()
    print(f"Final workers: {status['running_workers']}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Atlas Worker Scaler")
    parser.add_argument("--test", action="store_true", help="Run scaling test")
    parser.add_argument("--monitor", action="store_true", help="Start monitoring mode")
    parser.add_argument("--status", action="store_true", help="Show worker status")
    parser.add_argument("--scale", type=int, help="Scale to specific worker count")
    parser.add_argument("--interval", type=int, default=60, help="Monitoring interval in seconds")
    
    args = parser.parse_args()
    
    scaler = WorkerScaler()
    
    if args.test:
        test_worker_scaling()
    elif args.monitor:
        scaler.monitor_and_scale(args.interval)
    elif args.status:
        status = scaler.get_worker_status()
        print(json.dumps(status, indent=2))
    elif args.scale is not None:
        result = scaler.scale_workers(args.scale)
        print(json.dumps(result, indent=2))
    else:
        # Default: show current recommendation
        recommendation = get_scaling_recommendation()
        print("=== SCALING RECOMMENDATION ===")
        print(json.dumps(recommendation, indent=2))