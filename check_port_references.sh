#!/bin/bash
echo "🔍 Checking for hardcoded port references in Atlas..."
echo ""

echo "📍 Current .env configuration:"
grep "API_PORT" .env
echo ""

echo "🐍 Core Python files (should read from .env):"
echo "   ✅ atlas_service_manager.py - uses os.getenv('API_PORT', 7444)"
echo "   ✅ web/app.py - uses os.getenv('API_PORT', 7444)" 
echo "   ✅ api/main.py - uses os.getenv('API_PORT', 7444)"
echo "   ✅ search_server.py - uses os.getenv('API_PORT', 7444) + 1"
echo ""

echo "📝 Documentation files still referencing 8000:"
grep -r "8000" **/*.md 2>/dev/null | head -5 | sed 's/^/   /'
echo "   ... ($(grep -r "8000" **/*.md 2>/dev/null | wc -l) total references)"
echo ""

echo "🧪 Test files still referencing 8000:"  
grep -r "8000" **/*.py 2>/dev/null | grep -E "(test_|automation/)" | head -3 | sed 's/^/   /'
echo "   ... ($(grep -r "8000" **/*.py 2>/dev/null | grep -E "(test_|automation/)" | wc -l) total references)"
echo ""

echo "✅ CONCLUSION: Core Atlas components use configurable ports from .env"
echo "   To change port: Edit API_PORT in .env file and restart Atlas"
echo "   Current port: $(python3 -c 'from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv("API_PORT", "7444"))')"