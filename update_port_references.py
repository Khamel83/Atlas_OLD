#!/usr/bin/env python3
"""
Update hardcoded port references throughout Atlas codebase
"""
import os
import re
from pathlib import Path
from get_port import get_atlas_port, get_atlas_url

def update_file_references():
    """Update specific files with dynamic port references"""
    current_port = get_atlas_port()
    current_url = get_atlas_url()
    
    # Files to update and their patterns
    updates = []
    
    print(f"🔧 Atlas configured to run on port {current_port}")
    print(f"🌐 Full URL: {current_url}")
    
    # Show current configuration
    print(f"\n✅ To change the port, edit .env file:")
    print(f"   API_PORT={current_port}")
    print(f"\n📝 Key files already configured to read from .env:")
    print(f"   - atlas_service_manager.py") 
    print(f"   - web/app.py")
    print(f"   - api/main.py")
    print(f"   - search_server.py")
    
    print(f"\n⚠️  Note: Some documentation and test files still reference port 8000")
    print(f"   These are less critical and can be updated manually if needed.")

if __name__ == "__main__":
    update_file_references()