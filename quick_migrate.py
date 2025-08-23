#!/usr/bin/env python3
"""
Quick Atlas Database Migration - No Dependencies
"""
import json
import os
import sqlite3
from pathlib import Path

def quick_migrate():
    """Quick migration without external dependencies"""
    
    # Database path
    db_path = "atlas.db"
    
    print(f"🚀 Quick Atlas Migration Starting...")
    print(f"📊 Database: {db_path}")
    
    # Create connection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Count current records
    cursor.execute("SELECT COUNT(*) FROM content")
    initial_count = cursor.fetchone()[0]
    print(f"📊 Initial database records: {initial_count}")
    
    # Find metadata files
    metadata_files = []
    output_dir = Path("output")
    
    for content_type in ['articles', 'documents', 'podcasts', 'youtube']:
        metadata_dir = output_dir / content_type / "metadata"
        if metadata_dir.exists():
            metadata_files.extend(metadata_dir.glob("*.json"))
    
    print(f"📊 Found {len(metadata_files)} metadata files")
    
    # Process files
    successful = 0
    failed = 0
    skipped = 0
    
    for i, metadata_file in enumerate(metadata_files):
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            # Only process successful items
            if metadata.get('status') != 'success':
                skipped += 1
                continue
            
            # Extract data
            title = metadata.get('title', '[no-title]')
            url = metadata.get('source', '')
            content_type = metadata.get('content_type', 'article')
            created_at = metadata.get('created_at', '')
            
            # Get content from file
            content_path = metadata.get('content_path')
            content = ""
            
            if content_path and Path(content_path).exists():
                try:
                    with open(content_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                except Exception:
                    content = ""
            
            # Skip if no content
            if not content or len(content.strip()) < 20:
                skipped += 1
                continue
            
            # Check if already exists
            cursor.execute("SELECT id FROM content WHERE url = ?", (url,))
            if cursor.fetchone():
                skipped += 1
                continue
            
            # Insert
            cursor.execute("""
                INSERT INTO content (title, url, content, content_type, metadata, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                title,
                url, 
                content[:50000],  # Limit content size
                content_type,
                json.dumps(metadata),
                created_at,
                created_at
            ))
            
            successful += 1
            
            # Progress update
            if (i + 1) % 100 == 0:
                conn.commit()
                print(f"Progress: {i+1}/{len(metadata_files)} - Success: {successful}, Skipped: {skipped}, Failed: {failed}")
        
        except Exception as e:
            failed += 1
            if failed < 10:  # Show first 10 errors
                print(f"Error with {metadata_file}: {e}")
    
    # Final commit
    conn.commit()
    
    # Final count
    cursor.execute("SELECT COUNT(*) FROM content")
    final_count = cursor.fetchone()[0]
    
    conn.close()
    
    print(f"\n✅ Migration Complete!")
    print(f"📊 Successful migrations: {successful}")
    print(f"📊 Skipped items: {skipped}")  
    print(f"📊 Failed items: {failed}")
    print(f"📊 Initial database records: {initial_count}")
    print(f"📊 Final database records: {final_count}")
    print(f"📊 Net new records: {final_count - initial_count}")
    
    if final_count > 1000:
        print("🎉 SUCCESS: Database now has substantial content!")
        return True
    else:
        print("⚠️ WARNING: Database still has few records")
        return False

if __name__ == "__main__":
    quick_migrate()