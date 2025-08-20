#!/bin/bash

# Atlas Environment Recovery Script
# This script implements the recovery steps from RECOVERY_PLAN.md

set -e  # Exit on any error

echo "🚀 Starting Atlas Environment Recovery..."

# 1. Identify the missing shared object file
echo "🔍 Step 1: Identifying missing shared object files..."
echo "Checking for temporary files that might be causing conflicts..."
ls -la /tmp/.3bdbfdadbd3a7ff2-00000001.node 2>/dev/null || echo "No problematic temporary file found at expected location"

# 2. Clear temporary files
echo "🧹 Step 2: Clearing temporary files..."
rm -f /tmp/.3bdbfdadbd3a7ff2-00000001.node
echo "✅ Temporary files cleared"

# 3. Backup current environment
echo "📦 Step 3: Backing up current virtual environment..."
if [ -d ".venv" ]; then
    BACKUP_NAME=".venv.backup.$(date +%s)"
    mv .venv "$BACKUP_NAME"
    echo "✅ Backed up current environment to $BACKUP_NAME"
else
    echo "ℹ️  No existing virtual environment found"
fi

# 4. Create fresh virtual environment
echo "🔧 Step 4: Creating fresh virtual environment..."
python3 -m venv .venv
source .venv/bin/activate
echo "✅ Virtual environment created and activated"

# 5. Upgrade pip
echo "⬆️  Step 5: Upgrading pip..."
pip install --upgrade pip
echo "✅ Pip upgraded"

# 6. Install dependencies
echo "📥 Step 6: Installing dependencies from requirements.txt..."
pip install -r requirements.txt
echo "✅ Dependencies installed"

# 7. Fix directory structure
echo "📁 Step 7: Fixing directory structure..."
./fix_atlas_structure.sh
echo "✅ Directory structure fixed"

# 8. Verify the fix
echo "✅ Step 8: Verifying the fix..."
echo "Python version: $(python --version)"
echo "Pip list:"
pip list | head -10

# 9. Test basic imports
echo "🧪 Step 9: Testing basic imports..."
python -c "import sys; print('✅ Python working:', sys.version)"
python -c "import requests; print('✅ Requests library working')"
python -c "import yaml; print('✅ PyYAML library working')"
python -c "from helpers.config import load_config; print('✅ Atlas config module working')"

echo "🎉 Recovery completed successfully!"
echo ""
echo "To activate the new environment, run:"
echo "source .venv/bin/activate"
echo ""
echo "To test Atlas functionality, run:"
echo "python scripts/diagnose_environment.py"