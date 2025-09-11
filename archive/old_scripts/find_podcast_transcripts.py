#!/usr/bin/env python3
"""
Find podcast transcripts from the web for user's podcast subscriptions
"""

import xml.etree.ElementTree as ET
import requests
import sqlite3
import re
import time
import json
from pathlib import Path
from datetime import datetime

# Known transcript sources and patterns
TRANSCRIPT_SOURCES = {
    "lex-fridman": {
        "patterns": ["lexfridman.com"],
        "transcript_url_pattern": "https://lexfridman.com/{episode_id}/",
        "method": "direct"
    },
    "conversations-with-tyler": {
        "patterns": ["cowenconvos.libsyn.com", "conversationswithtyler.com"],
        "transcript_url_pattern": "https://conversationswithtyler.com/episodes/{slug}/",
        "method": "web_scraping"
    },
    "this-american-life": {
        "patterns": ["thisamericanlife.org"],
        "transcript_url_pattern": "https://www.thisamericanlife.org/transcript/{episode}",
        "method": "direct"
    },
    "freakonomics": {
        "patterns": ["freakonomics.com"],
        "method": "check_website"
    },
    "econtalk": {
        "patterns": ["econtalk.org", "econtalklibrary.org"],
        "method": "direct"
    },
    "planet-money": {
        "patterns": ["npr.org/510289"],
        "method": "npr_transcripts"
    },
    "the-indicator": {
        "patterns": ["npr.org/510325"],
        "method": "npr_transcripts"
    }
}

def parse_opml(opml_file):
    """Parse OPML file and extract podcast feeds"""
    podcasts = []
    
    try:
        tree = ET.parse(opml_file)
        root = tree.getroot()
        
        for outline in root.findall(".//outline[@type='rss']"):
            podcast = {
                'title': outline.get('text', 'Unknown'),
                'feed_url': outline.get('xmlUrl', ''),
                'apple_id': outline.get('applePodcastsID', ''),
                'transcript_status': 'unknown'
            }
            podcasts.append(podcast)
            
    except Exception as e:
        print(f"❌ Error parsing OPML: {e}")
        
    return podcasts

def check_transcript_availability(podcast):
    """Check if transcripts are available for a podcast"""
    
    title = podcast['title'].lower()
    feed_url = podcast['feed_url'].lower()
    
    # Check against known transcript sources
    for source_key, source_info in TRANSCRIPT_SOURCES.items():
        for pattern in source_info['patterns']:
            if pattern in feed_url or pattern in title:
                return {
                    'has_transcripts': True,
                    'source': source_key,
                    'method': source_info['method'],
                    'confidence': 'high'
                }
    
    # Check for common transcript indicators in title/URL
    transcript_indicators = [
        'transcript', 'text', 'readable', 'written'
    ]
    
    for indicator in transcript_indicators:
        if indicator in title:
            return {
                'has_transcripts': True, 
                'source': 'inferred',
                'method': 'unknown',
                'confidence': 'medium'
            }
    
    # High-probability shows that often have transcripts
    high_prob_shows = [
        'this american life', 'freakonomics', 'radiolab', 'planet money',
        'hidden brain', 'invisibilia', 'on the media', 'throughline',
        'the indicator', 'pop culture happy hour', 'wait wait',
        'lex fridman', 'conversations with tyler', 'econtalk',
        'the ezra klein show', 'hard fork', 'on with kara swisher'
    ]
    
    for show in high_prob_shows:
        if show in title:
            return {
                'has_transcripts': True,
                'source': 'high_probability',
                'method': 'web_search_required',
                'confidence': 'medium'
            }
    
    return {
        'has_transcripts': False,
        'source': None,
        'method': None,
        'confidence': 'low'
    }

def prioritize_podcasts(podcasts_with_transcripts):
    """Sort podcasts by transcript likelihood"""
    
    def priority_score(podcast):
        info = podcast['transcript_info']
        if info['confidence'] == 'high':
            return 3
        elif info['confidence'] == 'medium':
            return 2
        else:
            return 1
    
    return sorted(podcasts_with_transcripts, key=priority_score, reverse=True)

def save_transcript_analysis(podcasts, output_file):
    """Save analysis results to file"""
    
    analysis = {
        'total_podcasts': len(podcasts),
        'has_transcripts': len([p for p in podcasts if p['transcript_info']['has_transcripts']]),
        'high_confidence': len([p for p in podcasts if p['transcript_info']['confidence'] == 'high']),
        'analysis_date': datetime.now().isoformat(),
        'podcasts': podcasts
    }
    
    with open(output_file, 'w') as f:
        json.dump(analysis, f, indent=2)
    
    return analysis

def main():
    """Main function to find podcast transcripts"""
    
    print("🎙️ Atlas Podcast Transcript Finder")
    print("=" * 50)
    
    # Parse OPML file
    opml_file = "inputs/podcasts.opml"
    if not Path(opml_file).exists():
        print(f"❌ OPML file not found: {opml_file}")
        return False
    
    print(f"📖 Parsing podcast subscriptions...")
    podcasts = parse_opml(opml_file)
    print(f"✅ Found {len(podcasts)} podcast subscriptions")
    
    # Check transcript availability
    print(f"\n🔍 Analyzing transcript availability...")
    podcasts_with_info = []
    
    for i, podcast in enumerate(podcasts, 1):
        if i % 20 == 0:
            print(f"   Progress: {i}/{len(podcasts)}")
        
        transcript_info = check_transcript_availability(podcast)
        podcast['transcript_info'] = transcript_info
        podcasts_with_info.append(podcast)
    
    # Prioritize and analyze
    prioritized = prioritize_podcasts(podcasts_with_info)
    
    # Save results
    output_file = "podcast_transcript_analysis.json"
    analysis = save_transcript_analysis(prioritized, output_file)
    
    # Print summary
    print(f"\n🎯 TRANSCRIPT ANALYSIS RESULTS")
    print(f"=" * 50)
    print(f"📊 Total podcasts: {analysis['total_podcasts']}")
    print(f"✅ Likely have transcripts: {analysis['has_transcripts']}")
    print(f"🔥 High confidence: {analysis['high_confidence']}")
    print(f"📄 Analysis saved: {output_file}")
    
    # Show top candidates
    high_confidence = [p for p in prioritized if p['transcript_info']['confidence'] == 'high']
    
    if high_confidence:
        print(f"\n🌟 HIGH CONFIDENCE TRANSCRIPT SOURCES:")
        for podcast in high_confidence[:10]:  # Top 10
            source = podcast['transcript_info']['source']
            print(f"  ✅ {podcast['title'][:50]}... ({source})")
    
    medium_confidence = [p for p in prioritized if p['transcript_info']['confidence'] == 'medium']
    
    if medium_confidence:
        print(f"\n💡 MEDIUM CONFIDENCE (needs verification):")
        for podcast in medium_confidence[:10]:  # Top 10
            print(f"  ⚠️ {podcast['title'][:50]}...")
    
    print(f"\n🚀 Next steps:")
    print(f"   1. Process high-confidence podcasts first")
    print(f"   2. Web-search for medium-confidence transcripts")  
    print(f"   3. Consider transcript generation for remainder")
    
    return analysis['has_transcripts'] > 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)