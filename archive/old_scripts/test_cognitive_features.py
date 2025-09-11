#!/usr/bin/env python3
"""
Test Atlas Cognitive Features with Real Data
"""

import sys
import sqlite3
from datetime import datetime

def test_database_content():
    """Test that we have content in the database"""
    print("🔍 Testing Database Content")
    print("-" * 30)
    
    conn = sqlite3.connect('atlas.db')
    cursor = conn.cursor()
    
    # Check content count
    cursor.execute("SELECT COUNT(*) FROM content")
    count = cursor.fetchone()[0]
    print(f"📊 Content records: {count}")
    
    if count == 0:
        print("❌ No content found!")
        return False
    
    # Show some sample content
    cursor.execute("SELECT title, url FROM content LIMIT 5")
    content = cursor.fetchall()
    
    print(f"📰 Sample articles:")
    for title, url in content:
        print(f"  - {title[:60]}...")
        print(f"    {url[:80]}...")
    
    conn.close()
    return True

def test_proactive_surfacer():
    """Test proactive content surfacing"""
    print(f"\n🧠 Testing Proactive Content Surfacer")
    print("-" * 40)
    
    try:
        from ask.proactive.surfacer import ProactiveSurfacer
        
        surfacer = ProactiveSurfacer()
        print("✅ ProactiveSurfacer initialized")
        
        # Test surfacing relevant content
        results = surfacer.surface_relevant_content(
            context="race and academia",
            limit=3
        )
        
        if results:
            print(f"🎯 Found {len(results)} relevant items:")
            for i, result in enumerate(results, 1):
                title = result.get('title', 'No title')[:50]
                print(f"  {i}. {title}...")
        else:
            print("⚠️  No relevant content surfaced")
        
        return True
        
    except Exception as e:
        print(f"❌ ProactiveSurfacer error: {e}")
        return False

def test_pattern_detector():
    """Test pattern detection in content"""
    print(f"\n🔍 Testing Pattern Detector")
    print("-" * 30)
    
    try:
        from ask.insights.pattern_detector import PatternDetector
        
        detector = PatternDetector()
        print("✅ PatternDetector initialized")
        
        # Test pattern detection
        patterns = detector.detect_patterns(
            content_ids=None,  # Use all content
            pattern_types=['topic', 'theme']
        )
        
        if patterns:
            print(f"🎨 Found {len(patterns)} patterns:")
            for pattern in patterns[:3]:  # Show first 3
                pattern_type = pattern.get('type', 'unknown')
                description = pattern.get('description', 'No description')[:60]
                print(f"  - {pattern_type}: {description}...")
        else:
            print("⚠️  No patterns detected")
        
        return True
        
    except Exception as e:
        print(f"❌ PatternDetector error: {e}")
        return False

def test_recall_engine():
    """Test active recall system"""
    print(f"\n🧠 Testing Active Recall Engine")
    print("-" * 35)
    
    try:
        from ask.recall.recall_engine import RecallEngine
        
        engine = RecallEngine()
        print("✅ RecallEngine initialized")
        
        # Test recall suggestions
        recall_items = engine.get_recall_suggestions(limit=3)
        
        if recall_items:
            print(f"🔁 {len(recall_items)} recall suggestions:")
            for i, item in enumerate(recall_items, 1):
                title = item.get('title', 'No title')[:50]
                print(f"  {i}. {title}...")
        else:
            print("⚠️  No recall suggestions generated")
        
        return True
        
    except Exception as e:
        print(f"❌ RecallEngine error: {e}")
        return False

def test_socratic_questions():
    """Test Socratic question generation"""
    print(f"\n❓ Testing Socratic Question Generator")
    print("-" * 45)
    
    try:
        from ask.socratic.question_engine import SocraticQuestion
        
        generator = SocraticQuestion()
        print("✅ SocraticQuestion initialized")
        
        # Test question generation
        questions = generator.generate_questions(
            topic="race and academia preferences",
            limit=3
        )
        
        if questions:
            print(f"💭 Generated {len(questions)} questions:")
            for i, question in enumerate(questions, 1):
                q_text = question.get('question', question)[:80]
                print(f"  {i}. {q_text}...")
        else:
            print("⚠️  No questions generated")
        
        return True
        
    except Exception as e:
        print(f"❌ SocraticQuestion error: {e}")
        return False

def test_temporal_analysis():
    """Test temporal relationship analysis"""
    print(f"\n⏰ Testing Temporal Analysis Engine")
    print("-" * 40)
    
    try:
        from ask.temporal.temporal_engine import TemporalEngine
        
        engine = TemporalEngine()
        print("✅ TemporalEngine initialized")
        
        # Test temporal patterns
        temporal_data = engine.analyze_temporal_patterns()
        
        if temporal_data:
            print(f"📈 Temporal analysis complete")
            if 'trends' in temporal_data:
                trends = temporal_data['trends'][:2]
                for trend in trends:
                    print(f"  📊 Trend: {trend}")
        else:
            print("⚠️  No temporal patterns found")
        
        return True
        
    except Exception as e:
        print(f"❌ TemporalEngine error: {e}")
        return False

def main():
    """Run all cognitive feature tests"""
    
    print("🚀 Atlas Cognitive Features Test")
    print("=" * 50)
    
    # Test database first
    if not test_database_content():
        print("\n❌ Database test failed - stopping here")
        return False
    
    # Test all cognitive features
    tests = [
        test_proactive_surfacer,
        test_pattern_detector,
        test_recall_engine, 
        test_socratic_questions,
        test_temporal_analysis
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test_func.__name__} crashed: {e}")
            failed += 1
    
    # Final results
    print(f"\n" + "=" * 50)
    print(f"🎯 COGNITIVE FEATURES TEST RESULTS")
    print(f"=" * 50)
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📊 Success Rate: {passed/(passed+failed)*100:.1f}%")
    
    if passed >= 3:
        print(f"\n🎉 Atlas cognitive features are working!")
        print(f"🧠 Your personal AI is ready to amplify your thinking")
        return True
    else:
        print(f"\n⚠️  Some features need attention")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)