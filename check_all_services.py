#!/usr/bin/env python3
"""
Atlas Unified Service Status Checker

Checks all Atlas background services and their coordination:
- Service Manager 
- Scheduler
- Process Watchdog
- API Server
- Recent activity and progress
"""

import psutil
import sqlite3
import subprocess
import json
from pathlib import Path
from datetime import datetime, timedelta

def check_atlas_services():
    """Check all Atlas services and their harmony"""
    
    print("🔍 Atlas Unified Service Status Check")
    print("=" * 50)
    
    services = {
        "service_manager": {"pattern": "atlas_service_manager.py", "expected": True},
        "scheduler": {"pattern": "atlas_scheduler.py", "expected": True}, 
        "watchdog": {"pattern": "process_watchdog.py", "expected": True},
        "api_server": {"pattern": "uvicorn", "expected": True}
    }
    
    # Check running processes
    running_services = {}
    for proc in psutil.process_iter(['pid', 'cmdline', 'create_time', 'cpu_percent', 'memory_info']):
        try:
            cmdline = ' '.join(proc.info.get('cmdline', []))
            
            for service_name, config in services.items():
                if config["pattern"] in cmdline:
                    uptime = datetime.now() - datetime.fromtimestamp(proc.info['create_time'])
                    memory_info = proc.info.get('memory_info')
                    memory_mb = memory_info.rss / (1024*1024) if memory_info else 0
                    running_services[service_name] = {
                        "pid": proc.info['pid'],
                        "uptime": str(uptime).split('.')[0],  # Remove microseconds
                        "cpu": proc.info.get('cpu_percent', 0),
                        "memory_mb": memory_mb
                    }
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    # Print service status
    all_running = True
    for service_name, config in services.items():
        if service_name in running_services:
            info = running_services[service_name]
            print(f"✅ {service_name:15} PID: {info['pid']:6} Uptime: {info['uptime']:10} CPU: {info['cpu']:4.1f}% Memory: {info['memory_mb']:5.1f}MB")
        else:
            print(f"❌ {service_name:15} NOT RUNNING")
            all_running = False
    
    print()
    
    # Check recent activity and coordination
    print("📊 Service Coordination & Activity")
    print("-" * 30)
    
    # Database activity
    try:
        conn = sqlite3.connect('data/atlas.db')
        content_count = conn.execute("SELECT COUNT(*) FROM content").fetchone()[0]
        conn.close()
        
        search_conn = sqlite3.connect('data/enhanced_search.db')  
        search_count = search_conn.execute("SELECT COUNT(*) FROM search_index").fetchone()[0]
        search_conn.close()
        
        print(f"📚 Content Database: {content_count:,} items")
        print(f"🔍 Search Index: {search_count:,} items ({search_count/content_count*100:.1f}% indexed)")
        
    except Exception as e:
        print(f"❌ Database check failed: {e}")
    
    # Check recent file activity
    try:
        output_path = Path("output")
        if output_path.exists():
            recent_files = [f for f in output_path.rglob("*.md") 
                          if f.stat().st_mtime > (datetime.now() - timedelta(hours=6)).timestamp()]
            print(f"📄 Recent content files (6h): {len(recent_files)}")
        
        # Check logs for recent activity
        log_path = Path("logs")
        if log_path.exists():
            recent_logs = [f for f in log_path.glob("*.log") 
                         if f.stat().st_mtime > (datetime.now() - timedelta(hours=1)).timestamp()]
            print(f"📝 Active log files (1h): {len(recent_logs)}")
            
    except Exception as e:
        print(f"❌ File activity check failed: {e}")
    
    # Check for any config issues
    print()
    print("⚙️  Configuration Status")
    print("-" * 20)
    
    config_files = {
        "Process Watchdog": "config/process_watchdog.json",
        "Articles Queue": "inputs/articles.txt", 
        "Environment": ".env"
    }
    
    for name, path in config_files.items():
        if Path(path).exists():
            print(f"✅ {name}: {path}")
        else:
            print(f"❌ {name}: {path} (missing)")
    
    # Overall status
    print()
    if all_running:
        print("🎉 ALL SERVICES RUNNING HARMONIOUSLY")
        print("   - Service Manager coordinates everything")
        print("   - Scheduler runs background tasks") 
        print("   - Watchdog prevents runaway processes")
        print("   - API serves requests")
        print()
        print("💡 The watchdog will kill any process taking >10-30 minutes")
        print("💡 Everything restarts automatically with delays")
        print("💡 Atlas prioritizes patient accumulation over speed")
    else:
        print("⚠️  SOME SERVICES NOT RUNNING - check individual services")
    
    return all_running

def main():
    """Main entry point"""
    try:
        check_atlas_services()
    except KeyboardInterrupt:
        print("\n👋 Status check interrupted")
    except Exception as e:
        print(f"❌ Status check error: {e}")

if __name__ == "__main__":
    main()