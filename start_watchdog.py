#!/usr/bin/env python3
"""
Start Atlas Process Watchdog

Quick script to start the process watchdog daemon.
"""

import subprocess
import sys
from helpers.bulletproof_process_manager import create_managed_process
from pathlib import Path

def main():
    """Start the watchdog daemon"""
    script_path = Path(__file__).parent / "helpers" / "process_watchdog.py"
    
    print("🐕 Starting Atlas Process Watchdog...")
    print("   - Monitors all Atlas processes for runaway behavior")
    print("   - Kills stuck processes after 10-30 minutes")
    print("   - Automatically restarts with delays")
    print("   - Aggressive: Better to kill and retry than waste resources")
    print()
    
    try:
        # Start as daemon with 3-minute check intervals
        create_managed_process([
            sys.executable, str(script_path), 
            "--daemon", "--interval", "3"
        ], "start_watchdog_daemon")
    except KeyboardInterrupt:
        print("\n👋 Watchdog stopped")
    except Exception as e:
        print(f"❌ Error starting watchdog: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()