#!/bin/bash
# Script to start the Atlas API server

# Check if virtual environment exists, if not create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r api/requirements.txt
    pip install -r requirements.txt  # Install main project requirements too
else
    source venv/bin/activate
fi

# Start the API server
echo "Starting Atlas API server on port 8001..."
python -m api.main