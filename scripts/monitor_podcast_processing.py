#!/usr/bin/env python3
"""
Monitor the bulk podcast processing progress.
"""

import os
import time
import subprocess
from pathlib import Path

def check_process_status():
    """Check if the bulk processing is still running"""
    try:
        result = subprocess.run(['pgrep', '-f', 'bulk_podcast_processing'], 
                              capture_output=True, text=True)
        return len(result.stdout.strip()) > 0
    except:
        return False

def get_log_tail(lines=10):
    """Get the last few lines from the processing log"""
    log_file = Path('/home/ubuntu/dev/atlas/logs/bulk_podcast_processing.log')
    if log_file.exists():
        try:
            result = subprocess.run(['tail', f'-{lines}', str(log_file)], 
                                  capture_output=True, text=True)
            return result.stdout
        except:
            return "Could not read log file"
    return "Log file not found"

def get_podcast_stats():
    """Get current podcast database stats"""
    try:
        os.chdir('/home/ubuntu/dev/atlas')
        result = subprocess.run([
            'bash', '-c', 
            'source atlas_venv/bin/activate && PYTHONPATH=. python -m modules.podcasts.cli doctor'
        ], capture_output=True, text=True, timeout=30)
        return result.stdout
    except:
        return "Could not get stats"

def main():
    print("📊 Atlas Podcast Processing Monitor")
    print("=" * 50)
    
    # Check if process is running
    is_running = check_process_status()
    print(f"🔄 Background Process: {'RUNNING' if is_running else 'STOPPED'}")
    
    if is_running:
        print(f"📝 Recent Log Output:")
        print("-" * 30)
        print(get_log_tail(15))
    
    print("\n📈 Current Database Stats:")
    print("-" * 30)
    print(get_podcast_stats())
    
    if is_running:
        print("\n💡 To monitor continuously:")
        print("   tail -f logs/bulk_podcast_processing.log")

if __name__ == "__main__":
    main()