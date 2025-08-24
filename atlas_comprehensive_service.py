#!/usr/bin/env python3
"""
Atlas COMPREHENSIVE Background Service

This is what should ACTUALLY be running - the relentless processing system
that never stops until everything possible is done.
"""

import time
import sys
import subprocess
import json
import os
from pathlib import Path
from datetime import datetime

class AtlasComprehensiveService:
    """The REAL Atlas background service that never stops"""
    
    def __init__(self):
        self.running = True
        self.cycles = 0
        self.log_file = Path("logs/comprehensive_service.log")
        self.log_file.parent.mkdir(exist_ok=True)
        
    def log(self, message):
        """Log with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] CYCLE {self.cycles}: {message}"
        print(log_msg)
        with open(self.log_file, 'a') as f:
            f.write(log_msg + '\n')
    
    def run_script(self, script_path, timeout=600, description=""):
        """Run a script with timeout and logging"""
        try:
            self.log(f"Starting: {description} - {script_path}")
            
            if not Path(script_path).exists():
                self.log(f"SKIP: Script not found - {script_path}")
                return False
                
            result = subprocess.run([
                sys.executable, script_path
            ], timeout=timeout, capture_output=True, text=True, cwd=Path(__file__).parent)
            
            if result.returncode == 0:
                self.log(f"SUCCESS: {description}")
                return True
            else:
                self.log(f"ERROR: {description} - {result.stderr[:200]}")
                return False
                
        except subprocess.TimeoutExpired:
            self.log(f"TIMEOUT: {description} after {timeout}s")
            return False
        except Exception as e:
            self.log(f"EXCEPTION: {description} - {e}")
            return False
    
    def comprehensive_processing_cycle(self):
        """One complete processing cycle - EVERYTHING Atlas should do"""
        self.cycles += 1
        self.log("=" * 60)
        self.log("STARTING COMPREHENSIVE PROCESSING CYCLE")
        self.log("=" * 60)
        
        # Phase 1: Transcript Discovery and Scraping (INTEGRATED!)
        self.log("PHASE 1: TRANSCRIPT DISCOVERY & SCRAPING")
        self.run_script("daily_transcript_polling.py", 600, "Unified transcript discovery and polling")
        
        # Phase 2: Content Processing
        self.log("PHASE 2: CONTENT PROCESSING")
        self.run_script("run.py --all", 300, "Main processing pipeline")
        self.run_script("process_podcasts.py", 600, "Podcast processing")
        
        # Phase 3: Database Integration  
        self.log("PHASE 3: DATABASE INTEGRATION")
        self.run_script("migrate_files_to_database.py", 300, "File to database migration")
        self.run_script("populate_search_index.py", 300, "Search index population")
        
        # Phase 4: Retry and Recovery
        self.log("PHASE 4: RETRY & RECOVERY")  
        self.run_script("retry_failed_articles.py", 600, "Article retry with enhanced strategies")
        
        # Phase 5: Maintenance
        self.log("PHASE 5: MAINTENANCE")
        # Check database integrity
        self.check_system_health()
        
        self.log("COMPREHENSIVE CYCLE COMPLETE")
        self.log("=" * 60)
    
    def check_system_health(self):
        """Check system health and log metrics"""
        try:
            # Database counts
            import sqlite3
            conn = sqlite3.connect('atlas.db')
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(*) FROM content")
            content_count = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM content WHERE LENGTH(content) > 100")  
            substantial_content = cursor.fetchone()[0]
            
            conn.close()
            
            self.log(f"HEALTH: {content_count:,} total records, {substantial_content:,} with substantial content")
            
            # File counts
            output_files = len(list(Path("output").rglob("*.json")))
            transcript_files = len(list(Path("output").rglob("*transcript*")))
            
            self.log(f"HEALTH: {output_files:,} output files, {transcript_files} transcript files")
            
        except Exception as e:
            self.log(f"HEALTH CHECK ERROR: {e}")
    
    def run_forever(self):
        """Run comprehensive processing forever"""
        self.log("🚀 ATLAS COMPREHENSIVE SERVICE STARTING")
        self.log("This service will run RELENTLESSLY until everything possible is processed")
        
        while self.running:
            try:
                # Run comprehensive cycle
                self.comprehensive_processing_cycle()
                
                # Wait 30 minutes before next cycle
                self.log("Sleeping 30 minutes until next comprehensive cycle...")
                
                for i in range(30 * 60):  # 30 minutes in seconds
                    if not self.running:
                        break
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                self.log("Received shutdown signal")
                self.running = False
            except Exception as e:
                self.log(f"CYCLE ERROR: {e}")
                self.log("Sleeping 5 minutes before retry...")
                time.sleep(300)

def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        # Show status
        log_file = Path("logs/comprehensive_service.log")
        if log_file.exists():
            print("Recent log entries:")
            with open(log_file, 'r') as f:
                lines = f.readlines()
                for line in lines[-20:]:  # Last 20 lines
                    print(line.strip())
        else:
            print("No log file found - service may not be running")
        return
    
    # Start the service
    service = AtlasComprehensiveService()
    service.run_forever()

if __name__ == "__main__":
    main()