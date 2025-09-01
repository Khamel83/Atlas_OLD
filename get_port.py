#!/usr/bin/env python3
"""
Universal port getter for Atlas
Returns the configured port from .env file
"""
import os
from dotenv import load_dotenv

def get_atlas_port():
    """Get Atlas port from environment, defaulting to 7444"""
    load_dotenv()
    return int(os.getenv('API_PORT', 7444))

def get_atlas_url():
    """Get full Atlas URL"""
    port = get_atlas_port()
    host = os.getenv('API_HOST', 'localhost')
    return f"http://{host}:{port}"

if __name__ == "__main__":
    print(get_atlas_port())