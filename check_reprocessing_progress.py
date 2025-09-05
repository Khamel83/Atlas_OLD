#!/usr/bin/env python3
"""
Quick progress checker for reprocessing
"""

import sqlite3
import subprocess
import os

def main():
    # Check if reprocessing is still running
    result = subprocess.run(['pgrep', '-f', 'reprocess_limited_content.py'], 
                          capture_output=True, text=True)
    running = bool(result.stdout.strip())
    
    # Count remaining limited items
    conn = sqlite3.connect('/home/ubuntu/dev/atlas/atlas.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT COUNT(*) FROM content 
    WHERE 
        (ai_tags IS NOT NULL AND length(ai_tags) < 50) OR
        (ai_summary IS NOT NULL AND length(ai_summary) < 100) OR  
        (ai_socratic IS NOT NULL AND length(ai_socratic) < 150) OR
        (ai_patterns IS NOT NULL AND length(ai_patterns) < 150) OR
        (ai_recommendations IS NOT NULL AND length(ai_recommendations) < 150)
    ''')
    
    remaining = cursor.fetchone()[0]
    original_count = 1504
    processed = original_count - remaining
    
    cursor.execute('SELECT COUNT(*) FROM content')
    total = cursor.fetchone()[0]
    
    print("🔄 ATLAS REPROCESSING STATUS")
    print("=" * 35)
    print(f"Status: {'🟢 RUNNING' if running else '🔴 STOPPED'}")
    print(f"Processed: {processed:,}/{original_count:,} ({processed/original_count*100:.1f}%)")
    print(f"Remaining: {remaining:,}")
    print(f"Total items: {total:,}")
    
    if running:
        # Check recent activity from logs
        try:
            log_size = os.path.getsize('reprocess_log.txt')
            print(f"Log size: {log_size:,} bytes")
            
            # Show last few lines for activity
            result = subprocess.run(['tail', '-5', 'reprocess_log.txt'], 
                                  capture_output=True, text=True)
            if result.stdout:
                print("\nRecent activity:")
                for line in result.stdout.strip().split('\n')[-2:]:
                    if 'tokens' in line:
                        print(f"  {line.split()[-4]} {line.split()[-2]}")
        except:
            pass
    
    print(f"\nEstimated time remaining: {remaining * 6 / 60:.0f} minutes" if running and remaining > 0 else "")
    
    conn.close()

if __name__ == '__main__':
    main()