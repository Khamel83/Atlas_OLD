#!/usr/bin/env python3
"""
Complete podcast processing workflow - discovery, fetch, and Atlas integration
"""

import sys
import logging
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

from helpers.podcast_transcript_ingestor import PodcastTranscriptIngestor
from helpers.config import load_config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    """Full podcast processing workflow"""
    print("🎙️  Atlas Podcast Processing Workflow")
    print("=" * 50)
    
    try:
        # Load configuration
        config = load_config()
        
        # Create integrated ingestor
        processor = PodcastTranscriptIngestor(config)
        
        print("📋 Processing flow:")
        print("   1. 🔍 Discovery - Find new episodes from RSS feeds")
        print("   2. 📥 Fetch - Download transcripts from web")
        print("   3. ⚙️  Process - Run through Atlas pipeline")
        print("   4. 🔍 Index - Add to search system")
        print()
        
        # Run full workflow for priority podcasts
        priority_podcasts = [
            'conversations-with-tyler',
            'planet-money', 
            'hard-fork',
            'ezra-klein-show'
        ]
        
        print(f"🎯 Processing priority podcasts: {', '.join(priority_podcasts)}")
        print()
        
        # Full discovery, fetch, and processing
        processor.discover_and_process_transcripts(priority_podcasts)
        
        # Show stats
        print("\n📊 Processing Statistics:")
        stats = processor.get_processing_stats()
        for key, value in stats.items():
            print(f"   {key}: {value}")
        
        print("\n✅ Podcast processing workflow complete!")
        print("💡 Transcripts are now searchable in Atlas system")
        
    except Exception as e:
        print(f"❌ Error in podcast processing: {e}")
        if '--verbose' in sys.argv:
            import traceback
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()