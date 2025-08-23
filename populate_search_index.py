#!/usr/bin/env python3
"""
Search Index Population Script
Populates search index from main content database
"""

import sqlite3
import sys
import json
from typing import Dict, Any, List
from pathlib import Path

def clean_content_for_search(content: str, max_length: int = 50000) -> str:
    """Clean and truncate content for search indexing."""
    if not content:
        return ""
    
    # Remove excessive whitespace
    cleaned = " ".join(content.split())
    
    # Truncate if too long
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length] + "..."
    
    return cleaned

def extract_content_and_tags_from_metadata(metadata_json: str, atlas_dir: Path) -> tuple[str, str]:
    """Extract content and tags from metadata JSON."""
    try:
        metadata = json.loads(metadata_json) if metadata_json else {}
        
        # Extract content from various possible locations
        content = ""
        
        # First check for content file path
        if 'content_path' in metadata and metadata['content_path']:
            content_path = atlas_dir / metadata['content_path']
            if content_path.exists():
                try:
                    content = content_path.read_text(encoding='utf-8')
                except Exception:
                    pass
        
        # Fallback to direct content in metadata
        if not content:
            if 'content' in metadata and metadata['content']:
                content = str(metadata['content'])
            elif 'text' in metadata and metadata['text']:
                content = str(metadata['text'])
            elif 'body' in metadata and metadata['body']:
                content = str(metadata['body'])
            elif 'description' in metadata and metadata['description']:
                content = str(metadata['description'])
        
        # Extract tags
        tags = []
        if 'tags' in metadata:
            if isinstance(metadata['tags'], list):
                tags.extend(metadata['tags'])
            elif isinstance(metadata['tags'], str):
                tags.extend(metadata['tags'].split(','))
        
        if 'categories' in metadata:
            if isinstance(metadata['categories'], list):
                tags.extend(metadata['categories'])
        
        if 'keywords' in metadata:
            if isinstance(metadata['keywords'], list):
                tags.extend(metadata['keywords'])
            elif isinstance(metadata['keywords'], str):
                tags.extend(metadata['keywords'].split(','))
        
        # Clean and deduplicate tags
        clean_tags = list(set([tag.strip() for tag in tags if tag and tag.strip()]))
        tags_str = ', '.join(clean_tags)
        
        return content, tags_str
        
    except (json.JSONDecodeError, TypeError):
        return "", ""

def populate_search_index(source_db: str, target_db: str, batch_size: int = 100) -> Dict[str, int]:
    """Populate search index from source database."""
    
    results = {
        "processed": 0,
        "inserted": 0,
        "skipped": 0,
        "errors": 0
    }
    
    try:
        # Connect to databases
        source_conn = sqlite3.connect(source_db)
        target_conn = sqlite3.connect(target_db)
        
        # Get source data
        cursor = source_conn.execute("""
            SELECT id, title, content_type, source_url, created_at, metadata, content
            FROM content 
            ORDER BY created_at DESC
        """)
        
        batch = []
        for row in cursor:
            results["processed"] += 1
            
            try:
                content_id, title, content_type, source_url, created_at, metadata_json, db_content = row
                
                # Parse metadata for enhanced title and other info
                try:
                    metadata = json.loads(metadata_json) if metadata_json else {}
                    enhanced_title = metadata.get('title', title) if metadata.get('title') not in [None, '', '[no-title]'] else title
                    if enhanced_title == '[no-title]' or not enhanced_title:
                        # Try to extract title from source URL
                        enhanced_title = source_url.split('/')[-1] if source_url else "Untitled"
                except:
                    enhanced_title = title or "Untitled"
                
                # Extract content and tags from metadata
                atlas_dir = Path(source_db).parent.parent
                metadata_content, tags = extract_content_and_tags_from_metadata(metadata_json, atlas_dir)
                
                # Use db_content if available, otherwise metadata content
                final_content = db_content if db_content and len(db_content.strip()) > 10 else metadata_content
                
                # Skip if no meaningful content
                if not final_content or len(final_content.strip()) < 10:
                    results["skipped"] += 1
                    continue
                
                # Clean content for search
                clean_content = clean_content_for_search(final_content)
                
                # Add to batch
                batch.append((
                    content_id,
                    enhanced_title,
                    clean_content,
                    content_type or "unknown",
                    source_url or "",
                    tags,
                    created_at
                ))
                
                # Insert batch when full
                if len(batch) >= batch_size:
                    insert_batch(target_conn, batch)
                    results["inserted"] += len(batch)
                    batch = []
                    print(f"Processed {results['processed']}, Inserted {results['inserted']}")
                    
            except Exception as e:
                print(f"Error processing row: {e}")
                results["errors"] += 1
                continue
        
        # Insert remaining batch
        if batch:
            insert_batch(target_conn, batch)
            results["inserted"] += len(batch)
        
        target_conn.commit()
        source_conn.close()
        target_conn.close()
        
    except Exception as e:
        print(f"Database error: {e}")
        results["errors"] += 1
    
    return results

def insert_batch(conn: sqlite3.Connection, batch: List[tuple]) -> None:
    """Insert batch of records into search index."""
    conn.executemany("""
        INSERT OR REPLACE INTO search_index 
        (content_id, title, content, content_type, url, tags, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, batch)

def main():
    """Main execution."""
    atlas_dir = Path(__file__).parent
    source_db = atlas_dir / "data" / "atlas.db"
    target_db = atlas_dir / "data" / "enhanced_search.db"
    
    print("🔍 Atlas Search Index Population")
    print(f"Source: {source_db}")
    print(f"Target: {target_db}")
    
    # Verify databases exist
    if not source_db.exists():
        print(f"❌ Source database not found: {source_db}")
        sys.exit(1)
    
    if not target_db.exists():
        print(f"❌ Target database not found: {target_db}")
        sys.exit(1)
    
    # Check current counts
    source_conn = sqlite3.connect(str(source_db))
    target_conn = sqlite3.connect(str(target_db))
    
    source_count = source_conn.execute("SELECT COUNT(*) FROM content").fetchone()[0]
    target_count = target_conn.execute("SELECT COUNT(*) FROM search_index").fetchone()[0]
    
    print(f"📊 Source records: {source_count}")
    print(f"📊 Current search index records: {target_count}")
    
    source_conn.close()
    target_conn.close()
    
    if source_count == 0:
        print("❌ No content to index")
        sys.exit(1)
    
    print("\n🚀 Starting population...")
    results = populate_search_index(str(source_db), str(target_db))
    
    print("\n✅ Population Complete!")
    print(f"📊 Processed: {results['processed']}")
    print(f"📊 Inserted: {results['inserted']}")
    print(f"📊 Skipped: {results['skipped']}")
    print(f"📊 Errors: {results['errors']}")
    
    # Verify final count
    target_conn = sqlite3.connect(str(target_db))
    final_count = target_conn.execute("SELECT COUNT(*) FROM search_index").fetchone()[0]
    target_conn.close()
    
    print(f"📊 Final search index records: {final_count}")
    
    if final_count > 0:
        print("🎉 Search index successfully populated!")
        return 0
    else:
        print("❌ Search index population failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())