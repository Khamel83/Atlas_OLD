#!/usr/bin/env python3
"""
Mass AI Reprocessing with Gemini 2.5 Flash Lite
Process ALL Atlas content with the new single optimal model
"""

import os
import time
import logging
from typing import List, Dict, Any
from atlas_model_client import create_client
from helpers.simple_database import SimpleDatabase

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('mass_reprocessing.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Set API key
os.environ['OPENROUTER_API_KEY'] = "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"

class MassAIReprocessor:
    def __init__(self):
        self.client = create_client()
        self.db = SimpleDatabase()
        self.processed_count = 0
        self.total_cost = 0.0
        self.total_tokens = 0
        self.errors = []
        
    def ensure_ai_columns(self):
        """Add AI processing columns to database if they don't exist"""
        with self.db.get_connection() as conn:
            # Check existing columns
            schema = conn.execute('PRAGMA table_info(content)').fetchall()
            existing_cols = [col[1] for col in schema]
            
            # Add missing columns
            if 'ai_summary' not in existing_cols:
                conn.execute('ALTER TABLE content ADD COLUMN ai_summary TEXT')
                logger.info("Added ai_summary column")
                
            if 'ai_tags' not in existing_cols:
                conn.execute('ALTER TABLE content ADD COLUMN ai_tags TEXT')
                logger.info("Added ai_tags column")
                
            if 'ai_socratic' not in existing_cols:
                conn.execute('ALTER TABLE content ADD COLUMN ai_socratic TEXT')
                logger.info("Added ai_socratic column")
                
            if 'ai_patterns' not in existing_cols:
                conn.execute('ALTER TABLE content ADD COLUMN ai_patterns TEXT')
                logger.info("Added ai_patterns column")
                
            if 'ai_recommendations' not in existing_cols:
                conn.execute('ALTER TABLE content ADD COLUMN ai_recommendations TEXT')
                logger.info("Added ai_recommendations column")
                
            conn.commit()
    
    def get_content_batch(self, batch_size: int = 50, offset: int = 0) -> List[Dict]:
        """Get batch of content for processing"""
        with self.db.get_connection() as conn:
            cursor = conn.execute("""
                SELECT id, title, content, url 
                FROM content 
                WHERE content IS NOT NULL 
                AND length(content) > 100
                AND (ai_summary IS NULL OR ai_summary = '')
                ORDER BY id
                LIMIT ? OFFSET ?
            """, (batch_size, offset))
            
            items = []
            for row in cursor.fetchall():
                items.append({
                    'id': row[0],
                    'title': row[1] or 'Untitled',
                    'content': row[2],
                    'url': row[3] or ''
                })
            return items
    
    def process_item(self, item: Dict) -> Dict[str, Any]:
        """Process single content item with all 5 workloads"""
        results = {}
        item_cost = 0.0
        item_tokens = 0
        
        workloads = ['tags', 'summary', 'socratic', 'patterns', 'recommendations']
        
        for workload in workloads:
            try:
                # Add delay between requests to avoid rate limiting
                time.sleep(0.5)
                
                result, metadata = self.client.process_workload(
                    workload, 
                    item['content'], 
                    item['title']
                )
                
                if metadata['status'] == 'success':
                    results[f'ai_{workload}'] = result
                    item_cost += metadata['cost']
                    item_tokens += metadata['tokens']
                else:
                    results[f'ai_{workload}'] = f"ERROR: {metadata.get('error', 'Unknown error')}"
                    self.errors.append(f"Item {item['id']} {workload}: {metadata.get('error', 'Unknown error')}")
                    
            except Exception as e:
                results[f'ai_{workload}'] = f"EXCEPTION: {str(e)}"
                self.errors.append(f"Item {item['id']} {workload}: EXCEPTION: {str(e)}")
                logger.error(f"Exception processing item {item['id']} workload {workload}: {str(e)}")
        
        return {
            'results': results,
            'cost': item_cost,
            'tokens': item_tokens
        }
    
    def save_results(self, item_id: int, results: Dict[str, str]):
        """Save AI processing results to database"""
        with self.db.get_connection() as conn:
            conn.execute("""
                UPDATE content SET 
                    ai_tags = ?,
                    ai_summary = ?,
                    ai_socratic = ?,
                    ai_patterns = ?,
                    ai_recommendations = ?,
                    updated_at = datetime('now')
                WHERE id = ?
            """, (
                results.get('ai_tags', ''),
                results.get('ai_summary', ''),
                results.get('ai_socratic', ''),
                results.get('ai_patterns', ''),
                results.get('ai_recommendations', ''),
                item_id
            ))
            conn.commit()
    
    def process_all_content(self, batch_size: int = 20, max_items: int = None):
        """Process all content in the database"""
        logger.info("🚀 Starting mass AI reprocessing with Gemini 2.5 Flash Lite")
        logger.info(f"Model: {self.client.model_id}")
        logger.info(f"Cost: ${self.client.cost_per_1k_tokens * 1000:.2f}/1M tokens")
        logger.info(f"Quality Score: {self.client.quality_score}/10")
        
        # Ensure database has AI columns
        self.ensure_ai_columns()
        
        # Get total count
        with self.db.get_connection() as conn:
            total_count = conn.execute("""
                SELECT COUNT(*) FROM content 
                WHERE content IS NOT NULL 
                AND length(content) > 100
                AND (ai_summary IS NULL OR ai_summary = '')
            """).fetchone()[0]
        
        if max_items:
            total_count = min(total_count, max_items)
        
        logger.info(f"📊 Processing {total_count:,} content items")
        
        start_time = time.time()
        offset = 0
        
        while offset < total_count:
            # Get batch
            batch = self.get_content_batch(batch_size, offset)
            if not batch:
                break
                
            logger.info(f"📋 Processing batch {offset//batch_size + 1}: items {offset+1}-{min(offset+len(batch), total_count)} of {total_count:,}")
            
            for item in batch:
                try:
                    # Process with all workloads
                    processing_result = self.process_item(item)
                    
                    # Save results
                    self.save_results(item['id'], processing_result['results'])
                    
                    # Update counters
                    self.processed_count += 1
                    self.total_cost += processing_result['cost']
                    self.total_tokens += processing_result['tokens']
                    
                    # Progress update
                    if self.processed_count % 10 == 0:
                        elapsed = time.time() - start_time
                        rate = self.processed_count / elapsed
                        eta = (total_count - self.processed_count) / rate if rate > 0 else 0
                        
                        logger.info(f"✅ Processed {self.processed_count:,}/{total_count:,} items "
                                  f"({100*self.processed_count/total_count:.1f}%) - "
                                  f"Cost: ${self.total_cost:.4f}, "
                                  f"Rate: {rate:.1f} items/min, "
                                  f"ETA: {eta/60:.1f} min")
                    
                    # Respect rate limits
                    time.sleep(1.0)  # 1 second between items
                    
                except Exception as e:
                    logger.error(f"Failed to process item {item['id']}: {str(e)}")
                    self.errors.append(f"Item {item['id']}: FAILED: {str(e)}")
            
            offset += len(batch)
            
            # Check if we've reached max_items
            if max_items and offset >= max_items:
                break
        
        # Final summary
        elapsed = time.time() - start_time
        logger.info(f"🏆 MASS REPROCESSING COMPLETE!")
        logger.info(f"  Processed: {self.processed_count:,} items")
        logger.info(f"  Total cost: ${self.total_cost:.4f}")
        logger.info(f"  Total tokens: {self.total_tokens:,}")
        logger.info(f"  Average cost per item: ${self.total_cost/self.processed_count:.6f}")
        logger.info(f"  Processing time: {elapsed/60:.1f} minutes")
        logger.info(f"  Rate: {self.processed_count/(elapsed/60):.1f} items/minute")
        logger.info(f"  Errors: {len(self.errors)}")
        
        if self.errors:
            logger.warning(f"⚠️ {len(self.errors)} errors occurred:")
            for error in self.errors[:10]:  # Show first 10 errors
                logger.warning(f"  - {error}")
            if len(self.errors) > 10:
                logger.warning(f"  ... and {len(self.errors) - 10} more errors")

def main():
    """Main execution"""
    reprocessor = MassAIReprocessor()
    
    # Process all remaining content in database
    reprocessor.process_all_content(batch_size=20)

if __name__ == "__main__":
    main()