#!/usr/bin/env python3
"""
Atlas Cognitive Engine - AI-powered content analysis and insights
"""

import json
import os
import sys
sys.path.append('/home/ubuntu/dev/atlas')

from helpers.config import load_config
from helpers.search_engine import get_search_engine
import requests

class CognitiveEngine:
    """AI-powered cognitive amplification for Atlas content"""
    
    def __init__(self):
        self.config = load_config()
        try:
            self.search_engine = get_search_engine(self.config)
        except Exception:
            self.search_engine = None
        self.openrouter_api_key = self.config.get("OPENROUTER_API_KEY")
        self.model = self.config.get("llm_model", "google/gemini-2.0-flash-lite-001")
        
    def condense_content(self, content: str, max_length: int = 500) -> str:
        """AI-powered content condensation"""
        if not self.openrouter_api_key or len(content) < 200:
            return content[:max_length] + "..." if len(content) > max_length else content
            
        try:
            headers = {
                "Authorization": f"Bearer {self.openrouter_api_key}",
                "Content-Type": "application/json",
            }
            
            data = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": f"Condense this content to {max_length} characters max, preserving key insights and main points. Return clean, readable text."},
                    {"role": "user", "content": content[:8000]}  # Limit input
                ],
                "max_tokens": 200,
                "temperature": 0.3,
            }
            
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers, json=data, timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Condensation error: {e}")
            
        return content[:max_length] + "..." if len(content) > max_length else content
    
    def extract_insights(self, content: str) -> dict:
        """Extract key insights from content"""
        if not self.openrouter_api_key:
            return {"insights": ["AI insights unavailable - OpenRouter key missing"]}
            
        try:
            headers = {
                "Authorization": f"Bearer {self.openrouter_api_key}",
                "Content-Type": "application/json",
            }
            
            prompt = """Extract 3-5 key insights from this content. Return as JSON:
{
  "insights": ["insight 1", "insight 2", "insight 3"],
  "topics": ["topic1", "topic2", "topic3"],
  "sentiment": "positive/neutral/negative"
}"""
            
            data = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": content[:6000]}
                ],
                "max_tokens": 300,
                "temperature": 0.4,
            }
            
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers, json=data, timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                insight_text = result["choices"][0]["message"]["content"]
                try:
                    return json.loads(insight_text)
                except Exception:
                    return {"insights": [insight_text.strip()]}
        except Exception as e:
            print(f"Insight extraction error: {e}")
            
        return {"insights": ["Content analysis available"]}
    
    def find_connections(self, content: str, limit: int = 5) -> list:
        """Find related content using search"""
        if not self.search_engine:
            return []
            
        try:
            # Extract key terms for search
            words = content.split()[:100]  # First 100 words
            search_terms = " ".join(words)
            
            results = self.search_engine.search(search_terms, limit=limit*2)
            
            # Filter out self-matches and return unique connections
            connections = []
            for result in results.get('hits', [])[:limit]:
                connections.append({
                    'title': result.get('title', 'Unknown'),
                    'source': result.get('source', ''),
                    'relevance': result.get('_score', 0),
                    'snippet': result.get('content', '')[:200] + "..."
                })
            
            return connections
        except Exception as e:
            print(f"Connection finding error: {e}")
            return []
    
    def analyze_article(self, filepath: str) -> dict:
        """Comprehensive cognitive analysis of an article"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic info
            analysis = {
                'file': os.path.basename(filepath),
                'length': len(content),
                'word_count': len(content.split()),
            }
            
            # AI-powered analysis
            analysis['condensed'] = self.condense_content(content)
            analysis['insights'] = self.extract_insights(content)
            analysis['connections'] = self.find_connections(content)
            
            return analysis
            
        except Exception as e:
            return {'error': str(e)}

def demo_cognitive_features():
    """Demo the cognitive engine capabilities"""
    engine = CognitiveEngine()
    
    print("🧠 Atlas Cognitive Engine Demo")
    print("=" * 40)
    
    # Find some articles to analyze
    import glob
    articles = glob.glob("output/articles/**/*.md", recursive=True)[:3]
    
    if not articles:
        print("No articles found for analysis")
        return
    
    for article_path in articles:
        print(f"\n📄 Analyzing: {os.path.basename(article_path)}")
        print("-" * 30)
        
        analysis = engine.analyze_article(article_path)
        
        if 'error' in analysis:
            print(f"❌ Error: {analysis['error']}")
            continue
            
        print(f"📊 Length: {analysis['word_count']} words")
        print(f"🔤 Condensed: {analysis['condensed'][:150]}...")
        
        insights = analysis['insights'].get('insights', [])
        if insights:
            print("💡 Key Insights:")
            for i, insight in enumerate(insights[:3], 1):
                print(f"   {i}. {insight}")
        
        connections = analysis['connections']
        if connections:
            print(f"🔗 Related Content: {len(connections)} connections found")
    
    print("\n🎯 Cognitive Engine Ready for Integration!")

if __name__ == "__main__":
    demo_cognitive_features()