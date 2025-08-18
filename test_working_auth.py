#!/usr/bin/env python3
"""
Test working authentication system on real NYTimes/WSJ articles
"""

import os
import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.simple_auth_strategy import SimpleAuthStrategy

def test_working_auth():
    """Test the working authentication system"""
    
    print("🔐 Testing Working Authentication System")
    print("=" * 50)
    
    config = load_config()
    auth_strategy = SimpleAuthStrategy(config)
    
    # Real NYTimes articles that should work with auth
    test_urls = [
        "https://www.nytimes.com/2024/12/15/business/economy/federal-reserve-interest-rates.html",
        "https://www.nytimes.com/2024/12/10/technology/ai-companies-regulation.html"
    ]
    
    for i, url in enumerate(test_urls, 1):
        print(f"\n🔗 Test {i}: {url}")
        
        try:
            result = auth_strategy.fetch(url, f"auth_test_{i}.log")
            
            if result.success:
                print(f"✅ SUCCESS with {result.method}")
                print(f"   Title: {result.title or 'N/A'}")
                print(f"   Content length: {len(result.content)} chars")
                print(f"   Truncated: {result.is_truncated}")
                
                if result.content and len(result.content) > 2000:
                    # Show meaningful content preview
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(result.content, 'html.parser')
                    text = soup.get_text()
                    
                    # Find article content (skip navigation, etc.)
                    paragraphs = [p.strip() for p in text.split('\n') if len(p.strip()) > 50]
                    if paragraphs:
                        preview = paragraphs[0][:300] + "..."
                        print(f"   Content preview: {preview}")
                        
                        # Check for paywall indicators
                        paywall_indicators = ['subscribe', 'sign in', 'login', 'register']
                        text_lower = text.lower()
                        paywall_found = any(indicator in text_lower for indicator in paywall_indicators)
                        print(f"   Paywall bypassed: {not paywall_found}")
                
            else:
                print(f"❌ FAILED: {result.error}")
                
        except Exception as e:
            print(f"💥 ERROR: {e}")
    
    print(f"\n✅ Authentication test completed")

if __name__ == "__main__":
    test_working_auth()