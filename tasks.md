# Atlas Production Fix Tasks - DEFINITIVE

**Current Reality**: 88,792 processed files, 8,216 database records, 37+ background processes, broken API endpoints
**Goal**: Make claimed functionality actually work + bulletproof clone experience  
**Timeline**: 6-8 days across 4 blocks

---

## **BLOCK 1: API ENDPOINT REPAIR** ⚡ (Days 1-2)

### **B1T1: Audit Cognitive API Failures**
- [ ] Test all cognitive endpoints: `curl http://localhost:8000/api/v1/cognitive/*`
- [ ] Document exact 404 errors and missing routes in `reports/api_audit_$(date +%Y%m%d).md`
- [ ] Map existing cognitive modules to expected endpoints
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Complete endpoint status report with specific error details

### **B1T2: Connect ProactiveSurfacer to API**
- [ ] Import `ask.proactive.surfacer.ProactiveSurfacer` in `api/routers/cognitive.py`
- [ ] Implement `/surface` endpoint calling `surface_content()` method
- [ ] Test endpoint returns real content recommendations (not empty/mock data)
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: `curl http://localhost:8000/api/v1/cognitive/surface` returns actual data

### **B1T3: Connect TemporalEngine to API**
- [ ] Import `ask.temporal.temporal_engine.TemporalEngine` in cognitive router
- [ ] Implement `/temporal` endpoint calling `analyze_patterns()` method
- [ ] Handle temporal analysis results in proper JSON format
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: `curl http://localhost:8000/api/v1/cognitive/temporal` returns pattern data

### **B1T4: Connect QuestionEngine to API**
- [ ] Import `ask.socratic.question_engine.QuestionEngine` in cognitive router
- [ ] Implement `/questions` endpoint calling `generate_questions()` method
- [ ] Accept topic parameter, return structured question list
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: `curl http://localhost:8000/api/v1/cognitive/questions?topic=technology` returns questions

### **B1T5: Validate All Cognitive Endpoints**
- [ ] Start FastAPI server: `uvicorn api.main:app --reload`
- [ ] Test all 4 cognitive endpoints return 200 status (not 404)
- [ ] Verify responses contain actual data (not empty/mock responses)
- [ ] Create `scripts/validate_cognitive_api.sh` test script
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: 4/4 cognitive endpoints functional with real data

---

## **BLOCK 2: BACKGROUND SERVICE CRISIS** 🚨 (Days 3-4)

### **B2T1: Kill Process Leak - EMERGENCY**
- [x] **IMMEDIATE**: Kill all background processes: `pkill -f "python.*run.py"`
- [x] Verify clean slate: `ps aux | grep atlas` shows no processes
- [x] Clear stale PID files in `logs/` directory
- [x] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Zero atlas processes running

### **B2T2: Analyze Service Architecture Crisis**
- [ ] Review `atlas_background_service.py` vs current inline python loop chaos
- [ ] Document why proper service manager not being used in `docs/SERVICE_ARCHITECTURE_ANALYSIS.md`
- [ ] Identify root cause of 37+ process spawning issue
- [ ] Define single unified service strategy
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Clear service strategy documented with implementation plan

### **B2T3: Implement Proper Service Control**
- [ ] Create `scripts/atlas_service.sh` with start/stop/status/restart commands
- [ ] Modify to use `atlas_background_service.py` (not inline python loops)
- [ ] Implement proper PID tracking and process monitoring
- [ ] Test service control commands work reliably
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Single controlled service process with proper management

### **B2T4: Service Health Monitoring & Auto-Recovery**
- [ ] Implement service health checks every 5 minutes
- [ ] Add automatic restart on service failure detection
- [ ] Log service status and restart events to `logs/atlas_service_health.log`
- [ ] Test recovery after simulated service crashes
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Self-healing background service with monitored health

### **B2T5: Validate Service Operation**
- [ ] Start service: `./scripts/atlas_service.sh start`
- [ ] Verify exactly 1 Atlas process running (not 37+)
- [ ] Test automatic restart after `kill -9 <pid>`
- [ ] Monitor service for 2+ hours to ensure stability
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Stable single-process service running for 2+ hours without issues

---

## **BLOCK 3: MAC MINI WORKER INTEGRATION** 🖥️ (Days 5-6)

### **B3T1: Verify Smart Dispatcher API**
- [ ] Test worker job creation endpoints: `curl http://localhost:8000/api/v1/worker/jobs`
- [ ] Validate job queue database tables exist and are populated
- [ ] Confirm API returns available jobs in proper format
- [ ] Document API endpoints in `docs/WORKER_API.md`
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Worker API endpoints functional and documented

### **B3T2: Mac Mini Client Development**
- [ ] Create `mac_mini_client.py` with job polling mechanism
- [ ] Implement job execution (transcription, content processing)
- [ ] Add result posting back to Atlas via API
- [ ] Test client connects and processes test jobs
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Mac Mini client connects, processes jobs, returns results

### **B3T3: Job Queue Integration Testing**
- [ ] Test job creation from Atlas content processing pipeline
- [ ] Verify Mac Mini picks up jobs automatically within 60 seconds
- [ ] Validate results integrate back into Atlas database correctly
- [ ] Test with 10+ different content types (podcasts, articles, documents)
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: End-to-end Atlas → Mac Mini → Atlas workflow tested and working

### **B3T4: Fallback and Recovery Validation**
- [ ] Test Atlas continues processing when Mac Mini offline (jobs queue but don't fail)
- [ ] Implement job timeout and retry logic for failed Mac Mini jobs
- [ ] Handle Mac Mini connection failures gracefully (no system crashes)
- [ ] Document fallback behavior in `docs/MAC_MINI_INTEGRATION.md`
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Atlas works independently, Mac Mini is optional acceleration

---

## **BLOCK 4: CLONE-AND-RUN EXPERIENCE** 📦 (Days 7-8)

### **B4T1: Bootstrap Script Enhancement**
- [ ] Update `start_work.sh` to handle complete setup automatically
- [ ] Include Python venv creation, dependency installation, database initialization
- [ ] Add environment validation and clear error messages for missing requirements
- [ ] Test script on fresh Ubuntu system to ensure zero manual intervention needed
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Single command `./start_work.sh` brings up fully functional Atlas

### **B4T2: Documentation Accuracy Audit & Correction**
- [ ] Test README.md instructions on fresh clone (document every step that fails)
- [ ] Verify all claimed features in CLAUDE.md actually work (test each claim)
- [ ] Update all documentation to match current reality (remove false claims)
- [ ] Create `docs/FRESH_INSTALL_GUIDE.md` with verified step-by-step instructions
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Documentation matches actual functionality, no false claims

### **B4T3: Zero-Config Database Setup**
- [ ] Ensure database auto-creates with proper schema on first run
- [ ] Pre-populate required initial data and configurations
- [ ] Handle missing database files gracefully with auto-recovery
- [ ] Test database setup on systems without existing Atlas data
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: Database works out of the box, no manual schema creation needed

### **B4T4: Integration Test Suite & Validation**
- [ ] Create `test_full_system.sh` testing: database, API, services, worker integration
- [ ] Test must pass on fresh clone without any manual setup
- [ ] Validate all core functionality automatically (no human verification needed)
- [ ] Create CI/CD workflow for GitHub Actions to run tests on pull requests
- [ ] **Task Completion**: Update tasks.md with ✅, commit changes, push to GitHub
- **Success**: `./test_full_system.sh` passes on fresh clone, automated testing works

---

## **FINAL DOCUMENTATION & GITHUB WORKFLOW** 📚

### **DOCUMENTATION UPDATE REQUIREMENTS** (After Each Block)
- [ ] **Update CLAUDE.md**: Remove false claims, add actual current functionality
- [ ] **Update README.md**: Ensure install instructions work on fresh systems
- [ ] **Create/Update docs/*.md**: Accurate technical documentation for working features
- [ ] **Archive old claims**: Move outdated status docs to `docs/archive/` folder

### **GITHUB WORKFLOW REQUIREMENTS** (After Each Task)
- [ ] **Commit Message Format**: `feat(block-X): [TaskID] - Brief description`
- [ ] **Push to GitHub**: `git push origin main` after each completed task
- [ ] **Create Issues**: For any discovered problems not in current task list
- [ ] **Update Project Board**: If using GitHub Projects, move tasks through pipeline

### **VALIDATION COMMANDS FOR FINAL SUCCESS**
```bash
# BLOCK 1: All cognitive endpoints work
curl -f http://localhost:8000/api/v1/cognitive/surface
curl -f http://localhost:8000/api/v1/cognitive/temporal  
curl -f http://localhost:8000/api/v1/cognitive/questions?topic=technology

# BLOCK 2: Single stable service
ps aux | grep atlas | wc -l  # Should return 1-2, not 37+
./scripts/atlas_service.sh status  # Should show healthy/running

# BLOCK 3: Mac Mini integration works
curl -f http://localhost:8000/api/v1/worker/jobs
python mac_mini_client.py --test  # Should connect and process

# BLOCK 4: Fresh clone works
cd /tmp && git clone [repo] test_atlas && cd test_atlas
./start_work.sh  # Should complete without errors
./test_full_system.sh  # Should pass all tests
```

---

## **REMOVED/COMPLETED TASKS FROM PREVIOUS VERSION**

**REMOVED** (Already completed based on current system state):
- ✅ Document extraction (88,792 files processed)
- ✅ Database population (8,216 records exist)
- ✅ Search system (36,303 searchable records confirmed)
- ✅ Article processing pipeline (working with content ingestion)
- ✅ All Phase 1-3 tasks from previous version (systems operational)

**FOCUS**: Fix what's broken (APIs, service management) and ensure new clone experience works perfectly.

---

## **SUCCESS CRITERIA - DEFINITIVE**

1. **API Endpoints**: All 4 cognitive endpoints return 200 with real data (not 404/empty)
2. **Background Service**: Exactly 1 Atlas service process (not 37+ spawning chaos)  
3. **Mac Mini Integration**: Optional worker system functional end-to-end OR gracefully offline
4. **Clone Experience**: Fresh clone → `./start_work.sh` → everything works without explanation
5. **Documentation Accuracy**: Every claim in docs validated and working
6. **GitHub Integration**: All work committed, pushed, and properly documented

**VALIDATION REQUIRED**: Each task must be validated with specific commands before marking complete. No "trust me it works" - prove it with curl/ps/test commands.