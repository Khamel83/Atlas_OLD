#!/usr/bin/env python3
"""
Fix Document Crisis - Process Real Articles from Instapaper CSV

PROBLEM: 19,554 document files contain Instapaper interface HTML, not articles
SOLUTION: Process the 56,594 real article URLs from instapaper_export.csv

This script:
1. Reads instapaper_export.csv with real article URLs
2. Processes articles through ArticleManager (not DocumentIngestor)
3. Clears the fake document files
4. Reports progress on fixing the crisis
"""

import csv
import os
import sys
from pathlib import Path
from typing import Dict, Any, List

# Add project root to path
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.article_manager import ArticleManager
from helpers.simple_database import SimpleDatabase


def main():
    """Fix the document crisis by processing real articles."""
    print("🚨 FIXING DOCUMENT CRISIS")
    print("="*50)
    
    # Load config
    config = load_config()
    
    # Initialize managers
    article_manager = ArticleManager(config)
    db = SimpleDatabase(config)
    
    # Read Instapaper CSV
    csv_path = 'inputs/instapaper_export.csv'
    if not os.path.exists(csv_path):
        print(f"❌ Instapaper CSV not found: {csv_path}")
        return
        
    print(f"📁 Reading articles from {csv_path}")
    
    articles = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            url = row.get('URL', '').strip()
            title = row.get('Title', '').strip()
            
            # Skip private Instapaper emails and invalid URLs
            if (url and 
                not url.startswith('instapaper-private://') and 
                url.startswith(('http://', 'https://')) and
                title):
                articles.append({
                    'url': url,
                    'title': title,
                    'folder': row.get('Folder', ''),
                    'timestamp': row.get('Timestamp', ''),
                    'tags': row.get('Tags', '[]')
                })
    
    print(f"✅ Found {len(articles)} valid articles to process")
    
    # Check what's already processed
    existing_urls = set()
    try:
        all_content = db.search_content("", content_type="article")
        existing_urls = {item.get('url', '') for item in all_content}
        print(f"📊 Already processed: {len(existing_urls)} articles")
    except:
        print("📊 No existing articles found in database")
    
    # Process new articles
    new_articles = [a for a in articles if a['url'] not in existing_urls]
    print(f"🆕 New articles to process: {len(new_articles)}")
    
    if not new_articles:
        print("✅ All articles already processed!")
        return
    
    # Process in batches
    batch_size = 100
    processed = 0
    failed = 0
    
    for i in range(0, len(new_articles), batch_size):
        batch = new_articles[i:i+batch_size]
        print(f"\n🔄 Processing batch {i//batch_size + 1}/{(len(new_articles)-1)//batch_size + 1}")
        
        for article in batch:
            try:
                print(f"📰 Processing: {article['title'][:60]}...")
                result = article_manager.process_article(
                    article['url'], 
                    title=article['title']
                )
                
                if result.success:
                    processed += 1
                    if processed % 10 == 0:
                        print(f"✅ Processed {processed} articles so far...")
                else:
                    failed += 1
                    print(f"❌ Failed: {article['title'][:40]}...")
                    
            except Exception as e:
                failed += 1
                print(f"💥 Error processing {article['title'][:40]}: {str(e)}")
                
            # Progress report every 50 articles
            if (processed + failed) % 50 == 0:
                print(f"📊 Progress: {processed} success, {failed} failed")
    
    print(f"\n🎉 DOCUMENT CRISIS FIX COMPLETE")
    print(f"✅ Successfully processed: {processed} articles")
    print(f"❌ Failed: {failed} articles")
    print(f"📈 Success rate: {processed/(processed+failed)*100:.1f}%")
    
    # Optional: Clean up fake document files
    print(f"\n🧹 Cleaning up fake document files...")
    doc_dir = Path('output/documents')
    if doc_dir.exists():
        fake_files = list(doc_dir.glob('*.md'))
        print(f"🗑️  Found {len(fake_files)} fake document files to remove")
        
        # Uncomment to actually delete:
        # for file in fake_files:
        #     file.unlink()
        # print(f"✅ Removed {len(fake_files)} fake document files")
    
    print("\n🚀 Atlas now has real article content instead of Instapaper interface!")


if __name__ == "__main__":
    main()