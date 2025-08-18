#!/usr/bin/env python3
"""
Enhanced retry mechanism for failed articles using new strategies
"""

import json
import os
import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config

def find_failed_articles():
    """Find all failed articles from metadata"""
    failed_articles = []
    metadata_dir = "output/articles/metadata"
    
    if not os.path.exists(metadata_dir):
        print(f"Metadata directory not found: {metadata_dir}")
        return failed_articles
    
    for filename in os.listdir(metadata_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(metadata_dir, filename)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    if data.get('status') == 'error':
                        failed_articles.append({
                            'uid': data.get('uid'),
                            'source': data.get('source'),
                            'error': data.get('error'),
                            'filepath': filepath
                        })
            except Exception as e:
                print(f"Error reading {filepath}: {e}")
    
    return failed_articles

def retry_with_enhanced_strategies(failed_articles, max_retries=None, use_skyvern=False):
    """Retry failed articles with enhanced strategies"""
    config = load_config()
    
    if use_skyvern:
        # Use Skyvern-enhanced ingestor for AI-powered recovery
        from helpers.skyvern_enhanced_ingestor import SkyvernEnhancedIngestor
        ingestor = SkyvernEnhancedIngestor(config)
        print("🤖 Using AI-Enhanced Skyvern recovery system")
        print(f"   AI Enhancement: {'enabled' if ingestor.ai_enabled else 'disabled'}")
        print(f"   Model: {ingestor.model if ingestor.ai_enabled else 'N/A'}")
    else:
        # Use traditional ArticleFetcher
        from helpers.article_strategies import ArticleFetcher
        ingestor = ArticleFetcher(config)
    
    print(f"🔄 Starting enhanced retry for {len(failed_articles)} failed articles")
    print("📋 Enhanced strategies available:")
    print(f"   ✅ NYTimes Authentication: {bool(config.get('NYTIMES_USERNAME'))}")
    print("   ✅ Enhanced Wayback Machine (10 timeframes)")
    print("   ✅ Archive.today fallback")
    print("   ✅ Multiple user agents and bypasses")
    if use_skyvern:
        print(f"   🤖 AI-powered content extraction: {ingestor.ai_enabled}")
        print("   🧠 Complex site detection: enabled")
        print("   🔐 Paywall intelligence: enabled")
    
    successes = 0
    failures = 0
    
    articles_to_process = failed_articles if max_retries is None else failed_articles[:max_retries]
    total_articles = len(articles_to_process)
    
    for i, article in enumerate(articles_to_process):
        print(f"\n[{i+1}/{total_articles}] Retrying: {article['source']}")
        print(f"Previous error: {article['error']}")
        
        try:
            if use_skyvern:
                # Use Skyvern AI-enhanced ingestor
                from helpers.metadata_manager import ContentMetadata, ContentType
                metadata = ContentMetadata(
                    uid=article['uid'] or f"retry_{i}", 
                    content_type=ContentType.ARTICLE, 
                    source=article['source']
                )
                success, content = ingestor.fetch_content(article['source'], metadata)
                result_method = getattr(metadata, 'fetch_method', 'unknown')
                
                if success and content and len(content) > 1000:
                    print(f"✅ SUCCESS! Method: {result_method}")
                    print(f"   Content length: {len(content)}")
                    successes += 1
                else:
                    print(f"❌ Still failed: {content if isinstance(content, str) and len(content) < 200 else 'Content extraction failed'}")
                    failures += 1
            else:
                # Use traditional ArticleFetcher
                result = ingestor.fetch_with_fallbacks(article['source'], "retry_log")
                
                if result.success and result.content and len(result.content) > 1000:
                    print(f"✅ SUCCESS! Method: {result.method}")
                    print(f"   Content length: {len(result.content)}")
                    successes += 1
                else:
                    print(f"❌ Still failed: {result.error or 'Unknown error'}")
                    failures += 1
                
        except Exception as e:
            print(f"❌ Exception during retry: {e}")
            failures += 1
    
    print("\n📊 Enhanced Retry Results:")
    print(f"✅ Recovered: {successes}")
    print(f"❌ Still failed: {failures}")
    print(f"📈 Recovery rate: {(successes/(successes+failures)*100):.1f}%" if (successes+failures) > 0 else "N/A")
    
    return successes, failures

def main():
    import sys
    use_skyvern = "--use-skyvern" in sys.argv
    
    print("🔍 Finding failed articles...")
    failed_articles = find_failed_articles()
    
    print(f"📊 Found {len(failed_articles)} failed articles")
    
    # Show breakdown by error type
    error_types = {}
    nytimes_count = 0
    complex_sites_count = 0
    
    for article in failed_articles:
        error = article['error'] or 'Unknown'
        error_types[error] = error_types.get(error, 0) + 1
        if 'nytimes.com' in article['source'].lower():
            nytimes_count += 1
        
        # Check for complex sites that would benefit from AI extraction
        if any(domain in article['source'].lower() for domain in ['medium.com', 'substack.com', 'reddit.com', 'notion.so']):
            complex_sites_count += 1
    
    print("\n📈 Error breakdown:")
    for error, count in sorted(error_types.items(), key=lambda x: x[1], reverse=True):
        print(f"   {error}: {count}")
    
    print(f"\n🗞️  NYTimes articles: {nytimes_count}")
    print(f"🤖 Complex sites (would benefit from AI): {complex_sites_count}")
    
    if failed_articles:
        mode = "AI-Enhanced Skyvern" if use_skyvern else "Traditional Enhanced"
        print(f"\n🚀 Starting {mode} recovery process...")
        successes, failures = retry_with_enhanced_strategies(failed_articles, use_skyvern=use_skyvern)
        
        if successes > 0:
            print(f"\n🎉 {mode} strategies recovered {successes} articles that were previously lost!")
            print("💾 This demonstrates the 'never lose data' principle in action")
    else:
        print("No failed articles found to retry.")
        
    if not use_skyvern and complex_sites_count > 0:
        print(f"\n💡 Tip: Run with --use-skyvern to try AI-enhanced recovery on {complex_sites_count} complex sites")

if __name__ == "__main__":
    main()