#!/usr/bin/env python3
"""
Create database schema for structured content insights.
Adds tables to store LLM-extracted entities, quotes, topics, and analysis.
"""

import sqlite3
import sys
from pathlib import Path

def create_insights_schema():
    """Create comprehensive schema for structured content insights."""
    
    # Connect to main Atlas database
    db_path = "data/atlas.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("🧠 Creating structured insights schema...")
    
    # 1. Content Insights table - main structured analysis
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS content_insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_id INTEGER NOT NULL,
            summary TEXT NOT NULL,
            key_points TEXT,  -- JSON array of key insights
            quality_score REAL,
            content_type_ai TEXT,  -- AI-determined content type
            extraction_model TEXT,
            extraction_timestamp TEXT,
            confidence_score REAL,
            processing_time_seconds REAL,
            FOREIGN KEY (content_id) REFERENCES content (id)
        )
    """)
    
    # 2. Entities table - people, companies, products mentioned
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS content_entities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            type TEXT NOT NULL,  -- person|company|product|org|location|misc
            canonical_name TEXT,
            confidence REAL,
            context TEXT,
            extraction_timestamp TEXT,
            FOREIGN KEY (content_id) REFERENCES content (id)
        )
    """)
    
    # 3. Quotes table - notable quotes and attributions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS content_quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            speaker TEXT,
            start_time TEXT,  -- For podcasts/videos
            end_time TEXT,
            confidence REAL,
            context TEXT,
            extraction_timestamp TEXT,
            FOREIGN KEY (content_id) REFERENCES content (id)
        )
    """)
    
    # 4. Topics table - hierarchical topic classification  
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS content_topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            relevance REAL,
            subtopics TEXT,  -- JSON array
            category TEXT,   -- tech|business|investment|personal|misc
            extraction_timestamp TEXT,
            FOREIGN KEY (content_id) REFERENCES content (id)
        )
    """)
    
    # 5. Thesis/Arguments table - key theses and investment arguments
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS content_theses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_id INTEGER NOT NULL,
            statement TEXT NOT NULL,
            rationale TEXT NOT NULL,
            confidence REAL,
            category TEXT,  -- investment|technical|business|misc
            supporting_evidence TEXT,
            extraction_timestamp TEXT,
            FOREIGN KEY (content_id) REFERENCES content (id)
        )
    """)
    
    # 6. Content Relations table - relationships between content
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS content_relations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_id_1 INTEGER NOT NULL,
            content_id_2 INTEGER NOT NULL,
            relation_type TEXT NOT NULL,  -- similar|references|contradicts|builds_on
            strength REAL,  -- 0-1 relationship strength
            explanation TEXT,
            extraction_timestamp TEXT,
            FOREIGN KEY (content_id_1) REFERENCES content (id),
            FOREIGN KEY (content_id_2) REFERENCES content (id)
        )
    """)
    
    # Commit table creation first
    conn.commit()
    
    # Create indexes for better performance
    print("📊 Creating performance indexes...")
    
    indexes = [
        "CREATE INDEX IF NOT EXISTS idx_content_insights_content_id ON content_insights(content_id)",
        "CREATE INDEX IF NOT EXISTS idx_content_insights_quality ON content_insights(quality_score DESC)",
        "CREATE INDEX IF NOT EXISTS idx_entities_content_id ON content_entities(content_id)",
        "CREATE INDEX IF NOT EXISTS idx_entities_type ON content_entities(type)",
        "CREATE INDEX IF NOT EXISTS idx_entities_name ON content_entities(canonical_name)",
        "CREATE INDEX IF NOT EXISTS idx_quotes_content_id ON content_quotes(content_id)", 
        "CREATE INDEX IF NOT EXISTS idx_quotes_speaker ON content_quotes(speaker)",
        "CREATE INDEX IF NOT EXISTS idx_topics_content_id ON content_topics(content_id)",
        "CREATE INDEX IF NOT EXISTS idx_topics_name ON content_topics(name)",
        "CREATE INDEX IF NOT EXISTS idx_topics_relevance ON content_topics(relevance DESC)",
        "CREATE INDEX IF NOT EXISTS idx_theses_content_id ON content_theses(content_id)",
        "CREATE INDEX IF NOT EXISTS idx_theses_category ON content_theses(category)",
        "CREATE INDEX IF NOT EXISTS idx_relations_content1 ON content_relations(content_id_1)",
        "CREATE INDEX IF NOT EXISTS idx_relations_content2 ON content_relations(content_id_2)",
        "CREATE INDEX IF NOT EXISTS idx_relations_type ON content_relations(relation_type)"
    ]
    
    for index_sql in indexes:
        cursor.execute(index_sql)
    
    # Check current state
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%content_%'")
    tables = [row[0] for row in cursor.fetchall()]
    
    conn.commit()
    conn.close()
    
    print("✅ Insights schema created successfully!")
    print(f"📋 Tables created: {', '.join(tables)}")
    print()
    print("🔍 Schema Summary:")
    print("   - content_insights: Main structured analysis per content item")
    print("   - content_entities: People, companies, products mentioned") 
    print("   - content_quotes: Notable quotes with attribution")
    print("   - content_topics: Hierarchical topic classification")
    print("   - content_theses: Key arguments and investment theses")
    print("   - content_relations: Relationships between content items")
    print()
    print("🚀 Ready for structured extraction processing!")
    
    return True

def validate_schema():
    """Validate the created schema works correctly."""
    try:
        conn = sqlite3.connect("data/atlas.db")
        cursor = conn.cursor()
        
        # Test insert into insights table
        cursor.execute("""
            INSERT OR IGNORE INTO content_insights 
            (content_id, summary, quality_score, content_type_ai, extraction_model, extraction_timestamp, confidence_score)
            VALUES (1, 'Test summary', 0.95, 'article', 'gpt-4o-mini', datetime('now'), 0.9)
        """)
        
        # Test query
        cursor.execute("SELECT COUNT(*) FROM content_insights")
        count = cursor.fetchone()[0]
        
        conn.rollback()  # Don't actually save test data
        conn.close()
        
        print(f"✅ Schema validation successful (test record handled)")
        return True
        
    except Exception as e:
        print(f"❌ Schema validation failed: {e}")
        return False

def main():
    """Main execution"""
    print("🧠 Atlas Structured Insights Schema Creator")
    print("=" * 50)
    
    # Create schema
    if create_insights_schema():
        # Validate it works
        validate_schema()
        print("🎉 Insights database schema ready for AI-powered content analysis!")
    else:
        print("❌ Failed to create insights schema")
        sys.exit(1)

if __name__ == "__main__":
    main()