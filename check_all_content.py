#!/usr/bin/env python3
"""Check all content types processed by Atlas"""

import os
import json
from pathlib import Path

def check_content_summary():
    """Check what content Atlas has actually processed"""
    
    output_dir = Path("output")
    
    # Content type analysis
    content_analysis = {
        "articles": {"total": 0, "success": 0, "with_content": 0},
        "documents": {"total": 0, "success": 0, "with_content": 0},
        "podcasts": {"total": 0, "success": 0, "with_content": 0, "with_transcripts": 0},
        "youtube": {"total": 0, "success": 0, "with_content": 0, "with_transcripts": 0},
        "captured": {"total": 0, "success": 0, "with_content": 0},
        "emails": {"total": 0, "success": 0, "with_content": 0}
    }
    
    # File counts by extension
    file_types = {
        ".md": 0, ".html": 0, ".txt": 0, ".json": 0, 
        ".mp3": 0, ".mp4": 0, ".pdf": 0, ".csv": 0
    }
    
    # Check each content type
    for content_type in ["articles", "documents", "podcasts", "youtube", "captured"]:
        type_dir = output_dir / content_type
        if not type_dir.exists():
            continue
            
        # Check metadata files
        metadata_dir = type_dir / "metadata"
        if metadata_dir.exists():
            for metadata_file in metadata_dir.glob("*.json"):
                content_analysis[content_type]["total"] += 1
                
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    
                    if metadata.get('status') == 'success':
                        content_analysis[content_type]["success"] += 1
                        
                        # Check for actual content
                        content_path = metadata.get('content_path')
                        if content_path and Path(content_path).exists():
                            content_analysis[content_type]["with_content"] += 1
                        
                        # Check for transcripts (podcasts/youtube)
                        if content_type in ["podcasts", "youtube"]:
                            transcript_text = metadata.get('transcript_text', '')
                            transcript_path = metadata.get('transcript_path')
                            if transcript_text or (transcript_path and Path(transcript_path).exists()):
                                content_analysis[content_type]["with_transcripts"] += 1
                                
                except Exception:
                    continue
    
    # Count all files by extension
    for file_path in output_dir.rglob("*"):
        if file_path.is_file():
            ext = file_path.suffix.lower()
            if ext in file_types:
                file_types[ext] += 1
    
    # Check for emails (might be in different location)
    email_dirs = [Path("emails"), Path("data/emails"), output_dir / "emails"]
    for email_dir in email_dirs:
        if email_dir.exists():
            email_files = list(email_dir.rglob("*.json")) + list(email_dir.rglob("*.html")) + list(email_dir.rglob("*.txt"))
            content_analysis["emails"]["total"] = len(email_files)
            # Count successful emails (simplified)
            content_analysis["emails"]["success"] = len([f for f in email_files if f.stat().st_size > 100])
    
    # Print comprehensive summary
    print("📊 ATLAS CONTENT PROCESSING SUMMARY")
    print("=" * 60)
    
    for content_type, stats in content_analysis.items():
        print(f"\n🗂️  {content_type.upper()}")
        print(f"   Total items: {stats['total']:,}")
        print(f"   Successful: {stats['success']:,}")
        print(f"   With content: {stats['with_content']:,}")
        if 'with_transcripts' in stats:
            print(f"   With transcripts: {stats['with_transcripts']:,}")
        
        if stats['total'] > 0:
            success_rate = (stats['success'] / stats['total']) * 100
            print(f"   Success rate: {success_rate:.1f}%")
    
    print(f"\n📁 FILE TYPES")
    for ext, count in file_types.items():
        if count > 0:
            print(f"   {ext}: {count:,}")
    
    # Overall totals
    total_items = sum(stats['total'] for stats in content_analysis.values())
    total_success = sum(stats['success'] for stats in content_analysis.values())
    total_content = sum(stats['with_content'] for stats in content_analysis.values())
    
    print(f"\n🎯 OVERALL TOTALS")
    print(f"   Total items processed: {total_items:,}")
    print(f"   Successfully processed: {total_success:,}")
    print(f"   Items with content: {total_content:,}")
    
    if total_items > 0:
        overall_success = (total_success / total_items) * 100
        print(f"   Overall success rate: {overall_success:.1f}%")
    
    # Check database population
    try:
        import sqlite3
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM content")
        db_count = cursor.fetchone()[0]
        cursor.execute("SELECT content_type, COUNT(*) FROM content GROUP BY content_type")
        db_types = dict(cursor.fetchall())
        conn.close()
        
        print(f"\n💾 DATABASE STATUS")
        print(f"   Total database records: {db_count:,}")
        for content_type, count in db_types.items():
            print(f"   {content_type}: {count:,}")
            
    except Exception as e:
        print(f"\n💾 DATABASE STATUS: Error checking database - {e}")

if __name__ == "__main__":
    check_content_summary()