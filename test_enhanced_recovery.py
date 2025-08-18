#!/usr/bin/env python3
"""
Test Enhanced Recovery Strategies for Failed Articles
"""

import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.article_strategies import ArticleFetcher, EnhancedWaybackMachineStrategy

def test_recovery_strategies():
    """Test Enhanced Wayback and other recovery strategies on real failed URLs"""
    
    print("🔄 Testing Enhanced Recovery Strategies")
    print("=" * 50)
    
    # Load config
    config = load_config()
    
    # Test URLs from different categories
    test_urls = [
        # NYTimes (should try authentication first, then fallback)
        "https://www.nytimes.com/2024/01/15/technology/artificial-intelligence.html",
        
        # General article (should test Enhanced Wayback)
        "https://example.com/article-that-might-be-archived",
        
        # WSJ 
        "https://www.wsj.com/articles/technology-innovation-2024",
    ]
    
    # Test individual strategies
    print("\n📊 Testing Enhanced Wayback Machine Strategy")
    wayback_strategy = EnhancedWaybackMachineStrategy()
    
    wayback_test_url = "https://techcrunch.com/2023/01/15/some-old-article"
    result = wayback_strategy.fetch(wayback_test_url, "test_wayback.log")
    
    if result.success:
        print("✅ Enhanced Wayback SUCCESS")
        print(f"   Method: {result.method}")
        print(f"   Content length: {len(result.content)} chars")
        if result.metadata:
            print(f"   Timestamp: {result.metadata.get('timestamp', 'N/A')}")
            print(f"   Timeframe: {result.metadata.get('timeframe_used', 'N/A')}")
    else:
        print(f"❌ Enhanced Wayback FAILED: {result.error}")
    
    # Test full ArticleFetcher with all strategies
    print("\n🎯 Testing Full Article Fetcher (All Strategies)")
    fetcher = ArticleFetcher(config)
    
    for i, url in enumerate(test_urls[:2]):  # Test first 2 URLs
        print(f"\n🔗 Test {i+1}: {url}")
        
        try:
            result = fetcher.fetch_with_fallbacks(url, f"test_recovery_{i}.log")
            
            if result.success:
                print(f"✅ SUCCESS with strategy: {result.method}")
                print(f"   Content length: {len(result.content) if result.content else 0} chars")
                print(f"   Truncated: {getattr(result, 'is_truncated', False)}")
                
                # Show strategy metadata
                if hasattr(result, 'metadata') and result.metadata:
                    for key, value in result.metadata.items():
                        print(f"   {key}: {value}")
                        
            else:
                print(f"❌ ALL STRATEGIES FAILED: {result.error}")
                
        except Exception as e:
            print(f"💥 ERROR: {e}")
    
    print("\n📈 Strategy Priority Order:")
    for i, strategy in enumerate(fetcher.strategies, 1):
        print(f"   {i}. {strategy.get_strategy_name()}")
    
    print("\n✅ Recovery test completed")

if __name__ == "__main__":
    test_recovery_strategies()