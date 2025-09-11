#!/bin/bash

# External recovery script to be run from a different environment
# This script should be copied to a different machine/environment and run from there

PROJECT_DIR="/home/ubuntu/dev/atlas"
TEMP_FILE="/tmp/.3bdbfdadbd3a7ff2-00000001.node"

echo "Starting external recovery process..."

# Step 1: Remove problematic file
echo "Step 1: Removing problematic file..."
if [ -f "$TEMP_FILE" ]; then
    rm "$TEMP_FILE"
    echo "Removed problematic file: $TEMP_FILE"
else
    echo "File not found: $TEMP_FILE"
fi

# Step 2: Backup virtual environment
echo "Step 2: Backing up virtual environment..."
if [ -d "$PROJECT_DIR/.venv" ]; then
    if [ -d "$PROJECT_DIR/.venv.backup" ]; then
        rm -rf "$PROJECT_DIR/.venv.backup"
        echo "Removed old backup"
    fi
    cp -r "$PROJECT_DIR/.venv" "$PROJECT_DIR/.venv.backup"
    echo "Backed up virtual environment"
else
    echo "Virtual environment not found"
fi

# Step 3: Create new virtual environment
echo "Step 3: Creating new virtual environment..."
if [ -d "$PROJECT_DIR/.venv.new" ]; then
    rm -rf "$PROJECT_DIR/.venv.new"
    echo "Removed existing new venv"
fi

python3 -m venv "$PROJECT_DIR/.venv.new"
echo "Created new virtual environment"

# Step 4: Install dependencies
echo "Step 4: Installing dependencies..."
if [ -f "$PROJECT_DIR/.venv.new/bin/pip" ]; then
    if [ -f "$PROJECT_DIR/requirements.txt" ]; then
        "$PROJECT_DIR/.venv.new/bin/pip" install -r "$PROJECT_DIR/requirements.txt"
        echo "Installed dependencies from requirements.txt"
    else
        echo "requirements.txt not found, skipping dependency installation"
    fi
else
    echo "Pip not found in new virtual environment"
fi

# Step 5: Create directory structure
echo "Step 5: Creating directory structure..."
mkdir -p "$PROJECT_DIR/ingest/queue"
mkdir -p "$PROJECT_DIR/ingest/capture"
mkdir -p "$PROJECT_DIR/ask/insights"
mkdir -p "$PROJECT_DIR/ask/proactive"
mkdir -p "$PROJECT_DIR/ask/recall"
mkdir -p "$PROJECT_DIR/ask/socratic"
mkdir -p "$PROJECT_DIR/ask/temporal"
echo "Created directory structure"

echo "External recovery process completed."