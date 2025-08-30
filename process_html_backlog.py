#!/usr/bin/env python3
"""
Process HTML backlog - get real content into Atlas database
"""

import os
import sqlite3
import html
import re
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup

def extract_content_from_html(html_file):
    """Extract meaningful content from HTML file"""
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get title
        title_elem = soup.find('title')
        title = title_elem.get_text().strip() if title_elem else html_file.stem
        
        # Get main content - try different approaches
        text_content = ""
        
        # Try to find main content area
        main_selectors = [
            'main', 'article', '.content', '.post', '.entry',
            '#content', '#main', '.article-body', '.post-body'
        ]
        
        for selector in main_selectors:
            main_elem = soup.select_one(selector)
            if main_elem:
                text_content = main_elem.get_text(separator=' ', strip=True)
                break
        
        # Fallback: get all text
        if not text_content or len(text_content) < 100:
            text_content = soup.get_text(separator=' ', strip=True)
        
        # Clean up text
        text_content = re.sub(r'\s+', ' ', text_content).strip()
        
        # Extract URL from filename if possible
        url = ""
        filename_parts = html_file.stem.split('_')
        for part in filename_parts:
            if 'http' in part or '.com' in part:
                url = part.replace('_', '/')
                break
        
        return {
            'title': title[:500],  # Limit title length
            'content': text_content[:10000],  # Limit content length
            'url': url[:500] if url else f"file://{html_file.name}",
            'filename': html_file.name
        }
        
    except Exception as e:
        print(f"❌ Error extracting from {html_file.name}: {e}")
        return None

def process_html_files(html_dir, max_files=None):
    """Process HTML files from the backlog"""
    
    # Connect to Atlas database
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    
    html_files = list(Path(html_dir).glob("*.html"))
    total_files = len(html_files)
    
    print(f"🚀 Processing {total_files} HTML files from processed backlog")
    
    if max_files:
        html_files = html_files[:max_files]
        print(f"🎯 Processing first {max_files} files as requested")
    
    processed = 0
    errors = 0
    skipped = 0
    
    for i, html_file in enumerate(html_files, 1):
        try:
            # Extract content
            extracted = extract_content_from_html(html_file)
            
            if not extracted:
                errors += 1
                continue
            
            # Skip if content too short
            if len(extracted['content'].strip()) < 100:
                skipped += 1
                if i % 100 == 0:
                    print(f"⚠️  Skipped {html_file.name} - insufficient content")
                continue
            
            # Insert into Atlas database
            cursor.execute("""
                INSERT OR REPLACE INTO content 
                (url, title, content, created_at)
                VALUES (?, ?, ?, ?)
            """, (
                extracted['url'],
                extracted['title'],
                extracted['content'],
                datetime.now().isoformat()
            ))
            
            processed += 1
            
            if i % 50 == 0:
                print(f"📈 Progress: {i}/{len(html_files)} ({processed} processed, {errors} errors, {skipped} skipped)")
                conn.commit()  # Commit batch
            
        except Exception as e:
            errors += 1
            if errors < 5:  # Only show first few errors
                print(f"❌ Error processing {html_file.name}: {e}")
    
    # Final commit
    conn.commit()
    conn.close()
    
    print(f"\n🎉 PROCESSING COMPLETE!")
    print(f"✅ Successfully processed: {processed}")
    print(f"❌ Errors: {errors}")
    print(f"⚠️  Skipped (too short): {skipped}")
    print(f"📊 Success rate: {processed/(processed+errors+skipped)*100:.1f}%")
    
    return processed

def main():
    """Main processing function"""
    
    import sys
    
    # Check arguments
    max_files = None
    if len(sys.argv) > 1:
        try:
            max_files = int(sys.argv[1])
            print(f"🎯 Will process maximum {max_files} files")
        except ValueError:
            print("Usage: python process_html_backlog.py [max_files]")
            sys.exit(1)
    
    html_dir = "inputs/PROCESSED/html/"
    
    if not Path(html_dir).exists():
        print(f"❌ HTML directory not found: {html_dir}")
        sys.exit(1)
    
    # Install BeautifulSoup if needed
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("📦 Installing BeautifulSoup...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
        from bs4 import BeautifulSoup
    
    # Process the files
    processed = process_html_files(html_dir, max_files)
    
    print(f"\n🚀 Atlas now has {processed} real articles!")
    print(f"🔍 This is your actual processed backlog in Atlas")
    
    return processed > 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)