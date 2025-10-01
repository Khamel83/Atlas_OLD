#!/usr/bin/env python3
"""
Quick Podcast Validator - Gets you the key metadata you need
"""

import xml.etree.ElementTree as ET
import feedparser
import csv
from datetime import datetime
from typing import Dict, List

def load_podcast_god() -> Dict:
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

def parse_opml(opml_path: str) -> List[Dict]:
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

def generate_podcast_id(podcast_name: str, rss_url: str) -> str:
    """Generate unique podcast ID"""
    import hashlib
    content = f"{podcast_name.lower().strip()}:{rss_url}"
    return hashlib.md5(content.encode()).hexdigest()[:12]

def match_podcasts():
    """Match requirements with OPML feeds quickly"""
    print("🔍 Quick Podcast Metadata Validation")

    # Load data
    requirements = load_podcast_god()
    feeds = parse_opml('podcast_opml.opml')

    print(f"📋 Requirements: {len(requirements)} podcasts")
    print(f"📡 OPML feeds: {len(feeds)} RSS feeds")

    results = []

    # Quick matching
    for podcast_name, req in requirements.items():
        # Find best match
        best_match = None
        best_score = 0

        for feed in feeds:
            name_lower = podcast_name.lower()
            feed_name_lower = feed['name'].lower()

            # Exact match
            if name_lower == feed_name_lower:
                score = 100
            # Contains match
            elif name_lower in feed_name_lower or feed_name_lower in name_lower:
                score = 80
            # Partial word match
            elif any(word in feed_name_lower for word in name_lower.split() if len(word) > 3):
                score = 60
            else:
                score = 0

            if score > best_score:
                best_score = score
                best_match = feed

        if best_match and best_score >= 60:
            podcast_id = generate_podcast_id(best_match['name'], best_match['rss_url'])

            result = {
                'podcast_name': podcast_name,
                'podcast_id': podcast_id,
                'rss_url': best_match['rss_url'],
                'feed_name': best_match['name'],
                'apple_id': best_match['apple_id'],
                'requested_count': req['requested_count'],
                'actual_count': 'PENDING',  # Will be updated when RSS is fetched
                'validation_status': 'MATCHED',
                'future': req['future'],
                'transcript_only': req['transcript_only'],
                'category': req['category'],
                'match_score': best_score
            }
            results.append(result)
            print(f"✅ {podcast_name} -> {best_match['name']} (score: {best_score})")
        else:
            result = {
                'podcast_name': podcast_name,
                'podcast_id': '',
                'rss_url': '',
                'feed_name': '',
                'apple_id': '',
                'requested_count': req['requested_count'],
                'actual_count': 'NOT_FOUND',
                'validation_status': 'MISSING',
                'future': req['future'],
                'transcript_only': req['transcript_only'],
                'category': req['category'],
                'match_score': 0
            }
            results.append(result)
            print(f"❌ {podcast_name} -> NOT FOUND")

    # Find new podcasts
    used_feeds = {r['rss_url'] for r in results if r['rss_url']}
    new_podcasts = []

    for feed in feeds:
        if feed['rss_url'] not in used_feeds:
            podcast_id = generate_podcast_id(feed['name'], feed['rss_url'])
            new_podcasts.append({
                'podcast_name': feed['name'],
                'podcast_id': podcast_id,
                'rss_url': feed['rss_url'],
                'feed_name': feed['name'],
                'apple_id': feed['apple_id'],
                'requested_count': 0,
                'actual_count': 'NEW',
                'validation_status': 'NEW',
                'future': False,
                'transcript_only': False,
                'category': 'NEW',
                'match_score': 100
            })

    print(f"\n🆕 New podcasts found: {len(new_podcasts)}")

    return results, new_podcasts

def create_export(results: List[Dict], new_podcasts: List[Dict]):
    """Create the export CSV"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'PODCAST_QUICK_EXPORT_{timestamp}.csv'

    fieldnames = [
        'podcast_name', 'podcast_id', 'rss_url', 'feed_name', 'validation_status',
        'requested_count', 'actual_count', 'future', 'transcript_only',
        'category', 'apple_id', 'match_score'
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Write matched podcasts
        for result in results:
            writer.writerow(result)

        # Write new podcasts
        for new_podcast in new_podcasts:
            writer.writerow(new_podcast)

    print(f"\n📄 Export created: {filename}")

    # Create summary
    matched = len([r for r in results if r['validation_status'] == 'MATCHED'])
    missing = len([r for r in results if r['validation_status'] == 'MISSING'])
    requested_total = sum(r['requested_count'] for r in results)

    summary = f"""
# PODCAST QUICK VALIDATION SUMMARY
Generated: {datetime.now().isoformat()}

## RESULTS
- Requirements Matched: {matched}/{len(results)} podcasts
- Missing from OPML: {missing} podcasts
- New Podcasts Found: {len(new_podcasts)}
- Total Requested Episodes: {requested_total:,}

## MATCHED PODCASTS ({matched})
"""

    matched_results = [r for r in results if r['validation_status'] == 'MATCHED']
    for result in sorted(matched_results, key=lambda x: x['requested_count'], reverse=True):
        summary += f"- {result['podcast_name']} (ID: {result['podcast_id']})\n"
        summary += f"  Requested: {result['requested_count']} | Feed: {result['feed_name']}\n"

    summary += f"\n## MISSING PODCASTS ({missing})\n"
    missing_results = [r for r in results if r['validation_status'] == 'MISSING']
    for result in missing_results:
        summary += f"- {result['podcast_name']}: {result['requested_count']} episodes requested\n"

    summary += f"\n## NEW PODCASTS ({len(new_podcasts)})\n"
    for new_podcast in new_podcasts[:10]:  # Show first 10
        summary += f"- {new_podcast['podcast_name']} (ID: {new_podcast['podcast_id']})\n"

    if len(new_podcasts) > 10:
        summary += f"... and {len(new_podcasts) - 10} more\n"

    summary_filename = f'PODCAST_QUICK_SUMMARY_{timestamp}.md'
    with open(summary_filename, 'w') as f:
        f.write(summary)

    print(f"📄 Summary created: {summary_filename}")
    print(f"\n🎯 VALIDATION COMPLETE:")
    print(f"✅ Matched: {matched} podcasts")
    print(f"❌ Missing: {missing} podcasts")
    print(f"🆕 New: {len(new_podcasts)} podcasts")
    print(f"📊 Total requested episodes: {requested_total:,}")

if __name__ == "__main__":
    results, new_podcasts = match_podcasts()
    create_export(results, new_podcasts)