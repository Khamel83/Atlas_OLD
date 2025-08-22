\"\"\"
Test script for Atlas API
\"\"\"

import requests
import time

def test_api():
    \"\"\"Test the Atlas API endpoints\"\"\"
    
    # Test health endpoint
    print(\"Testing health endpoint...\")
    try:
        response = requests.get(\"http://localhost:8000/health\")
        print(f\"Health check: {response.status_code} - {response.json()}\")
    except Exception as e:
        print(f\"Health check failed: {e}\")
    
    # Test auth health endpoint
    print(\"\\nTesting auth health endpoint...\")
    try:
        response = requests.get(\"http://localhost:8000/auth/health\")
        print(f\"Auth health check: {response.status_code} - {response.json()}\")
    except Exception as e:
        print(f\"Auth health check failed: {e}\")
    
    # Test content health endpoint
    print(\"\\nTesting content health endpoint...\")
    try:
        response = requests.get(\"http://localhost:8000/content/health\")
        print(f\"Content health check: {response.status_code} - {response.json()}\")
    except Exception as e:
        print(f\"Content health check failed: {e}\")
    
    # Test cognitive health endpoint
    print(\"\\nTesting cognitive health endpoint...\")
    try:
        response = requests.get(\"http://localhost:8000/cognitive/health\")
        print(f\"Cognitive health check: {response.status_code} - {response.json()}\")
    except Exception as e:
        print(f\"Cognitive health check failed: {e}\")
    
    # Test existing Flask endpoints
    print(\"\\nTesting existing Flask analytics endpoint...\")
    try:
        response = requests.get(\"http://localhost:8000/api/analytics/health\")
        print(f\"Analytics health check: {response.status_code} - {response.json()}\")
    except Exception as e:
        print(f\"Analytics health check failed: {e}\")
    
    print(\"\\nTest completed.\")

if __name__ == \"__main__\":
    test_api()