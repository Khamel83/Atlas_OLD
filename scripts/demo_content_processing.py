#!/usr/bin/env python3
"""
Demo script for Atlas Advanced Content Processing
"""

import sys
import os
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent.parent))

def demo_multilang_processor():
    """Demo the multi-language processor"""
    print("🌍 Atlas Multi-Language Processor Demo")
    print("=" * 50)
    
    try:
        from content.multilang_processor import MultiLanguageProcessor, Language
        
        # Create processor
        processor = MultiLanguageProcessor()
        
        # Sample multilingual content
        content = {
            'en': 'Python is a high-level programming language with dynamic semantics. It is used for web development, data science, and automation.',
            'es': 'Python es un lenguaje de programación de alto nivel con semántica dinámica. Se utiliza para desarrollo web, ciencia de datos y automatización.',
            'fr': 'Python est un langage de programmation de haut niveau avec une sémantique dynamique. Il est utilisé pour le développement web, la science des données et l\'automatisation.',
            'de': 'Python ist eine hochrangige Programmiersprache mit dynamischer Semantik. Sie wird für die Webentwicklung, Datenwissenschaft und Automatisierung verwendet.'
        }
        
        # Process content
        print("Processing multilingual content...")
        processed_content = processor.process_multilingual_content(content)
        
        # Display results
        print("\nProcessed Content:")
        for lang_code, text in processed_content.items():
            print(f"  {lang_code.upper()}: {text[:100]}...")
        
        # Detect language
        unknown_text = "Python è un linguaggio di programmazione di alto livello."
        detected_lang = processor.detect_language(unknown_text)
        print(f"\nDetected language: {detected_lang.name}")
        
        # Translate text
        translated_text = processor.translate_text(unknown_text, Language.ENGLISH)
        print(f"Translated to English: {translated_text}")
        
        print("\n✅ Multi-Language Processor demo completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Multi-Language Processor demo failed: {e}")
        return False

def demo_enhanced_summarizer():
    """Demo the enhanced summarizer"""
    print("\n📝 Atlas Enhanced Summarizer Demo")
    print("=" * 50)
    
    try:
        from content.enhanced_summarizer import EnhancedSummarizer
        
        # Create summarizer
        summarizer = EnhancedSummarizer()
        
        # Sample long content
        content = """
        Python is a high-level programming language with dynamic semantics. It is used for web development, 
        data science, and automation. Python has a simple syntax similar to English, making it easy to learn. 
        The language supports multiple programming paradigms, including procedural, object-oriented, and functional programming. 
        Python has a large standard library and a vibrant community that contributes to thousands of third-party modules and packages. 
        Popular frameworks like Django and Flask make web development with Python straightforward. 
        For data science, libraries like NumPy, Pandas, and Matplotlib provide powerful tools for analysis and visualization. 
        Machine learning practitioners use Python with libraries like TensorFlow, PyTorch, and Scikit-learn. 
        Python is also popular for automation tasks, scripting, and rapid prototyping. 
        The language continues to evolve with regular updates and improvements to performance and features.
        """
        
        # Generate different types of summaries
        print("Generating enhanced content summaries...")
        
        # Extractive summary
        extractive_summary = summarizer.summarize(content, method='extractive', summary_length=2)
        print(f"\nExtractive Summary:\n{extractive_summary}")
        
        # Abstractive summary
        abstractive_summary = summarizer.summarize(content, method='abstractive', summary_length=2)
        print(f"\nAbstractive Summary:\n{abstractive_summary}")
        
        # Keyword-based summary
        keyword_summary = summarizer.summarize(content, method='keyword_based', summary_length=2)
        print(f"\nKeyword-based Summary:\n{keyword_summary}")
        
        # Sentence scoring summary
        sentence_summary = summarizer.summarize(content, method='sentence_scoring', summary_length=2)
        print(f"\nSentence Scoring Summary:\n{sentence_summary}")
        
        print("\n✅ Enhanced Summarizer demo completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Enhanced Summarizer demo failed: {e}")
        return False

def demo_topic_clusterer():
    """Demo the topic clusterer"""
    print("\n🔍 Atlas Topic Clusterer Demo")
    print("=" * 50)
    
    try:
        from content.topic_clusterer import TopicClusterer
        
        # Create clusterer
        clusterer = TopicClusterer()
        
        # Sample documents
        documents = [
            {
                'id': 'python_basics',
                'content': 'Python is a high-level programming language with dynamic semantics. It is used for web development, data science, and automation. Python has a simple syntax similar to English.'
            },
            {
                'id': 'machine_learning',
                'content': 'Machine learning is a subset of artificial intelligence that provides systems the ability to automatically learn and improve from experience. It focuses on the development of computer programs that can access data and use it to learn for themselves.'
            },
            {
                'id': 'data_science',
                'content': 'Data science combines statistics, mathematics, and computer science to extract insights from data. It involves data cleaning, data analysis, and data visualization. Popular tools include Python, R, and SQL.'
            },
            {
                'id': 'web_development',
                'content': 'Web development involves creating websites and web applications. Frontend development focuses on user interfaces using HTML, CSS, and JavaScript. Backend development handles server-side logic using languages like Python, Java, or Node.js.'
            },
            {
                'id': 'artificial_intelligence',
                'content': 'Artificial intelligence is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of intelligent agents.'
            }
        ]
        
        # Add documents
        print("Adding documents for clustering...")
        clusterer.add_documents(documents)
        
        # Perform clustering
        print("Clustering documents...")
        clusters = clusterer.cluster_documents()
        
        # Display results
        print(f"\nClustering Results ({len(clusters)} clusters):")
        for cluster in clusters:
            print(f"\nCluster {cluster['id']}:")
            print(f"  Documents: {', '.join(cluster['documents'])}")
            print(f"  Keywords: {', '.join(cluster['keywords'])}")
        
        # Get statistics
        stats = clusterer.get_cluster_statistics()
        print(f"\nClustering Statistics:")
        print(f"  Total Documents: {stats['total_documents']}")
        print(f"  Total Clusters: {stats['total_clusters']}")
        print(f"  Average Cluster Size: {stats['avg_cluster_size']:.2f}")
        
        print("\n✅ Topic Clusterer demo completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Topic Clusterer demo failed: {e}")
        return False

def demo_smart_recommender():
    """Demo the smart recommender"""
    print("\n🤖 Atlas Smart Recommender Demo")
    print("=" * 50)
    
    try:
        from content.smart_recommender import ContentRecommender
        
        # Create recommender
        recommender = ContentRecommender()
        
        # Add sample user profiles
        print("Adding user profiles...")
        users = [
            {
                'id': 'alice',
                'preferences': {'reading_time': 'evening', 'device': 'desktop'},
                'interests': ['python', 'data-science', 'machine-learning'],
                'skills': ['intermediate'],
                'goals': ['learn-ml', 'career-change'],
                'reading_history': []
            },
            {
                'id': 'bob',
                'preferences': {'reading_time': 'morning', 'device': 'mobile'},
                'interests': ['web-development', 'javascript', 'react'],
                'skills': ['beginner'],
                'goals': ['build-portfolio', 'learn-js'],
                'reading_history': []
            }
        ]
        
        for user in users:
            recommender.add_user_profile(user['id'], user)
        
        # Add sample content metadata
        print("Adding content metadata...")
        content_items = [
            {
                'id': 'python_intro',
                'title': 'Introduction to Python Programming',
                'type': 'article',
                'categories': ['programming'],
                'tags': ['python', 'beginner'],
                'authors': ['John Doe'],
                'publication_date': '2023-01-15T10:00:00Z',
                'difficulty': 'beginner',
                'estimated_reading_time': 15,
                'language': 'en',
                'keywords': ['python', 'programming', 'tutorial'],
                'summary': 'Learn Python programming basics in this comprehensive tutorial.'
            },
            {
                'id': 'ml_with_python',
                'title': 'Machine Learning with Python',
                'type': 'article',
                'categories': ['data-science', 'machine-learning'],
                'tags': ['python', 'ml', 'scikit-learn'],
                'authors': ['Jane Smith'],
                'publication_date': '2023-02-20T14:30:00Z',
                'difficulty': 'intermediate',
                'estimated_reading_time': 25,
                'language': 'en',
                'keywords': ['machine-learning', 'python', 'data-science'],
                'summary': 'Explore machine learning concepts and implementation with Python.'
            },
            {
                'id': 'react_fundamentals',
                'title': 'React Fundamentals',
                'type': 'article',
                'categories': ['web-development', 'javascript'],
                'tags': ['react', 'javascript', 'frontend'],
                'authors': ['Bob Johnson'],
                'publication_date': '2023-03-10T09:15:00Z',
                'difficulty': 'beginner',
                'estimated_reading_time': 20,
                'language': 'en',
                'keywords': ['react', 'javascript', 'components'],
                'summary': 'Master React fundamentals including components, props, and state.'
            }
        ]
        
        for content in content_items:
            recommender.add_content_metadata(content['id'], content)
        
        # Record sample interactions
        print("Recording user interactions...")
        interactions = [
            ('alice', 'python_intro', 'read', {'duration': 18}),
            ('alice', 'ml_with_python', 'like', {}),
            ('alice', 'ml_with_python', 'share', {'platform': 'twitter'}),
            ('bob', 'react_fundamentals', 'read', {'duration': 22}),
            ('bob', 'python_intro', 'like', {}),
            ('bob', 'react_fundamentals', 'complete', {'quiz_score': 95})
        ]
        
        for user_id, content_id, interaction_type, data in interactions:
            recommender.record_interaction(user_id, content_id, interaction_type, data)
        
        # Generate recommendations
        print("\nGenerating content recommendations...")
        
        # For Alice
        alice_recs = recommender.generate_recommendations('alice', num_recommendations=3)
        print(f"\nRecommendations for Alice:")
        for i, rec in enumerate(alice_recs, 1):
            content_meta = recommender.get_content_metadata(rec['content_id'])
            title = content_meta['title'] if content_meta else rec['content_id']
            print(f"  {i}. {title}")
            print(f"     Score: {rec['score']:.2f}")
            print(f"     Reason: {rec['reason']}")
        
        # For Bob
        bob_recs = recommender.generate_recommendations('bob', num_recommendations=3)
        print(f"\nRecommendations for Bob:")
        for i, rec in enumerate(bob_recs, 1):
            content_meta = recommender.get_content_metadata(rec['content_id'])
            title = content_meta['title'] if content_meta else rec['content_id']
            print(f"  {i}. {title}")
            print(f"     Score: {rec['score']:.2f}")
            print(f"     Reason: {rec['reason']}")
        
        print("\n✅ Smart Recommender demo completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Smart Recommender demo failed: {e}")
        return False

def main():
    """Run all demos"""
    print("🚀 Atlas Advanced Content Processing Demo")
    print("=" * 60)
    
    demos = [
        demo_multilang_processor,
        demo_enhanced_summarizer,
        demo_topic_clusterer,
        demo_smart_recommender
    ]
    
    passed = 0
    failed = 0
    
    for demo in demos:
        if demo():
            passed += 1
        else:
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"Demo Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All demos completed successfully!")
        print("\n🎯 Atlas Advanced Content Processing is ready for use!")
        return True
    else:
        print("⚠️  Some demos failed!")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)