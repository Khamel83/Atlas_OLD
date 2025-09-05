#!/usr/bin/env python3
"""
Reprocess all content that was limited by previous token constraints
"""

import sqlite3
import os
import time
from atlas_model_client import create_client

def main():
    # Set correct API key
    os.environ['OPENROUTER_API_KEY'] = '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'
    
    conn = sqlite3.connect('/home/ubuntu/dev/atlas/atlas.db')
    cursor = conn.cursor()
    
    # Get all items that need reprocessing
    cursor.execute('''
    SELECT id, title, content 
    FROM content 
    WHERE 
        (ai_tags IS NOT NULL AND length(ai_tags) < 50) OR
        (ai_summary IS NOT NULL AND length(ai_summary) < 100) OR  
        (ai_socratic IS NOT NULL AND length(ai_socratic) < 150) OR
        (ai_patterns IS NOT NULL AND length(ai_patterns) < 150) OR
        (ai_recommendations IS NOT NULL AND length(ai_recommendations) < 150)
    ORDER BY id DESC
    ''')
    
    items = cursor.fetchall()
    total_items = len(items)
    
    print(f'🚀 Starting reprocessing of {total_items} items with unlimited tokens')
    print('=' * 60)
    
    client = create_client()
    print(f'✅ Using API key ending: {client.api_key[-4:]}')
    print(f'✅ Token limits: {client.workload_tokens}')
    print()
    
    processed = 0
    skipped = 0
    errors = 0
    
    for i, (id, title, content) in enumerate(items):
        print(f'[{i+1}/{total_items}] Processing ID {id}: {title[:30]}...' if title else f'[{i+1}/{total_items}] Processing ID {id}')
        
        if not content or len(content.strip()) < 50:
            print('   ⚠️  Content too short, skipping')
            skipped += 1
            continue
            
        try:
            # Generate all AI workloads with unlimited tokens
            new_tags, _ = client.process_workload('tags', content, title or '')
            new_summary, _ = client.process_workload('summary', content, title or '')
            new_socratic, _ = client.process_workload('socratic', content, title or '')
            new_patterns, _ = client.process_workload('patterns', content, title or '')
            new_recommendations, _ = client.process_workload('recommendations', content, title or '')
            
            # Update database
            cursor.execute('''
            UPDATE content 
            SET ai_tags = ?, ai_summary = ?, ai_socratic = ?, ai_patterns = ?, ai_recommendations = ?, 
                updated_at = datetime('now')
            WHERE id = ?
            ''', (new_tags, new_summary, new_socratic, new_patterns, new_recommendations, id))
            
            processed += 1
            
            print(f'   ✅ Complete: tags:{len(new_tags)}, summary:{len(new_summary)}, socratic:{len(new_socratic)}, patterns:{len(new_patterns)}, recs:{len(new_recommendations)}')
            
            # Commit every 10 items and brief pause to avoid rate limits
            if processed % 10 == 0:
                conn.commit()
                time.sleep(1)
                print(f'   💾 Committed batch. Total processed: {processed}/{total_items}')
                
        except Exception as e:
            print(f'   ❌ Error: {str(e)}')
            errors += 1
            continue
    
    conn.commit()
    conn.close()
    
    print()
    print('🎉 REPROCESSING COMPLETE!')
    print('=' * 30)
    print(f'✅ Processed: {processed}')
    print(f'⚠️  Skipped: {skipped}')  
    print(f'❌ Errors: {errors}')
    print(f'📊 Total: {total_items}')

if __name__ == '__main__':
    main()