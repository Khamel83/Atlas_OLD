# Atlas Environment Recovery Plan

## 1. Immediate Steps to Diagnose Root Cause

1. **Identify the missing shared object file**
   - Determine which process is trying to load `/tmp/.3bdbfdadbd3a7ff2-00000001.node`
   - Check if this is related to Node.js, Python extensions, or other runtime dependencies

2. **Check system library dependencies**
   - Verify all required system libraries are installed
   - Check for missing or corrupted shared libraries
   - Examine LD_LIBRARY_PATH and other library loading environment variables

3. **Review recent changes**
   - Check git history for recent commits that might have introduced the issue
   - Review any dependency updates or environment changes
   - Examine system updates or configuration changes

## 2. Short-term Fixes to Restore Basic Functionality

1. **Rebuild the virtual environment**
   ```bash
   cd /home/ubuntu/dev/atlas
   rm -rf .venv
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Clear temporary files and caches**
   ```bash
   # Remove temporary files that might be causing conflicts
   rm -f /tmp/.3bdbfdadbd3a7ff2-00000001.node
   rm -rf /tmp/*  # Be careful with this command
   ```

3. **Reinstall problematic packages**
   - Identify Python packages that might have native extensions
   - Reinstall packages that might be causing the shared object error

## 3. Long-term Solutions to Prevent Recurrence

1. **Implement proper dependency management**
   - Use pip-tools or similar to lock dependencies
   - Create a dependency audit process
   - Regularly update and test dependencies

2. **Improve environment isolation**
   - Use Docker containers for consistent environments
   - Implement proper virtual environment management
   - Create reproducible build scripts

3. **Add monitoring and alerting**
   - Implement health checks for the environment
   - Add logging for shared library loading failures
   - Create automated recovery procedures

## 4. Specific Commands to Rebuild the Environment

1. **Complete environment rebuild**
   ```bash
   # Navigate to project directory
   cd /home/ubuntu/dev/atlas
   
   # Backup current environment
   mv .venv .venv.backup.$(date +%s)
   
   # Create fresh virtual environment
   python3 -m venv .venv
   source .venv/bin/activate
   
   # Upgrade pip
   pip install --upgrade pip
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Install development dependencies (if applicable)
   pip install -r requirements-dev.txt
   ```

2. **System-level fixes**
   ```bash
   # Update system packages
   sudo apt update && sudo apt upgrade -y
   
   # Install common development libraries
   sudo apt install build-essential libssl-dev libffi-dev python3-dev
   
   # Clean package cache
   sudo apt clean
   ```

3. **Node.js environment (if applicable)**
   ```bash
   # If Node.js is required
   npm cache clean --force
   rm -rf node_modules
   npm install
   ```

## 5. Verification Steps to Confirm Fixes

1. **Test basic command execution**
   ```bash
   # Test Python
   python --version
   
   # Test pip
   pip list
   
   # Test basic imports
   python -c "import sys; print('Python working')"
   ```

2. **Run environment validation**
   ```bash
   # Run the Atlas environment check
   python scripts/diagnose_environment.py
   
   # Run basic tests
   python -m pytest tests/test_environment_validation.py
   ```

3. **Verify application functionality**
   ```bash
   # Test core Atlas functionality
   python run.py --help
   
   # Run a simple ingestion test
   python helpers/article_fetcher.py
   ```

4. **Check for shared object errors**
   ```bash
   # Verify no shared object errors
   ldd $(which python)  # Check Python shared libraries
   ```

## Additional Troubleshooting Steps

If the issue persists:

1. **Check for conflicting processes**
   ```bash
   ps aux | grep node
   ps aux | grep python
   ```

2. **Examine system logs**
   ```bash
   journalctl -u atlas  # If running as a service
   dmesg | grep error
   ```

3. **Reboot the system**
   ```bash
   sudo reboot  # As a last resort
   ```

## Rollback Plan

If recovery attempts fail:

1. Restore from the most recent backup
2. Revert to a known working commit
3. Recreate the entire development environment from scratch