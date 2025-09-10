#!/usr/bin/env python3
"""
Test Queue Failure Handling
Tests dead letter queue, exponential backoff, and circuit breakers.
"""

import sys
import time
import uuid
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers.queue_manager import (
    get_queue_manager, enqueue_task, get_circuit_breaker_status, get_queue_status
)


def test_basic_queue_operations():
    """Test basic enqueue/dequeue operations."""
    print("🔍 Testing Basic Queue Operations")
    print("=" * 40)
    
    qm = get_queue_manager()
    worker_id = "test-worker-1"
    
    # Enqueue some tasks
    tasks_created = []
    for i in range(3):
        task_id = f"test-task-{i}-{uuid.uuid4().hex[:8]}"
        task_data = {"test_data": f"value_{i}", "iteration": i}
        
        success = enqueue_task(task_id, "test", task_data, priority=i)
        if success:
            tasks_created.append(task_id)
            print(f"  ✅ Enqueued: {task_id}")
        else:
            print(f"  ❌ Failed to enqueue: {task_id}")
    
    # Dequeue tasks
    tasks_processed = []
    for i in range(len(tasks_created)):
        task = qm.dequeue_task(worker_id, ["test"])
        if task:
            tasks_processed.append(task.task_id)
            print(f"  📤 Dequeued: {task.task_id} (data: {task.task_data})")
            
            # Complete the task
            qm.complete_task(task.task_id, worker_id)
            print(f"  ✅ Completed: {task.task_id}")
        else:
            print(f"  ⚠️  No task available for dequeue")
    
    print(f"📊 Created: {len(tasks_created)}, Processed: {len(tasks_processed)}")
    return len(tasks_created) == len(tasks_processed)


def test_dead_letter_queue():
    """Test dead letter queue and exponential backoff."""
    print("\n💀 Testing Dead Letter Queue")
    print("=" * 40)
    
    qm = get_queue_manager()
    worker_id = "test-worker-dlq"
    
    # Create a task that will fail
    task_id = f"failing-task-{uuid.uuid4().hex[:8]}"
    task_data = {"will_fail": True, "test_mode": True}
    
    enqueue_task(task_id, "test", task_data)
    print(f"📥 Enqueued failing task: {task_id}")
    
    # Dequeue and fail the task multiple times
    for attempt in range(5):
        task = qm.dequeue_task(worker_id, ["test"])
        if task and task.task_id == task_id:
            error_msg = f"Simulated failure attempt {attempt + 1}"
            qm.fail_task(task.task_id, worker_id, error_msg)
            print(f"  ❌ Failed task (attempt {attempt + 1}): {error_msg}")
            time.sleep(0.1)  # Small delay
        else:
            print(f"  ⚠️  Task not available for retry (attempt {attempt + 1})")
            break
    
    # Check queue status
    status = get_queue_status()
    failed_count = status.get("failed_tasks", 0)
    print(f"📊 Failed tasks in DLQ: {failed_count}")
    
    return failed_count > 0


def test_circuit_breaker():
    """Test circuit breaker functionality."""
    print("\n⚡ Testing Circuit Breaker")
    print("=" * 40)
    
    qm = get_queue_manager()
    worker_id = "test-worker-cb"
    
    # Get initial circuit breaker status
    initial_status = get_circuit_breaker_status(worker_id)
    print(f"📊 Initial CB status: {initial_status}")
    
    # Create multiple failing tasks to trigger circuit breaker
    for i in range(12):  # More than threshold (10)
        task_id = f"cb-task-{i}-{uuid.uuid4().hex[:8]}"
        task_data = {"circuit_breaker_test": True, "iteration": i}
        
        enqueue_task(task_id, "test", task_data)
        
        task = qm.dequeue_task(worker_id, ["test"])
        if task:
            qm.fail_task(task.task_id, worker_id, f"Circuit breaker test failure {i}")
            print(f"  ❌ Failed task {i+1}/12")
        else:
            print(f"  🚫 Worker blocked by circuit breaker at task {i+1}")
            break
    
    # Check final circuit breaker status
    final_status = get_circuit_breaker_status(worker_id)
    print(f"📊 Final CB status: {final_status}")
    
    # Verify circuit breaker is open
    is_open = final_status.get("state") == "open"
    if is_open:
        print("✅ Circuit breaker successfully opened")
    else:
        print("⚠️  Circuit breaker did not open as expected")
    
    return is_open


def test_manual_retry():
    """Test manual retry functionality."""
    print("\n🔄 Testing Manual Retry")
    print("=" * 40)
    
    qm = get_queue_manager()
    worker_id = "test-worker-retry"
    
    # Create and fail a task
    task_id = f"retry-task-{uuid.uuid4().hex[:8]}"
    task_data = {"manual_retry_test": True}
    
    enqueue_task(task_id, "test", task_data)
    print(f"📥 Enqueued task: {task_id}")
    
    # Dequeue and fail
    task = qm.dequeue_task(worker_id, ["test"])
    if task:
        qm.fail_task(task.task_id, worker_id, "Initial failure for retry test")
        print(f"❌ Failed task: {task_id}")
    
    # Manual retry
    retry_success = qm.retry_failed_task(task_id)
    if retry_success:
        print(f"🔄 Successfully queued for retry: {task_id}")
        
        # Try to dequeue the retried task
        retried_task = qm.dequeue_task(worker_id, ["test"])
        if retried_task and retried_task.task_id == task_id:
            print(f"📤 Successfully dequeued retried task: {task_id}")
            qm.complete_task(retried_task.task_id, worker_id)
            print(f"✅ Completed retried task: {task_id}")
            return True
        else:
            print(f"⚠️  Could not dequeue retried task")
    else:
        print(f"❌ Failed to retry task: {task_id}")
    
    return False


def test_queue_monitoring():
    """Test queue monitoring and status."""
    print("\n📊 Testing Queue Monitoring")
    print("=" * 40)
    
    # Get comprehensive queue status
    status = get_queue_status()
    
    print("Queue Status:")
    for key, value in status.items():
        if key == "circuit_breakers":
            print(f"  {key}:")
            for worker, cb_status in value.items():
                print(f"    {worker}: {cb_status}")
        else:
            print(f"  {key}: {value}")
    
    # Check for alerts
    queue_counts = status.get("queue_counts", {})
    pending_count = queue_counts.get("pending", 0)
    
    if pending_count > 1000:
        print("🚨 ALERT: Queue depth exceeds 1000 pending tasks")
    elif pending_count > 100:
        print("⚠️  WARNING: High queue depth detected")
    else:
        print("✅ Queue depth within normal limits")
    
    return True


def test_cleanup():
    """Test cleanup of old tasks."""
    print("\n🧹 Testing Cleanup")
    print("=" * 40)
    
    qm = get_queue_manager()
    
    # Clean up tasks older than 0 days (clean everything for testing)
    cleaned_count = qm.cleanup_old_tasks(days_old=0)
    print(f"🗑️  Cleaned up {cleaned_count} old tasks")
    
    return True


def main():
    """Run all queue failure tests."""
    print("🧪 Atlas Queue Failure Tests")
    print("=" * 50)
    
    tests = [
        ("Basic Queue Operations", test_basic_queue_operations),
        ("Dead Letter Queue", test_dead_letter_queue),
        ("Circuit Breaker", test_circuit_breaker),
        ("Manual Retry", test_manual_retry),
        ("Queue Monitoring", test_queue_monitoring),
        ("Cleanup", test_cleanup),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            print(f"\n{'='*50}")
            result = test_func()
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"\n{test_name}: {status}")
            results.append((test_name, result))
        except Exception as e:
            print(f"\n{test_name}: ❌ ERROR - {e}")
            results.append((test_name, False))
    
    # Summary
    print(f"\n{'='*50}")
    print("📋 Test Summary:")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅" if result else "❌"
        print(f"  {status} {test_name}")
    
    print(f"\n🎯 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All queue failure tests passed!")
        return True
    else:
        print("⚠️  Some tests failed")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)