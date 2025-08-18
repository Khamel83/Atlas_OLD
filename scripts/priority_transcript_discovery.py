#!/usr/bin/env python3
"""
Priority Podcast Transcript Discovery

Efficiently discovers transcripts for high-value podcasts using the comprehensive
system but with optimized settings for production use.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse
import logging
import time
from pathlib import Path

# Import our comprehensive system
from scripts.comprehensive_transcript_discovery import ComprehensiveTranscriptDiscovery

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# High-priority podcasts with high transcript availability
PRIORITY_PODCASTS = [
    "Lex Fridman Podcast",           # 91 transcripts confirmed
    "Conversations with Tyler",      # High-quality economic conversations
    "Acquired",                      # Business deep dives
    "This American Life",            # 10 transcripts confirmed  
    "The Tim Ferriss Show",          # Popular productivity podcast
    "EconTalk",                      # Economics conversations
    "The Knowledge Project",         # Farnam Street insights
    "Masters in Business",           # Bloomberg finance
    "The Joe Rogan Experience",      # Massive archive
    "Sam Harris",                    # Philosophy and AI
]

def run_priority_discovery():
    """Run discovery on priority podcasts with optimized settings"""
    
    discovery = ComprehensiveTranscriptDiscovery()
    
    # Get priority podcasts from database
    all_podcasts = discovery.store.list_podcasts()
    priority_podcasts = [p for p in all_podcasts if p.name in PRIORITY_PODCASTS]
    
    logger.info(f"🎯 Running priority discovery on {len(priority_podcasts)} podcasts")
    logger.info(f"📋 Priority list: {[p.name for p in priority_podcasts]}")
    
    results = {}
    total_transcripts = 0
    total_episodes = 0
    
    for i, podcast in enumerate(priority_podcasts, 1):
        logger.info(f"\n[{i}/{len(priority_podcasts)}] Processing: {podcast.name}")
        
        try:
            start_time = time.time()
            
            # Convert to config dict
            podcast_config = {
                'title': podcast.name,
                'slug': podcast.slug,
                'rss_url': podcast.rss_url,
                'site_url': podcast.site_url,
                'resolver': podcast.resolver,
                'episode_selector': podcast.episode_selector,
                'transcript_selector': podcast.transcript_selector,
                'config': podcast.config or {}
            }
            
            # Run discovery with reasonable limits
            result = discovery.discover_podcast_transcripts(
                podcast_config, 
                max_episodes=100  # Increased for priority podcasts
            )
            
            processing_time = time.time() - start_time
            result.processing_time = processing_time
            
            results[podcast.name] = result
            total_transcripts += result.transcripts_found
            total_episodes += result.episodes_checked
            
            logger.info(f"✅ {podcast.name}: {result.transcripts_found}/{result.episodes_checked} "
                       f"({result.success_rate:.1%}) - {result.high_confidence_transcripts} high-conf - "
                       f"{processing_time:.1f}s")
            
            if result.transcripts_found > 0:
                logger.info(f"   💬 Sample: {result.transcript_sources[0]['episode_title'][:50]}...")
            
        except Exception as e:
            logger.error(f"❌ Error processing {podcast.name}: {e}")
    
    # Final summary
    logger.info("\n🎯 PRIORITY DISCOVERY COMPLETE")
    logger.info("📊 Total Results:")
    logger.info(f"   • Podcasts processed: {len(priority_podcasts)}")
    logger.info(f"   • Episodes checked: {total_episodes}")
    logger.info(f"   • Transcripts found: {total_transcripts}")
    logger.info(f"   • Overall success rate: {total_transcripts/total_episodes*100 if total_episodes > 0 else 0:.1f}%")
    
    # Top performers
    top_results = sorted(
        [(name, result) for name, result in results.items() if result.transcripts_found > 0],
        key=lambda x: x[1].transcripts_found,
        reverse=True
    )
    
    logger.info("\n🏆 TOP PERFORMERS:")
    for i, (name, result) in enumerate(top_results[:5], 1):
        logger.info(f"   {i}. {name}: {result.transcripts_found} transcripts ({result.success_rate:.1%})")
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Priority podcast transcript discovery")
    parser.add_argument('--quick', action='store_true', 
                       help='Quick mode with fewer episodes per podcast')
    
    args = parser.parse_args()
    
    if args.quick:
        logger.info("🚀 Running in QUICK MODE (10 episodes per podcast)")
        # Monkey patch the max episodes for quick testing
        import scripts.comprehensive_transcript_discovery
        original_method = scripts.comprehensive_transcript_discovery.ComprehensiveTranscriptDiscovery.discover_podcast_transcripts
        
        def quick_discover(self, podcast_config, max_episodes=10):
            return original_method(self, podcast_config, max_episodes=10)
        
        scripts.comprehensive_transcript_discovery.ComprehensiveTranscriptDiscovery.discover_podcast_transcripts = quick_discover
    
    results = run_priority_discovery()
    
    # Save results summary
    data_dir = Path("data/podcasts")
    summary_file = data_dir / "priority_discovery_summary.json"
    
    import json
    from dataclasses import asdict
    
    summary_data = {}
    for name, result in results.items():
        summary_data[name] = asdict(result)
        summary_data[name]['timestamp'] = time.time()
    
    with open(summary_file, 'w') as f:
        json.dump(summary_data, f, indent=2, default=str)
    
    logger.info(f"💾 Results saved to: {summary_file}")

if __name__ == "__main__":
    main()