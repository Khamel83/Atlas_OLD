#!/usr/bin/env python3
"""
Add limited content to Atlas's built-in job queue for reprocessing
"""

import sqlite3
import json
import os

def main():
    # Set correct API key
    os.environ['OPENROUTER_API_KEY'] = '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'
    
    conn = sqlite3.connect('/home/ubuntu/dev/atlas/atlas.db')
    cursor = conn.cursor()
    
    # Get items that need reprocessing
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
    LIMIT 100
    ''')
    
    items = cursor.fetchall()
    print(f'🎯 Queuing {len(items)} items for reprocessing...')
    
    # Add jobs to Atlas's built-in queue
    jobs_added = 0
    
    for id, title, content in items:
        if not content or len(content.strip()) < 50:
            continue
            
        # Create job for AI reprocessing
        job_data = {
            'type': 'ai_reprocessing',
            'content_id': id,
            'title': title[:50] + '...' if title and len(title) > 50 else title,
            'workloads': ['tags', 'summary', 'socratic', 'patterns', 'recommendations']
        }
        
        # Generate unique job ID
        job_id = f'reprocess_{id}_{jobs_added}'
        
        cursor.execute('''
        INSERT INTO worker_jobs (id, type, data, status, created_at, priority)
        VALUES (?, ?, ?, 'pending', datetime('now'), 5)
        ''', (job_id, 'ai_reprocessing', json.dumps(job_data)))
        
        jobs_added += 1
        
        if jobs_added % 25 == 0:
            print(f'  ✅ Queued {jobs_added} jobs...')
    
    conn.commit()
    conn.close()
    
    print(f'🎉 Successfully queued {jobs_added} reprocessing jobs!')
    print('Atlas background workers will process them automatically.')

if __name__ == '__main__':
    main()