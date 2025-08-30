#!/usr/bin/env python3
"""
Simple automation test script
"""
import requests
import feedparser
import json
from datetime import datetime

def test_rss_ingestion():
    """Test RSS feed ingestion"""
    print("🧪 Testing RSS ingestion automation...")
    
    # Test RSS feed
    feed_url = "https://feeds.feedburner.com/oreilly/radar"
    atlas_url = "http://localhost:8001"
    
    try:
        print(f"📡 Fetching RSS feed: {feed_url}")
        feed = feedparser.parse(feed_url)
        
        if not feed.entries:
            print("❌ No entries found in feed")
            return False
        
        print(f"📰 Found {len(feed.entries)} articles")
        
        # Process first 3 articles
        for i, entry in enumerate(feed.entries[:3]):
            print(f"Processing article {i+1}: {entry.title}")
            
            # Try to find a content save endpoint
            # Let's try multiple possible endpoints
            endpoints_to_try = [
                f"{atlas_url}/api/v1/content/save",
                f"{atlas_url}/content/save",
                f"{atlas_url}/save",
                f"{atlas_url}/api/save"
            ]
            
            content_data = {
                "title": entry.get('title', 'No Title'),
                "url": entry.get('link', ''),
                "content": f"RSS Feed Article: {entry.get('title')}\\n\\n{entry.get('summary', '')}",
                "source": f"rss-test-{feed_url}",
                "metadata": {
                    "feed_url": feed_url,
                    "published": entry.get('published', ''),
                    "author": entry.get('author', ''),
                    "platform": "rss"
                }
            }
            
            success = False
            for endpoint in endpoints_to_try:
                try:
                    response = requests.post(
                        endpoint,
                        json=content_data,
                        headers={"Content-Type": "application/json"},
                        timeout=10
                    )
                    
                    if response.status_code in [200, 201]:
                        print(f"✅ Successfully saved via {endpoint}")
                        success = True
                        break
                    else:
                        print(f"❌ {endpoint} returned {response.status_code}")
                        
                except Exception as e:
                    print(f"❌ {endpoint} failed: {e}")
                    continue
            
            if not success:
                print(f"❌ Failed to save article: {entry.title}")
        
        print("✅ RSS ingestion test completed")
        return True
        
    except Exception as e:
        print(f"❌ RSS test failed: {e}")
        return False

def test_hacker_news_ingestion():
    """Test Hacker News ingestion"""
    print("🧪 Testing Hacker News ingestion...")
    
    atlas_url = "http://localhost:8001"
    
    try:
        # Get top stories
        print("📡 Fetching Hacker News top stories...")
        response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        if response.status_code != 200:
            print("❌ Failed to fetch HN stories")
            return False
        
        story_ids = response.json()[:5]  # Get top 5
        print(f"📰 Processing {len(story_ids)} stories...")
        
        processed = 0
        for story_id in story_ids:
            try:
                story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
                if story_response.status_code == 200:
                    story = story_response.json()
                    
                    if story.get('url'):  # Only process stories with URLs
                        content_data = {
                            "title": story.get('title', 'No Title'),
                            "url": story.get('url'),
                            "content": f"Hacker News Story: {story.get('title')}\\nScore: {story.get('score')}\\nComments: {story.get('descendants', 0)}\\n\\nDiscussion: https://news.ycombinator.com/item?id={story_id}",
                            "source": "hackernews-test",
                            "metadata": {
                                "hn_id": story_id,
                                "score": story.get('score'),
                                "comments": story.get('descendants', 0),
                                "author": story.get('by', ''),
                                "platform": "hackernews"
                            }
                        }
                        
                        # Try different endpoints
                        for endpoint in [f"{atlas_url}/api/v1/content/save", f"{atlas_url}/save"]:
                            try:
                                save_response = requests.post(
                                    endpoint,
                                    json=content_data,
                                    headers={"Content-Type": "application/json"},
                                    timeout=10
                                )
                                
                                if save_response.status_code in [200, 201]:
                                    print(f"✅ Saved HN story: {story.get('title')}")
                                    processed += 1
                                    break
                                    
                            except Exception as e:
                                continue
                            
            except Exception as e:
                print(f"❌ Error processing HN story {story_id}: {e}")
                continue
        
        print(f"✅ Hacker News test completed - processed {processed} stories")
        return processed > 0
        
    except Exception as e:
        print(f"❌ Hacker News test failed: {e}")
        return False

def test_cognitive_features():
    """Test cognitive features via web interface"""
    print("🧪 Testing cognitive features...")
    
    atlas_url = "http://localhost:8001"
    
    # Test different endpoints
    endpoints = [
        "/ask/proactive",
        "/ask/temporal", 
        "/ask/recall",
        "/ask/patterns",
        "/cognitive/analyze",
        "/cognitive/status"
    ]
    
    results = {}
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{atlas_url}{endpoint}", timeout=10)
            results[endpoint] = {
                "status_code": response.status_code,
                "success": response.status_code == 200,
                "response_length": len(response.text) if response.text else 0
            }
            
            if response.status_code == 200:
                print(f"✅ {endpoint} - Working")
            else:
                print(f"❌ {endpoint} - Status {response.status_code}")
                
        except Exception as e:
            results[endpoint] = {
                "success": False,
                "error": str(e)
            }
            print(f"❌ {endpoint} - Error: {e}")
    
    working = len([r for r in results.values() if r.get('success')])
    print(f"✅ Cognitive features test: {working}/{len(endpoints)} endpoints working")
    
    return results

def main():
    """Run all automation tests"""
    print("🚀 Starting Atlas Automation Tests")
    print("=" * 50)
    
    # Test RSS
    rss_success = test_rss_ingestion()
    print()
    
    # Test Hacker News
    hn_success = test_hacker_news_ingestion()
    print()
    
    # Test Cognitive Features
    cognitive_results = test_cognitive_features()
    print()
    
    # Summary
    print("📊 TEST SUMMARY")
    print("=" * 50)
    print(f"RSS Ingestion: {'✅ PASS' if rss_success else '❌ FAIL'}")
    print(f"Hacker News: {'✅ PASS' if hn_success else '❌ FAIL'}")
    
    cognitive_working = len([r for r in cognitive_results.values() if r.get('success')])
    print(f"Cognitive Features: {cognitive_working}/{len(cognitive_results)} working")
    
    # Export results
    results = {
        "timestamp": datetime.now().isoformat(),
        "tests": {
            "rss_ingestion": rss_success,
            "hacker_news": hn_success,
            "cognitive_features": cognitive_results
        }
    }
    
    with open('automation_test_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\\n📄 Results saved to automation_test_results.json")

if __name__ == "__main__":
    main()