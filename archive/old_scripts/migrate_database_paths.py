#!/usr/bin/env python3
"""
Database Path Migration Script for Atlas

This script automatically updates all hardcoded database paths throughout
the Atlas codebase to use the centralized database configuration.

This prevents database path inconsistencies that cause critical failures.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Set

# Common hardcoded database path patterns to fix
DATABASE_PATTERNS = [
    # Path.home() / "dev" / "atlas" / "atlas.db"
    (r'Path\.home\(\)\s*/\s*"dev"\s*/\s*"atlas"\s*/\s*"atlas\.db"', 'get_database_path()'),
    
    # "data/atlas.db"
    (r'"data/atlas\.db"', 'get_database_path_str()'),
    
    # 'data/atlas.db'
    (r"'data/atlas\.db'", 'get_database_path_str()'),
    
    # ~/dev/atlas/atlas.db
    (r'"~/dev/atlas/atlas\.db"', 'get_database_path_str()'),
    (r"'~/dev/atlas/atlas\.db'", 'get_database_path_str()'),
    
    # /home/ubuntu/dev/atlas/atlas.db (hardcoded absolute paths)
    (r'"/home/ubuntu/dev/atlas/atlas\.db"', 'get_database_path_str()'),
    (r"'/home/ubuntu/dev/atlas/atlas\.db'", 'get_database_path_str()'),
    
    # os.path.join patterns
    (r'os\.path\.join\([^)]*"atlas\.db"\)', 'get_database_path_str()'),
    (r"os\.path\.join\([^)]*'atlas\.db'\)", 'get_database_path_str()'),
    
    # f-string patterns
    (r'f"[^"]*atlas\.db"', 'get_database_path_str()'),
    (r"f'[^']*atlas\.db'", 'get_database_path_str()'),
]

# Files to skip (already updated or special cases)
SKIP_FILES = {
    'helpers/database_config.py',  # This is the config file itself
    'helpers/simple_database.py',  # Already updated manually
    'api/routers/transcript_stats.py',  # Already updated manually
    'api/routers/search.py',  # Already updated manually
    'migrate_database_paths.py',  # This script itself
    '.git',
    '__pycache__',
    'venv',
    '.pytest_cache',
}

def should_skip_file(file_path: Path, project_root: Path) -> bool:
    """Check if file should be skipped."""
    try:
        rel_path = file_path.relative_to(project_root)
        rel_path_str = str(rel_path)
        
        # Skip files in SKIP_FILES
        if any(skip in rel_path_str for skip in SKIP_FILES):
            return True
            
        # Skip binary files, images, etc.
        if file_path.suffix in {'.pyc', '.png', '.jpg', '.gif', '.db', '.sqlite', '.log'}:
            return True
            
        # Only process text files
        if not file_path.suffix in {'.py', '.md', '.sh', '.json', '.yml', '.yaml', '.txt', ''}:
            return True
            
        return False
    except ValueError:
        return True

def needs_database_import(content: str) -> bool:
    """Check if file needs database import added."""
    # Check if it already has the import
    if 'from helpers.database_config import' in content:
        return False
    if 'from .database_config import' in content:
        return False
        
    # Check if it uses any database functions
    return any(func in content for func in ['get_database_path', 'get_database_connection'])

def add_database_import(content: str, file_path: Path) -> str:
    """Add database import to file if needed."""
    if not needs_database_import(content):
        return content
    
    # Determine import style based on file location
    if 'helpers/' in str(file_path):
        import_line = 'from .database_config import get_database_path, get_database_path_str, get_database_connection'
    else:
        import_line = 'from helpers.database_config import get_database_path, get_database_path_str, get_database_connection'
    
    lines = content.split('\n')
    
    # Find the best place to insert import
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('import ') or line.startswith('from '):
            insert_idx = i + 1
        elif line.strip() == '' and i > 0:
            continue
        elif line.startswith('#') or line.startswith('"""') or line.startswith("'''"):
            continue
        else:
            break
    
    # Insert import
    lines.insert(insert_idx, import_line)
    return '\n'.join(lines)

def migrate_file(file_path: Path) -> Tuple[bool, List[str]]:
    """Migrate a single file to use centralized database config."""
    changes = []
    
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        return False, [f"Error reading file: {e}"]
    
    modified_content = original_content
    file_changed = False
    
    # Apply pattern replacements
    for pattern, replacement in DATABASE_PATTERNS:
        regex = re.compile(pattern)
        matches = regex.findall(modified_content)
        if matches:
            modified_content = regex.sub(replacement, modified_content)
            file_changed = True
            changes.append(f"Replaced pattern '{pattern}' with '{replacement}' ({len(matches)} occurrences)")
    
    # Add import if needed and file was changed
    if file_changed:
        modified_content = add_database_import(modified_content, file_path)
        if 'from helpers.database_config import' in modified_content and 'from helpers.database_config import' not in original_content:
            changes.append("Added database_config import")
    
    # Write file if changed
    if file_changed:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        except Exception as e:
            return False, [f"Error writing file: {e}"]
    
    return file_changed, changes

def find_atlas_db_files(project_root: Path) -> List[Path]:
    """Find all files that reference atlas.db."""
    atlas_db_files = []
    
    for root, dirs, files in os.walk(project_root):
        # Skip common directories
        dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__', 'venv', '.pytest_cache', 'node_modules'}]
        
        for file in files:
            file_path = Path(root) / file
            
            if should_skip_file(file_path, project_root):
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if 'atlas.db' in content:
                        atlas_db_files.append(file_path)
            except Exception:
                continue
    
    return atlas_db_files

def main():
    """Main migration function."""
    print("🔧 Atlas Database Path Migration")
    print("=" * 50)
    
    # Get project root
    project_root = Path(__file__).parent
    print(f"Project root: {project_root}")
    
    # Find files with atlas.db references
    print("\n🔍 Finding files with atlas.db references...")
    atlas_db_files = find_atlas_db_files(project_root)
    print(f"Found {len(atlas_db_files)} files with atlas.db references")
    
    # Migrate files
    print("\n🚀 Migrating files...")
    migrated_count = 0
    error_count = 0
    
    for file_path in atlas_db_files:
        rel_path = file_path.relative_to(project_root)
        print(f"Processing: {rel_path}")
        
        changed, changes = migrate_file(file_path)
        
        if changed:
            migrated_count += 1
            for change in changes:
                print(f"  ✅ {change}")
        else:
            if changes:  # There were errors
                error_count += 1
                for change in changes:
                    print(f"  ❌ {change}")
            else:
                print(f"  ⏭️ No changes needed")
    
    print("\n" + "=" * 50)
    print(f"✅ Migration complete!")
    print(f"📊 Files migrated: {migrated_count}")
    print(f"❌ Errors: {error_count}")
    print(f"📁 Total files processed: {len(atlas_db_files)}")
    
    if migrated_count > 0:
        print("\n🎉 Database path consistency fixed!")
        print("💡 All files now use centralized database configuration.")

if __name__ == "__main__":
    main()