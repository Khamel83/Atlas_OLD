#!/usr/bin/env python3
"""
Test paywall recovery with rate limiting
"""

import json
import os
import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.article_strategies import ArticleFetcher

def find_paywall_articles(limit=5):
    """Find failed paywall articles (NYTimes, WSJ)"""
    paywall_articles = []
    metadata_dir = "output/articles/metadata"
    
    for filename in os.listdir(metadata_dir):
        if filename.endswith('.json') and len(paywall_articles) < limit:
            filepath = os.path.join(metadata_dir, filename)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    if data.get('status') == 'error':
                        source = data.get('source', '').lower()
                        if 'nytimes.com' in source or 'wsj.com' in source:
                            site = 'NYTimes' if 'nytimes.com' in source else 'WSJ'
                            paywall_articles.append({
                                'site': site,
                                'source': data.get('source'),
                                'error': data.get('error')
                            })
            except Exception:
                continue
    
    return paywall_articles

def test_paywall_recovery():
    """Test paywall recovery with enhanced strategies"""
    config = load_config()
    fetcher = ArticleFetcher(config)
    
    print("🔓 Testing Enhanced Paywall Recovery")
    print(f"✅ NYTimes credentials: {bool(config.get('NYTIMES_USERNAME'))}")
    print(f"✅ WSJ credentials: {bool(config.get('WSJ_USERNAME'))}")
    print("⏱️  Rate limiting: 3-17 second delays to avoid bans")
    
    paywall_articles = find_paywall_articles(5)
    print(f"\n📊 Found {len(paywall_articles)} paywall articles to test")
    
    successes = 0
    for i, article in enumerate(paywall_articles):
        print(f"\n[{i+1}/{len(paywall_articles)}] Testing {article['site']}: {article['source']}")
        print(f"Previous error: {article['error']}")
        
        try:
            result = fetcher.fetch_with_fallbacks(article['source'], "paywall_test")
            
            if result.success and result.content and len(result.content) > 5000:
                print(f"🎉 SUCCESS! Method: {result.method}")
                print(f"   Content length: {len(result.content):,} characters")
                print(f"   {article['site']} paywall bypassed successfully!")
                successes += 1
            else:
                print(f"❌ Still failed: {result.error}")
                
        except Exception as e:
            print(f"❌ Exception: {e}")
    
    print("\n📈 Paywall Recovery Results:")
    print(f"✅ Recovered: {successes}/{len(paywall_articles)}")
    if successes > 0:
        print("🎯 This proves Atlas can recover premium content that was previously lost!")

if __name__ == "__main__":
    test_paywall_recovery()