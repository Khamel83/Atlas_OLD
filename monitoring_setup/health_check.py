#!/usr/bin/env python3
import requests
import sys
import json
from datetime import datetime

def check_api_health():
    try:
        response = requests.get('http://localhost:8000/api/v1/health', timeout=10)
        return response.status_code == 200
    except:
        return False

def check_database_health():
    try:
        from helpers.simple_database import SimpleDatabase
        db = SimpleDatabase()
        content = db.get_all_content()
        return True
    except:
        return False

def check_search_health():
    try:
        response = requests.get('http://localhost:8000/api/v1/search/?q=test&limit=1', timeout=10)
        return response.status_code == 200
    except:
        return False

def main():
    checks = {
        'api': check_api_health(),
        'database': check_database_health(),
        'search': check_search_health(),
        'timestamp': datetime.now().isoformat()
    }
    
    all_healthy = all(checks[k] for k in ['api', 'database', 'search'])
    
    print(json.dumps(checks, indent=2))
    sys.exit(0 if all_healthy else 1)

if __name__ == "__main__":
    main()
