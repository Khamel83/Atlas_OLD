#!/usr/bin/env python3
"""
Atlas Database Migration Script
Migrate processed files from output/ and processed_backlog/ to database
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from helpers.simple_database import SimpleDatabase

def extract_metadata_from_markdown(file_path, content):
    """Extract metadata from markdown file"""
    lines = content.split('\n')
    title = "Untitled"
    url = ""
    source = ""
    processed_date = ""
    
    # Extract title (first # line)
    for line in lines[:10]:
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    # Extract metadata from markdown headers
    for line in lines[:15]:
        if line.startswith('**URL:**'):
            url = line.replace('**URL:**', '').strip()
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
    
    actual_content = '\n'.join(content_lines).strip()
    
    # Determine content type from file path
    if 'email' in str(file_path).lower():
        content_type = 'email'
    elif 'podcast' in str(file_path).lower():
        content_type = 'podcast'
    elif 'transcript' in str(file_path).lower():
        content_type = 'transcript'
    else:
        content_type = 'article'
    
    return {
        'title': title,
        'url': url or source,
        'content': actual_content,
        'content_type': content_type,
        'metadata': {
            'source_file': str(file_path),
            'original_source': source,
            'processed_date': processed_date,
            'migrated_at': datetime.now().isoformat()
        }
    }

def migrate_directory(directory, db, stats):
    """Migrate all markdown files from a directory"""
    print(f"\n📂 Migrating {directory}...")
    
    if not Path(directory).exists():
        print(f"   Directory not found: {directory}")
        return
    
    markdown_files = list(Path(directory).rglob("*.md"))
    print(f"   Found {len(markdown_files)} markdown files")
    
    for i, file_path in enumerate(markdown_files):
        try:
            # Read file content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Extract metadata
            data = extract_metadata_from_markdown(file_path, content)
            
            # Check for duplicates by URL or title hash
            content_hash = hashlib.md5(f"{data['title']}{data['url']}".encode()).hexdigest()
            
            # Store in database
            content_id = db.store_content(
                title=data['title'],
                url=data['url'], 
                content=data['content'],
                content_type=data['content_type'],
                metadata=data['metadata']
            )
            
            stats['success'] += 1
            
            if (i + 1) % 100 == 0:
                print(f"   ✅ Migrated {i + 1}/{len(markdown_files)} files...")
            
        except Exception as e:
            print(f"   ❌ Error with {file_path.name}: {e}")
            stats['failed'] += 1
            continue

def migrate_all_files():
    """Migrate all processed files to database"""
    print("🚀 Starting Atlas Database Migration...")
    print("   This will populate the database with all processed content")
    
    db = SimpleDatabase()
    
    # Get initial count
    conn = db.get_connection() 
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM content')
    initial_count = cursor.fetchone()[0]
    conn.close()
    
    print(f"   Initial database records: {initial_count}")
    
    stats = {'success': 0, 'failed': 0}
    
    # Migrate from processed_backlog (recent processing)
    migrate_directory("processed_backlog", db, stats)
    
    # Migrate from output directory (historical processing) 
    migrate_directory("output", db, stats)
    
    # Final count
    conn = db.get_connection()
    cursor = conn.cursor() 
    cursor.execute('SELECT COUNT(*) FROM content')
    final_count = cursor.fetchone()[0]
    conn.close()
    
    added_records = final_count - initial_count
    
    print(f"\n✅ Migration Complete!")
    print(f"   📊 Results:")
    print(f"      Success: {stats['success']} files")
    print(f"      Failed: {stats['failed']} files")
    print(f"      Database records: {initial_count} → {final_count}")
    print(f"      Records added: {added_records}")
    
    if added_records > 0:
        print(f"\n🎯 Database integration crisis RESOLVED!")
        print(f"   Atlas now has {final_count} searchable records")
    else:
        print(f"\n⚠️ No new records added - check for duplicates or issues")

if __name__ == "__main__":
    migrate_all_files()