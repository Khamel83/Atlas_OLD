#!/usr/bin/env python3
"""
Test script for persistent authentication strategy
"""

import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.persistent_auth_strategy import PersistentAuthStrategy

def test_auth():
    """Test authentication with real credentials"""
    config = load_config()
    
    print("🔐 Testing Persistent Authentication Strategy")
    print("=" * 50)
    
    # Test URLs
    test_urls = [
        "https://www.nytimes.com/2024/12/01/business/economy/inflation-november.html",
        "https://www.wsj.com/business/energy-oil/oil-companies-bet-on-trump-cutting-red-tape-d7234567"
    ]
    
    auth_strategy = PersistentAuthStrategy(config)
    
    for url in test_urls:
        print(f"\n🔗 Testing: {url}")
        
        try:
            result = auth_strategy.fetch(url, log_path="test_auth.log")
            
            if result.success:
                print(f"✅ SUCCESS with {result.method}")
                print(f"   Title: {result.title or 'N/A'}")
                print(f"   Content length: {len(result.content) if result.content else 0} chars")
                print(f"   Truncated: {result.is_truncated}")
                
                if result.content:
                    # Show first 200 chars
                    preview = result.content.replace('\n', ' ')[:200] + "..."
                    print(f"   Preview: {preview}")
            else:
                print(f"❌ FAILED: {result.error}")
                
        except Exception as e:
            print(f"💥 ERROR: {e}")
    
    # Cleanup
    auth_strategy.cleanup()
    print("\n✅ Test completed")

if __name__ == "__main__":
    test_auth()