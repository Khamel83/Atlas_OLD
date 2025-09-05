#!/usr/bin/env python3
"""
Atlas Comprehensive Service
Processes content that needs AI analysis
"""

import os
import sys
import sqlite3
import time
from datetime import datetime

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Process content items that need AI analysis"""
    try:
        from atlas_model_client import create_client
        
        # Create AI client (only print on first run)
        client = create_client()
        
        # Connect to database
        conn = sqlite3.connect('atlas.db')
        cursor = conn.cursor()
        
        # Find items that need AI processing (have content but missing AI fields)
        cursor.execute('''
        SELECT id, title, content
        FROM content 
        WHERE length(content) > 100 
        AND (ai_summary IS NULL OR ai_tags IS NULL OR ai_socratic IS NULL 
             OR ai_patterns IS NULL OR ai_recommendations IS NULL)
        ORDER BY id ASC
        LIMIT 10
        ''')
        
        items = cursor.fetchall()
        
        if not items:
            # Only print occasionally when caught up
            return
        
        print(f"🔄 Processing {len(items)} items...")
        processed = 0
        for item_id, title, content in items:
            try:
                # Generate all AI workloads
                tags, _ = client.process_workload('tags', content, title or '')
                summary, _ = client.process_workload('summary', content, title or '')
                socratic, _ = client.process_workload('socratic', content, title or '')
                patterns, _ = client.process_workload('patterns', content, title or '')
                recommendations, _ = client.process_workload('recommendations', content, title or '')
                
                # Update database
                cursor.execute('''
                UPDATE content 
                SET ai_tags = ?, ai_summary = ?, ai_socratic = ?, ai_patterns = ?, ai_recommendations = ?, 
                    updated_at = datetime('now')
                WHERE id = ?
                ''', (tags, summary, socratic, patterns, recommendations, item_id))
                
                processed += 1
                    
            except Exception as e:
                print(f"❌ Error processing item {item_id}: {e}")
                continue
        
        conn.commit()
        conn.close()
        
        print(f"✅ Processed {processed}/{len(items)} items")
        
    except Exception as e:
        print(f"❌ Comprehensive service failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()