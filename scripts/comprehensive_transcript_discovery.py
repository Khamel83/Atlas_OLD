#!/usr/bin/env python3
"""
Comprehensive Podcast Transcript Discovery System

Systematically discovers and fetches transcripts for all podcasts using:
1. Smart discovery patterns (learns from successful sources)
2. Site-specific URL patterns 
3. Generic HTML extraction
4. RSS metadata analysis
5. Google search as fallback

This replaces bespoke per-podcast approaches with a comprehensive system.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import argparse
import logging
import time
import json
from typing import Dict, List, Any, Optional
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime

from modules.podcasts.store import PodcastStore, Episode
from modules.podcasts.resolvers.smart_discovery import SmartDiscoveryResolver
from modules.podcasts.resolvers.pattern import PatternResolver
from modules.podcasts.resolvers.generic_html import GenericHTMLResolver
from modules.podcasts.resolvers.google_search import GoogleSearchResolver

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EpisodeAdapter:
    """Adapter to make store Episode compatible with resolver Episode expectations"""
    def __init__(self, store_episode: Episode):
        self.title = store_episode.title
        self.url = store_episode.url
        self.guid = store_episode.guid
        self.metadata = store_episode.metadata or {}
        self.publish_date = store_episode.publish_date  # Keep original for pattern resolver
        
        # Parse published_at from string for smart resolver
        self.published_at = None
        if store_episode.publish_date:
            try:
                self.published_at = datetime.fromisoformat(store_episode.publish_date.replace('Z', '+00:00'))
            except:
                self.published_at = None

@dataclass
class DiscoveryResult:
    """Result of transcript discovery for a podcast"""
    podcast_title: str
    episodes_checked: int
    transcripts_found: int
    success_rate: float
    high_confidence_transcripts: int
    total_content_length: int
    processing_time: float
    errors: List[str]
    transcript_sources: List[Dict[str, Any]]

class ComprehensiveTranscriptDiscovery:
    """Comprehensive transcript discovery system for all podcasts"""
    
    def __init__(self, data_dir: str = "data/podcasts"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize store and resolvers
        self.store = PodcastStore(str(self.data_dir / "atlas_podcasts.db"))
        self.smart_resolver = SmartDiscoveryResolver(str(self.data_dir))
        self.pattern_resolver = PatternResolver()
        self.html_resolver = GenericHTMLResolver()
        self.google_resolver = GoogleSearchResolver()
        
        # Results tracking
        self.results_file = self.data_dir / "discovery_results.json"
        self.transcripts_dir = self.data_dir / "transcripts"
        self.transcripts_dir.mkdir(exist_ok=True)
        
        # Priority podcasts (high-value for transcripts)
        self.priority_podcasts = [
            "The Lex Fridman Podcast",
            "Conversations with Tyler",
            "Acquired",
            "This American Life",
            "The Tim Ferriss Show",
            "The Joe Rogan Experience",
            "Sam Harris",
            "EconTalk",
            "The Knowledge Project",
            "Masters in Business",
            "The Stratechery Daily Briefing",
            "The Ben Thompson Podcast"
        ]
    
    def discover_all_podcasts(self, max_episodes_per_podcast: int = 50, 
                            priority_only: bool = False,
                            resume_from: Optional[str] = None) -> Dict[str, DiscoveryResult]:
        """
        Comprehensive discovery across all podcasts
        
        Args:
            max_episodes_per_podcast: Limit episodes to process per podcast
            priority_only: Only process priority podcasts
            resume_from: Resume from specific podcast title
        """
        results = {}
        
        # Load existing results
        if self.results_file.exists():
            try:
                with open(self.results_file, 'r') as f:
                    existing_results = json.load(f)
                    logger.info(f"Loaded {len(existing_results)} existing results")
            except Exception as e:
                logger.error(f"Error loading existing results: {e}")
                existing_results = {}
        else:
            existing_results = {}
        
        # Get all podcasts
        podcasts = self.store.list_podcasts()
        logger.info(f"Processing {len(podcasts)} total podcasts")
        
        # Filter by priority if requested
        if priority_only:
            podcasts = [p for p in podcasts if p.name in self.priority_podcasts]
            logger.info(f"Filtered to {len(podcasts)} priority podcasts")
        
        # Sort by priority
        def priority_sort_key(podcast):
            title = podcast.name
            if title in self.priority_podcasts:
                return (0, self.priority_podcasts.index(title))  # Priority podcasts first
            return (1, title)  # Then alphabetically
        
        podcasts.sort(key=priority_sort_key)
        
        # Resume functionality
        if resume_from:
            start_index = 0
            for i, podcast in enumerate(podcasts):
                if podcast.name == resume_from:
                    start_index = i
                    break
            podcasts = podcasts[start_index:]
            logger.info(f"Resuming from podcast {start_index}: {resume_from}")
        
        total_podcasts = len(podcasts)
        
        for i, podcast_config in enumerate(podcasts, 1):
            podcast_title = podcast_config.name
            
            try:
                # Skip if already processed recently (within 24 hours)
                if podcast_title in existing_results:
                    last_processed = existing_results[podcast_title].get('timestamp', '')
                    if last_processed:
                        try:
                            last_time = datetime.fromisoformat(last_processed)
                            hours_since = (datetime.now() - last_time).total_seconds() / 3600
                            if hours_since < 24:
                                logger.info(f"[{i}/{total_podcasts}] Skipping {podcast_title} (processed {hours_since:.1f}h ago)")
                                continue
                        except:
                            pass
                
                logger.info(f"\n[{i}/{total_podcasts}] Processing: {podcast_title}")
                logger.info(f"Progress: {(i-1)/total_podcasts*100:.1f}% complete")
                
                start_time = time.time()
                
                # Convert podcast object to config dict for compatibility
                podcast_dict = {
                    'title': podcast_config.name,
                    'slug': podcast_config.slug,
                    'rss_url': podcast_config.rss_url,
                    'site_url': podcast_config.site_url,
                    'resolver': podcast_config.resolver,
                    'episode_selector': podcast_config.episode_selector,
                    'transcript_selector': podcast_config.transcript_selector,
                    'config': podcast_config.config or {}
                }
                
                # Discover transcripts for this podcast
                result = self.discover_podcast_transcripts(
                    podcast_dict, 
                    max_episodes=max_episodes_per_podcast
                )
                
                processing_time = time.time() - start_time
                result.processing_time = processing_time
                
                results[podcast_title] = result
                
                # Save results incrementally
                self.save_results(results, existing_results)
                
                logger.info(f"✅ {podcast_title}: {result.transcripts_found}/{result.episodes_checked} "
                          f"({result.success_rate:.1%}) - {result.high_confidence_transcripts} high-conf - "
                          f"{processing_time:.1f}s")
                
                # Rate limiting
                time.sleep(2)
                
            except Exception as e:
                logger.error(f"❌ Error processing {podcast_title}: {e}")
                results[podcast_title] = DiscoveryResult(
                    podcast_title=podcast_title,
                    episodes_checked=0,
                    transcripts_found=0,
                    success_rate=0.0,
                    high_confidence_transcripts=0,
                    total_content_length=0,
                    processing_time=0.0,
                    errors=[str(e)],
                    transcript_sources=[]
                )
                
        return results
    
    def discover_podcast_transcripts(self, podcast_config: Dict[str, Any], 
                                   max_episodes: int = 50) -> DiscoveryResult:
        """
        Comprehensive transcript discovery for a single podcast
        """
        podcast_title = podcast_config.get('title', 'Unknown')
        errors = []
        transcript_sources = []
        
        try:
            # Get episodes for this podcast
            podcast_obj = None
            for p in self.store.list_podcasts():
                if p.name == podcast_title:
                    podcast_obj = p
                    break
            
            if not podcast_obj:
                logger.warning(f"Podcast not found: {podcast_title}")
                return DiscoveryResult(
                    podcast_title=podcast_title,
                    episodes_checked=0,
                    transcripts_found=0,
                    success_rate=0.0,
                    high_confidence_transcripts=0,
                    total_content_length=0,
                    processing_time=0.0,
                    errors=["Podcast not found"],
                    transcript_sources=[]
                )
            
            episodes = self.store.get_episodes_by_podcast(podcast_obj.id)
            
            if not episodes:
                logger.warning(f"No episodes found for {podcast_title}")
                return DiscoveryResult(
                    podcast_title=podcast_title,
                    episodes_checked=0,
                    transcripts_found=0,
                    success_rate=0.0,
                    high_confidence_transcripts=0,
                    total_content_length=0,
                    processing_time=0.0,
                    errors=["No episodes found"],
                    transcript_sources=[]
                )
            
            # Limit episodes to process
            episodes_to_process = episodes[:max_episodes]
            logger.info(f"Processing {len(episodes_to_process)} episodes (of {len(episodes)} total)")
            
            episodes_checked = 0
            transcripts_found = 0
            high_confidence_count = 0
            total_content_length = 0
            
            for episode in episodes_to_process:
                try:
                    episodes_checked += 1
                    
                    # Convert to adapter
                    episode_adapter = EpisodeAdapter(episode)
                    
                    # Run all resolvers
                    episode_sources = self.discover_episode_transcripts(episode_adapter, podcast_config)
                    
                    if episode_sources:
                        transcripts_found += 1
                        
                        # Find best source
                        best_source = max(episode_sources, key=lambda s: s.get('confidence', 0))
                        
                        # Check confidence
                        if best_source.get('confidence', 0) >= 0.7:
                            high_confidence_count += 1
                            
                        # Add content length
                        content = best_source.get('metadata', {}).get('content', '')
                        total_content_length += len(content)
                        
                        # Store transcript source info
                        transcript_sources.append({
                            'episode_title': episode_adapter.title,
                            'episode_url': episode_adapter.url,
                            'transcript_url': best_source.get('url'),
                            'confidence': best_source.get('confidence'),
                            'resolver': best_source.get('resolver'),
                            'content_length': len(content),
                            'metadata': best_source.get('metadata', {})
                        })
                        
                        # Save transcript content
                        self.save_transcript(podcast_title, episode_adapter, best_source)
                        
                        logger.debug(f"  ✅ {episode_adapter.title[:50]}... - conf: {best_source.get('confidence', 0):.2f}")
                    else:
                        logger.debug(f"  ❌ {episode_adapter.title[:50]}... - no transcript found")
                    
                    # Rate limiting between episodes
                    time.sleep(0.5)
                    
                except Exception as e:
                    error_msg = f"Error processing episode {episode.title}: {e}"
                    errors.append(error_msg)
                    logger.debug(f"  ❌ {error_msg}")
            
            success_rate = transcripts_found / episodes_checked if episodes_checked > 0 else 0.0
            
            return DiscoveryResult(
                podcast_title=podcast_title,
                episodes_checked=episodes_checked,
                transcripts_found=transcripts_found,
                success_rate=success_rate,
                high_confidence_transcripts=high_confidence_count,
                total_content_length=total_content_length,
                processing_time=0.0,  # Set by caller
                errors=errors,
                transcript_sources=transcript_sources
            )
            
        except Exception as e:
            error_msg = f"Error discovering transcripts for {podcast_title}: {e}"
            errors.append(error_msg)
            logger.error(error_msg)
            
            return DiscoveryResult(
                podcast_title=podcast_title,
                episodes_checked=0,
                transcripts_found=0,
                success_rate=0.0,
                high_confidence_transcripts=0,
                total_content_length=0,
                processing_time=0.0,
                errors=errors,
                transcript_sources=[]
            )
    
    def discover_episode_transcripts(self, episode: Episode, 
                                   podcast_config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Run all resolvers to discover transcripts for a single episode
        """
        all_sources = []
        
        try:
            # 1. Smart Discovery (learns patterns)
            try:
                smart_sources = self.smart_resolver.resolve(episode, podcast_config)
                all_sources.extend(smart_sources)
                logger.debug(f"    Smart discovery: {len(smart_sources)} sources")
            except Exception as e:
                logger.debug(f"    Smart discovery error: {e}")
            
            # 2. Pattern-based (site-specific patterns)  
            try:
                pattern_sources = self.pattern_resolver.resolve(episode, podcast_config)
                all_sources.extend(pattern_sources)
                logger.debug(f"    Pattern resolver: {len(pattern_sources)} sources")
            except Exception as e:
                logger.debug(f"    Pattern resolver error: {e}")
            
            # 3. HTML extraction (if we have episode URLs)
            try:
                html_sources = self.html_resolver.resolve(episode, podcast_config)
                all_sources.extend(html_sources)
                logger.debug(f"    HTML resolver: {len(html_sources)} sources")
            except Exception as e:
                logger.debug(f"    HTML resolver error: {e}")
            
            # 4. Google search (if other methods find nothing)
            if not any(s.get('confidence', 0) > 0.6 for s in all_sources):
                try:
                    google_sources = self.google_resolver.resolve(episode, podcast_config)
                    all_sources.extend(google_sources)
                    logger.debug(f"    Google search: {len(google_sources)} sources")
                except Exception as e:
                    logger.debug(f"    Google search error: {e}")
            
            # Deduplicate by URL
            seen_urls = set()
            unique_sources = []
            for source in all_sources:
                url = source.get('url')
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    unique_sources.append(source)
            
            # Sort by confidence
            unique_sources.sort(key=lambda s: s.get('confidence', 0), reverse=True)
            
            return unique_sources
            
        except Exception as e:
            logger.error(f"Error discovering episode transcripts: {e}")
            return []
    
    def save_transcript(self, podcast_title: str, episode: Episode, source: Dict[str, Any]):
        """Save transcript content to file"""
        try:
            # Create podcast directory
            podcast_dir = self.transcripts_dir / self.slugify(podcast_title)
            podcast_dir.mkdir(exist_ok=True)
            
            # Create filename
            episode_slug = self.slugify(episode.title or "untitled")
            filename = f"{episode_slug}.md"
            filepath = podcast_dir / filename
            
            # Get content
            content = source.get('metadata', {}).get('content', '')
            if not content:
                return
            
            # Create markdown with metadata
            markdown_content = f"""---
title: {episode.title or "Untitled"}
podcast: {podcast_title}
episode_url: {episode.url or ""}
transcript_url: {source.get('url', '')}
confidence: {source.get('confidence', 0)}
resolver: {source.get('resolver', '')}
published_at: {episode.published_at.isoformat() if episode.published_at else ''}
extracted_at: {datetime.now().isoformat()}
content_length: {len(content)}
---

# {episode.title or "Untitled"}

**Podcast:** {podcast_title}
**Published:** {episode.published_at.strftime('%Y-%m-%d') if episode.published_at else 'Unknown'}
**Source:** {source.get('url', '')}
**Confidence:** {source.get('confidence', 0):.2f}

---

{content}
"""
            
            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
            logger.debug(f"    Saved transcript: {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving transcript: {e}")
    
    def slugify(self, text: str) -> str:
        """Convert text to filename-safe slug"""
        import re
        if not text:
            return "untitled"
        slug = re.sub(r'[^\w\s-]', '', text).strip().lower()
        slug = re.sub(r'[-\s]+', '-', slug)
        return slug[:80]  # Limit length
    
    def save_results(self, current_results: Dict[str, DiscoveryResult],
                    existing_results: Dict[str, Any]):
        """Save discovery results to JSON"""
        try:
            # Merge with existing results
            all_results = existing_results.copy()
            
            for podcast_title, result in current_results.items():
                result_dict = asdict(result)
                result_dict['timestamp'] = datetime.now().isoformat()
                all_results[podcast_title] = result_dict
            
            # Write to file
            with open(self.results_file, 'w') as f:
                json.dump(all_results, f, indent=2, default=str)
                
        except Exception as e:
            logger.error(f"Error saving results: {e}")
    
    def generate_report(self, results: Dict[str, DiscoveryResult]) -> str:
        """Generate summary report"""
        total_podcasts = len(results)
        total_episodes = sum(r.episodes_checked for r in results.values())
        total_transcripts = sum(r.transcripts_found for r in results.values())
        total_high_conf = sum(r.high_confidence_transcripts for r in results.values())
        total_content = sum(r.total_content_length for r in results.values())
        
        overall_success_rate = total_transcripts / total_episodes if total_episodes > 0 else 0
        
        # Top performers
        top_podcasts = sorted(
            [(title, result) for title, result in results.items() if result.transcripts_found > 0],
            key=lambda x: x[1].transcripts_found,
            reverse=True
        )[:10]
        
        report = f"""
# Comprehensive Transcript Discovery Report

## Overall Statistics
- **Podcasts processed:** {total_podcasts}
- **Episodes checked:** {total_episodes:,}
- **Transcripts found:** {total_transcripts:,}
- **Overall success rate:** {overall_success_rate:.1%}
- **High-confidence transcripts:** {total_high_conf:,}
- **Total content:** {total_content:,} characters ({total_content/1024/1024:.1f} MB)

## Top 10 Podcasts by Transcript Count
"""
        
        for i, (title, result) in enumerate(top_podcasts, 1):
            report += f"{i:2d}. **{title}**: {result.transcripts_found} transcripts ({result.success_rate:.1%} success rate)\n"
        
        report += f"""
## Processing Summary
- Average processing time per podcast: {sum(r.processing_time for r in results.values()) / len(results):.1f}s
- Total processing time: {sum(r.processing_time for r in results.values()):.1f}s
"""
        
        return report

def main():
    parser = argparse.ArgumentParser(description="Comprehensive podcast transcript discovery")
    parser.add_argument('--max-episodes', type=int, default=50, 
                       help='Maximum episodes per podcast')
    parser.add_argument('--priority-only', action='store_true',
                       help='Only process priority podcasts')
    parser.add_argument('--resume-from', type=str,
                       help='Resume from specific podcast title')
    parser.add_argument('--podcast', type=str,
                       help='Process single podcast by title')
    parser.add_argument('--report-only', action='store_true',
                       help='Generate report from existing results')
    
    args = parser.parse_args()
    
    discovery = ComprehensiveTranscriptDiscovery()
    
    if args.report_only:
        # Load existing results and generate report
        if discovery.results_file.exists():
            with open(discovery.results_file, 'r') as f:
                existing_data = json.load(f)
            
            results = {}
            for title, data in existing_data.items():
                results[title] = DiscoveryResult(**{k: v for k, v in data.items() 
                                                   if k != 'timestamp'})
            
            report = discovery.generate_report(results)
            print(report)
        else:
            print("No existing results found. Run discovery first.")
        return
    
    if args.podcast:
        # Process single podcast
        logger.info(f"Processing single podcast: {args.podcast}")
        
        podcasts = discovery.store.list_podcasts()
        podcast_obj = None
        for p in podcasts:
            if p.name == args.podcast:
                podcast_obj = p
                break
        
        if not podcast_obj:
            logger.error(f"Podcast not found: {args.podcast}")
            return
        
        # Convert to config dict
        podcast_config = {
            'title': podcast_obj.name,
            'slug': podcast_obj.slug,
            'rss_url': podcast_obj.rss_url,
            'site_url': podcast_obj.site_url,
            'resolver': podcast_obj.resolver,
            'episode_selector': podcast_obj.episode_selector,
            'transcript_selector': podcast_obj.transcript_selector,
            'config': podcast_obj.config or {}
        }
        
        result = discovery.discover_podcast_transcripts(podcast_config, args.max_episodes)
        
        print(f"\n✅ Results for {args.podcast}:")
        print(f"   Episodes checked: {result.episodes_checked}")
        print(f"   Transcripts found: {result.transcripts_found}")
        print(f"   Success rate: {result.success_rate:.1%}")
        print(f"   High-confidence: {result.high_confidence_transcripts}")
        print(f"   Total content: {result.total_content_length:,} characters")
        
        if result.transcript_sources:
            print("\n📄 Sample transcripts found:")
            for source in result.transcript_sources[:5]:
                print(f"   • {source['episode_title'][:60]}... (conf: {source['confidence']:.2f})")
    
    else:
        # Process all podcasts
        logger.info("Starting comprehensive transcript discovery...")
        
        results = discovery.discover_all_podcasts(
            max_episodes_per_podcast=args.max_episodes,
            priority_only=args.priority_only,
            resume_from=args.resume_from
        )
        
        # Generate and print report
        report = discovery.generate_report(results)
        print(report)
        
        # Save report to file
        report_file = discovery.data_dir / "transcript_discovery_report.md"
        with open(report_file, 'w') as f:
            f.write(report)
        
        logger.info(f"Report saved to: {report_file}")

if __name__ == "__main__":
    main()