#!/usr/bin/env python3
"""
Manual Failed Task Retry Script
Allows manual retrying of failed tasks from the dead letter queue.
"""

import sys
import argparse
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers.queue_manager import get_queue_manager
from helpers.database_config import get_database_connection


def list_failed_tasks(limit: int = 20):
    """List failed tasks available for retry."""
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT task_id, task_type, attempt_count, error_msg, last_failure, next_retry
            FROM failed_tasks 
            WHERE status = 'failed'
            ORDER BY last_failure DESC
            LIMIT ?
        """, (limit,))
        
        tasks = cursor.fetchall()
        conn.close()
        
        if not tasks:
            print("📭 No failed tasks found")
            return
        
        print(f"📋 Found {len(tasks)} failed tasks:")
        print("-" * 80)
        
        for task_id, task_type, attempt_count, error_msg, last_failure, next_retry in tasks:
            print(f"🆔 Task ID: {task_id}")
            print(f"   Type: {task_type}")
            print(f"   Attempts: {attempt_count}")
            print(f"   Last Error: {error_msg[:60]}{'...' if len(error_msg) > 60 else ''}")
            print(f"   Last Failure: {last_failure}")
            print(f"   Next Retry: {next_retry or 'Manual only'}")
            print()
        
    except Exception as e:
        print(f"❌ Error listing failed tasks: {e}")


def show_task_details(task_id: str):
    """Show detailed information about a failed task."""
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT task_id, task_type, task_data, attempt_count, next_retry, 
                   error_msg, first_failure, last_failure, status
            FROM failed_tasks 
            WHERE task_id = ?
        """, (task_id,))
        
        task = cursor.fetchone()
        conn.close()
        
        if not task:
            print(f"❌ Task {task_id} not found in failed tasks")
            return False
        
        task_id, task_type, task_data, attempt_count, next_retry, error_msg, first_failure, last_failure, status = task
        
        print(f"📋 Task Details: {task_id}")
        print("=" * 50)
        print(f"Type: {task_type}")
        print(f"Status: {status}")
        print(f"Attempt Count: {attempt_count}")
        print(f"First Failure: {first_failure}")
        print(f"Last Failure: {last_failure}")
        print(f"Next Retry: {next_retry or 'Manual only'}")
        print(f"Error Message: {error_msg}")
        print(f"Task Data: {task_data}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error getting task details: {e}")
        return False


def retry_task(task_id: str, force: bool = False):
    """Retry a failed task."""
    if not force:
        # Show task details first
        if not show_task_details(task_id):
            return False
        
        # Confirm retry
        response = input(f"\n⚠️  Retry task {task_id}? (y/N): ")
        if response.lower() != 'y':
            print("❌ Retry cancelled")
            return False
    
    qm = get_queue_manager()
    
    success = qm.retry_failed_task(task_id)
    if success:
        print(f"✅ Task {task_id} queued for retry")
        return True
    else:
        print(f"❌ Failed to retry task {task_id}")
        return False


def retry_all_ready():
    """Retry all tasks that are ready for retry."""
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        
        # Get tasks ready for retry
        cursor.execute("""
            SELECT task_id FROM failed_tasks 
            WHERE status = 'failed' 
            AND next_retry IS NOT NULL 
            AND next_retry <= CURRENT_TIMESTAMP
        """)
        
        ready_tasks = [row[0] for row in cursor.fetchall()]
        conn.close()
        
        if not ready_tasks:
            print("📭 No tasks ready for retry")
            return 0
        
        print(f"🔄 Found {len(ready_tasks)} tasks ready for retry")
        
        qm = get_queue_manager()
        success_count = 0
        
        for task_id in ready_tasks:
            if qm.retry_failed_task(task_id):
                print(f"  ✅ Retried: {task_id}")
                success_count += 1
            else:
                print(f"  ❌ Failed to retry: {task_id}")
        
        print(f"📊 Successfully retried {success_count}/{len(ready_tasks)} tasks")
        return success_count
        
    except Exception as e:
        print(f"❌ Error retrying ready tasks: {e}")
        return 0


def main():
    """Main retry management function."""
    parser = argparse.ArgumentParser(description="Atlas Failed Task Retry Manager")
    parser.add_argument("--task-id", help="Specific task ID to retry")
    parser.add_argument("--list", action="store_true", help="List failed tasks")
    parser.add_argument("--details", help="Show details for specific task")
    parser.add_argument("--retry-all", action="store_true", help="Retry all ready tasks")
    parser.add_argument("--force", action="store_true", help="Force retry without confirmation")
    parser.add_argument("--limit", type=int, default=20, help="Limit for list command")
    
    args = parser.parse_args()
    
    print("🔄 Atlas Failed Task Retry Manager")
    print("=" * 40)
    
    if args.list:
        list_failed_tasks(args.limit)
    
    elif args.details:
        show_task_details(args.details)
    
    elif args.task_id:
        retry_task(args.task_id, args.force)
    
    elif args.retry_all:
        retry_all_ready()
    
    else:
        # Interactive mode
        print("📋 Available Commands:")
        print("  --list              List failed tasks")
        print("  --details TASK_ID   Show task details")
        print("  --task-id TASK_ID   Retry specific task")
        print("  --retry-all         Retry all ready tasks")
        print("  --force             Skip confirmation")
        print()
        print("Example: python3 retry_failed_task.py --list")
        print("Example: python3 retry_failed_task.py --task-id abc123")


if __name__ == "__main__":
    main()