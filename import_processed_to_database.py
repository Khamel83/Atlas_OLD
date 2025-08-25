#!/usr/bin/env python3
"""
Import all processed backlog content into Atlas database
"""

import os
import re
from pathlib import Path
from helpers.simple_database import SimpleDatabase

def extract_metadata_from_markdown(content):
    """Extract metadata from processed markdown files"""
    lines = content.split('\n')
    title = "Untitled"
    source = ""
    processed_date = ""
    
    # Get title (first line after # )
    for line in lines[:5]:
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    # Extract metadata
    for line in lines[:10]:
        if line.startswith('**From:**'):
            source = line.replace('**From:**', '').strip()
        elif line.startswith('**Source:**'):
            source = line.replace('**Source:**', '').strip()
        elif line.startswith('**Processed:**'):
            processed_date = line.replace('**Processed:**', '').strip()
    
    # Get content (skip metadata section)
    content_lines = []
    skip_metadata = True
    for line in lines:
        if skip_metadata and line.strip() == "":
            skip_metadata = False
            continue
        if not skip_metadata and not line.startswith('**'):
            content_lines.append(line)
    
    content_text = '\n'.join(content_lines).strip()
    
    return title, content_text, source, processed_date

def import_processed_files():
    """Import all processed files into database"""
    db = SimpleDatabase()
    
    processed_dir = Path("processed_backlog")
    imported = 0
    
    # Process each category
    for category in ["html", "emails", "articles"]:
        category_dir = processed_dir / category
        if not category_dir.exists():
            continue
            
        print(f"\nImporting {category}...")
        
        for md_file in category_dir.glob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                title, text, source, processed_date = extract_metadata_from_markdown(content)
                
                # Determine content type
                if category == "emails":
                    content_type = "email"
                elif category == "html":
                    content_type = "article" 
                else:
                    content_type = "article"
                
                # Store in database
                content_id = db.store_content(
                    content=text,
                    title=title,
                    url=source if source.startswith('http') else "",
                    content_type=content_type,
                    metadata={
                        "source_file": str(md_file),
                        "original_source": source,
                        "processed_date": processed_date,
                        "import_category": category
                    }
                )
                
                imported += 1
                if imported % 100 == 0:
                    print(f"  Imported {imported} items...")
                    
            except Exception as e:
                print(f"  Error importing {md_file}: {e}")
                continue
    
    print(f"\n✅ Import complete: {imported} items added to database")
    
    # Verify database count
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM content')
    total_count = cursor.fetchone()[0]
    conn.close()
    
    print(f"📊 Total items in database: {total_count}")

if __name__ == "__main__":
    import_processed_files()