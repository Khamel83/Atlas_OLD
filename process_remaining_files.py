#!/usr/bin/env python3
"""
Process All Remaining HTML Files

Process the 2366 files that haven't been processed yet
"""

import sqlite3
from pathlib import Path
import trafilatura
from datetime import datetime
import re

def get_processed_urls():
    """Get URLs that are already processed"""
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT url FROM content")
    processed_urls = set(row[0] for row in cursor.fetchall())
    
    conn.close()
    return processed_urls

def extract_clean_content(html_file):
    """Extract content using trafilatura"""
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
        
        # Use trafilatura for clean extraction
        extracted = trafilatura.extract(
            html_content,
            include_comments=False,
            include_tables=True,
            include_links=False,
            deduplicate=True,
            output_format='txt'
        )
        
        if not extracted or len(extracted.strip()) < 50:
            return None
        
        # Get metadata
        metadata = trafilatura.extract_metadata(html_content)
        
        # Get title
        title = "Unknown"
        if metadata and metadata.title:
            title = metadata.title
        elif html_file.stem:
            title = html_file.stem.replace('_', ' ')[:100]
        
        # Extract URL from filename
        url = f"file://{html_file.name}"
        filename_parts = html_file.stem.split('_')
        for part in filename_parts:
            if 'http' in part or '.com' in part:
                url = part.replace('_', '/')
                break
        
        # Clean extracted text
        cleaned = re.sub(r'\xa0|\u200c|\u200b', ' ', extracted)
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        
        return {
            'title': title[:500],
            'content': cleaned,  # NO LIMIT!
            'url': url[:500],
            'filename': html_file.name
        }
        
    except Exception as e:
        print(f"❌ Error processing {html_file.name}: {e}")
        return None

def process_all_remaining():
    """Process all files not yet in database"""
    
    print("🔍 Finding unprocessed files...")
    
    # Get already processed URLs
    processed_urls = get_processed_urls()
    print(f"📊 Already processed: {len(processed_urls)} items")
    
    # Get all HTML files
    html_dir = Path("inputs/PROCESSED/html/")
    all_files = list(html_dir.glob("*.html"))
    print(f"📁 Total HTML files available: {len(all_files)}")
    
    # Find unprocessed files
    unprocessed = []
    for html_file in all_files:
        file_url = f"file://{html_file.name}"
        if file_url not in processed_urls:
            unprocessed.append(html_file)
    
    print(f"🎯 Unprocessed files: {len(unprocessed)}")
    
    if len(unprocessed) == 0:
        print("✅ All files already processed!")
        return True
    
    # Process unprocessed files
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    
    processed = 0
    errors = 0
    skipped = 0
    
    for i, html_file in enumerate(unprocessed, 1):
        try:
            extracted = extract_clean_content(html_file)
            
            if extracted:
                # Insert into database
                cursor.execute("""
                    INSERT OR IGNORE INTO content 
                    (url, title, content, created_at)
                    VALUES (?, ?, ?, ?)
                """, (
                    extracted['url'],
                    extracted['title'],
                    extracted['content'],
                    datetime.now().isoformat()
                ))
                
                processed += 1
                
                if i % 100 == 0:
                    print(f"📈 Progress: {i}/{len(unprocessed)} ({processed} processed, {errors} errors, {skipped} skipped)")
                    conn.commit()
            else:
                skipped += 1
                
        except Exception as e:
            errors += 1
            if errors < 5:
                print(f"❌ Error processing {html_file.name}: {e}")
    
    conn.commit()
    conn.close()
    
    print(f"\n🎉 PROCESSING COMPLETE!")
    print(f"✅ Successfully processed: {processed}")
    print(f"❌ Errors: {errors}")
    print(f"⚠️  Skipped (too short): {skipped}")
    print(f"📊 Success rate: {processed/(processed+errors+skipped)*100:.1f}%")
    
    return processed > 0

def get_final_stats():
    """Get final database statistics"""
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM content")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM content WHERE title LIKE '%TRANSCRIPT%'")
    transcripts = cursor.fetchone()[0]
    
    cursor.execute("SELECT AVG(LENGTH(content)) FROM content WHERE title NOT LIKE '%TRANSCRIPT%'")
    avg_length = cursor.fetchone()[0]
    
    cursor.execute("SELECT MAX(LENGTH(content)) FROM content")
    max_length = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM content WHERE LENGTH(content) > 20000")
    long_articles = cursor.fetchone()[0]
    
    conn.close()
    
    return {
        'total': total,
        'articles': total - transcripts,
        'transcripts': transcripts,
        'avg_length': int(avg_length) if avg_length else 0,
        'max_length': max_length,
        'long_articles': long_articles
    }

def main():
    """Process remaining files and show final stats"""
    
    print("🚀 Atlas Complete Content Processor")
    print("=" * 50)
    print("🎯 Processing ALL remaining HTML files with trafilatura")
    print("=" * 50)
    
    # Process remaining files
    success = process_all_remaining()
    
    # Show final statistics
    stats = get_final_stats()
    
    print(f"\n📊 FINAL ATLAS CONTENT STATISTICS")
    print("=" * 50)
    print(f"📄 Total content items: {stats['total']}")
    print(f"📰 Articles: {stats['articles']}")
    print(f"🎙️ Transcripts: {stats['transcripts']}")
    print(f"📏 Average article length: {stats['avg_length']} chars")
    print(f"📈 Longest article: {stats['max_length']} chars")  
    print(f"📚 Long articles (>20K): {stats['long_articles']}")
    
    if stats['total'] >= 4000:
        print(f"\n🎉 ATLAS IS FULLY LOADED!")
        print(f"✨ {stats['articles']} articles with unlimited length")
        print(f"🧠 Content extraction powered by trafilatura")
        print(f"🔍 No more 10K character limits")
        print(f"🚀 Ready for production use!")
    else:
        print(f"\n⚠️  Expected more content, check for processing issues")
    
    return success

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)