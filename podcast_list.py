#!/usr/bin/env python3
"""
Parse OPML and extract podcast list for review
"""

import xml.etree.ElementTree as ET
import html

def parse_podcasts():
    """Parse podcasts from OPML file"""
    tree = ET.parse('/home/ubuntu/dev/atlas/inputs/podcasts.opml')
    root = tree.getroot()
    
    podcasts = []
    for outline in root.findall('.//outline[@type="rss"]'):
        title = outline.get('text', 'Unknown')
        xml_url = outline.get('xmlUrl', '')
        apple_id = outline.get('applePodcastsID', '')
        
        # Clean up HTML entities
        title = html.unescape(title)
        
        podcasts.append({
            'title': title,
            'feed_url': xml_url,
            'apple_id': apple_id
        })
    
    return sorted(podcasts, key=lambda x: x['title'])

def categorize_podcasts(podcasts):
    """Categorize podcasts for easier review"""
    categories = {
        'News & Politics': [],
        'Tech & Business': [],
        'Sports': [],
        'Finance & Economics': [],
        'Culture & Entertainment': [],
        'Science & Education': [],
        'Food': [],
        'Other': []
    }
    
    keywords = {
        'News & Politics': ['news', 'politics', 'political', 'npr', 'today', 'daily', 'frontline'],
        'Tech & Business': ['tech', 'ai', 'startup', 'business', 'verge', 'decoder', 'acquired'],
        'Sports': ['nfl', 'nba', 'sports', 'bears', 'basketball', 'football'],
        'Finance & Economics': ['money', 'economic', 'finance', 'market', 'planet money', 'bloomberg'],
        'Culture & Entertainment': ['culture', 'film', 'movie', 'tv', 'prestige', 'rewatchables'],
        'Science & Education': ['science', 'brain', 'invisible', 'radiolab', 'explained'],
        'Food': ['food', 'recipe', 'kitchen', 'cook']
    }
    
    for podcast in podcasts:
        title_lower = podcast['title'].lower()
        categorized = False
        
        for category, terms in keywords.items():
            if any(term in title_lower for term in terms):
                categories[category].append(podcast)
                categorized = True
                break
        
        if not categorized:
            categories['Other'].append(podcast)
    
    return categories

def main():
    podcasts = parse_podcasts()
    categories = categorize_podcasts(podcasts)
    
    print("🎧 YOUR PODCAST COLLECTION ANALYSIS")
    print("=" * 50)
    print(f"📊 Total Podcasts: {len(podcasts)}")
    print()
    
    for category, podcast_list in categories.items():
        if podcast_list:
            print(f"📂 {category} ({len(podcast_list)})")
            print("-" * 30)
            for i, podcast in enumerate(podcast_list, 1):
                print(f"  {i:2d}. {podcast['title']}")
            print()
    
    # Top recommendations for processing
    high_value_podcasts = [
        'This American Life', 'Radiolab', 'Planet Money', 'The Ezra Klein Show',
        'Conversations with Tyler', 'EconTalk', 'Acquired', 'Hard Fork',
        'The Journal.', 'Making Sense with Sam Harris', 'Lex Fridman Podcast',
        'All-In with Chamath, Jason, Sacks & Friedberg', 'The Knowledge Project with Shane Parrish'
    ]
    
    found_high_value = []
    for podcast in podcasts:
        if podcast['title'] in high_value_podcasts:
            found_high_value.append(podcast)
    
    print("🌟 RECOMMENDED HIGH-VALUE PODCASTS FOR PROCESSING")
    print("=" * 55)
    print("(Based on content quality and cognitive value)")
    print()
    for i, podcast in enumerate(found_high_value, 1):
        print(f"  {i:2d}. {podcast['title']}")
    
    print(f"\n💡 RECOMMENDATION:")
    print(f"   Start with 5-10 high-value podcasts")
    print(f"   Process last 10-20 episodes each")
    print(f"   Focus on evergreen content over news")

if __name__ == "__main__":
    main()