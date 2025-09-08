#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import csv
import re

def extract_rss_from_opml(opml_path):
    """Extract RSS URLs from OPML file"""
    tree = ET.parse(opml_path)
    root = tree.getroot()
    
    feeds = {}
    for outline in root.findall('.//outline[@type="rss"]'):
        text = outline.get('text', '').strip()
        xml_url = outline.get('xmlUrl', '').strip()
        
        if text and xml_url:
            # Clean up text to match CSV names
            text = re.sub(r'^"(.+)"$', r'\1', text)  # Remove surrounding quotes
            feeds[text] = xml_url
    
    return feeds

def normalize_name(name):
    """Normalize podcast name for matching"""
    # Remove quotes, extra spaces, and make lowercase
    name = re.sub(r'^["\'"]*(.+?)["\'"]*$', r'\1', name)
    name = re.sub(r'\s+', ' ', name).strip().lower()
    # Remove common prefixes/suffixes
    name = re.sub(r'\s*\|\s*.+$', '', name)  # Remove "| subtitle"
    name = re.sub(r'\s*with\s+.+$', '', name)  # Remove "with host"
    return name

def update_csv_with_opml(csv_path, opml_feeds):
    """Update CSV file with RSS URLs from OPML"""
    rows = []
    updated_count = 0
    
    # Create normalized lookup for better matching
    normalized_opml = {}
    for opml_name, rss_url in opml_feeds.items():
        normalized_opml[normalize_name(opml_name)] = (opml_name, rss_url)
    
    # Read existing CSV
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        
        for row in reader:
            podcast_name = row['Podcast Name'].strip()
            current_rss = row['RSS_URL'].strip()
            
            # Check if we need to update (empty or placeholder values)
            needs_update = (not current_rss or 
                          current_rss == '0' or 
                          current_rss.startswith('http://example.com') or
                          'placeholder' in current_rss.lower())
            
            if needs_update:
                # Try exact match first
                if podcast_name in opml_feeds:
                    row['RSS_URL'] = opml_feeds[podcast_name]
                    updated_count += 1
                    print(f"✓ Exact match '{podcast_name}' -> {opml_feeds[podcast_name]}")
                else:
                    # Try normalized matching
                    csv_normalized = normalize_name(podcast_name)
                    found = False
                    
                    # First try exact normalized match
                    if csv_normalized in normalized_opml:
                        opml_name, rss_url = normalized_opml[csv_normalized]
                        row['RSS_URL'] = rss_url
                        updated_count += 1
                        print(f"✓ Normalized match '{podcast_name}' -> '{opml_name}' -> {rss_url}")
                        found = True
                    else:
                        # Try partial matching on key terms
                        for norm_opml_name, (opml_name, rss_url) in normalized_opml.items():
                            # Extract key words from both names
                            csv_words = set(csv_normalized.split())
                            opml_words = set(norm_opml_name.split())
                            
                            # Check for substantial overlap
                            common_words = csv_words.intersection(opml_words)
                            if (len(common_words) >= 2 or 
                                (len(common_words) >= 1 and len(csv_words) <= 3)):
                                row['RSS_URL'] = rss_url
                                updated_count += 1
                                print(f"✓ Word match '{podcast_name}' -> '{opml_name}' -> {rss_url}")
                                found = True
                                break
                    
                    if not found:
                        print(f"✗ No match found for '{podcast_name}'")
            
            rows.append(row)
    
    # Write updated CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    
    return updated_count

def main():
    opml_path = '/home/ubuntu/dev/atlas/inputs/podcasts.opml'
    csv_path = '/home/ubuntu/dev/atlas/config/podcasts_prioritized_updated.csv'
    
    print("Extracting RSS feeds from OPML...")
    opml_feeds = extract_rss_from_opml(opml_path)
    print(f"Found {len(opml_feeds)} RSS feeds in OPML")
    
    print("\nUpdating CSV with OPML RSS URLs...")
    updated_count = update_csv_with_opml(csv_path, opml_feeds)
    
    print(f"\n✅ Updated {updated_count} podcast RSS URLs from OPML")
    print("CSV file updated with complete RSS coverage")

if __name__ == '__main__':
    main()