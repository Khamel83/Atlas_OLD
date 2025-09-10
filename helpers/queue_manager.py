"""
Atlas Queue Manager - Bulletproof Queue Semantics
Implements dead letter queues, exponential backoff, and circuit breakers.
"""

import time
import json
import logging
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass
from pathlib import Path

from .database_config import get_database_connection


@dataclass
class QueueTask:
    """Represents a task in the queue."""
    task_id: str
    task_type: str
    task_data: Dict[str, Any]
    priority: int = 0
    created_at: Optional[datetime] = None
    retry_count: int = 0
    next_retry: Optional[datetime] = None
    error_message: Optional[str] = None


@dataclass
class CircuitBreakerState:
    """Circuit breaker state."""
    failure_count: int = 0
    last_failure: Optional[datetime] = None
    state: str = "closed"  # closed, open, half-open
    next_retry: Optional[datetime] = None


class QueueManager:
    """Bulletproof queue manager with dead letter queue and circuit breaker."""
    
    # Exponential backoff intervals (seconds)
    RETRY_INTERVALS = [1, 2, 4, 8, 16, 32, 60, 120, 300]  # Max 5 minutes
    
    # Circuit breaker settings
    CIRCUIT_BREAKER_THRESHOLD = 10
    CIRCUIT_BREAKER_TIMEOUT = 300  # 5 minutes
    
    def __init__(self):
        """Initialize queue manager."""
        self.logger = logging.getLogger(__name__)
        self._initialize_tables()
        self._circuit_breakers: Dict[str, CircuitBreakerState] = {}
        
    def _initialize_tables(self):
        """Initialize queue tables in database."""
        conn = get_database_connection()
        cursor = conn.cursor()
        
        # Main task queue
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS task_queue (
                task_id TEXT PRIMARY KEY,
                task_type TEXT NOT NULL,
                task_data TEXT NOT NULL,
                priority INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                worker_id TEXT,
                started_at TIMESTAMP,
                completed_at TIMESTAMP
            )
        """)
        
        # Failed tasks (dead letter queue)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS failed_tasks (
                task_id TEXT PRIMARY KEY,
                task_type TEXT NOT NULL,
                task_data TEXT NOT NULL,
                attempt_count INTEGER DEFAULT 0,
                next_retry TIMESTAMP,
                error_msg TEXT,
                first_failure TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_failure TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'failed'
            )
        """)
        
        # Queue metrics
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS queue_metrics (
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                metric_name TEXT NOT NULL,
                metric_value REAL NOT NULL,
                worker_type TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def enqueue_task(self, task_id: str, task_type: str, task_data: Dict[str, Any], 
                    priority: int = 0) -> bool:
        """Add a task to the queue."""
        try:
            conn = get_database_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT OR REPLACE INTO task_queue 
                (task_id, task_type, task_data, priority)
                VALUES (?, ?, ?, ?)
            """, (task_id, task_type, json.dumps(task_data), priority))
            
            conn.commit()
            conn.close()
            
            self.logger.debug(f"Enqueued task: {task_id} ({task_type})")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to enqueue task {task_id}: {e}")
            return False
    
    def dequeue_task(self, worker_id: str, task_types: Optional[List[str]] = None) -> Optional[QueueTask]:
        """Dequeue the next available task."""
        if self._is_circuit_breaker_open(worker_id):
            self.logger.debug(f"Circuit breaker open for worker {worker_id}")
            return None
        
        try:
            conn = get_database_connection()
            cursor = conn.cursor()
            
            # Build query with optional task type filter
            where_clause = "status = 'pending'"
            params = []
            
            if task_types:
                placeholders = ",".join("?" * len(task_types))
                where_clause += f" AND task_type IN ({placeholders})"
                params.extend(task_types)
            
            cursor.execute(f"""
                SELECT task_id, task_type, task_data, priority, created_at
                FROM task_queue 
                WHERE {where_clause}
                ORDER BY priority DESC, created_at ASC
                LIMIT 1
            """, params)
            
            row = cursor.fetchone()
            if not row:
                conn.close()
                return None
            
            task_id, task_type, task_data, priority, created_at = row
            
            # Mark as in progress
            cursor.execute("""
                UPDATE task_queue 
                SET status = 'processing', worker_id = ?, started_at = CURRENT_TIMESTAMP
                WHERE task_id = ?
            """, (worker_id, task_id))
            
            conn.commit()
            conn.close()
            
            task = QueueTask(
                task_id=task_id,
                task_type=task_type,
                task_data=json.loads(task_data),
                priority=priority,
                created_at=datetime.fromisoformat(created_at) if created_at else None
            )
            
            self.logger.debug(f"Dequeued task: {task_id} for worker {worker_id}")
            return task
            
        except Exception as e:
            self.logger.error(f"Failed to dequeue task for worker {worker_id}: {e}")
            return None
    
    def complete_task(self, task_id: str, worker_id: str) -> bool:
        """Mark a task as completed."""
        try:
            conn = get_database_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                UPDATE task_queue 
                SET status = 'completed', completed_at = CURRENT_TIMESTAMP
                WHERE task_id = ? AND worker_id = ?
            """, (task_id, worker_id))
            
            conn.commit()
            conn.close()
            
            # Reset circuit breaker on success
            self._reset_circuit_breaker(worker_id)
            
            self.logger.debug(f"Completed task: {task_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to complete task {task_id}: {e}")
            return False
    
    def fail_task(self, task_id: str, worker_id: str, error_message: str) -> bool:
        """Mark a task as failed and move to dead letter queue."""
        try:
            conn = get_database_connection()
            cursor = conn.cursor()
            
            # Get task details
            cursor.execute("""
                SELECT task_type, task_data FROM task_queue 
                WHERE task_id = ? AND worker_id = ?
            """, (task_id, worker_id))
            
            row = cursor.fetchone()
            if not row:
                self.logger.error(f"Task {task_id} not found for worker {worker_id}")
                return False
            
            task_type, task_data = row
            
            # Check if already in failed_tasks table
            cursor.execute("""
                SELECT attempt_count FROM failed_tasks WHERE task_id = ?
            """, (task_id,))
            
            existing = cursor.fetchone()
            attempt_count = (existing[0] + 1) if existing else 1
            
            # Calculate next retry time with exponential backoff
            next_retry = None
            if attempt_count <= len(self.RETRY_INTERVALS):
                retry_delay = self.RETRY_INTERVALS[attempt_count - 1]
                next_retry = datetime.now() + timedelta(seconds=retry_delay)
            
            # Insert or update failed task
            cursor.execute("""
                INSERT OR REPLACE INTO failed_tasks 
                (task_id, task_type, task_data, attempt_count, next_retry, error_msg, last_failure)
                VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (task_id, task_type, task_data, attempt_count, next_retry, error_message))
            
            # Remove from main queue
            cursor.execute("""
                DELETE FROM task_queue WHERE task_id = ? AND worker_id = ?
            """, (task_id, worker_id))
            
            conn.commit()
            conn.close()
            
            # Update circuit breaker
            self._record_failure(worker_id)
            
            self.logger.warning(f"Failed task: {task_id} (attempt {attempt_count})")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to handle task failure {task_id}: {e}")
            return False
    
    def retry_failed_task(self, task_id: str) -> bool:
        """Manually retry a failed task."""
        try:
            conn = get_database_connection()
            cursor = conn.cursor()
            
            # Get failed task
            cursor.execute("""
                SELECT task_type, task_data FROM failed_tasks 
                WHERE task_id = ?
            """, (task_id,))
            
            row = cursor.fetchone()
            if not row:
                self.logger.error(f"Failed task {task_id} not found")
                return False
            
            task_type, task_data = row
            
            # Move back to main queue
            cursor.execute("""
                INSERT OR REPLACE INTO task_queue 
                (task_id, task_type, task_data, status)
                VALUES (?, ?, ?, 'pending')
            """, (task_id, task_type, task_data))
            
            # Update failed task status
            cursor.execute("""
                UPDATE failed_tasks 
                SET status = 'retrying' 
                WHERE task_id = ?
            """, (task_id,))
            
            conn.commit()
            conn.close()
            
            self.logger.info(f"Retrying failed task: {task_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to retry task {task_id}: {e}")
            return False
    
    def get_queue_status(self) -> Dict[str, Any]:
        """Get comprehensive queue status."""
        try:
            conn = get_database_connection()
            cursor = conn.cursor()
            
            # Count tasks by status
            cursor.execute("""
                SELECT status, COUNT(*) FROM task_queue GROUP BY status
            """)
            queue_counts = dict(cursor.fetchall())
            
            # Count failed tasks
            cursor.execute("""
                SELECT COUNT(*) FROM failed_tasks WHERE status = 'failed'
            """)
            failed_count = cursor.fetchone()[0]
            
            # Get retry queue (ready for retry)
            cursor.execute("""
                SELECT COUNT(*) FROM failed_tasks 
                WHERE status = 'failed' AND next_retry IS NOT NULL AND next_retry <= CURRENT_TIMESTAMP
            """)
            retry_ready_count = cursor.fetchone()[0]
            
            # Get oldest pending task age
            cursor.execute("""
                SELECT MIN(created_at) FROM task_queue WHERE status = 'pending'
            """)
            oldest_pending = cursor.fetchone()[0]
            oldest_age = None
            if oldest_pending:
                oldest_age = (datetime.now() - datetime.fromisoformat(oldest_pending)).total_seconds()
            
            conn.close()
            
            status = {
                "queue_counts": queue_counts,
                "failed_tasks": failed_count,
                "retry_ready": retry_ready_count,
                "oldest_pending_age_seconds": oldest_age,
                "circuit_breakers": {
                    worker: {
                        "state": cb.state,
                        "failure_count": cb.failure_count,
                        "last_failure": cb.last_failure.isoformat() if cb.last_failure else None
                    }
                    for worker, cb in self._circuit_breakers.items()
                }
            }
            
            return status
            
        except Exception as e:
            self.logger.error(f"Failed to get queue status: {e}")
            return {"error": str(e)}
    
    def cleanup_old_tasks(self, days_old: int = 7) -> int:
        """Clean up old completed and failed tasks."""
        try:
            cutoff_date = datetime.now() - timedelta(days=days_old)
            conn = get_database_connection()
            cursor = conn.cursor()
            
            # Clean up old completed tasks
            cursor.execute("""
                DELETE FROM task_queue 
                WHERE status = 'completed' AND completed_at < ?
            """, (cutoff_date,))
            completed_cleaned = cursor.rowcount
            
            # Clean up old failed tasks
            cursor.execute("""
                DELETE FROM failed_tasks 
                WHERE first_failure < ?
            """, (cutoff_date,))
            failed_cleaned = cursor.rowcount
            
            conn.commit()
            conn.close()
            
            total_cleaned = completed_cleaned + failed_cleaned
            self.logger.info(f"Cleaned up {total_cleaned} old tasks ({completed_cleaned} completed, {failed_cleaned} failed)")
            return total_cleaned
            
        except Exception as e:
            self.logger.error(f"Failed to cleanup old tasks: {e}")
            return 0
    
    def _is_circuit_breaker_open(self, worker_id: str) -> bool:
        """Check if circuit breaker is open for worker."""
        if worker_id not in self._circuit_breakers:
            return False
        
        cb = self._circuit_breakers[worker_id]
        
        if cb.state == "closed":
            return False
        elif cb.state == "open":
            # Check if timeout has passed
            if cb.next_retry and datetime.now() >= cb.next_retry:
                cb.state = "half-open"
                self.logger.info(f"Circuit breaker for {worker_id} moved to half-open")
                return False
            return True
        elif cb.state == "half-open":
            return False
        
        return False
    
    def _record_failure(self, worker_id: str):
        """Record a failure for circuit breaker."""
        if worker_id not in self._circuit_breakers:
            self._circuit_breakers[worker_id] = CircuitBreakerState()
        
        cb = self._circuit_breakers[worker_id]
        cb.failure_count += 1
        cb.last_failure = datetime.now()
        
        if cb.failure_count >= self.CIRCUIT_BREAKER_THRESHOLD:
            cb.state = "open"
            cb.next_retry = datetime.now() + timedelta(seconds=self.CIRCUIT_BREAKER_TIMEOUT)
            self.logger.warning(f"Circuit breaker opened for {worker_id} after {cb.failure_count} failures")
    
    def _reset_circuit_breaker(self, worker_id: str):
        """Reset circuit breaker on success."""
        if worker_id in self._circuit_breakers:
            cb = self._circuit_breakers[worker_id]
            if cb.state in ["half-open", "closed"]:
                cb.failure_count = 0
                cb.state = "closed"
                cb.next_retry = None
                self.logger.debug(f"Circuit breaker reset for {worker_id}")
    
    def get_circuit_breaker_status(self, worker_id: Optional[str] = None) -> Dict[str, Any]:
        """Get circuit breaker status."""
        if worker_id:
            if worker_id in self._circuit_breakers:
                cb = self._circuit_breakers[worker_id]
                return {
                    "worker_id": worker_id,
                    "state": cb.state,
                    "failure_count": cb.failure_count,
                    "last_failure": cb.last_failure.isoformat() if cb.last_failure else None,
                    "next_retry": cb.next_retry.isoformat() if cb.next_retry else None
                }
            else:
                return {"worker_id": worker_id, "state": "closed", "failure_count": 0}
        else:
            return {
                worker: {
                    "state": cb.state,
                    "failure_count": cb.failure_count,
                    "last_failure": cb.last_failure.isoformat() if cb.last_failure else None,
                    "next_retry": cb.next_retry.isoformat() if cb.next_retry else None
                }
                for worker, cb in self._circuit_breakers.items()
            }


# Global queue manager instance
_queue_manager = QueueManager()


def get_queue_manager() -> QueueManager:
    """Get the global queue manager instance."""
    return _queue_manager


def enqueue_task(task_id: str, task_type: str, task_data: Dict[str, Any], priority: int = 0) -> bool:
    """Convenience function to enqueue a task."""
    return _queue_manager.enqueue_task(task_id, task_type, task_data, priority)


def get_circuit_breaker_status(worker_id: Optional[str] = None) -> Dict[str, Any]:
    """Convenience function to get circuit breaker status."""
    return _queue_manager.get_circuit_breaker_status(worker_id)


def get_queue_status() -> Dict[str, Any]:
    """Convenience function to get queue status."""
    return _queue_manager.get_queue_status()