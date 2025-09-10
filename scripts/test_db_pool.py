#!/usr/bin/env python3
"""
Test Database Connection Pool
Tests connection pooling, durability settings, and performance.
"""

import sys
import time
import threading
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers.database_config import (
    get_pooled_connection, return_pooled_connection,
    test_database_integrity, create_database_backup
)


def test_connection_pool():
    """Test connection pool functionality."""
    print("🔍 Testing Database Connection Pool")
    print("=" * 40)
    
    connections = []
    
    # Test getting multiple connections
    print("Getting 5 connections from pool...")
    start_time = time.time()
    
    for i in range(5):
        conn = get_pooled_connection()
        connections.append(conn)
        
        # Test that connection works
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()[0]
        assert result == 1
        
        print(f"  ✅ Connection {i+1}: Active")
    
    pool_time = time.time() - start_time
    print(f"⏱️  Pool retrieval time: {pool_time:.3f}s")
    
    # Return connections to pool
    print("\nReturning connections to pool...")
    for i, conn in enumerate(connections):
        return_pooled_connection(conn)
        print(f"  ↩️  Connection {i+1}: Returned")
    
    print("✅ Connection pool test completed")


def test_wal_mode():
    """Test WAL mode configuration."""
    print("\n🗄️  Testing WAL Mode Configuration")
    print("=" * 40)
    
    conn = get_pooled_connection()
    cursor = conn.cursor()
    
    # Check journal mode
    cursor.execute("PRAGMA journal_mode")
    journal_mode = cursor.fetchone()[0]
    print(f"Journal Mode: {journal_mode}")
    
    # Check synchronous mode
    cursor.execute("PRAGMA synchronous")
    sync_mode = cursor.fetchone()[0]
    print(f"Synchronous Mode: {sync_mode}")
    
    # Check cache size
    cursor.execute("PRAGMA cache_size")
    cache_size = cursor.fetchone()[0]
    print(f"Cache Size: {cache_size}")
    
    # Check busy timeout
    cursor.execute("PRAGMA busy_timeout")
    busy_timeout = cursor.fetchone()[0]
    print(f"Busy Timeout: {busy_timeout}ms")
    
    return_pooled_connection(conn)
    
    if journal_mode.upper() == 'WAL':
        print("✅ WAL mode successfully enabled")
    else:
        print(f"⚠️  Expected WAL mode, got {journal_mode}")


def test_concurrent_access():
    """Test concurrent database access."""
    print("\n🔄 Testing Concurrent Access")
    print("=" * 40)
    
    results = []
    
    def worker(worker_id):
        """Worker function for concurrent testing."""
        try:
            conn = get_pooled_connection()
            cursor = conn.cursor()
            
            # Perform some database operation
            cursor.execute("SELECT COUNT(*) FROM sqlite_master")
            count = cursor.fetchone()[0]
            
            # Simulate some work
            time.sleep(0.1)
            
            return_pooled_connection(conn)
            results.append(f"Worker {worker_id}: {count} tables")
        except Exception as e:
            results.append(f"Worker {worker_id}: ERROR - {e}")
    
    # Start 10 concurrent workers
    threads = []
    start_time = time.time()
    
    for i in range(10):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    concurrent_time = time.time() - start_time
    
    print(f"⏱️  Concurrent access time: {concurrent_time:.3f}s")
    print(f"📊 Results from {len(results)} workers:")
    for result in results:
        print(f"  {result}")
    
    error_count = sum(1 for r in results if "ERROR" in r)
    if error_count == 0:
        print("✅ Concurrent access test passed")
    else:
        print(f"⚠️  {error_count} errors in concurrent access")


def test_integrity_and_backup():
    """Test integrity checking and backup functionality."""
    print("\n🛡️  Testing Integrity & Backup")
    print("=" * 40)
    
    # Test integrity check
    print("Running integrity check...")
    integrity_ok = test_database_integrity()
    if integrity_ok:
        print("✅ Database integrity check passed")
    else:
        print("❌ Database integrity check failed")
    
    # Test backup creation
    print("Creating database backup...")
    backup_path = create_database_backup()
    if backup_path:
        print(f"✅ Backup created: {backup_path}")
        print(f"📁 Backup size: {backup_path.stat().st_size / 1024 / 1024:.1f} MB")
    else:
        print("❌ Backup creation failed")


def main():
    """Main test function."""
    print("🧪 Atlas Database Durability Tests")
    print("=" * 50)
    
    try:
        # Run all tests
        test_connection_pool()
        test_wal_mode()
        test_concurrent_access()
        test_integrity_and_backup()
        
        print("\n🎉 All database tests completed!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()