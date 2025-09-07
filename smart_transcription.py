#!/usr/bin/env python3
"""
Smart Transcription CLI

Command-line interface for the smart transcription pipeline.
Manages podcast transcription with Mac Mini processing and prioritized configuration.
"""

import os
import sys
import argparse
import json
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

from helpers.smart_transcription_pipeline import SmartTranscriptionPipeline

def main():
    parser = argparse.ArgumentParser(
        description="Smart Podcast Transcription Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process all prioritized podcasts
  python smart_transcription.py --process-all

  # Process specific podcasts
  python smart_transcription.py --process-podcasts "Acquired" "99% Invisible"
  
  # Process transcription queue (Mac Mini jobs)
  python smart_transcription.py --process-queue
  
  # Show status and statistics
  python smart_transcription.py --status
  
  # Show prioritized podcasts configuration
  python smart_transcription.py --show-config
        """)
    
    parser.add_argument("--process-all", action="store_true", 
                       help="Process all prioritized podcasts according to their configuration")
    
    parser.add_argument("--process-podcasts", nargs="+", metavar="PODCAST", 
                       help="Process specific podcasts by name")
    
    parser.add_argument("--process-queue", action="store_true", 
                       help="Process the Mac Mini transcription queue")
    
    parser.add_argument("--status", action="store_true", 
                       help="Show processing queue status and statistics")
    
    parser.add_argument("--show-config", action="store_true", 
                       help="Show prioritized podcasts configuration")
    
    parser.add_argument("--max-concurrent", type=int, default=2, 
                       help="Maximum concurrent transcription jobs (default: 2)")
    
    parser.add_argument("--dry-run", action="store_true", 
                       help="Show what would be processed without actually processing")
    
    parser.add_argument("--verbose", "-v", action="store_true", 
                       help="Enable verbose logging")
    
    args = parser.parse_args()
    
    # Configure logging level
    import logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        pipeline = SmartTranscriptionPipeline()
        
        if args.show_config:
            print("📋 Prioritized Podcasts Configuration:")
            print("=" * 50)
            
            for podcast_name, config in pipeline.prioritized_podcasts.items():
                status_emoji = "⏭️" if config['exclude'] else ("📝" if config['transcript_only'] else "🎵")
                print(f"{status_emoji} {podcast_name}")
                print(f"   Episodes: {config['count']}")
                print(f"   Category: {config['category']}")
                print(f"   Transcript Only: {'Yes' if config['transcript_only'] else 'No'}")
                print(f"   Excluded: {'Yes' if config['exclude'] else 'No'}")
                print()
            
            print(f"Total podcasts: {len(pipeline.prioritized_podcasts)}")
            excluded_count = sum(1 for c in pipeline.prioritized_podcasts.values() if c['exclude'])
            print(f"Excluded: {excluded_count}")
            print(f"Active: {len(pipeline.prioritized_podcasts) - excluded_count}")
            
        elif args.status:
            print("📊 Smart Transcription Pipeline Status:")
            print("=" * 50)
            
            status = pipeline.get_queue_status()
            
            if 'error' in status:
                print(f"❌ Error: {status['error']}")
                return 1
            
            # Queue status
            print("🔄 Processing Queue:")
            for status_name, count in status.get('status_counts', {}).items():
                emoji = {
                    'pending': '⏳',
                    'processing': '🔄', 
                    'completed': '✅',
                    'error': '❌'
                }.get(status_name, '📄')
                print(f"   {emoji} {status_name.title()}: {count}")
            
            # Mac Mini status
            mac_enabled = status.get('mac_mini_enabled', False)
            print(f"🖥️  Mac Mini: {'✅ Enabled' if mac_enabled else '❌ Disabled'}")
            
            # Prioritized podcasts
            podcast_count = status.get('prioritized_podcasts_count', 0)
            print(f"📋 Prioritized Podcasts: {podcast_count}")
            
            # Recent activity
            recent = status.get('recent_items', [])
            if recent:
                print("\n🕒 Recent Activity:")
                for item in recent[:5]:  # Show last 5
                    status_emoji = {
                        'pending': '⏳',
                        'processing': '🔄', 
                        'completed': '✅',
                        'error': '❌'
                    }.get(item['status'], '📄')
                    print(f"   {status_emoji} {item['podcast_name']}: {item['episode_title'][:40]}...")
            
        elif args.process_queue:
            print("🔄 Processing Mac Mini transcription queue...")
            
            if args.dry_run:
                print("🧪 DRY RUN MODE - No actual processing will occur")
                # Show what would be processed
                status = pipeline.get_queue_status()
                pending_count = status.get('status_counts', {}).get('pending', 0)
                print(f"Would process up to {min(pending_count, args.max_concurrent)} pending items")
                return 0
            
            processed = pipeline.process_transcription_queue(args.max_concurrent)
            print(f"✅ Processed {processed} items from transcription queue")
            
        elif args.process_all:
            print("🚀 Processing all prioritized podcasts...")
            
            if args.dry_run:
                print("🧪 DRY RUN MODE - Showing what would be processed")
                active_podcasts = [
                    name for name, config in pipeline.prioritized_podcasts.items() 
                    if not config['exclude']
                ]
                print(f"Would process {len(active_podcasts)} podcasts:")
                for name in active_podcasts[:10]:  # Show first 10
                    config = pipeline.prioritized_podcasts[name]
                    mode = "transcript-only" if config['transcript_only'] else "full processing"
                    print(f"   🎙️ {name} ({config['count']} episodes, {mode})")
                if len(active_podcasts) > 10:
                    print(f"   ... and {len(active_podcasts) - 10} more")
                return 0
            
            total = pipeline.process_prioritized_podcasts()
            print(f"✅ Processed {total} total episodes across all prioritized podcasts")
            
        elif args.process_podcasts:
            print(f"🎙️ Processing specific podcasts: {', '.join(args.process_podcasts)}")
            
            # Validate podcast names
            invalid_podcasts = []
            for podcast_name in args.process_podcasts:
                if podcast_name not in pipeline.prioritized_podcasts:
                    invalid_podcasts.append(podcast_name)
            
            if invalid_podcasts:
                print(f"❌ Unknown podcasts: {', '.join(invalid_podcasts)}")
                print("💡 Use --show-config to see available podcasts")
                return 1
            
            if args.dry_run:
                print("🧪 DRY RUN MODE - Showing what would be processed")
                for podcast_name in args.process_podcasts:
                    config = pipeline.prioritized_podcasts[podcast_name]
                    if config['exclude']:
                        print(f"   ⏭️ {podcast_name}: EXCLUDED")
                    else:
                        mode = "transcript-only" if config['transcript_only'] else "full processing"
                        print(f"   🎙️ {podcast_name}: {config['count']} episodes, {mode}")
                return 0
            
            total = 0
            for podcast_name in args.process_podcasts:
                config = pipeline.prioritized_podcasts[podcast_name]
                if config['exclude']:
                    print(f"⏭️ Skipping excluded podcast: {podcast_name}")
                    continue
                
                processed = pipeline._process_single_podcast(podcast_name, config)
                total += processed
                print(f"✅ {podcast_name}: {processed} episodes processed")
            
            print(f"✅ Total: {total} episodes processed")
            
        else:
            parser.print_help()
            return 1
    
    except KeyboardInterrupt:
        print("\n⚡ Interrupted by user")
        return 1
    
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())