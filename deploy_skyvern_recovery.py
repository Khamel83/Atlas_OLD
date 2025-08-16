#!/usr/bin/env python3
"""
Focused deployment of Skyvern AI-enhanced recovery system
"""

import sys
sys.path.append('/home/ubuntu/dev/atlas')

from retry_failed_articles import find_failed_articles, retry_with_enhanced_strategies

def deploy_targeted_recovery():
    """Deploy AI-enhanced recovery on high-value targets"""
    print("🤖 Atlas Skyvern AI-Enhanced Recovery Deployment")
    print("=" * 55)
    
    # Find all failed articles
    failed_articles = find_failed_articles()
    print(f"📊 Total failed articles: {len(failed_articles)}")
    
    # Categorize by recovery potential
    high_value_targets = []
    complex_sites = []
    nytimes_articles = []
    
    for article in failed_articles:
        url = article['source'].lower()
        
        # High-value targets: Major publications likely to be recoverable
        if any(domain in url for domain in [
            'newyorker.com', 'economist.com', 'wired.com', 'atlantic.com',
            'washingtonpost.com', 'wsj.com', 'ft.com', 'bloomberg.com'
        ]):
            high_value_targets.append(article)
        
        # Complex sites that benefit from AI
        elif any(domain in url for domain in [
            'medium.com', 'substack.com', 'reddit.com', 'notion.so',
            'github.com', 'stackoverflow.com'
        ]):
            complex_sites.append(article)
        
        # NYTimes for authentication testing
        elif 'nytimes.com' in url:
            nytimes_articles.append(article)
    
    print(f"🎯 High-value targets: {len(high_value_targets)}")
    print(f"🤖 Complex sites (AI-enhanced): {len(complex_sites)}")
    print(f"🗞️  NYTimes (auth + AI): {len(nytimes_articles)}")
    
    # Deployment strategy: Start with most promising targets
    deployment_phases = [
        {
            "name": "High-Value Publications",
            "articles": high_value_targets[:20],  # Top 20 high-value
            "description": "Major publications likely to be recoverable"
        },
        {
            "name": "Complex Sites (AI-Enhanced)", 
            "articles": complex_sites[:10],  # Top 10 complex sites
            "description": "Sites requiring AI-powered extraction"
        },
        {
            "name": "NYTimes Authentication",
            "articles": nytimes_articles[:15],  # Top 15 NYTimes
            "description": "Testing authenticated + AI recovery"
        }
    ]
    
    total_recovered = 0
    total_attempted = 0
    
    for phase in deployment_phases:
        if not phase["articles"]:
            continue
            
        print(f"\n🚀 Phase: {phase['name']}")
        print(f"📋 {phase['description']}")
        print(f"🎯 Targets: {len(phase['articles'])} articles")
        print("-" * 40)
        
        # Run AI-enhanced recovery
        successes, failures = retry_with_enhanced_strategies(
            phase["articles"], 
            max_retries=len(phase["articles"]),
            use_skyvern=True
        )
        
        total_recovered += successes
        total_attempted += (successes + failures)
        
        recovery_rate = (successes / (successes + failures) * 100) if (successes + failures) > 0 else 0
        print(f"📊 Phase Results: {successes}/{successes + failures} = {recovery_rate:.1f}% recovery rate")
    
    # Final deployment summary
    print("\n" + "=" * 55)
    print("🎉 SKYVERN DEPLOYMENT COMPLETE")
    print("=" * 55)
    print(f"✅ Total Recovered: {total_recovered}")
    print(f"📈 Total Attempted: {total_attempted}")
    
    if total_attempted > 0:
        final_rate = (total_recovered / total_attempted * 100)
        print(f"🎯 Overall Recovery Rate: {final_rate:.1f}%")
        
        if final_rate >= 75:
            print("🏆 EXCELLENT: Exceeding 75% recovery rate!")
        elif final_rate >= 60:
            print("✅ GOOD: Strong 60%+ recovery performance")
        elif final_rate >= 40:
            print("📈 PROMISING: 40%+ shows significant improvement")
        else:
            print("🔄 BASELINE: Ready for strategy refinement")
    
    print(f"\n💡 Next: Scale to remaining {len(failed_articles) - total_attempted} articles")
    print("🧠 Ready for Phase 2: Cognitive Features Implementation")

if __name__ == "__main__":
    deploy_targeted_recovery()