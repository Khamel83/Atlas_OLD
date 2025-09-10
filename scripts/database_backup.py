#!/usr/bin/env python3
"""
Database Backup Automation Script
Performs scheduled backups, cleanup, and restoration.
"""

import sys
import os
import argparse
from pathlib import Path
from datetime import datetime, timedelta

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers.database_config import (
    create_database_backup, restore_database,
    test_database_integrity, vacuum_database,
    get_database_path
)


def cleanup_old_backups(backup_dir: Path, keep_days: int = 7):
    """Clean up backups older than specified days."""
    cutoff_date = datetime.now() - timedelta(days=keep_days)
    
    backup_files = list(backup_dir.glob("atlas_backup_*.db"))
    removed_count = 0
    
    for backup_file in backup_files:
        # Extract timestamp from filename
        try:
            timestamp_str = backup_file.stem.split("_")[-2:]  # ['20251010', '143052']
            timestamp_str = "_".join(timestamp_str)
            file_date = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
            
            if file_date < cutoff_date:
                backup_file.unlink()
                removed_count += 1
                print(f"🗑️  Removed old backup: {backup_file.name}")
                
        except (ValueError, IndexError) as e:
            print(f"⚠️  Could not parse backup filename: {backup_file.name}")
    
    print(f"🧹 Cleanup complete: {removed_count} old backups removed")


def backup_with_verification():
    """Create backup with integrity verification."""
    print("🔄 Starting backup process...")
    
    # Check integrity before backup
    print("1. Checking database integrity...")
    if not test_database_integrity():
        print("❌ Database integrity check failed - aborting backup")
        return False
    
    # Vacuum if needed
    print("2. Checking if vacuum is needed...")
    if vacuum_database():
        print("✅ Database vacuum completed")
    else:
        print("ℹ️  Database vacuum not needed")
    
    # Create backup
    print("3. Creating backup...")
    backup_path = create_database_backup()
    if not backup_path:
        print("❌ Backup creation failed")
        return False
    
    # Verify backup integrity
    print("4. Verifying backup integrity...")
    import sqlite3
    try:
        conn = sqlite3.connect(str(backup_path))
        cursor = conn.cursor()
        cursor.execute("PRAGMA integrity_check")
        result = cursor.fetchone()[0]
        conn.close()
        
        if result == "ok":
            print(f"✅ Backup verified successfully: {backup_path}")
            return True
        else:
            print(f"❌ Backup verification failed: {result}")
            backup_path.unlink()  # Remove corrupted backup
            return False
            
    except Exception as e:
        print(f"❌ Backup verification error: {e}")
        return False


def list_backups():
    """List all available backups."""
    db_path = get_database_path()
    backup_dir = db_path.parent / "backups"
    
    if not backup_dir.exists():
        print("📁 No backup directory found")
        return
    
    backups = list(backup_dir.glob("atlas_backup_*.db"))
    
    if not backups:
        print("📁 No backups found")
        return
    
    print(f"📋 Found {len(backups)} backups:")
    print("-" * 60)
    
    # Sort by date (newest first)
    backups.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    
    for backup in backups:
        stat = backup.stat()
        size_mb = stat.st_size / 1024 / 1024
        mod_time = datetime.fromtimestamp(stat.st_mtime)
        
        print(f"📁 {backup.name}")
        print(f"   Size: {size_mb:.1f} MB")
        print(f"   Date: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print()


def restore_interactive():
    """Interactive restore process."""
    db_path = get_database_path()
    backup_dir = db_path.parent / "backups"
    
    backups = list(backup_dir.glob("atlas_backup_*.db"))
    
    if not backups:
        print("❌ No backups available for restore")
        return False
    
    backups.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    
    print("📋 Available backups:")
    for i, backup in enumerate(backups):
        mod_time = datetime.fromtimestamp(backup.stat().st_mtime)
        size_mb = backup.stat().st_size / 1024 / 1024
        print(f"{i+1}. {backup.name} ({size_mb:.1f} MB, {mod_time.strftime('%Y-%m-%d %H:%M')})")
    
    while True:
        try:
            choice = input("\nSelect backup to restore (number, or 'q' to quit): ").strip()
            if choice.lower() == 'q':
                print("Restore cancelled")
                return False
            
            idx = int(choice) - 1
            if 0 <= idx < len(backups):
                selected_backup = backups[idx]
                break
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Please enter a number")
    
    # Confirm restore
    print(f"\n⚠️  WARNING: This will replace the current database!")
    print(f"Selected backup: {selected_backup.name}")
    confirm = input("Type 'RESTORE' to confirm: ")
    
    if confirm != 'RESTORE':
        print("Restore cancelled")
        return False
    
    # Perform restore
    print("🔄 Restoring database...")
    if restore_database(selected_backup):
        print("✅ Database restored successfully")
        return True
    else:
        print("❌ Database restore failed")
        return False


def main():
    """Main backup management function."""
    parser = argparse.ArgumentParser(description="Atlas Database Backup Manager")
    parser.add_argument("command", choices=["backup", "restore", "list", "cleanup"],
                       help="Backup operation to perform")
    parser.add_argument("--keep-days", type=int, default=7,
                       help="Days to keep backups (for cleanup)")
    parser.add_argument("--auto", action="store_true",
                       help="Auto mode (no prompts)")
    
    args = parser.parse_args()
    
    print("🗄️  Atlas Database Backup Manager")
    print("=" * 40)
    
    if args.command == "backup":
        success = backup_with_verification()
        if success:
            print("🎉 Backup completed successfully")
        else:
            print("❌ Backup failed")
            sys.exit(1)
    
    elif args.command == "list":
        list_backups()
    
    elif args.command == "cleanup":
        db_path = get_database_path()
        backup_dir = db_path.parent / "backups"
        if backup_dir.exists():
            cleanup_old_backups(backup_dir, args.keep_days)
        else:
            print("📁 No backup directory found")
    
    elif args.command == "restore":
        if args.auto:
            # Auto restore from latest backup
            if restore_database():
                print("✅ Auto restore completed")
            else:
                print("❌ Auto restore failed")
                sys.exit(1)
        else:
            # Interactive restore
            restore_interactive()


if __name__ == "__main__":
    main()