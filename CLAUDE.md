# Atlas Project Context

**📝 SYNC RULE**: When updating CLAUDE.md, also update agents.md to maintain consistency.

## 🎯 Key Directives
*   **Token Efficiency**: Use compact responses, abbreviations, and bullet points to conserve tokens.
*   **Configuration Management**: All user-configurable values must be in `.env` and loaded via environment variables. Update `.env.template` with any new variables.
*   **Component Registry**: Check `ATLAS_COMPONENT_INDEX.md` before creating new components to avoid duplication. Update the index when adding new capabilities.

## 📊 Authoritative Status
For the most detailed implementation status, see: `ATLAS_IMPLEMENTATION_STATUS.md`.

##  STATUS (Aug 28, 2025)

**REALITY CHECK**: The Atlas system is 95% production-ready, not "partially complete." All major features are implemented and functional. The remaining 5% is service integration work to prevent memory leaks and log growth.

### ✅ FULLY IMPLEMENTED FEATURES
- **Intelligence Modules**: All 6 ask modules complete (4,951 lines of production code)
  - Proactive content surfacing, temporal analysis, Socratic questioning  
  - Active recall system, pattern detection, content recommendations
- **Content Processing**: Full pipelines for articles, podcasts, documents, emails
- **Search & Semantic Indexing**: 240,026+ items indexed with AI-powered ranking  
- **Web Dashboard**: Complete cognitive amplification UI with all features
- **API Framework**: FastAPI with comprehensive endpoints for all cognitive features
- **Apple Integration**: iOS shortcuts, extensions, voice processing complete
- **Background Services**: Scheduling, monitoring, watchdog systems operational
- **Bulletproof Architecture**: Memory leak prevention system implemented

### 🚨 REMAINING INTEGRATION GAPS (5%)
- **Subprocess Integration**: Services use dangerous subprocess calls instead of bulletproof manager
- **Log Rotation Missing**: 5GB log files because rotation not enabled  
- **Health Checks Missing**: System health monitoring not integrated into main services
- **Service Integration**: Bulletproof architecture exists but not wired into service startup

### ⚡ COMPLETION PLAN (18 hours total)

**CRITICAL REALITY**: The system has incredible AI and processing capabilities but **TERRIBLE user experience**. Getting it "working" ≠ making it usable.

**Phase 1 - System Stability** (3.5h): Bulletproof architecture integration
**Phase 2 - User Documentation** (14.5h): Comprehensive user guides for everything
  - Mac integration and shortcuts setup (2h)
  - Content ingestion for every method (3h) 
  - Search and cognitive features (2h)
  - Setup guides for non-technical users (2.5h)
  - Mobile usage and automation (3.5h)
  - Maintenance and backup (1.5h)

**Result**: Truly production-ready Atlas that normal humans can actually use

### **Documentation Progress - 50% COMPLETE**
- **User Guides Created**: Maintenance, Automation, Mobile, Setup guides completed
- **User Guides Pending**: Mac workflows, Quick Start, Troubleshooting
- **Technical Docs**: API, Architecture, Configuration guides up-to-date

## 🚀 Daily Development Startup

### Recommended Startup
```bash
# This script should contain the necessary steps to start the development environment.
./start_work.sh
```

### Status Dashboard
```bash
# These scripts provide status checks on the system.
python atlas_status.py
python atlas_status.py --detailed
```

## 📝 COMPLETION TASKS (See TASKS.md for atomic tasks)

### **ATLAS-COMPLETE-001**: Replace Dangerous Subprocess Calls (1.5h)
- Replace subprocess usage in 4 critical service files with bulletproof process manager
- Add cleanup methods and signal handlers to prevent memory leaks

### **ATLAS-COMPLETE-002**: Enable Log Rotation (0.5h)  
- Create logrotate config to prevent 5GB file growth
- Immediate cleanup of existing large log files

### **ATLAS-COMPLETE-003**: Add System Health Monitoring (1h)
- Integrate pre-flight health checks into all services  
- Abort services if disk space <5GB or other resource issues

### **ATLAS-COMPLETE-004**: Create Production Systemd Service (0.5h)
- Bulletproof systemd service with resource limits and pre-flight checks

### **ATLAS-COMPLETE-005-008**: Validation & Deployment (1h)
- Test all features work, deploy services, validate end-to-end system

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
