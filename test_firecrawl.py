#!/usr/bin/env python3
"""
Test Firecrawl integration with real API key
"""

import os
import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.firecrawl_strategy import FirecrawlStrategy

def test_firecrawl():
    """Test Firecrawl with real API key"""
    
    print("🔥 Testing Firecrawl Integration")
    print("=" * 50)
    
    config = load_config()
    firecrawl = FirecrawlStrategy(config)
    
    # Check API key
    if not firecrawl.api_key:
        print("❌ No Firecrawl API key found")
        return
    
    print(f"✅ API key configured: {firecrawl.api_key[:8]}...")
    
    # Check usage stats
    stats = firecrawl.get_usage_stats()
    print(f"📊 Usage stats:")
    print(f"   • Current month: {stats['current_month']}")
    print(f"   • Used this month: {stats['usage_this_month']}/{stats['monthly_limit']}")
    print(f"   • Remaining: {stats['remaining']}")
    print(f"   • Total used: {stats['total_used']}")
    
    # Test on a simple article
    test_urls = [
        "https://example.com/simple-test",
        "https://techcrunch.com/2024/12/01/ai-news-article"
    ]
    
    for i, url in enumerate(test_urls, 1):
        print(f"\n🔗 Test {i}: {url}")
        
        try:
            result = firecrawl.fetch(url, f"firecrawl_test_{i}.log")
            
            if result.success:
                print(f"✅ SUCCESS with Firecrawl")
                print(f"   Content length: {len(result.content)} chars")
                print(f"   Title: {result.title or 'N/A'}")
                print(f"   Content type: {result.metadata.get('content_type', 'unknown')}")
                print(f"   Truncated: {result.is_truncated}")
                
                if result.content:
                    # Show preview
                    preview = result.content.replace('\n', ' ')[:200] + "..."
                    print(f"   Preview: {preview}")
                
            else:
                print(f"❌ FAILED: {result.error}")
                
        except Exception as e:
            print(f"💥 ERROR: {e}")
        
        # Check updated usage
        stats = firecrawl.get_usage_stats()
        print(f"   Usage after request: {stats['usage_this_month']}/{stats['monthly_limit']}")
    
    print(f"\n📈 Final Usage Statistics:")
    final_stats = firecrawl.get_usage_stats()
    for key, value in final_stats.items():
        print(f"   • {key}: {value}")
    
    print(f"\n✅ Firecrawl test completed")

if __name__ == "__main__":
    test_firecrawl()