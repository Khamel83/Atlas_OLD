# Atlas Project Context

## 🎯 Key Directives
*   **Token Efficiency**: Use compact responses, abbreviations, and bullet points to conserve tokens.
*   **Configuration Management**: All user-configurable values must be in `.env` and loaded via environment variables. Update `.env.template` with any new variables.
*   **Component Registry**: Check `ATLAS_COMPONENT_INDEX.md` before creating new components to avoid duplication. Update the index when adding new capabilities.

## 📊 Authoritative Status
For the most detailed implementation status, see: `ATLAS_IMPLEMENTATION_STATUS.md`.

##  STATUS (Aug 27, 2025)

The project is partially complete. Core ingestion and processing pipelines are functional, but several key features are either not yet implemented or require validation. The background services have known stability issues that are being addressed.

### Core Accomplishments
- **Content Processing**: Pipelines for articles, podcasts, and other sources are established.
- **Refactoring**: Phases 3 & 4 (ArticleManager, ContentPipeline) have been consolidated.
- **API Framework**: A FastAPI-based API is in place for core functions.
- **Metadata & Email**: Block 15 (Metadata Discovery) and Block 16 (Email Integration) are functional.
- **Background Services**: Service scripts exist but require hardening (see below).

### 🚨 Critical Known Issues & Required Fixes
- **Service Stability**: Background services are prone to failure due to not using the correct Python virtual environment (`venv`) and lacking resource checks.
- **Storage Crisis**: A previous failure involved uncontrolled log growth (5.2GB+) due to a lack of disk space checks, log rotation, and circuit breakers.

### Mandatory Stability Rules (Resulting from Storage Crisis)
1.  **Pre-flight Disk Checks**: All background operations must verify sufficient disk space (>5GB) before starting.
2.  **Circuit Breakers**: Services must stop retrying after a set number of consecutive failures (e.g., 3-10).
3.  **Log Rotation**: Log files must be rotated to prevent uncontrolled growth.
4.  **Failure Rate Monitoring**: High failure rates (>50%) should trigger alerts.
5.  **Deduplicate Error Logs**: Avoid logging identical errors repeatedly.

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

## 📝 Key Development Areas

### 1. Service Hardening (Immediate Priority)
- **Fix Venv Path**: Ensure all `subprocess` calls use the correct Python executable from the `atlas_venv`.
- **Integrate Pre-flight Checks**: Add the mandatory stability rules (disk space, log size) directly into the service startup logic.
- **Implement Circuit Breakers**: Add logic to services to halt after consecutive failures.

### 2. Feature Implementation & Validation
- **Cognitive Features**: The `ask` modules are mostly stubs and need to be implemented.
- **Analytics Dashboard (Block 8)**: The core structure exists but needs to be connected to live data.
- **Enhanced Search (Block 9)**: Basic search is functional but requires the implementation of ranking and semantic search capabilities.
- **Validate Frameworks**: Test and verify Docker/OCI deployment, Apple integration, and export tools.

### 3. Documentation & Cleanup
- **Update README**: Revise the main README with a realistic description of features and status.
- **Create Troubleshooting Guide**: Document common errors and their solutions.
- **Remove Superlatives**: Remove any remaining marketing language (e.g., "breakthrough", "revolutionary") from all project documentation.

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
