#!/usr/bin/env python3
"""
Atlas API Demo Script

This script demonstrates how to use the Atlas API to access cognitive features.
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:8001/api/v1"

def demo_api():
    """Demonstrate API usage"""
    print("Atlas API Demo")
    print("=" * 50)
    
    # 1. Health check
    print("\n1. Health Check:")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # 2. Generate API key
    print("\n2. Generate API Key:")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/generate",
            json={"name": "demo_key"}
        )
        if response.status_code == 200:
            api_key = response.json()["api_key"]
            print(f"   API Key Generated: {api_key[:10]}...")
        else:
            print(f"   Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # 3. List content
    print("\n3. List Content:")
    try:
        response = requests.get(f"{BASE_URL}/content/")
        if response.status_code == 200:
            data = response.json()
            print(f"   Total items: {data['total']}")
            print(f"   First {min(3, len(data['items']))} items:")
            for item in data['items'][:3]:
                print(f"     - {item['title'][:50]}...")
        else:
            print(f"   Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # 4. Generate Socratic questions
    print("\n4. Generate Socratic Questions:")
    try:
        response = requests.post(
            f"{BASE_URL}/cognitive/socratic",
            data={"content": "The sky is blue because of Rayleigh scattering."}
        )
        if response.status_code == 200:
            data = response.json()
            print(f"   Content: {data['content']}")
            print("   Questions:")
            for i, question in enumerate(data['questions'][:3], 1):
                print(f"     {i}. {question}")
        elif response.status_code == 501:
            print("   Cognitive features not available")
        else:
            print(f"   Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # 5. Get proactive content
    print("\n5. Proactive Content:")
    try:
        response = requests.get(f"{BASE_URL}/cognitive/proactive")
        if response.status_code == 200:
            items = response.json()
            print(f"   Found {len(items)} items:")
            for item in items[:3]:
                print(f"     - {item['title'][:50]}...")
        elif response.status_code == 501:
            print("   Cognitive features not available")
        else:
            print(f"   Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"   Error: {e}")

if __name__ == "__main__":
    demo_api()