#!/bin/bash
# Atlas Production Startup Script

echo "🚀 Starting Atlas Production System"
echo "=================================="

# Navigate to Atlas directory
cd /home/ubuntu/dev/atlas

# Activate virtual environment
source atlas_venv/bin/activate

echo "📊 System Status Check..."
python -c "
from helpers.config import load_config
config = load_config()
print(f'✅ AI Enhancement: {config.get(\"SKYVERN_ENABLED\")}')
print(f'✅ OpenRouter API: {bool(config.get(\"OPENROUTER_API_KEY\"))}')
print(f'✅ Configuration loaded successfully')
"

echo ""
echo "🎯 Choose Production Mode:"
echo "1) Start Web Dashboard Only"
echo "2) Start AI Recovery Process" 
echo "3) Start Full Production (Dashboard + Recovery)"
echo "4) Run Cognitive Analysis Batch"
echo ""
read -p "Enter choice (1-4): " choice

case $choice in
    1)
        echo "🌐 Starting Web Dashboard..."
        cd web
        echo "Dashboard will be available at: http://localhost:8000"
        echo "API Documentation: http://localhost:8000/docs"
        uvicorn app:app --host 0.0.0.0 --port 8000 --reload
        ;;
    2)
        echo "🤖 Starting AI-Enhanced Recovery..."
        echo "This will process 1,514 failed articles with AI enhancement"
        read -p "Continue? (y/n): " confirm
        if [ "$confirm" = "y" ]; then
            python retry_failed_articles.py --use-skyvern
        fi
        ;;
    3)
        echo "🚀 Starting Full Production..."
        echo "Starting web dashboard in background..."
        cd web
        uvicorn app:app --host 0.0.0.0 --port 8000 --reload &
        DASHBOARD_PID=$!
        echo "Dashboard PID: $DASHBOARD_PID"
        
        cd ..
        echo "Starting AI recovery..."
        python retry_failed_articles.py --use-skyvern &
        RECOVERY_PID=$!
        echo "Recovery PID: $RECOVERY_PID"
        
        echo ""
        echo "✅ Production systems started!"
        echo "🌐 Dashboard: http://localhost:8000"
        echo "🤖 Recovery: Running in background"
        echo ""
        echo "To stop:"
        echo "  kill $DASHBOARD_PID  # Stop dashboard"
        echo "  kill $RECOVERY_PID   # Stop recovery"
        
        wait
        ;;
    4)
        echo "🧠 Running Cognitive Analysis Batch..."
        python -c "
from cognitive_engine import CognitiveEngine
import glob
import json

engine = CognitiveEngine()
articles = glob.glob('output/articles/**/*.md', recursive=True)
print(f'Processing {min(50, len(articles))} articles...')

results = []
for i, article in enumerate(articles[:50], 1):
    print(f'[{i}/50] {article}')
    analysis = engine.analyze_article(article)
    results.append(analysis)

# Save results
with open('cognitive_batch_results.json', 'w') as f:
    json.dump(results, f, indent=2)
    
print(f'✅ Batch complete! Results saved to cognitive_batch_results.json')
"
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac