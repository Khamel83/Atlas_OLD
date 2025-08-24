#!/usr/bin/env python3
"""
Atlas Reality Monitor - Truth about what's actually happening

Run this every 10-15 minutes to see REAL progress, not fake success claims.
"""

import os
import json
from pathlib import Path
from datetime import datetime, timedelta

def main():
    print(f"🔍 ATLAS REALITY CHECK - {datetime.now().strftime('%H:%M:%S')}")
    print("="*60)
    
    # 1. ACTUAL article files created
    article_dir = Path("output/articles/markdown")
    if article_dir.exists():
        articles = list(article_dir.glob("*.md"))
        
        # Check how many in last hour
        now = datetime.now()
        recent_articles = []
        for article in articles:
            mtime = datetime.fromtimestamp(article.stat().st_mtime)
            if mtime > now - timedelta(hours=1):
                recent_articles.append((article, mtime))
        
        print(f"📰 ARTICLES:")
        print(f"   Total: {len(articles)}")
        print(f"   Last hour: {len(recent_articles)}")
        
        if recent_articles:
            recent_articles.sort(key=lambda x: x[1], reverse=True)
            print(f"   Most recent: {recent_articles[0][1].strftime('%H:%M:%S')}")
        else:
            print(f"   ❌ NO NEW ARTICLES IN LAST HOUR")
    else:
        print("❌ No article directory found")
    
    # 2. Queue status - what's waiting
    if os.path.exists("inputs/articles.txt"):
        with open("inputs/articles.txt", "r") as f:
            queue = [line.strip() for line in f if line.strip()]
        print(f"📋 QUEUE: {len(queue)} URLs waiting")
    else:
        print("❌ No articles.txt queue")
    
    # 3. Background process activity
    import subprocess
    try:
        result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
        atlas_processes = [line for line in result.stdout.split('\n') 
                          if 'python' in line and ('run.py' in line or 'atlas' in line)]
        print(f"🔄 BACKGROUND PROCESSES: {len(atlas_processes)} running")
        
        if not atlas_processes:
            print("❌ NO BACKGROUND PROCESSES - ATLAS IS STOPPED!")
    except:
        print("❌ Can't check processes")
    
    # 4. Recent log activity
    log_file = "output/Full_Pipeline.log"
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            lines = f.readlines()
        
        # Check last 10 log entries
        recent_logs = lines[-10:]
        latest_time = None
        for line in reversed(recent_logs):
            if " - INFO - " in line:
                try:
                    time_part = line.split(" - INFO - ")[0]
                    latest_time = time_part
                    break
                except:
                    pass
        
        print(f"📜 LOGS:")
        print(f"   Total lines: {len(lines)}")
        print(f"   Latest activity: {latest_time or 'Unknown'}")
        print(f"   Last few entries:")
        for line in recent_logs[-3:]:
            print(f"      {line.strip()}")
    else:
        print("❌ No pipeline log found")
    
    # 5. Critical truth check
    print(f"\n🎯 TRUTH CHECK:")
    if article_dir.exists() and len(recent_articles) > 0:
        print(f"✅ REAL PROGRESS: {len(recent_articles)} articles in last hour")
    elif article_dir.exists() and len(articles) > 1900:
        print(f"⚠️  SLOW/STOPPED: {len(articles)} total but none in last hour")
    else:
        print(f"❌ NOT WORKING: No recent article creation")

if __name__ == "__main__":
    main()