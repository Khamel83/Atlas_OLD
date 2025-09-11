#!/usr/bin/env python3
"""
Process JSON article backlog - dogfood Atlas with real user data
"""

import os
import json
import sys
import sqlite3
from pathlib import Path
from datetime import datetime

def process_json_files(json_dir, max_files=None):
    """Process JSON files from the backlog"""
    
    # Initialize Atlas components
    db = SimpleDatabase()
    processor = AtlasDocumentProcessor()
    
    json_files = list(Path(json_dir).glob("*.json"))
    total_files = len(json_files)
    
    print(f"🚀 Starting Atlas JSON Processing")
    print(f"📊 Found {total_files} JSON files to process")
    
    if max_files:
        json_files = json_files[:max_files]
        print(f"🎯 Processing first {max_files} files as requested")
    
    processed = 0
    errors = 0
    
    for i, json_file in enumerate(json_files, 1):
        try:
            print(f"📄 Processing {i}/{len(json_files)}: {json_file.name[:50]}...")
            
            # Read JSON file
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract content - JSON format may vary
            if isinstance(data, dict):
                # Try different JSON structures
                content = data.get('content') or data.get('text') or data.get('body') or ""
                title = data.get('title') or data.get('name') or json_file.stem
                url = data.get('url') or data.get('link') or ""
                
                if not content and 'html' in data:
                    content = data['html']
                    
                # Some files might have the content at root level
                if not content and len(str(data)) > 100:
                    content = str(data)[:5000]  # Use first part as content
                    
            else:
                # JSON might be a list or string
                content = str(data)[:5000]
                title = json_file.stem
                url = ""
            
            if not content or len(content.strip()) < 50:
                print(f"⚠️  Skipping {json_file.name} - insufficient content")
                continue
                
            # Create a temporary file-like object for processing
            temp_file_path = f"/tmp/{json_file.stem}.txt"
            with open(temp_file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Process with Atlas document processor
            result = processor.process_document(temp_file_path)
            
            # Clean up temp file
            try:
                os.remove(temp_file_path)
            except:
                pass
            
            if result and result.get('success'):
                processed += 1
                print(f"✅ Processed: {title[:40]}...")
            else:
                errors += 1
                print(f"❌ Failed: {json_file.name}")
                
        except Exception as e:
            errors += 1
            print(f"❌ Error processing {json_file.name}: {e}")
            
        # Progress update
        if i % 10 == 0:
            print(f"📈 Progress: {i}/{len(json_files)} ({processed} processed, {errors} errors)")
    
    print(f"\n🎉 PROCESSING COMPLETE!")
    print(f"✅ Successfully processed: {processed}")
    print(f"❌ Errors: {errors}")
    print(f"📊 Success rate: {processed/(processed+errors)*100:.1f}%")
    
    return processed, errors

def main():
    """Main processing function"""
    
    # Check arguments
    max_files = None
    if len(sys.argv) > 1:
        try:
            max_files = int(sys.argv[1])
            print(f"🎯 Will process maximum {max_files} files")
        except ValueError:
            print("Usage: python process_json_backlog.py [max_files]")
            sys.exit(1)
    
    json_dir = "inputs/New Docs/json/"
    
    if not Path(json_dir).exists():
        print(f"❌ JSON directory not found: {json_dir}")
        sys.exit(1)
    
    # Process the files
    processed, errors = process_json_files(json_dir, max_files)
    
    print(f"\n🚀 Atlas has processed {processed} new articles!")
    print(f"🔍 Check your dashboard: http://localhost:8000/ask/html")
    
    return processed > 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)