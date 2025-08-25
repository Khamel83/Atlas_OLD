#!/usr/bin/env python3
import re
import json
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import glob

def analyze_logs(hours=24):
    log_files = glob.glob('logs/*.log')
    
    errors = []
    warnings = []
    requests = []
    
    cutoff_time = datetime.now() - timedelta(hours=hours)
    
    for log_file in log_files:
        try:
            with open(log_file, 'r') as f:
                for line in f:
                    if 'ERROR' in line:
                        errors.append(line.strip())
                    elif 'WARNING' in line:
                        warnings.append(line.strip())
                    elif 'REQUEST' in line or 'GET' in line or 'POST' in line:
                        requests.append(line.strip())
        except Exception as e:
            continue
    
    analysis = {
        'timestamp': datetime.now().isoformat(),
        'period_hours': hours,
        'error_count': len(errors),
        'warning_count': len(warnings),
        'request_count': len(requests),
        'recent_errors': errors[-10:] if errors else [],
        'recent_warnings': warnings[-5:] if warnings else []
    }
    
    return analysis

def main():
    analysis = analyze_logs()
    
    # Write analysis to file
    with open('logs/log_analysis.json', 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print(json.dumps(analysis, indent=2))
    
    # Alert if too many errors
    if analysis['error_count'] > 10:
        print(f"⚠️  HIGH ERROR COUNT: {analysis['error_count']} errors in last 24h")
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
