"""
Simple database interface for Atlas
"""

import sqlite3
import json
import os
from datetime import datetime
from pathlib import Path

class SimpleDatabase:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = Path.home() / "dev" / "atlas" / "atlas.db"
        
        self.db_path = db_path
        self._init_tables()
    
    def get_connection(self):
        """Get database connection"""
        return sqlite3.connect(self.db_path)
    
    def _init_tables(self):
        """Initialize database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Content table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS content (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                url TEXT,
                content TEXT,
                content_type TEXT,
                metadata TEXT,
                created_at TEXT,
                updated_at TEXT
            )
        """)
        
        # Worker jobs table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS worker_jobs (
                id TEXT PRIMARY KEY,
                type TEXT,
                data TEXT,
                priority INTEGER,
                status TEXT DEFAULT 'pending',
                assigned_worker TEXT,
                created_at TEXT,
                assigned_at TEXT,
                completed_at TEXT,
                result TEXT
            )
        """)
        
        # Workers table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workers (
                worker_id TEXT PRIMARY KEY,
                capabilities TEXT,
                platform TEXT,
                whisper_available INTEGER,
                ytdlp_available INTEGER,
                metadata TEXT,
                registered_at TEXT,
                last_seen TEXT,
                status TEXT DEFAULT 'active'
            )
        """)
        
        # Transcriptions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transcriptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT,
                transcript TEXT,
                source TEXT,
                metadata TEXT,
                created_at TEXT,
                processed INTEGER DEFAULT 0
            )
        """)
        
        conn.commit()
        conn.close()
    
    def store_content(self, content, title, url, content_type, metadata=None):
        """Store content record"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        now = datetime.utcnow().isoformat()
        
        cursor.execute("""
            INSERT INTO content (title, url, content, content_type, metadata, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            title,
            url, 
            content,
            content_type,
            json.dumps(metadata or {}),
            now,
            now
        ))
        
        content_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return content_id
    
    def store_transcription(self, transcription_data):
        """Store transcription record"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO transcriptions (filename, transcript, source, metadata, created_at, processed)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            transcription_data['filename'],
            transcription_data['transcript'],
            transcription_data['source'], 
            transcription_data['metadata'],
            transcription_data['created_at'],
            1 if transcription_data.get('processed', False) else 0
        ))
        
        transcription_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return transcription_id
    
    def _get_current_timestamp(self):
        """Get current timestamp"""
        return datetime.utcnow().isoformat()