#!/usr/bin/env python3
"""
Podcast Metadata Validator and Export System
Validates RSS metadata against PODCAST_GOD.CSV requirements
Creates export with real episode counts and unique IDs
"""

import xml.etree.ElementTree as ET
import feedparser
import asyncio
import aiohttp
import aiosqlite
import hashlib
import json
import csv
from datetime import datetime
from typing import Dict, List, Optional, Set
import sys

sys.path.append('.')

from modules.database import DatabaseManager

class PodcastMetadataValidator:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
            headers={'User-Agent': 'Mozilla/5.0 (compatible; Atlas-Podcast-Validator/1.0)'}
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    def load_podcast_god(self) -> Dict:
        """Load PODCAST_GOD.CSV requirements"""
        requirements = {}

        with open('PODCAST_GOD.CSV', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Exclude'] == '1':
                    continue

                count = int(row['Count'])
                if count == 0:
                    continue

                requirements[row['Podcast Name'].strip('"')] = {
                    'requested_count': count,
                    'future': row['Future'] == '1',
                    'transcript_only': row['Trasncript_Only'] == '1',
                    'category': row['Category']
                }

        return requirements

    def parse_opml(self, opml_path: str) -> List[Dict]:
        """Parse OPML file and extract RSS feeds"""
        feeds = []

        tree = ET.parse(opml_path)
        root = tree.getroot()

        for outline in root.findall('.//outline[@type="rss"]'):
            feed = {
                'name': outline.get('text', '').strip(),
                'rss_url': outline.get('xmlUrl', ''),
                'apple_id': outline.get('applePodcastsID', ''),
            }
            if feed['rss_url'] and feed['name']:
                feeds.append(feed)

        return feeds

    def generate_podcast_id(self, podcast_name: str, rss_url: str) -> str:
        """Generate unique podcast ID"""
        content = f"{podcast_name.lower().strip()}:{rss_url}"
        return hashlib.md5(content.encode()).hexdigest()[:12]

    def generate_episode_id(self, podcast_id: str, episode_title: str, episode_url: str) -> str:
        """Generate unique episode ID that tracks back to podcast"""
        content = f"{podcast_id}:{episode_title.lower().strip()}:{episode_url}"
        return hashlib.md5(content.encode()).hexdigest()[:16]

    async def fetch_rss_metadata(self, rss_url: str) -> Optional[Dict]:
        """Fetch RSS metadata without downloading all episodes"""
        try:
            if not self.session:
                return None

            async with self.session.get(rss_url) as response:
                if response.status != 200:
                    return None

                content = await response.text()
                feed = feedparser.parse(content)

                if not feed.get('entries'):
                    return None

                # Extract key metadata
                total_episodes = len(feed.entries)

                # Get feed info
                feed_info = {
                    'title': feed.feed.get('title', ''),
                    'description': feed.feed.get('description', ''),
                    'total_episodes': total_episodes,
                    'latest_episode': None,
                    'oldest_episode': None
                }

                # Get episode date range
                if feed.entries:
                    dates = []
                    for entry in feed.entries:
                        pub_date = entry.get('published', entry.get('updated'))
                        if pub_date:
                            dates.append(pub_date)

                    if dates:
                        dates.sort()
                        feed_info['oldest_episode'] = dates[0]
                        feed_info['latest_episode'] = dates[-1]

                return feed_info

        except Exception as e:
            return None

    async def validate_all_podcasts(self, opml_path: str) -> Dict:
        """Validate all podcasts against requirements"""
        print("🔍 Validating podcast metadata...")

        # Load requirements
        requirements = self.load_podcast_god()
        print(f"📋 PODCAST_GOD requirements: {len(requirements)} podcasts")

        # Parse OPML
        feeds = self.parse_opml(opml_path)
        print(f"📡 OPML feeds found: {len(feeds)} RSS feeds")

        results = {
            'matched_podcasts': [],
            'new_podcasts': [],
            'missing_podcasts': [],
            'validation_errors': [],
            'summary': {}
        }

        processed_feeds = set()

        # Match requirements with OPML feeds
        for podcast_name, req in requirements.items():
            print(f"\n🔍 Validating: {podcast_name}")

            # Find matching feed
            matching_feed = None
            best_match_score = 0

            for feed in feeds:
                # Simple name matching
                name_lower = podcast_name.lower()
                feed_name_lower = feed['name'].lower()

                if name_lower == feed_name_lower:
                    match_score = 100
                elif name_lower in feed_name_lower or feed_name_lower in name_lower:
                    match_score = 80
                elif any(word in feed_name_lower for word in name_lower.split() if len(word) > 3):
                    match_score = 60
                else:
                    match_score = 0

                if match_score > best_match_score:
                    best_match_score = match_score
                    matching_feed = feed

            if matching_feed and best_match_score >= 60:
                # Get metadata
                metadata = await self.fetch_rss_metadata(matching_feed['rss_url'])

                if metadata:
                    podcast_id = self.generate_podcast_id(matching_feed['name'], matching_feed['rss_url'])

                    validation_result = {
                        'podcast_name': podcast_name,
                        'podcast_id': podcast_id,
                        'rss_url': matching_feed['rss_url'],
                        'feed_name': matching_feed['name'],
                        'match_score': best_match_score,
                        'requested_count': req['requested_count'],
                        'actual_count': metadata['total_episodes'],
                        'available_count': metadata['total_episodes'],
                        'future': req['future'],
                        'transcript_only': req['transcript_only'],
                        'category': req['category'],
                        'apple_id': matching_feed['apple_id'],
                        'validation_status': 'VALID' if metadata['total_episodes'] > 0 else 'NO_EPISODES',
                        'latest_episode': metadata['latest_episode'],
                        'oldest_episode': metadata['oldest_episode'],
                        'feed_title': metadata['title'],
                        'processable_count': min(req['requested_count'], metadata['total_episodes'])
                    }

                    results['matched_podcasts'].append(validation_result)
                    processed_feeds.add(matching_feed['rss_url'])

                    print(f"✅ {podcast_name}: {metadata['total_episodes']} episodes (requested: {req['requested_count']})")
                else:
                    results['validation_errors'].append({
                        'podcast_name': podcast_name,
                        'error': 'Failed to fetch RSS metadata',
                        'rss_url': matching_feed['rss_url']
                    })
                    print(f"❌ {podcast_name}: Failed to fetch metadata")
            else:
                results['missing_podcasts'].append({
                    'podcast_name': podcast_name,
                    'requested_count': req['requested_count'],
                    'error': 'No matching RSS feed found'
                })
                print(f"❌ {podcast_name}: No matching RSS feed")

        # Find new podcasts in OPML
        for feed in feeds:
            if feed['rss_url'] not in processed_feeds:
                metadata = await self.fetch_rss_metadata(feed['rss_url'])
                if metadata:
                    podcast_id = self.generate_podcast_id(feed['name'], feed['rss_url'])

                    new_podcast = {
                        'podcast_name': feed['name'],
                        'podcast_id': podcast_id,
                        'rss_url': feed['rss_url'],
                        'apple_id': feed['apple_id'],
                        'actual_count': metadata['total_episodes'],
                        'available_count': metadata['total_episodes'],
                        'validation_status': 'NEW',
                        'latest_episode': metadata['latest_episode'],
                        'oldest_episode': metadata['oldest_episode'],
                        'feed_title': metadata['title'],
                        'category': 'Unknown',
                        'future': False,
                        'transcript_only': False,
                        'processable_count': metadata['total_episodes']
                    }

                    results['new_podcasts'].append(new_podcast)

        # Create summary
        results['summary'] = {
            'total_requirements': len(requirements),
            'matched_count': len(results['matched_podcasts']),
            'new_count': len(results['new_podcasts']),
            'missing_count': len(results['missing_podcasts']),
            'error_count': len(results['validation_errors']),
            'total_requested_episodes': sum(req['requested_count'] for req in requirements.values()),
            'total_available_episodes': sum(p['actual_count'] for p in results['matched_podcasts']),
            'total_processable_episodes': sum(p['processable_count'] for p in results['matched_podcasts'])
        }

        return results

    def create_export_csv(self, results: Dict, filename: str):
        """Create comprehensive export CSV"""
        print(f"\n📄 Creating export: {filename}")

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'podcast_name', 'podcast_id', 'rss_url', 'feed_name', 'validation_status',
                'requested_count', 'actual_count', 'processable_count', 'available_count',
                'future', 'transcript_only', 'category', 'apple_id',
                'latest_episode', 'oldest_episode', 'feed_title', 'match_score'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Write matched podcasts
            for podcast in results['matched_podcasts']:
                writer.writerow(podcast)

            # Write new podcasts (with default values for missing fields)
            for podcast in results['new_podcasts']:
                row = {field: '' for field in fieldnames}
                row.update(podcast)
                writer.writerow(row)

        print(f"✅ Export created: {filename}")

    def create_summary_report(self, results: Dict, filename: str):
        """Create summary report"""
        summary = results['summary']

        report = f"""
# PODCAST METADATA VALIDATION REPORT
Generated: {datetime.now().isoformat()}

## SUMMARY
- Total Requirements: {summary['total_requirements']} podcasts
- Matched Successfully: {summary['matched_count']} podcasts
- New Podcasts Found: {summary['new_count']} podcasts
- Missing from OPML: {summary['missing_count']} podcasts
- Validation Errors: {summary['error_count']} podcasts

## EPISODE COUNTS
- Requested Episodes: {summary['total_requested_episodes']:,}
- Available Episodes: {summary['total_available_episodes']:,}
- Processable Episodes: {summary['total_processable_episodes']:,}
- Coverage: {(summary['total_processable_episodes']/summary['total_requested_episodes']*100):.1f}%

## TOP PODCASTS BY EPISODE COUNT
"""

        # Sort matched podcasts by actual count
        top_podcasts = sorted(results['matched_podcasts'], key=lambda x: x['actual_count'], reverse=True)[:10]
        for i, podcast in enumerate(top_podcasts, 1):
            report += f"{i}. {podcast['podcast_name']}: {podcast['actual_count']:,} episodes\n"

        report += "\n## NEW PODCASTS DISCOVERED\n"
        for podcast in results['new_podcasts'][:10]:
            report += f"- {podcast['podcast_name']}: {podcast['actual_count']:,} episodes\n"

        if len(results['new_podcasts']) > 10:
            report += f"... and {len(results['new_podcasts']) - 10} more\n"

        report += "\n## MISSING PODCASTS\n"
        for podcast in results['missing_podcasts']:
            report += f"- {podcast['podcast_name']}: {podcast['requested_count']} episodes requested\n"

        with open(filename, 'w') as f:
            f.write(report)

        print(f"✅ Summary report created: {filename}")

async def main():
    """Main validation function"""
    db_manager = DatabaseManager()
    await db_manager.initialize()

    async with PodcastMetadataValidator(db_manager) as validator:
        # Validate all podcasts
        results = await validator.validate_all_podcasts('podcast_opml.opml')

        # Create exports
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        validator.create_export_csv(results, f'PODCAST_VALIDATION_EXPORT_{timestamp}.csv')
        validator.create_summary_report(results, f'PODCAST_VALIDATION_SUMMARY_{timestamp}.md')

        # Print summary
        summary = results['summary']
        print(f"\n🎯 VALIDATION COMPLETE:")
        print(f"📊 Matched: {summary['matched_count']}/{summary['total_requirements']} podcasts")
        print(f"🆕 New: {summary['new_count']} podcasts")
        print(f"❌ Missing: {summary['missing_count']} podcasts")
        print(f"📈 Processable episodes: {summary['total_processable_episodes']:,}/{summary['total_requested_episodes']:,}")

    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(main())