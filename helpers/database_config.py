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
from pathlib import Path
from typing import Union


class DatabaseConfig:
    """Centralized database configuration for Atlas."""
    
    def __init__(self):
        """Initialize database configuration."""
        # Use environment variable or default to data/atlas.db
        self._db_path = self._determine_database_path()
        self._ensure_database_directory()
    
    def _determine_database_path(self) -> Path:
        """Determine the canonical database path."""
        # Check environment variable first
        env_path = os.getenv('ATLAS_DATABASE_PATH')
        if env_path:
            return Path(env_path).resolve()
        
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
    
    def get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        return sqlite3.connect(str(self._db_path))


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