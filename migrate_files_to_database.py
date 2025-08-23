#!/usr/bin/env python3
"""
Migrate processed files to database

This script migrates processed content files to the main Atlas database,
populating the content table with metadata from processed files.
"""

import json
import os
import sqlite3
from pathlib import Path
from typing import Any, Dict, List

from helpers.metadata_manager import MetadataManager
from helpers.config import load_config


def get_processed_files(base_directory: str = "output") -> List[str]:
    """
    Get all processed metadata files.
    
    Args:
        base_directory: Base directory to search for metadata files
        
    Returns:
        List of paths to metadata files
    """
    metadata_files = []
    
    # Walk through the directory structure to find all .json files
    for root, dirs, files in os.walk(base_directory):
        for file in files:
            if file.endswith(".json"):
                metadata_files.append(os.path.join(root, file))
    
    return metadata_files


def load_metadata_file(file_path: str) -> Dict[str, Any]:
    """
    Load metadata from a JSON file.
    
    Args:
        file_path: Path to the metadata file
        
    Returns:
        Dictionary with metadata
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading metadata file {file_path}: {e}")
        return {}


def create_database_schema(db_path: str):
    """
    Create the database schema if it doesn't exist.
    
    Args:
        db_path: Path to the database file
    """
    try:
        with sqlite3.connect(db_path) as conn:
            # Create content table if it doesn't exist
            conn.execute('''
                CREATE TABLE IF NOT EXISTS content (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    uid TEXT UNIQUE,
                    content_type TEXT,
                    source TEXT,
                    title TEXT,
                    status TEXT,
                    created_at TEXT,
                    updated_at TEXT,
                    error TEXT,
                    tags TEXT,
                    metadata TEXT
                )
            ''')
            
            # Create indexes for performance
            conn.execute('CREATE INDEX IF NOT EXISTS idx_content_uid ON content (uid)')
            conn.execute('CREATE INDEX IF NOT EXISTS idx_content_type ON content (content_type)')
            conn.execute('CREATE INDEX IF NOT EXISTS idx_content_status ON content (status)')
            
        print("Database schema initialized")
    except Exception as e:
        print(f"Error creating database schema: {e}")


def insert_content_to_database(db_path: str, metadata: Dict[str, Any]) -> bool:
    """
    Insert content metadata into the database.
    
    Args:
        db_path: Path to the database file
        metadata: Content metadata dictionary
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with sqlite3.connect(db_path) as conn:
            # Convert metadata to database format to match existing schema
            id_val = metadata.get("uid", metadata.get("id", ""))
            title = metadata.get("title", "")
            content_type = metadata.get("content_type", "")
            source_url = metadata.get("source", metadata.get("source_url", ""))
            created_at = metadata.get("created_at", metadata.get("date", ""))
            metadata_json = json.dumps(metadata)
            
            # Read actual content from file paths
            content = metadata.get("content", "")
            content_path = metadata.get("content_path")
            if content_path and os.path.exists(content_path):
                try:
                    with open(content_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                except Exception as e:
                    print(f"Error reading content file {content_path}: {e}")
            
            # Skip if no meaningful content
            if not content or len(content.strip()) < 20:
                return False
            
            # Insert or replace content using existing schema (fix schema mismatch)
            conn.execute('''
                INSERT OR REPLACE INTO content 
                (title, url, content_type, metadata, created_at, updated_at, content)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (title, source_url, content_type, metadata_json, created_at, created_at, content))
            
        return True
    except Exception as e:
        print(f"Error inserting content to database: {e}")
        return False


def migrate_files_to_database():
    """
    Main function to migrate processed files to database.
    """
    # Load configuration
    config = load_config()
    
    # Database path - use actual location
    db_path = config.get("database_path", "atlas.db")
    
    # Create database schema
    create_database_schema(db_path)
    
    # Get processed files
    metadata_files = get_processed_files()
    print(f"Found {len(metadata_files)} metadata files to process")
    
    # Process files
    success_count = 0
    error_count = 0
    
    for file_path in metadata_files:
        try:
            # Load metadata
            metadata = load_metadata_file(file_path)
            if not metadata:
                error_count += 1
                continue
            
            # Insert into database
            if insert_content_to_database(db_path, metadata):
                success_count += 1
            else:
                error_count += 1
                
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
            error_count += 1
    
    print(f"Migration complete: {success_count} successful, {error_count} errors")
    
    # Verify results
    try:
        with sqlite3.connect(db_path) as conn:
            count = conn.execute('SELECT COUNT(*) FROM content').fetchone()[0]
            print(f"Database now contains {count} content entries")
    except Exception as e:
        print(f"Error verifying database: {e}")


if __name__ == "__main__":
    migrate_files_to_database()