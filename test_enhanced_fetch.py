#!/usr/bin/env python3
"""
Test script for enhanced article fetching strategies
"""

import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.article_strategies import ArticleFetcher

def test_nytimes_fetch():
    """Test NYTimes authenticated fetch"""
    config = load_config()
    fetcher = ArticleFetcher(config)
    
    # Test with a failed NYTimes URL from our dataset
    nytimes_url = "http://www.nytimes.com/2016/02/07/nyregion/jeremy-wilson-a-compulsive-con-man.html"
    
    print(f"Testing enhanced fetch for: {nytimes_url}")
    print(f"NYTimes credentials configured: {bool(config.get('NYTIMES_USERNAME'))}")
    
    result = fetcher.fetch_with_fallbacks(nytimes_url, "test_log")
    
    print(f"Success: {result.success}")
    print(f"Method: {result.method}")
    print(f"Content length: {len(result.content) if result.content else 0}")
    print(f"Error: {result.error}")
    
    if result.success:
        print("✅ Enhanced fetch SUCCESS!")
        return True
    else:
        print("❌ Enhanced fetch failed")
        return False

if __name__ == "__main__":
    test_nytimes_fetch()