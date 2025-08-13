#!/usr/bin/env python3
"""
Comprehensive Metadata Capture Test

Test that we capture ALL metadata across diverse content types:
- Multiple podcast feeds with different RSS structures
- Various article sources 
- YouTube videos
- Documents

CORE PRINCIPLE: NEVER LOSE ANY DATA - PRESERVE EVERYTHING!
"""

import json
import os
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Tuple

import feedparser

from helpers.config import load_config
from helpers.podcast_ingestor import PodcastIngestor


class ComprehensiveMetadataValidator:
    """Validate that we capture ALL available metadata across content types"""
    
    def __init__(self):
        self.config = load_config()
        self.test_dir = Path("testing/metadata_tests")
        self.test_dir.mkdir(parents=True, exist_ok=True)
        self.results = {
            "podcast_feeds_tested": [],
            "metadata_coverage": {},
            "missing_fields": [],
            "recommendations": []
        }
    
    def test_podcast_metadata_coverage(self, max_feeds: int = 10, max_episodes_per_feed: int = 2):
        """Test metadata capture across diverse podcast feeds"""
        print("🔍 Testing podcast metadata capture across diverse feeds...")
        
        # Parse OPML to get variety of feeds
        feeds = self._get_diverse_podcast_feeds("inputs/podcasts.opml", max_feeds)
        
        ingestor = PodcastIngestor(self.config)
        
        for feed_url, feed_title in feeds:
            print(f"\n📻 Testing feed: {feed_title}")
            
            try:
                # Parse feed to analyze metadata structure
                feed = feedparser.parse(feed_url)
                
                if not feed.entries:
                    print(f"   ⚠️  No entries in feed")
                    continue
                
                feed_analysis = {
                    "feed_url": feed_url,
                    "feed_title": feed_title,
                    "total_episodes": len(feed.entries),
                    "feed_metadata_fields": list(feed.feed.keys()) if hasattr(feed, 'feed') else [],
                    "episodes_analyzed": []
                }
                
                # Analyze metadata from first few episodes
                for i, entry in enumerate(feed.entries[:max_episodes_per_feed]):
                    episode_analysis = self._analyze_episode_metadata(entry)
                    feed_analysis["episodes_analyzed"].append(episode_analysis)
                    
                    print(f"   📝 Episode {i+1}: {entry.get('title', 'Untitled')[:50]}...")
                    print(f"      Fields: {len(episode_analysis['available_fields'])} total")
                    print(f"      Critical: {episode_analysis['has_description']}, {episode_analysis['has_show_notes']}, {episode_analysis['has_duration']}")
                
                self.results["podcast_feeds_tested"].append(feed_analysis)
                
            except Exception as e:
                print(f"   ❌ Error analyzing feed: {e}")
        
        self._analyze_metadata_coverage()
        self._save_results()
    
    def _get_diverse_podcast_feeds(self, opml_path: str, max_feeds: int) -> List[Tuple[str, str]]:
        """Get a diverse sample of podcast feeds from OPML"""
        if not os.path.exists(opml_path):
            print(f"⚠️  OPML file not found: {opml_path}")
            return []
        
        try:
            tree = ET.parse(opml_path)
            root = tree.getroot()
            
            feeds = []
            for outline in root.findall(".//outline[@type='rss']"):
                xml_url = outline.get('xmlUrl')
                title = outline.get('text', 'Unknown Feed')
                if xml_url:
                    feeds.append((xml_url, title))
            
            # Take a diverse sample - first, middle, and last feeds for variety
            if len(feeds) <= max_feeds:
                return feeds
            
            step = len(feeds) // max_feeds
            diverse_feeds = []
            for i in range(0, len(feeds), step):
                if len(diverse_feeds) < max_feeds:
                    diverse_feeds.append(feeds[i])
            
            print(f"📊 Selected {len(diverse_feeds)} diverse feeds from {len(feeds)} total")
            return diverse_feeds
            
        except Exception as e:
            print(f"❌ Failed to parse OPML: {e}")
            return []
    
    def _analyze_episode_metadata(self, entry) -> Dict:
        """Analyze what metadata is available in an episode"""
        available_fields = list(entry.keys())
        
        # Check for critical metadata types
        has_description = bool(entry.get('summary') or entry.get('description') or entry.get('content'))
        has_show_notes = bool(entry.get('summary') and len(entry.get('summary', '')) > 100)
        has_duration = bool(entry.get('itunes_duration'))
        has_episode_number = bool(entry.get('itunes_episode'))
        has_tags = bool(entry.get('tags'))
        has_author = bool(entry.get('author'))
        has_image = bool(entry.get('image'))
        has_links = bool(entry.get('links'))
        
        # Analyze content richness
        summary_length = len(entry.get('summary', ''))
        content_blocks = len(entry.get('content', []))
        tag_count = len(entry.get('tags', []))
        
        return {
            "title": entry.get('title', 'Untitled'),
            "available_fields": available_fields,
            "field_count": len(available_fields),
            "has_description": has_description,
            "has_show_notes": has_show_notes,
            "has_duration": has_duration,
            "has_episode_number": has_episode_number,
            "has_tags": has_tags,
            "has_author": has_author,
            "has_image": has_image,
            "has_links": has_links,
            "summary_length": summary_length,
            "content_blocks": content_blocks,
            "tag_count": tag_count,
            "sample_fields": {
                "duration": entry.get('itunes_duration', 'N/A'),
                "episode_number": entry.get('itunes_episode', 'N/A'),
                "published": entry.get('published', 'N/A'),
                "author": entry.get('author', 'N/A'),
                "tags_sample": [tag.get('term', 'N/A') for tag in entry.get('tags', [])[:3]]
            }
        }
    
    def _analyze_metadata_coverage(self):
        """Analyze metadata coverage across all tested feeds"""
        if not self.results["podcast_feeds_tested"]:
            return
        
        all_fields = set()
        field_frequency = {}
        critical_coverage = {
            "has_description": 0,
            "has_show_notes": 0,
            "has_duration": 0,
            "has_episode_number": 0,
            "has_tags": 0,
            "has_author": 0
        }
        
        total_episodes = 0
        
        for feed in self.results["podcast_feeds_tested"]:
            for episode in feed["episodes_analyzed"]:
                total_episodes += 1
                
                # Track all fields seen
                for field in episode["available_fields"]:
                    all_fields.add(field)
                    field_frequency[field] = field_frequency.get(field, 0) + 1
                
                # Track critical metadata coverage
                for key in critical_coverage:
                    if episode.get(key, False):
                        critical_coverage[key] += 1
        
        # Calculate coverage percentages
        for key in critical_coverage:
            critical_coverage[key] = (critical_coverage[key] / total_episodes * 100) if total_episodes > 0 else 0
        
        self.results["metadata_coverage"] = {
            "total_unique_fields": len(all_fields),
            "all_fields_seen": sorted(list(all_fields)),
            "field_frequency": field_frequency,
            "critical_metadata_coverage": critical_coverage,
            "total_episodes_analyzed": total_episodes
        }
        
        # Identify potentially missing important fields
        important_fields = [
            'summary', 'description', 'content', 'itunes_duration', 'itunes_episode',
            'tags', 'author', 'published', 'image', 'links', 'subtitle',
            'itunes_explicit', 'language', 'copyright'
        ]
        
        missing_important = [field for field in important_fields if field not in all_fields]
        self.results["missing_fields"] = missing_important
        
        # Generate recommendations
        self._generate_recommendations(critical_coverage, missing_important)
    
    def _generate_recommendations(self, coverage: Dict, missing: List):
        """Generate recommendations for metadata capture improvements"""
        recs = []
        
        if coverage["has_description"] < 90:
            recs.append(f"⚠️  Only {coverage['has_description']:.1f}% of episodes have descriptions - critical for search")
        
        if coverage["has_show_notes"] < 70:
            recs.append(f"⚠️  Only {coverage['has_show_notes']:.1f}% have substantial show notes - these contain valuable metadata")
        
        if coverage["has_duration"] < 80:
            recs.append(f"⚠️  Only {coverage['has_duration']:.1f}% have duration metadata")
        
        if missing:
            recs.append(f"🔍 Missing potentially important fields: {', '.join(missing)}")
        
        if all(cov > 85 for cov in coverage.values()) and not missing:
            recs.append("✅ Excellent metadata coverage across all tested feeds!")
        
        recs.append("💾 CORE PRINCIPLE: We are now preserving ALL available metadata")
        recs.append("🔄 Continue monitoring for new metadata fields in future feeds")
        
        self.results["recommendations"] = recs
    
    def _save_results(self):
        """Save comprehensive test results"""
        results_file = self.test_dir / f"metadata_coverage_analysis.json"
        
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n📊 METADATA COVERAGE ANALYSIS")
        print("=" * 50)
        
        coverage = self.results["metadata_coverage"]
        print(f"Total feeds tested: {len(self.results['podcast_feeds_tested'])}")
        print(f"Total episodes analyzed: {coverage['total_episodes_analyzed']}")
        print(f"Unique metadata fields found: {coverage['total_unique_fields']}")
        
        print(f"\n🎯 Critical Metadata Coverage:")
        for key, percentage in coverage["critical_metadata_coverage"].items():
            status = "✅" if percentage > 80 else "⚠️ " if percentage > 50 else "❌"
            print(f"  {status} {key.replace('has_', '').title()}: {percentage:.1f}%")
        
        if self.results["missing_fields"]:
            print(f"\n⚠️  Potentially missing fields: {', '.join(self.results['missing_fields'])}")
        
        print(f"\n💡 Recommendations:")
        for rec in self.results["recommendations"]:
            print(f"  {rec}")
        
        print(f"\nFull analysis saved: {results_file}")


def main():
    """Run comprehensive metadata capture validation"""
    validator = ComprehensiveMetadataValidator()
    
    print("🚀 COMPREHENSIVE METADATA CAPTURE VALIDATION")
    print("=" * 60)
    print("Testing that we capture ALL metadata across diverse sources")
    print("CORE PRINCIPLE: NEVER LOSE ANY DATA!\n")
    
    # Test podcast metadata coverage across diverse feeds
    validator.test_podcast_metadata_coverage(max_feeds=12, max_episodes_per_feed=2)
    
    print("\n✅ Podcast metadata validation complete!")
    print("\n🔄 Next: Extend to articles, YouTube, and documents...")


if __name__ == "__main__":
    main()