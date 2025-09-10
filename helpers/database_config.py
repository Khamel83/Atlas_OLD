"""
Centralized Database Configuration for Atlas

This module provides a single source of truth for all database paths and connections
throughout the Atlas system. Use this to prevent database path inconsistencies.

Usage:
    from helpers.database_config import get_database_path, get_database_connection
    
    # Get the canonical database path
    db_path = get_database_path()
    
    # Get a database connection
    conn = get_database_connection()
"""

import os
import sqlite3
import threading
import time
import logging
from pathlib import Path
from typing import Union, Optional
from queue import Queue, Empty
from datetime import datetime


class DatabaseConfig:
    """Centralized database configuration for Atlas with durability and pooling."""
    
    def __init__(self):
        """Initialize database configuration."""
        # Use environment variable or default to data/atlas.db
        self._db_path = self._determine_database_path()
        self._ensure_database_directory()
        
        # Connection pool settings
        self._max_connections = 10
        self._connection_pool = Queue(maxsize=self._max_connections)
        self._pool_lock = threading.Lock()
        self._pool_initialized = False
        
        # Durability settings
        self._wal_enabled = False
        self._last_integrity_check = None
        self._backup_directory = self._db_path.parent / "backups"
        self._backup_directory.mkdir(exist_ok=True)
        
        # Logging
        self.logger = logging.getLogger(__name__)
    
    def _determine_database_path(self) -> Path:
        """Determine the canonical database path."""
        # Check ATLAS_DB_PATH environment variable first
        env_path = os.getenv('ATLAS_DB_PATH')
        if env_path:
            project_root = Path(__file__).parent.parent
            return project_root / env_path
        
        # Fallback to legacy ATLAS_DATABASE_PATH
        legacy_env_path = os.getenv('ATLAS_DATABASE_PATH')
        if legacy_env_path:
            return Path(legacy_env_path).resolve()
        
        # Default to data/atlas.db relative to project root
        project_root = Path(__file__).parent.parent
        return project_root / "data" / "atlas.db"
    
    def _ensure_database_directory(self):
        """Ensure the database directory exists."""
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
    
    @property
    def path(self) -> Path:
        """Get the canonical database path."""
        return self._db_path
    
    @property
    def path_str(self) -> str:
        """Get the canonical database path as string."""
        return str(self._db_path)
    
    def _configure_connection(self, conn: sqlite3.Connection) -> sqlite3.Connection:
        """Configure a connection with durability settings."""
        try:
            # Enable WAL mode for better concurrency and durability
            conn.execute("PRAGMA journal_mode=WAL")
            
            # Durability settings
            conn.execute("PRAGMA synchronous=NORMAL")  # Balance between safety and performance
            conn.execute("PRAGMA cache_size=-64000")   # 64MB cache
            conn.execute("PRAGMA busy_timeout=30000")  # 30 second busy timeout
            conn.execute("PRAGMA foreign_keys=ON")     # Enable foreign key constraints
            conn.execute("PRAGMA temp_store=MEMORY")   # Store temp tables in memory
            
            # Check if WAL mode was enabled
            cursor = conn.cursor()
            cursor.execute("PRAGMA journal_mode")
            mode = cursor.fetchone()[0]
            if mode.upper() == 'WAL' and not self._wal_enabled:
                self._wal_enabled = True
                self.logger.info("SQLite WAL mode enabled for enhanced durability")
            
            return conn
        except Exception as e:
            self.logger.error(f"Failed to configure database connection: {e}")
            raise

    def get_connection(self) -> sqlite3.Connection:
        """Get a configured database connection."""
        conn = sqlite3.connect(str(self._db_path), check_same_thread=False)
        return self._configure_connection(conn)
    
    def get_pooled_connection(self) -> sqlite3.Connection:
        """Get a connection from the pool."""
        if not self._pool_initialized:
            self._initialize_pool()
        
        try:
            # Try to get a connection from pool with timeout
            conn = self._connection_pool.get(timeout=5.0)
            # Test if connection is still valid
            try:
                conn.execute("SELECT 1")
                return conn
            except sqlite3.Error:
                # Connection is stale, create new one
                conn.close()
                return self.get_connection()
        except Empty:
            # Pool is empty, create new connection
            return self.get_connection()
    
    def return_connection(self, conn: sqlite3.Connection):
        """Return a connection to the pool."""
        if conn and not self._connection_pool.full():
            try:
                self._connection_pool.put_nowait(conn)
            except:
                conn.close()
        else:
            if conn:
                conn.close()
    
    def _initialize_pool(self):
        """Initialize the connection pool."""
        with self._pool_lock:
            if self._pool_initialized:
                return
            
            # Pre-populate pool with connections
            for _ in range(min(3, self._max_connections)):  # Start with 3 connections
                try:
                    conn = self.get_connection()
                    self._connection_pool.put_nowait(conn)
                except Exception as e:
                    self.logger.error(f"Failed to initialize connection pool: {e}")
                    break
            
            self._pool_initialized = True
            self.logger.info(f"Database connection pool initialized with {self._connection_pool.qsize()} connections")
    
    def check_integrity(self) -> bool:
        """Check database integrity."""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("PRAGMA integrity_check")
            result = cursor.fetchone()[0]
            conn.close()
            
            if result == "ok":
                self._last_integrity_check = datetime.now()
                self.logger.info("Database integrity check passed")
                return True
            else:
                self.logger.error(f"Database integrity check failed: {result}")
                return False
        except Exception as e:
            self.logger.error(f"Failed to check database integrity: {e}")
            return False
    
    def should_check_integrity(self) -> bool:
        """Check if integrity check is due (every 24 hours)."""
        if not self._last_integrity_check:
            return True
        
        hours_since_check = (datetime.now() - self._last_integrity_check).total_seconds() / 3600
        return hours_since_check >= 24
    
    def vacuum_if_needed(self) -> bool:
        """Vacuum database if fragmentation > 25%."""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # Get page count and free pages
            cursor.execute("PRAGMA page_count")
            page_count = cursor.fetchone()[0]
            cursor.execute("PRAGMA freelist_count") 
            free_pages = cursor.fetchone()[0]
            
            if page_count > 0:
                fragmentation = (free_pages / page_count) * 100
                if fragmentation > 25:
                    self.logger.info(f"Database fragmentation at {fragmentation:.1f}%, running VACUUM")
                    cursor.execute("VACUUM")
                    conn.close()
                    self.logger.info("Database VACUUM completed")
                    return True
                else:
                    self.logger.debug(f"Database fragmentation at {fragmentation:.1f}%, VACUUM not needed")
            
            conn.close()
            return False
        except Exception as e:
            self.logger.error(f"Failed to vacuum database: {e}")
            return False
    
    def create_backup(self) -> Optional[Path]:
        """Create a database backup."""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = self._backup_directory / f"atlas_backup_{timestamp}.db"
            
            # Use SQLite backup API for consistent backup
            source_conn = self.get_connection()
            backup_conn = sqlite3.connect(str(backup_path), check_same_thread=False)
            
            source_conn.backup(backup_conn)
            
            backup_conn.close()
            source_conn.close()
            
            self.logger.info(f"Database backup created: {backup_path}")
            return backup_path
        except Exception as e:
            self.logger.error(f"Failed to create database backup: {e}")
            return None
    
    def restore_from_backup(self, backup_path: Optional[Path] = None) -> bool:
        """Restore database from backup."""
        try:
            if not backup_path:
                # Find most recent backup
                backups = list(self._backup_directory.glob("atlas_backup_*.db"))
                if not backups:
                    self.logger.error("No backups found for restoration")
                    return False
                backup_path = max(backups, key=lambda p: p.stat().st_mtime)
            
            if not backup_path.exists():
                self.logger.error(f"Backup file not found: {backup_path}")
                return False
            
            # Create backup of current DB before restore
            self.create_backup()
            
            # Restore from backup
            backup_conn = sqlite3.connect(str(backup_path), check_same_thread=False)
            current_conn = sqlite3.connect(str(self._db_path), check_same_thread=False)
            
            backup_conn.backup(current_conn)
            
            current_conn.close()
            backup_conn.close()
            
            self.logger.info(f"Database restored from backup: {backup_path}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to restore from backup: {e}")
            return False


# Global instance
_db_config = DatabaseConfig()


def get_database_path() -> Path:
    """Get the canonical Atlas database path.
    
    Returns:
        Path to the Atlas database file
    """
    return _db_config.path


def get_database_path_str() -> str:
    """Get the canonical Atlas database path as string.
    
    Returns:
        String path to the Atlas database file
    """
    return _db_config.path_str


def get_database_connection() -> sqlite3.Connection:
    """Get a connection to the Atlas database.
    
    Returns:
        SQLite connection to the Atlas database
    """
    return _db_config.get_connection()


def get_pooled_connection() -> sqlite3.Connection:
    """Get a pooled connection to the Atlas database.
    
    Returns:
        SQLite connection from the connection pool
    """
    return _db_config.get_pooled_connection()


def return_pooled_connection(conn: sqlite3.Connection):
    """Return a connection to the pool.
    
    Args:
        conn: Connection to return to pool
    """
    _db_config.return_connection(conn)


def test_database_integrity() -> bool:
    """Test database integrity.
    
    Returns:
        True if integrity check passes
    """
    return _db_config.check_integrity()


def vacuum_database() -> bool:
    """Vacuum database if needed.
    
    Returns:
        True if vacuum was performed
    """
    return _db_config.vacuum_if_needed()


def create_database_backup() -> Optional[Path]:
    """Create a database backup.
    
    Returns:
        Path to backup file if successful
    """
    return _db_config.create_backup()


def restore_database(backup_path: Optional[Path] = None) -> bool:
    """Restore database from backup.
    
    Args:
        backup_path: Path to backup file (uses latest if None)
        
    Returns:
        True if restore successful
    """
    return _db_config.restore_from_backup(backup_path)


def update_database_path(new_path: Union[str, Path]) -> None:
    """Update the database path (for migration purposes).
    
    Args:
        new_path: New database path
    """
    global _db_config
    _db_config._db_path = Path(new_path).resolve()
    _db_config._ensure_database_directory()


# Backward compatibility functions
def get_atlas_db_path() -> str:
    """Backward compatibility function."""
    return get_database_path_str()


if __name__ == "__main__":
    print(f"Atlas Database Path: {get_database_path()}")
    print(f"Database exists: {get_database_path().exists()}")
    
    # Test connection
    try:
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
        table_count = cursor.fetchone()[0]
        conn.close()
        print(f"Database tables: {table_count}")
    except Exception as e:
        print(f"Database connection error: {e}")