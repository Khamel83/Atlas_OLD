#!/usr/bin/env python3
"""
Test real authenticated login without stealth
"""

import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.article_strategies import PaywallAuthenticatedStrategy

def test_authentic_login():
    """Test authentic login for paywall sites"""
    config = load_config()
    auth_strategy = PaywallAuthenticatedStrategy(config)
    
    print("🔐 Testing Authentic Paywall Login (No Stealth)")
    print(f"✅ NYTimes credentials: {bool(config.get('NYTIMES_USERNAME'))}")
    print(f"✅ WSJ credentials: {bool(config.get('WSJ_USERNAME'))}")
    
    # Test NYTimes authentication
    nyt_url = "https://www.nytimes.com/2024/10/19/magazine/mia-khalifa-interview.html"
    print(f"\n🗞️  Testing NYTimes auth with: {nyt_url}")
    
    result = auth_strategy.fetch(nyt_url, "auth_test")
    
    if result.success:
        print("🎉 NYTimes Authentication SUCCESS!")
        print(f"   Method: {result.method}")
        print(f"   Content length: {len(result.content):,} characters")
        print("   Full article content retrieved!")
        
        # Check if it's actually authenticated content
        if "subscribe" not in result.content.lower() and len(result.content) > 20000:
            print("✅ Appears to be full authenticated content (no paywall)")
        else:
            print("⚠️  May still be paywalled content")
    else:
        print(f"❌ NYTimes Authentication failed: {result.error}")
    
    return result.success

if __name__ == "__main__":
    test_authentic_login()