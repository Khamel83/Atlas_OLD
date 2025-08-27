#!/usr/bin/env python3
"""
Database Cleanup Script for Atlas - Phase 3.1
Safe cleanup of junk entries with backup and progressive processing
"""

import sqlite3
import os
import sys
from pathlib import Path
import json
from datetime import datetime
import shutil
import argparse

class AtlasDatabaseCleaner:
    def __init__(self, base_path="/home/ubuntu/dev/atlas", dry_run=True):
        self.base_path = Path(base_path)
        self.dry_run = dry_run
        self.backup_dir = self.base_path / "backups"
        self.backup_dir.mkdir(exist_ok=True)
        self.cleanup_log = []
        
    def create_backup(self, db_path):
        """Create backup of database before cleanup"""
        db_path = Path(db_path)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{db_path.stem}_cleanup_backup_{timestamp}.db"
        backup_path = self.backup_dir / backup_name
        
        if not self.dry_run:
            shutil.copy2(db_path, backup_path)
            self.log(f"✅ Backup created: {backup_path}")
        else:
            self.log(f"🔄 DRY RUN: Would backup {db_path} to {backup_path}")
        
        return backup_path
    
    def log(self, message):
        """Log cleanup actions"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        self.cleanup_log.append(log_entry)
        
    def identify_junk_content(self, db_path):
        """Identify specific junk entries for removal"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            junk_criteria = {
                'very_short_content': [],
                'interface_html': [],
                'duplicate_entries': [],
                'empty_content': []
            }
            
            # Get table structure
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]
            
            for table in tables:
                if table.startswith('sqlite_'):
                    continue
                    
                try:
                    # Get column info
                    cursor.execute(f"PRAGMA table_info({table})")
                    columns = {row[1]: row[0] for row in cursor.fetchall()}
                    
                    if 'content' not in columns:
                        continue
                    
                    # Find very short content (likely interface elements)
                    cursor.execute(f"""
                        SELECT id, title, LENGTH(content) as content_len 
                        FROM {table} 
                        WHERE LENGTH(content) < 200 
                        ORDER BY content_len
                    """)
                    short_entries = cursor.fetchall()
                    if short_entries:
                        junk_criteria['very_short_content'].extend([(table, entry) for entry in short_entries])
                    
                    # Find interface HTML junk
                    interface_keywords = [
                        'instapaper', 'javascript', 'loading', 'cookie policy', 
                        'navigation', 'menu', 'header', 'footer', 'login',
                        'sign in', 'create account', 'privacy policy'
                    ]
                    
                    for keyword in interface_keywords:
                        cursor.execute(f"""
                            SELECT id, title, substr(content, 1, 100) as content_preview
                            FROM {table}
                            WHERE content LIKE '%{keyword}%' 
                            AND LENGTH(content) < 1000
                        """)
                        interface_entries = cursor.fetchall()
                        if interface_entries:
                            junk_criteria['interface_html'].extend([(table, entry, keyword) for entry in interface_entries])
                    
                    # Find empty or near-empty content
                    cursor.execute(f"""
                        SELECT id, title 
                        FROM {table} 
                        WHERE content IS NULL OR TRIM(content) = '' OR LENGTH(TRIM(content)) < 50
                    """)
                    empty_entries = cursor.fetchall()
                    if empty_entries:
                        junk_criteria['empty_content'].extend([(table, entry) for entry in empty_entries])
                        
                except Exception as e:
                    self.log(f"⚠️ Error analyzing table {table}: {e}")
            
            conn.close()
            return junk_criteria
            
        except Exception as e:
            self.log(f"❌ Error identifying junk content in {db_path}: {e}")
            return {}
    
    def clean_database(self, db_path, batch_size=1000):
        """Clean junk entries from database in batches"""
        try:
            # Create backup first
            backup_path = self.create_backup(db_path)
            
            # Identify junk entries
            self.log(f"🔍 Analyzing {db_path} for junk entries...")
            junk_criteria = self.identify_junk_content(db_path)
            
            if not junk_criteria:
                self.log("✅ No junk entries identified")
                return
            
            # Count total junk entries
            total_junk = sum(len(entries) for entries in junk_criteria.values())
            self.log(f"📊 Identified {total_junk} junk entries for removal")
            
            if self.dry_run:
                self.log("🔄 DRY RUN: Would remove the following:")
                for category, entries in junk_criteria.items():
                    if entries:
                        self.log(f"  {category}: {len(entries)} entries")
                return total_junk
            
            # Perform actual cleanup
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            removed_count = 0
            
            # Remove very short content
            for table, entry in junk_criteria.get('very_short_content', []):
                try:
                    cursor.execute(f"DELETE FROM {table} WHERE id = ?", (entry[0],))
                    removed_count += 1
                    if removed_count % batch_size == 0:
                        conn.commit()
                        self.log(f"🗑️ Removed {removed_count} entries so far...")
                except Exception as e:
                    self.log(f"⚠️ Error removing short content entry {entry[0]}: {e}")
            
            # Remove interface HTML
            for table, entry, keyword in junk_criteria.get('interface_html', []):
                try:
                    cursor.execute(f"DELETE FROM {table} WHERE id = ?", (entry[0],))
                    removed_count += 1
                    if removed_count % batch_size == 0:
                        conn.commit()
                        self.log(f"🗑️ Removed {removed_count} entries so far...")
                except Exception as e:
                    self.log(f"⚠️ Error removing interface entry {entry[0]}: {e}")
            
            # Remove empty content
            for table, entry in junk_criteria.get('empty_content', []):
                try:
                    cursor.execute(f"DELETE FROM {table} WHERE id = ?", (entry[0],))
                    removed_count += 1
                    if removed_count % batch_size == 0:
                        conn.commit()
                        self.log(f"🗑️ Removed {removed_count} entries so far...")
                except Exception as e:
                    self.log(f"⚠️ Error removing empty entry {entry[0]}: {e}")
            
            # Final commit and vacuum
            conn.commit()
            
            # Vacuum to reclaim space
            self.log("🧹 Running VACUUM to reclaim disk space...")
            cursor.execute("VACUUM")
            
            conn.close()
            
            self.log(f"✅ Cleanup complete: Removed {removed_count} junk entries")
            return removed_count
            
        except Exception as e:
            self.log(f"❌ Error cleaning database {db_path}: {e}")
            return 0
    
    def verify_database_integrity(self, db_path):
        """Verify database integrity after cleanup"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Check database integrity
            cursor.execute("PRAGMA integrity_check")
            integrity_result = cursor.fetchall()
            
            if integrity_result and integrity_result[0][0] == 'ok':
                self.log("✅ Database integrity check passed")
                
                # Get final counts
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = [row[0] for row in cursor.fetchall()]
                
                total_remaining = 0
                for table in tables:
                    if not table.startswith('sqlite_'):
                        cursor.execute(f"SELECT COUNT(*) FROM {table}")
                        count = cursor.fetchone()[0]
                        total_remaining += count
                        self.log(f"📊 Table {table}: {count} entries remaining")
                
                self.log(f"📊 Total remaining entries: {total_remaining}")
                
            else:
                self.log(f"❌ Database integrity check failed: {integrity_result}")
                
            conn.close()
            return True
            
        except Exception as e:
            self.log(f"❌ Error verifying database integrity: {e}")
            return False
    
    def cleanup_main_databases(self):
        """Clean up the main Atlas databases with known issues"""
        priority_databases = [
            ("atlas.db", "data/atlas.db"),
            ("enhanced_search.db", "data/enhanced_search.db"), 
            ("atlas_search.db", "data/atlas_search.db")
        ]
        
        total_removed = 0
        
        for db_name, db_relative_path in priority_databases:
            db_path = self.base_path / db_relative_path
            
            if not db_path.exists():
                # Try alternative locations
                alt_path = self.base_path / db_name
                if alt_path.exists():
                    db_path = alt_path
                else:
                    self.log(f"⚠️ Database not found: {db_path}")
                    continue
            
            self.log(f"\n{'='*50}")
            self.log(f"🎯 Cleaning {db_name}")
            self.log(f"{'='*50}")
            
            removed = self.clean_database(db_path)
            total_removed += removed
            
            if not self.dry_run:
                self.verify_database_integrity(db_path)
        
        return total_removed
    
    def generate_cleanup_report(self, total_removed):
        """Generate cleanup summary report"""
        report = {
            'cleanup_timestamp': datetime.now().isoformat(),
            'dry_run': self.dry_run,
            'total_entries_removed': total_removed,
            'cleanup_log': self.cleanup_log
        }
        
        # Save report
        docs_dir = self.base_path / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        report_name = f"database_cleanup_{'dry_run_' if self.dry_run else ''}report.json"
        with open(docs_dir / report_name, 'w') as f:
            json.dump(report, f, indent=2)
        
        self.log(f"📄 Cleanup report saved to: {docs_dir / report_name}")
        return report

def main():
    parser = argparse.ArgumentParser(description="Atlas Database Cleanup Tool")
    parser.add_argument('--execute', action='store_true', 
                       help='Execute cleanup (default is dry-run mode)')
    parser.add_argument('--batch-size', type=int, default=1000,
                       help='Batch size for cleanup operations')
    
    args = parser.parse_args()
    
    dry_run = not args.execute
    
    print("🗑️ Atlas Database Cleanup - Phase 3.1")
    print("=" * 50)
    
    if dry_run:
        print("🔄 RUNNING IN DRY-RUN MODE")
        print("Use --execute flag to perform actual cleanup")
    else:
        print("🚨 EXECUTING ACTUAL CLEANUP")
        print("Backups will be created automatically")
    
    print("=" * 50)
    
    # Initialize cleaner
    cleaner = AtlasDatabaseCleaner(dry_run=dry_run)
    
    # Run cleanup
    total_removed = cleaner.cleanup_main_databases()
    
    # Generate report
    report = cleaner.generate_cleanup_report(total_removed)
    
    print("\n" + "=" * 50)
    print("📊 CLEANUP SUMMARY")
    print("=" * 50)
    print(f"Mode: {'DRY RUN' if dry_run else 'EXECUTED'}")
    print(f"Total Entries Processed: {total_removed}")
    
    if dry_run:
        print("\n🎯 To execute actual cleanup, run:")
        print("python3 scripts/database_cleanup.py --execute")
    else:
        print("✅ Cleanup completed successfully!")
        print("🔄 Restart Atlas services to see the changes")

if __name__ == "__main__":
    main()