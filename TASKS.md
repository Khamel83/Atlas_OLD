# 🛡️ BULLETPROOF ATLAS PROCESS MANAGEMENT IMPLEMENTATION

**CRITICAL CONTEXT**: This is a complete implementation plan to eliminate memory leaks and runaway processes in the Atlas system. All tasks are designed to be executed by an AI model without ambiguity or token-intensive research.

## 📁 PROJECT CONTEXT FOR AI MODELS

### Key File Locations (Verified Present):
- **Main Project Root**: `/home/ubuntu/dev/atlas/`
- **Python Environment**: `/home/ubuntu/dev/atlas/venv/bin/python` (MUST use this Python)
- **Existing Services**: `atlas_service_manager.py`, `atlas_background_service.py`, `atlas_status.py`
- **Process Manager**: `helpers/bulletproof_process_manager.py` (Already created, fully functional)
- **Test Directory**: `tests/` (Contains 25+ test files already)
- **Config System**: `helpers/config.py` loads from `.env` file
- **Log Directory**: `logs/` (Auto-created by services)

### Dependencies Available:
- **Python**: 3.12 via `/home/ubuntu/dev/atlas/venv/bin/python`
- **Testing**: pytest available in venv
- **Process Management**: psutil 7.0.0 installed
- **Required Tools**: All dependencies in `requirements.txt` (8 bytes, minimal file)

### Subprocess Usage (Found 10+ instances):
- Located in: `testing/`, `monitoring/`, core service files
- Pattern: `subprocess.run()`, `subprocess.Popen()` calls need replacement

### Systemd Services (Found):
- `/etc/systemd/system/atlas-health-check.service`
- `/etc/systemd/system/atlas-health-check.timer`
- `/etc/systemd/system/atlas_metrics_exporter.service`
- **NOTE**: No main `atlas.service` exists yet (will be created)

---

## 🎯 IMPLEMENTATION PHASES

### **PHASE 1: IMMEDIATE SYSTEM STABILIZATION** *(45 minutes)*

#### Task 1.1: Verify Project Environment *(5 minutes)*
**Objective**: Confirm all prerequisites before making changes

**Validation Commands** (Execute in sequence):
```bash
cd /home/ubuntu/dev/atlas
./venv/bin/python --version  # Must return Python 3.12.x
./venv/bin/python -c "import psutil; print(f'psutil {psutil.__version__}')"  # Must return psutil 7.x
./venv/bin/python -c "import pytest; print('pytest OK')"  # Must not error
ls -la helpers/bulletproof_process_manager.py  # Must exist and be >30KB
```

**Success Criteria**:
- All commands execute without error
- Files exist at specified locations
- Dependencies are available

**Failure Recovery**: If any command fails, STOP and report the specific failure.

#### Task 1.2: Install Required Monitoring Tools *(10 minutes)*
**Objective**: Install memory profiling and testing tools

**Commands** (Execute using correct Python path):
```bash
cd /home/ubuntu/dev/atlas
./venv/bin/pip install memray pytest-memray tracemalloc-python
./venv/bin/python -c "import memray; print('memray installed')"
export PYTHONMALLOC=malloc
echo "export PYTHONMALLOC=malloc" >> ~/.bashrc
```

**Success Criteria**:
- `memray` imports without error
- Environment variable set

#### Task 1.3: Create Main Systemd Service *(20 minutes)*
**Objective**: Create bulletproof systemd service configuration

**IMPORTANT**: Check if service already exists first:
```bash
ls -la /etc/systemd/system/atlas.service
```

If service does NOT exist, create it:
```bash
sudo tee /etc/systemd/system/atlas.service > /dev/null << 'EOF'
[Unit]
Description=Atlas Content Intelligence Platform - Process-Safe Version
After=network-online.target
StartLimitIntervalSec=300
StartLimitBurst=3

[Service]
Type=oneshot
User=ubuntu
WorkingDirectory=/home/ubuntu/dev/atlas
Environment=PYTHONMALLOC=malloc
Environment=PYTHONPATH=/home/ubuntu/dev/atlas
ExecStartPre=/home/ubuntu/dev/atlas/venv/bin/python -c "import psutil; d=psutil.disk_usage('/'); print(f'Disk: {d.free/1024**3:.1f}GB free'); assert d.free/1024**3 > 5, 'Insufficient disk space'"
ExecStart=/home/ubuntu/dev/atlas/venv/bin/python atlas_service_manager.py start --daemon
ExecStop=/home/ubuntu/dev/atlas/venv/bin/python atlas_service_manager.py stop --force-cleanup
ExecStopPost=/usr/bin/pkill -f "atlas_"
Restart=on-failure
RestartSec=30
TimeoutStartSec=120
TimeoutStopSec=60

# Resource limits (CRITICAL for preventing runaway processes)
LimitNOFILE=1024
LimitNPROC=50
MemoryMax=1G
CPUQuota=200%

[Install]
WantedBy=multi-user.target
EOF
```

**Validation**:
```bash
sudo systemctl daemon-reload
sudo systemctl status atlas.service  # Should show 'loaded' state
```

#### Task 1.4: Emergency Process Cleanup *(10 minutes)*
**Objective**: Clean any existing runaway processes

```bash
# Find and kill any existing atlas processes
pkill -f "atlas_" || echo "No atlas processes found"
pkill -f "python.*atlas" || echo "No python atlas processes found"

# Verify cleanup
ps aux | grep atlas | grep -v grep || echo "No atlas processes remaining"

# Clean up any large log files
find /home/ubuntu/dev/atlas/logs -name "*.log" -size +100M -exec mv {} {}.old \; 2>/dev/null || echo "No large log files found"
```

---

### **PHASE 2: CORE INFRASTRUCTURE DEPLOYMENT** *(2 hours)*

#### Task 2.1: Integration Testing of BulletproofProcessManager *(30 minutes)*
**Objective**: Verify the existing process manager works correctly

**Test Script** (Create and run):
```bash
cd /home/ubuntu/dev/atlas
cat > test_bulletproof_manager.py << 'EOF'
#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/ubuntu/dev/atlas')

from helpers.bulletproof_process_manager import get_manager, create_managed_process
import time
import os

def test_basic_functionality():
    print("🧪 Testing BulletproofProcessManager...")
    
    # Test process creation
    process = create_managed_process(['sleep', '5'], 'test_process')
    print(f"✅ Created process PID: {process.pid}")
    
    # Test status
    manager = get_manager()
    status = manager.get_status()
    print(f"✅ Manager status: {status['total_processes']} processes")
    
    # Test cleanup
    success = manager.kill_process(process.pid)
    print(f"✅ Process cleanup: {'SUCCESS' if success else 'FAILED'}")
    
    print("🎉 BulletproofProcessManager test completed!")
    return True

if __name__ == "__main__":
    test_basic_functionality()
EOF

# Run the test
./venv/bin/python test_bulletproof_manager.py
```

**Success Criteria**:
- Test script runs without errors
- Process creation and cleanup work
- Manager status returns valid data

#### Task 2.2: Find and Replace Subprocess Calls *(45 minutes)*
**Objective**: Replace all dangerous subprocess calls with managed versions

**Step 1**: Find all subprocess usage:
```bash
cd /home/ubuntu/dev/atlas
rg -n "subprocess\.(Popen|run|call)" --type py > subprocess_locations.txt
cat subprocess_locations.txt  # Review all locations
```

**Step 2**: For each file found, apply this replacement pattern:

**OLD CODE**:
```python
import subprocess
result = subprocess.run(command, capture_output=True, text=True)
# or
process = subprocess.Popen(command, stdout=subprocess.PIPE)
```

**NEW CODE**:
```python
from helpers.bulletproof_process_manager import create_managed_process
process = create_managed_process(command, f"operation_name_{os.getpid()}")
result = process.communicate()  # For run() replacement
```

**Specific Files to Update** (Based on analysis):
1. `testing/mac_mini_bulk_processor.py:166,476,568`
2. `testing/ground_truth_setup.py:249,260`
3. `testing/ingestion_prototype.py:292`
4. `monitoring/grafana_config.py:38,44,49`
5. `test_block_executor.py:21`

**Step 3**: Validate each change:
```bash
./venv/bin/python -m py_compile [modified_file.py]
```

#### Task 2.3: Update Service Manager Integration *(30 minutes)*
**Objective**: Integrate bulletproof management into atlas_service_manager.py

**Location**: `/home/ubuntu/dev/atlas/atlas_service_manager.py`

**Modifications Required**:
1. Add import at top of file (after line 30):
```python
from helpers.bulletproof_process_manager import get_manager, create_managed_process
```

2. Find any subprocess calls in the file and replace with `create_managed_process()`

3. Add cleanup method to `AtlasServiceManager` class:
```python
def cleanup_processes(self):
    """Cleanup all managed processes"""
    manager = get_manager()
    manager.cleanup_all()
    logging.info("🧹 All processes cleaned up")
```

4. Add signal handlers in `__init__` method:
```python
# Register cleanup on exit
import atexit
atexit.register(self.cleanup_processes)
signal.signal(signal.SIGTERM, lambda s, f: self.cleanup_processes())
signal.signal(signal.SIGINT, lambda s, f: self.cleanup_processes())
```

**Validation**:
```bash
./venv/bin/python -m py_compile atlas_service_manager.py
./venv/bin/python atlas_service_manager.py --help  # Should not error
```

#### Task 2.4: Implement Resource Monitoring *(15 minutes)*
**Objective**: Add pre-flight checks to all service operations

**Create monitoring script**:
```bash
cat > helpers/resource_monitor.py << 'EOF'
#!/usr/bin/env python3
import psutil
import sys
from pathlib import Path

def check_system_health():
    """Pre-flight system health check"""
    issues = []
    
    # Disk space
    disk = psutil.disk_usage('/')
    free_gb = disk.free / (1024**3)
    if free_gb < 5.0:
        issues.append(f"Low disk space: {free_gb:.1f}GB (need 5GB+)")
    
    # Memory
    memory = psutil.virtual_memory()
    if memory.percent > 90:
        issues.append(f"High memory usage: {memory.percent}%")
    
    # Log files
    log_dir = Path("logs")
    if log_dir.exists():
        for log_file in log_dir.glob("*.log"):
            size_mb = log_file.stat().st_size / (1024**2)
            if size_mb > 100:
                issues.append(f"Large log file: {log_file} ({size_mb:.1f}MB)")
    
    if issues:
        print("🚨 SYSTEM HEALTH ISSUES:")
        for issue in issues:
            print(f"   ❌ {issue}")
        return False
    
    print("✅ System health check passed")
    return True

if __name__ == "__main__":
    success = check_system_health()
    sys.exit(0 if success else 1)
EOF
```

---

### **PHASE 3: COMPREHENSIVE TESTING SUITE** *(2.5 hours)*

#### Task 3.1: Create Memory Leak Detection Tests *(60 minutes)*
**Objective**: Build automated tests to detect memory leaks

**Location**: `tests/test_memory_leaks.py`

```python
#!/usr/bin/env python3
"""
Memory Leak Detection Test Suite
Verifies that the bulletproof process manager prevents memory leaks
"""
import pytest
import psutil
import time
import threading
from helpers.bulletproof_process_manager import get_manager, create_managed_process

class TestMemoryLeaks:
    def test_no_subprocess_memory_leaks(self):
        """Test that subprocess creation doesn't leak memory"""
        manager = get_manager()
        initial_memory = psutil.Process().memory_info().rss
        
        # Create and cleanup 10 processes
        for i in range(10):
            process = create_managed_process(['echo', f'test_{i}'], f'test_process_{i}')
            process.wait()
            manager.kill_process(process.pid)
            time.sleep(0.1)
        
        final_memory = psutil.Process().memory_info().rss
        memory_growth_mb = (final_memory - initial_memory) / (1024 * 1024)
        
        # Should not grow more than 10MB
        assert memory_growth_mb < 10, f"Memory grew by {memory_growth_mb:.1f}MB"
    
    def test_process_tree_cleanup(self):
        """Test that child processes are properly cleaned up"""
        # Create a process that spawns children
        process = create_managed_process(['bash', '-c', 'sleep 5 & sleep 5 & wait'], 'multi_process_test')
        time.sleep(1)  # Let children spawn
        
        manager = get_manager()
        manager.kill_process(process.pid)
        time.sleep(2)  # Allow cleanup
        
        # Verify no orphaned processes
        for proc in psutil.process_iter(['pid', 'cmdline']):
            if proc.info['cmdline'] and 'sleep 5' in ' '.join(proc.info['cmdline']):
                pytest.fail(f"Found orphaned process: {proc.info}")
    
    @pytest.mark.limit_memory("256 MB")
    def test_memory_growth_under_load(self):
        """Test memory usage under process creation load"""
        manager = get_manager()
        processes = []
        
        # Create 20 concurrent processes
        for i in range(20):
            proc = create_managed_process(['sleep', '2'], f'load_test_{i}')
            processes.append(proc)
        
        # Wait for all to complete
        for proc in processes:
            proc.wait()
        
        # Cleanup
        for proc in processes:
            manager.kill_process(proc.pid)
```

**Validation**:
```bash
./venv/bin/python -m pytest tests/test_memory_leaks.py -v
```

#### Task 3.2: Create Process Management Tests *(45 minutes)*
**Objective**: Test process lifecycle management

**Location**: `tests/test_process_management.py`

```python
#!/usr/bin/env python3
"""
Process Management Test Suite
Tests all aspects of bulletproof process management
"""
import pytest
import time
import signal
from helpers.bulletproof_process_manager import get_manager, create_managed_process

class TestProcessManagement:
    def test_concurrent_process_creation(self):
        """Test creating multiple processes concurrently"""
        manager = get_manager()
        processes = []
        
        # Create 5 processes simultaneously
        for i in range(5):
            proc = create_managed_process(['sleep', '3'], f'concurrent_{i}')
            processes.append(proc)
        
        # Verify all are running
        assert len(manager.get_status()['processes']) >= 5
        
        # Cleanup
        for proc in processes:
            manager.kill_process(proc.pid)
    
    def test_process_timeout_handling(self):
        """Test that processes respect timeout limits"""
        # Create process with 2-second timeout
        process = create_managed_process(['sleep', '10'], 'timeout_test', timeout=2)
        
        start_time = time.time()
        process.wait()  # Should be killed by timeout
        elapsed = time.time() - start_time
        
        # Should complete within 3 seconds (2s timeout + 1s buffer)
        assert elapsed < 3, f"Process ran for {elapsed:.1f}s, expected ~2s"
    
    def test_circuit_breaker_prevents_runaway(self):
        """Test that circuit breaker stops failing operations"""
        manager = get_manager()
        
        # Trigger multiple failures
        for i in range(10):
            try:
                create_managed_process(['nonexistent_command'], f'fail_test_{i}')
            except:
                pass  # Expected to fail
        
        # Circuit breaker should be open now
        status = manager.get_status()
        circuit_states = [cb['state'] for cb in status['circuit_breakers'].values()]
        assert 'OPEN' in circuit_states, "Circuit breaker should be open after failures"
```

**Validation**:
```bash
./venv/bin/python -m pytest tests/test_process_management.py -v
```

#### Task 3.3: Create System Endurance Tests *(60 minutes)*
**Objective**: Long-running stability tests

**Location**: `tests/test_system_endurance.py`

```python
#!/usr/bin/env python3
"""
System Endurance Test Suite
Tests long-term stability and resource management
"""
import pytest
import time
import threading
from helpers.bulletproof_process_manager import get_manager, create_managed_process
from helpers.resource_monitor import check_system_health

class TestSystemEndurance:
    def test_continuous_operation_stability(self):
        """Test system stability over extended operation (5 minutes)"""
        manager = get_manager()
        end_time = time.time() + 300  # 5 minutes
        process_count = 0
        
        while time.time() < end_time:
            # Create short-lived processes continuously
            proc = create_managed_process(['echo', f'test_{process_count}'], f'endurance_{process_count}')
            proc.wait()
            manager.kill_process(proc.pid)
            process_count += 1
            time.sleep(0.5)
        
        # Verify system is still healthy
        assert check_system_health(), "System health check failed after endurance test"
        assert process_count > 100, f"Only created {process_count} processes in 5 minutes"
    
    def test_memory_stability_under_load(self):
        """Test memory remains stable under continuous load"""
        import psutil
        initial_memory = psutil.Process().memory_info().rss
        
        # Run load for 2 minutes
        end_time = time.time() + 120
        while time.time() < end_time:
            processes = []
            for i in range(5):
                proc = create_managed_process(['sleep', '1'], f'memory_load_{i}')
                processes.append(proc)
            
            for proc in processes:
                proc.wait()
            
            time.sleep(1)
        
        final_memory = psutil.Process().memory_info().rss
        growth_mb = (final_memory - initial_memory) / (1024 * 1024)
        
        assert growth_mb < 50, f"Memory grew by {growth_mb:.1f}MB during load test"
    
    @pytest.mark.slow
    def test_service_restart_resilience(self):
        """Test that services can be restarted without issues"""
        manager = get_manager()
        
        # Create some processes
        processes = []
        for i in range(3):
            proc = create_managed_process(['sleep', '30'], f'restart_test_{i}')
            processes.append(proc)
        
        # Simulate service restart
        manager.cleanup_all()
        
        # Verify all processes are cleaned up
        time.sleep(2)
        remaining = [p for p in processes if p.poll() is None]
        assert len(remaining) == 0, f"{len(remaining)} processes not cleaned up"
```

**Validation**:
```bash
./venv/bin/python -m pytest tests/test_system_endurance.py::test_continuous_operation_stability -v -s
```

#### Task 3.4: Configure pytest with Memory Profiling *(30 minutes)*
**Objective**: Set up automatic memory leak detection in tests

**Update**: `pytest.ini`
```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v 
    --tb=short
    --memray
    --memray-bin-path=memray-logs
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    limit_memory: marks tests with memory limits
```

**Create memory test configuration**:
```bash
mkdir -p memray-logs
cat > conftest.py << 'EOF'
import pytest
import psutil
import os

@pytest.fixture(autouse=True)
def memory_leak_detector():
    """Automatically detect memory leaks in tests"""
    initial_memory = psutil.Process().memory_info().rss
    yield
    final_memory = psutil.Process().memory_info().rss
    
    growth_mb = (final_memory - initial_memory) / (1024 * 1024)
    if growth_mb > 10:  # Alert if test grows memory by >10MB
        pytest.fail(f"Test caused memory leak: {growth_mb:.1f}MB growth")
EOF
```

**Validation**:
```bash
./venv/bin/python -m pytest --help | grep memray  # Should show memray options
```

---

### **PHASE 4: SERVICE HARDENING** *(1.5 hours)*

#### Task 4.1: Update All Service Scripts *(45 minutes)*
**Objective**: Integrate bulletproof management into all services

**Files to Update**:
1. `atlas_background_service.py`
2. `atlas_service_manager.py` 
3. `scripts/atlas_scheduler.py`

**Standard Integration Pattern** (Apply to each file):

1. Add imports at the top:
```python
from helpers.bulletproof_process_manager import get_manager, create_managed_process
from helpers.resource_monitor import check_system_health
```

2. Add pre-flight check to main execution:
```python
def main():
    if not check_system_health():
        logging.error("System health check failed, aborting")
        sys.exit(1)
    
    # Existing main logic...
```

3. Replace subprocess calls:
```python
# OLD: subprocess.run(command, ...)
# NEW: process = create_managed_process(command, operation_name)
```

4. Add cleanup in main():
```python
def cleanup_and_exit():
    manager = get_manager()
    manager.cleanup_all()
    sys.exit(0)

# Register cleanup
signal.signal(signal.SIGTERM, lambda s, f: cleanup_and_exit())
signal.signal(signal.SIGINT, lambda s, f: cleanup_and_exit())
```

**Validation for Each File**:
```bash
./venv/bin/python -m py_compile [filename.py]
./venv/bin/python [filename.py] --help  # Should not error
```

#### Task 4.2: Create Process Watchdog Service *(30 minutes)*
**Objective**: Monitor and restart failed services automatically

**Location**: `helpers/bulletproof_watchdog.py`

```python
#!/usr/bin/env python3
"""
Bulletproof Watchdog Service
Monitors Atlas services and ensures they stay healthy
"""
import time
import psutil
import logging
import threading
from pathlib import Path
from helpers.bulletproof_process_manager import get_manager

class AtlasWatchdog:
    def __init__(self, check_interval=30):
        self.check_interval = check_interval
        self.running = False
        self.services_to_monitor = [
            'atlas_background_service.py',
            'atlas_service_manager.py'
        ]
    
    def start(self):
        """Start the watchdog"""
        self.running = True
        thread = threading.Thread(target=self._monitor_loop, daemon=True)
        thread.start()
        logging.info("🐕 Atlas watchdog started")
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                self._check_services()
                self._check_resources()
                time.sleep(self.check_interval)
            except Exception as e:
                logging.error(f"Watchdog error: {e}")
    
    def _check_services(self):
        """Check if required services are running"""
        manager = get_manager()
        status = manager.get_status()
        
        if status['total_processes'] == 0:
            logging.warning("🚨 No processes running, may need to restart services")
        
        # Check for failed circuit breakers
        for name, cb_status in status['circuit_breakers'].items():
            if cb_status['state'] == 'OPEN':
                logging.error(f"🔴 Circuit breaker OPEN for {name}")
    
    def _check_resources(self):
        """Check system resources"""
        # Memory check
        memory = psutil.virtual_memory()
        if memory.percent > 95:
            logging.error(f"🚨 Critical memory usage: {memory.percent}%")
        
        # Disk check  
        disk = psutil.disk_usage('/')
        free_gb = disk.free / (1024**3)
        if free_gb < 1.0:
            logging.error(f"🚨 Critical disk space: {free_gb:.1f}GB")

if __name__ == "__main__":
    watchdog = AtlasWatchdog()
    watchdog.start()
    
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        watchdog.running = False
```

#### Task 4.3: Update Task Management Integration *(15 minutes)*
**Objective**: Integrate with existing task management system

**Location**: `task_management/enhanced_task_manager.py`

**Modifications**:
1. Import bulletproof manager at top
2. Replace any subprocess calls with `create_managed_process()`
3. Add cleanup to task completion

**Validation**:
```bash
./venv/bin/python -m py_compile task_management/enhanced_task_manager.py
```

---

### **PHASE 5: CI/CD AND AUTOMATION** *(1 hour)*

#### Task 5.1: Create GitHub Actions Workflow *(30 minutes)*
**Objective**: Automate testing and deployment

**Location**: `.github/workflows/bulletproof-ci.yml`

```yaml
name: Bulletproof Process Management CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python 3.12
      uses: actions/setup-python@v4
      with:
        python-version: '3.12'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install memray pytest-memray
    
    - name: Run bulletproof manager tests
      run: |
        python -m pytest tests/test_memory_leaks.py -v
        python -m pytest tests/test_process_management.py -v
    
    - name: Test subprocess replacement
      run: |
        # Verify no dangerous subprocess usage remains
        ! grep -r "subprocess\\.\\(run\\|call\\|Popen\\)" --include="*.py" . || exit 1
    
    - name: System integration test
      run: |
        python test_bulletproof_manager.py
    
    - name: Memory leak scan
      run: |
        python -m pytest tests/test_system_endurance.py::test_memory_stability_under_load -v
```

#### Task 5.2: Create Deployment Script *(30 minutes)*
**Objective**: Automated deployment with safety checks

**Location**: `scripts/bulletproof_deploy.sh`

```bash
#!/bin/bash
set -euo pipefail

echo "🚀 Atlas Bulletproof Deployment Script"
echo "======================================"

# Pre-deployment checks
echo "📋 Pre-deployment checks..."
cd /home/ubuntu/dev/atlas

# Verify environment
./venv/bin/python --version
./venv/bin/python -c "import psutil; print(f'psutil {psutil.__version__}')"

# Run tests
echo "🧪 Running tests..."
./venv/bin/python -m pytest tests/test_memory_leaks.py -v
./venv/bin/python -m pytest tests/test_process_management.py -v

# System health check
./venv/bin/python helpers/resource_monitor.py

# Stop existing services
echo "⏹️ Stopping existing services..."
sudo systemctl stop atlas.service || echo "Service not running"
pkill -f "atlas_" || echo "No atlas processes found"

# Deploy new configuration
echo "📦 Deploying bulletproof configuration..."
sudo systemctl daemon-reload
sudo systemctl enable atlas.service

# Start services
echo "▶️ Starting services..."
sudo systemctl start atlas.service

# Verification
echo "✅ Deployment verification..."
sleep 10
sudo systemctl status atlas.service
./venv/bin/python atlas_status.py

echo "🎉 Bulletproof deployment completed successfully!"
```

---

### **PHASE 6: DOCUMENTATION AND MONITORING** *(45 minutes)*

#### Task 6.1: Update Project Documentation *(20 minutes)*
**Objective**: Document the new bulletproof system

**Update CLAUDE.md** (Append to existing file):
```markdown

## 🛡️ BULLETPROOF PROCESS MANAGEMENT

### New Architecture (Aug 2025)
The Atlas system now uses bulletproof process management to eliminate memory leaks and runaway processes.

### Key Components:
- **BulletproofProcessManager**: All process creation goes through this manager
- **Memory Leak Detection**: Continuous monitoring with automatic alerts
- **Circuit Breakers**: Prevent cascading failures
- **Resource Limits**: Hard limits on memory, files, processes
- **Process Registry**: Tracks and cleans up all spawned processes

### Usage:
```python
# OLD (dangerous)
import subprocess
process = subprocess.run(command)

# NEW (bulletproof) 
from helpers.bulletproof_process_manager import create_managed_process
process = create_managed_process(command, "operation_name")
```

### System Health:
```bash
./venv/bin/python helpers/resource_monitor.py  # Check system health
./venv/bin/python atlas_status.py --detailed    # Full system status
```

### Testing:
```bash
./venv/bin/python -m pytest tests/test_memory_leaks.py -v
./venv/bin/python -m pytest tests/test_process_management.py -v
```
```

#### Task 6.2: Create Troubleshooting Guide *(15 minutes)*
**Objective**: Help debug common issues

**Location**: `TROUBLESHOOTING.md`

```markdown
# 🔧 Atlas Bulletproof Troubleshooting Guide

## Common Issues and Solutions

### Memory Leaks Detected
**Symptoms**: Memory usage continuously grows
**Solution**:
1. Check logs: `tail -f logs/bulletproof_process_manager.log`
2. Review memory reports: `ls -la logs/memory_leak_*.json`
3. Restart services: `sudo systemctl restart atlas.service`

### Circuit Breaker Open
**Symptoms**: Operations failing with "Circuit breaker is OPEN"
**Solution**:
1. Check what's failing: `./venv/bin/python atlas_status.py --detailed`
2. Fix underlying issue (disk space, permissions, etc.)
3. Wait for automatic reset or restart service

### Service Won't Start
**Symptoms**: `systemctl start atlas.service` fails
**Solution**:
1. Check system health: `./venv/bin/python helpers/resource_monitor.py`
2. Check logs: `journalctl -u atlas.service -f`
3. Verify Python environment: `./venv/bin/python --version`

### High Resource Usage
**Symptoms**: High CPU/memory alerts
**Solution**:
1. Check process status: `./venv/bin/python atlas_status.py`
2. Kill runaway processes: `sudo systemctl stop atlas.service`
3. Clean up: `pkill -f atlas_`

## Emergency Commands
```bash
# Emergency stop everything
sudo systemctl stop atlas.service
pkill -f "atlas_"

# Clean up large log files
find logs/ -name "*.log" -size +100M -exec mv {} {}.old \;

# Reset circuit breakers
sudo systemctl restart atlas.service
```
```

#### Task 6.3: Create Monitoring Dashboard *(10 minutes)*
**Objective**: Real-time system monitoring

**Location**: `monitoring/bulletproof_dashboard.py`

```python
#!/usr/bin/env python3
"""
Bulletproof Process Management Dashboard
Real-time monitoring of system health
"""
import time
import json
from helpers.bulletproof_process_manager import get_manager
from helpers.resource_monitor import check_system_health

def generate_dashboard():
    """Generate system dashboard data"""
    manager = get_manager()
    status = manager.get_status()
    
    dashboard = {
        'timestamp': str(status['timestamp']),
        'system_health': check_system_health(),
        'processes': {
            'total': status['total_processes'],
            'running': status['running_processes'],
        },
        'resources': {
            'memory_mb': status['memory_usage_mb'],
            'cpu_percent': status['cpu_percent'],
            'open_files': status['open_files']
        },
        'circuit_breakers': status['circuit_breakers']
    }
    
    return dashboard

if __name__ == "__main__":
    while True:
        dashboard = generate_dashboard()
        print(f"\n🛡️ Atlas Bulletproof Dashboard - {dashboard['timestamp']}")
        print(f"System Health: {'✅' if dashboard['system_health'] else '❌'}")
        print(f"Processes: {dashboard['processes']['running']}/{dashboard['processes']['total']}")
        print(f"Memory: {dashboard['resources']['memory_mb']:.1f}MB")
        print(f"CPU: {dashboard['resources']['cpu_percent']:.1f}%")
        
        time.sleep(10)
```

---

## 🎯 VALIDATION CHECKLIST

After completing all phases, verify success with these commands:

```bash
# 1. All tests pass
./venv/bin/python -m pytest tests/ -v

# 2. No dangerous subprocess usage
! rg "subprocess\.(run|call|Popen)" --type py . || echo "❌ Found unsafe subprocess usage"

# 3. Services start cleanly
sudo systemctl restart atlas.service
sudo systemctl status atlas.service

# 4. System health is good
./venv/bin/python helpers/resource_monitor.py

# 5. Bulletproof manager works
./venv/bin/python test_bulletproof_manager.py

# 6. Memory leak detection active
ls -la logs/bulletproof_process_manager.log

# 7. Circuit breakers functional
./venv/bin/python atlas_status.py --detailed
```

## 🚨 SUCCESS CRITERIA

**MANDATORY REQUIREMENTS** - All must be met:
1. ✅ All tests pass without errors
2. ✅ Zero unsafe subprocess usage in codebase
3. ✅ Services start and run stably
4. ✅ System health checks pass
5. ✅ Memory leak detection active
6. ✅ Process cleanup works correctly
7. ✅ Circuit breakers prevent runaway failures

**OPTIONAL ENHANCEMENTS**:
- GitHub Actions workflow configured
- Monitoring dashboard functional
- Documentation updated
- Troubleshooting guide created

## 🔥 EMERGENCY PROCEDURES

If ANY task fails:
1. **STOP immediately** - Do not proceed to next task
2. **Log the specific error** - Copy exact error message
3. **Check prerequisites** - Verify all dependencies are met
4. **Roll back changes** - Restore previous working state
5. **Report issue** - Include context and error details

**Emergency Recovery Commands**:
```bash
# Stop all Atlas processes
sudo systemctl stop atlas.service
pkill -f "atlas_"

# Restore system
cd /home/ubuntu/dev/atlas
git checkout HEAD -- .  # Restore files if needed

# Clean up
rm -f test_bulletproof_manager.py subprocess_locations.txt
```

This plan is designed to be executed by an AI model with zero ambiguity and maximum safety. Each task includes explicit success criteria and failure recovery procedures.