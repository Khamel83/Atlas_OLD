#!/usr/bin/env python3
"""
Test simplified authentication approach
"""

import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.article_strategies import PaywallAuthenticatedStrategy

def test_simple_auth():
    """Test the updated authentication"""
    config = load_config()
    auth_strategy = PaywallAuthenticatedStrategy(config)
    
    print("🔐 Testing Updated Authentication")
    print("⏱️  With improved error handling and multiple login attempts")
    
    # Test with a paywall article
    test_urls = [
        ("NYTimes", "https://www.nytimes.com/2024/10/19/magazine/mia-khalifa-interview.html"),
        ("WSJ", "http://www.wsj.com/articles/how-law-order-creator-dick-wolf-took-chicago-1447357783")
    ]
    
    for site, url in test_urls:
        print(f"\n🗞️  Testing {site}: {url}")
        
        result = auth_strategy.fetch(url, "simple_auth_test")
        
        if result.success:
            print(f"🎉 {site} Authentication SUCCESS!")
            print(f"   Content length: {len(result.content):,} characters")
            
            # Quick paywall check
            content_lower = result.content.lower()
            paywall_indicators = ['subscribe', 'subscription', 'sign in to continue', 'create account']
            paywall_found = any(indicator in content_lower for indicator in paywall_indicators)
            
            if not paywall_found and len(result.content) > 15000:
                print("✅ Full authenticated content retrieved!")
            else:
                print("⚠️  May still contain paywall elements")
                
        else:
            print(f"❌ {site} failed: {result.error}")
        
        print("-" * 60)

if __name__ == "__main__":
    test_simple_auth()