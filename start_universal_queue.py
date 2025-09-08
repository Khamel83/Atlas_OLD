#!/usr/bin/env python3
"""
Start Universal Processing Queue

Simple script to start the universal queue processing system.
Replaces multiple competing processes with a single coordinated system.
"""

import sys
import signal
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from universal_processing_queue import UniversalProcessingQueue

def signal_handler(signum, frame):
    print("\n🛑 Shutdown signal received")
    sys.exit(0)

def main():
    print("🚀 Starting Universal Atlas Processing Queue")
    
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    queue = UniversalProcessingQueue()
    
    # Show initial stats
    stats = queue.get_queue_stats()
    print("📊 Initial Queue Stats:")
    for key, value in stats.items():
        print(f"   {key}: {value}")
    print()
    
    # Start processing
    print("▶️  Processing jobs... (Ctrl+C to stop)")
    queue.process_jobs()

if __name__ == "__main__":
    main()