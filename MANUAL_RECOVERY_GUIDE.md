# Atlas Manual Recovery Guide

This guide provides step-by-step instructions to recover the Atlas environment when automated scripts fail due to shared object errors.

## Understanding the Problem

The error `/tmp/.3bdbfdadbd3a7ff2-00000001.node: cannot open shared object file: No such file or directory` indicates that some process is trying to load a shared library file that doesn't exist or is corrupted. This is commonly caused by:

1. Corrupted Python virtual environment
2. Incompatible native extensions
3. Temporary files conflicts
4. Missing system dependencies

## Manual Recovery Steps

### Step 1: Clean Up Problematic Files

1. Manually delete the problematic temporary file:
   ```bash
   sudo rm -f /tmp/.3bdbfdadbd3a7ff2-00000001.node
   ```

2. Clear all temporary files (be careful with this):
   ```bash
   sudo rm -rf /tmp/*
   ```

### Step 2: Rebuild the Virtual Environment

1. Navigate to the Atlas project directory:
   ```bash
   cd /home/ubuntu/dev/atlas
   ```

2. Backup the current environment:
   ```bash
   mv .venv .venv.backup.$(date +%s)
   ```

3. Create a fresh virtual environment:
   ```bash
   python3 -m venv .venv
   ```

4. Activate the new environment:
   ```bash
   source .venv/bin/activate
   ```

5. Upgrade pip:
   ```bash
   pip install --upgrade pip
   ```

6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Fix Directory Structure

Run the existing fix script:
```bash
./fix_atlas_structure.sh
```

Or manually create the required directories:
```bash
mkdir -p data/raw data/parsed data/transcripts data/collateral logs
mkdir -p output/articles output/youtube output/podcasts
mkdir -p ask process ingest helpers
touch run.py helpers/config.py
```

### Step 4: Install System Dependencies

If you continue to have issues, install required system packages:
```bash
sudo apt update
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

### Step 5: Verify the Fix

1. Test Python functionality:
   ```bash
   python --version
   ```

2. Test basic imports:
   ```bash
   python -c "import sys; print('Python working')"
   python -c "import requests; print('Requests working')"
   ```

3. Run Atlas diagnostics:
   ```bash
   python scripts/diagnose_environment.py
   ```

## If Problems Persist

1. Reboot the system to clear any locked resources:
   ```bash
   sudo reboot
   ```

2. After reboot, repeat the recovery steps.

3. Check for conflicting processes:
   ```bash
   ps aux | grep node
   ps aux | grep python
   ```

4. Examine system logs:
   ```bash
   dmesg | grep error
   journalctl -xe
   ```

## Prevention

1. Regularly update dependencies:
   ```bash
   pip install -r requirements.txt --upgrade
   ```

2. Use the environment diagnostic script regularly:
   ```bash
   python scripts/diagnose_environment.py
   ```

3. Keep system packages updated:
   ```bash
   sudo apt update && sudo apt upgrade
   ```

This guide should help you recover the Atlas environment manually when automated recovery scripts fail.