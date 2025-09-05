#!/bin/bash
# Atlas startup script with clean environment and correct API key

# Kill any existing API server
pkill -f "uvicorn api.main:app"

# Wait a moment
sleep 2

# Source the virtual environment and .env, then start with clean environment
cd /home/ubuntu/dev/atlas

# Explicitly set the correct API key
export OPENROUTER_API_KEY="[REMOVED]"

# Activate virtual environment and start server
source venv/bin/activate
python -m uvicorn api.main:app --host 0.0.0.0 --port 7444 --reload &

echo "Atlas API started with correct OpenRouter key (ending d25f)"
echo "Token limits set to 10,000 for all workloads"

# Show the key being used (last 4 chars only)
python3 -c "import os; print('Using API key ending:', os.getenv('OPENROUTER_API_KEY', 'NONE')[-4:])"