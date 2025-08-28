#!/usr/bin/env python3
"""
Atlas Background Service (Legacy)

This service is for backward compatibility with system tests.
The primary service manager is atlas_service_manager.py.
"""

import time
import sys
import subprocess
import os
import psutil
from pathlib import Path
from datetime import datetime
import atexit
from helpers.bulletproof_process_manager import get_manager, create_managed_process
from helpers.resource_monitor import check_system_health

class AtlasComprehensiveService:
    """A legacy version of the comprehensive Atlas background service."""
    
    def __init__(self):
        self.running = True
        self.cycles = 0
        self.consecutive_failures = 0
        self.log_dir = Path("logs")
        self.log_dir.mkdir(exist_ok=True)
        self.log_file = self.log_dir / "comprehensive_service.log"
        self.project_root = Path(__file__).parent.resolve()
        self.python_executable = str(self.project_root / "venv" / "bin" / "python3")

        # Register cleanup on exit
        atexit.register(self.cleanup_processes)
        signal.signal(signal.SIGTERM, lambda s, f: self.cleanup_processes())
        signal.signal(signal.SIGINT, lambda s, f: self.cleanup_processes())

    def log(self, message, level="INFO"):
        """Log with timestamp and level."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] [{level}] CYCLE {self.cycles}: {message}"
        print(log_msg)
        with open(self.log_file, 'a') as f:
            f.write(log_msg + '\n')

    def perform_preflight_checks(self) -> bool:
        """Perform mandatory pre-flight safety checks using resource_monitor."""
        self.log("Performing pre-flight safety checks using resource_monitor...")
        if not check_system_health():
            self.log("System health check failed, aborting.", "CRITICAL")
            return False
        self.log("All pre-flight checks passed.")
        return True

    def run_script(self, script_path, timeout=600, description=""):
        """Run a script with timeout and progress logging."""
        try:
            self.log(f"Starting: {description} - {script_path}")
            # Use a list for the command
            command = [self.python_executable]
            # Split the script_path string into a list of arguments
            command.extend(script_path.split())
            script_full_path = self.project_root / command[1]
            if not script_full_path.exists():
                self.log(f"SKIP: Script not found - {script_full_path}", "WARNING")
                return True # Return True to not count as a failure
            
            process = create_managed_process(
                command,
                description,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=self.project_root,
                timeout=timeout
            )
            
            stdout, stderr = process.communicate() # Timeout is handled by create_managed_process
            
            if process.returncode == 0:
                self.log(f"SUCCESS: {description} completed.")
                return True
            else:
                self.log(f"ERROR: {description} failed. STDERR: {stderr[:500]}", "ERROR")
                return False
                
        except Exception as e: # subprocess.TimeoutExpired is handled by create_managed_process
            self.log(f"EXCEPTION running {description}: {e}", "ERROR")
            return False
    
    def comprehensive_processing_cycle(self):
        """One complete processing cycle."""
        self.cycles += 1
        self.log("=" * 60)
        self.log("STARTING COMPREHENSIVE PROCESSING CYCLE")
        
        tasks = [
            ("enhanced_transcript_discovery.py", 900, "Enhanced transcript discovery"),
            ("run.py --all", 300, "Main processing pipeline"),
            ("process_podcasts.py", 600, "Podcast processing"),
            ("migrate_files_to_database.py", 300, "File to database migration"),
            ("populate_search_index.py", 300, "Search index population"),
            ("retry_failed_articles.py", 600, "Article retry with enhanced strategies")
        ]
        
        success_count = 0
        for script, timeout, desc in tasks:
            if self.run_script(script, timeout, desc):
                success_count += 1
        
        if success_count < len(tasks):
            self.consecutive_failures += 1
            self.log(f"Cycle finished with {len(tasks) - success_count} failed tasks.", "WARNING")
        else:
            self.consecutive_failures = 0 # Reset on a fully successful cycle

        self.log("COMPREHENSIVE CYCLE COMPLETE")
        self.log("=" * 60)
    
    def run_forever(self):
        """Run comprehensive processing forever with safety checks."""
        self.log("Atlas Comprehensive Service (Legacy) starting up.")
        
        if not self.perform_preflight_checks():
            self.log("Halting due to pre-flight check failures.", "CRITICAL")
            return

        while self.running:
            try:
                self.comprehensive_processing_cycle()
                
                # Circuit Breaker
                if self.consecutive_failures >= 3:
                    self.log(f"CIRCUIT BREAKER: Halting after {self.consecutive_failures} consecutive failed cycles.", "CRITICAL")
                    self.running = False
                    continue

                self.log("Sleeping 30 minutes until next cycle...")
                time.sleep(1800)
                    
            except KeyboardInterrupt:
                self.log("Received shutdown signal.")
                self.running = False
            except Exception as e:
                self.log(f"UNHANDLED CYCLE ERROR: {e}", "CRITICAL")
                self.consecutive_failures += 1
                self.log("Sleeping 5 minutes before retry...")
                time.sleep(300)

    def cleanup_processes(self):
        """Cleanup all managed processes"""
        manager = get_manager()
        manager.cleanup_all()
        self.log("🧹 All processes cleaned up")

def main():
    """Main entry point"""
    # This is a legacy service and should not be run directly.
    # Use atlas_service_manager.py instead.
    print("This is a legacy service and is not intended to be run directly.")
    print("Please use 'python atlas_service_manager.py start' instead.")

if __name__ == "__main__":
    main()
