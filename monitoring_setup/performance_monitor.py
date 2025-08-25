#!/usr/bin/env python3
import psutil
import requests
import json
import sqlite3
from datetime import datetime
import os

def get_system_metrics():
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
        'load_average': os.getloadavg()[0] if hasattr(os, 'getloadavg') else 0
    }

def get_atlas_metrics():
    try:
        # API response time
        start_time = time.time()
        response = requests.get('http://localhost:8000/api/v1/health', timeout=10)
        api_response_time = (time.time() - start_time) * 1000
        
        # Database metrics
        db_path = 'atlas.db'
        if os.path.exists(db_path):
            db_size = os.path.getsize(db_path) / (1024 * 1024)  # MB
            
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM content")
            content_count = cursor.fetchone()[0]
            conn.close()
        else:
            db_size = 0
            content_count = 0
        
        return {
            'api_response_time_ms': api_response_time,
            'database_size_mb': db_size,
            'content_count': content_count,
            'api_healthy': response.status_code == 200
        }
    except Exception as e:
        return {
            'api_response_time_ms': -1,
            'database_size_mb': 0,
            'content_count': 0,
            'api_healthy': False,
            'error': str(e)
        }

def main():
    metrics = {
        'timestamp': datetime.now().isoformat(),
        'system': get_system_metrics(),
        'atlas': get_atlas_metrics()
    }
    
    # Write to log file
    with open('logs/performance_metrics.log', 'a') as f:
        f.write(json.dumps(metrics) + '\n')
    
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    import time
    main()
