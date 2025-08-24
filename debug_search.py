#!/usr/bin/env python3
"""Debug search functionality to see what's working"""

import sqlite3
import os
from helpers.config import load_config

def test_databases():
    """Test different search databases"""
    databases = [
        'data/enhanced_search.db',
        'atlas_search.db', 
        'data/atlas_search.db',
        'search_index.db'
    ]
    
    for db_path in databases:
        if os.path.exists(db_path):
            print(f"\n🔍 Testing {db_path}:")
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # List tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]
            print(f"  Tables: {tables}")
            
            # Check search_index if it exists
            if 'search_index' in tables:
                cursor.execute("SELECT COUNT(*), content_type FROM search_index GROUP BY content_type;")
                results = cursor.fetchall()
                print(f"  Search Index: {results}")
                
                # Sample data
                cursor.execute("SELECT title, content_type FROM search_index LIMIT 3;")
                samples = cursor.fetchall()
                for title, ctype in samples:
                    print(f"    - {ctype}: {title[:50]}...")
                    
            # Check for direct search
            if 'search_index' in tables:
                cursor.execute("SELECT COUNT(*) FROM search_index WHERE title LIKE '%technology%' OR content LIKE '%technology%';")
                tech_count = cursor.fetchone()[0]
                print(f"  'technology' matches: {tech_count}")
                
            conn.close()

def test_enhanced_search():
    """Test enhanced search directly"""
    try:
        from helpers.enhanced_search import EnhancedSearchEngine
        config = load_config()
        engine = EnhancedSearchEngine(config)
        
        # Try basic search
        results = engine.search("technology", limit=5)
        print(f"\n🔍 Enhanced Search Test:")
        print(f"  Results for 'technology': {len(results)}")
        
        # Debug the enhanced search database path
        print(f"  Enhanced DB path: {engine.db_path}")
        print(f"  Enhanced DB exists: {os.path.exists(engine.db_path)}")
        
        if os.path.exists(engine.db_path):
            conn = sqlite3.connect(engine.db_path)
            cursor = conn.cursor()
            
            # Check tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]
            print(f"  Enhanced DB tables: {tables}")
            
            if 'enhanced_content_index' in tables:
                cursor.execute("SELECT COUNT(*) FROM enhanced_content_index;")
                count = cursor.fetchone()[0]
                print(f"  Enhanced content items: {count}")
                
                cursor.execute("SELECT COUNT(*) FROM enhanced_content_index WHERE title LIKE '%technology%' OR content LIKE '%technology%';")
                tech_count = cursor.fetchone()[0]
                print(f"  Technology matches in enhanced: {tech_count}")
                
            if 'search_index' in tables:
                cursor.execute("SELECT COUNT(*) FROM search_index;")
                count = cursor.fetchone()[0]
                print(f"  Search index items: {count}")
                
            conn.close()
            
    except Exception as e:
        print(f"Enhanced search error: {e}")

if __name__ == "__main__":
    print("🚀 Atlas Search Debug")
    print("=" * 40)
    
    test_databases()
    test_enhanced_search()