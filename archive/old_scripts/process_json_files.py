#!/usr/bin/env python3
"""
Process JSON files from inputs/New Docs/json/
"""

import json
import sqlite3
import os
from datetime import datetime
from pathlib import Path

def process_json_files():
    """Process all JSON files from New Docs directory"""
    
    print("📄 PROCESSING JSON FILES")
    print("=" * 30)
    
    json_dir = Path("inputs/New Docs/json/")
    if not json_dir.exists():
        print(f"❌ Directory not found: {json_dir}")
        return 0
    
    json_files = list(json_dir.glob("*.json"))
    print(f"📊 Found {len(json_files)} JSON files")
    
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    
    processed = 0
    errors = 0
    
    for i, json_file in enumerate(json_files, 1):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract title and content
            title = data.get('title', json_file.stem)
            content = data.get('content', data.get('text', ''))
            url = data.get('url', str(json_file))
            
            # Skip if no content
            if not content or len(content) < 100:
                continue
            
            # Clean and prepare
            title = title.strip()[:500]
            content = str(content).strip()
            
            if len(content) > 50:  # Minimum content check
                cursor.execute("""
                    INSERT OR IGNORE INTO content 
                    (url, title, content, created_at)
                    VALUES (?, ?, ?, ?)
                """, (
                    url,
                    title,
                    content,
                    datetime.now().isoformat()
                ))
                
                if cursor.rowcount > 0:
                    processed += 1
                    print(f"  {i:3}. ✅ {title[:50]}...")
                else:
                    print(f"  {i:3}. ➖ Duplicate: {title[:40]}...")
            
        except Exception as e:
            errors += 1
            print(f"  {i:3}. ❌ Error processing {json_file.name}: {e}")
            
        if i % 50 == 0:
            conn.commit()
            print(f"      💾 Committed batch at {i}")
    
    conn.commit()
    conn.close()
    
    print(f"\n📊 JSON PROCESSING COMPLETE!")
    print(f"✅ Files processed: {processed}")
    print(f"❌ Errors: {errors}")
    
    return processed

if __name__ == "__main__":
    process_json_files()