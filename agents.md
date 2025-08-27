# Agents — Single Source of Truth

**CURRENT STATUS**: Atlas 97% Complete - Phase A Core Functionality Nearly Complete (Aug 27, 2025)
**PRODUCTION READINESS**: 97% - Search + Intelligence Integration Operational  
**DEFINITIVE COMPLETION PLAN**: See `FINAL_DEVELOPMENT_PLAN.md` - THE ONLY roadmap to follow
**CROSS-REFERENCE**: See `CLAUDE.md` for detailed completion status and technical implementation notes

This file governs how any agent (Gemini, Claude, Qwen, etc.) executes work. Model-specific nuances belong in their respective files and do not override this lifecycle.

## 🚨 MAJOR ACHIEVEMENTS (August 27, 2025)
- ✅ **Search Revolution**: 240,026 items searchable (203% coverage) - indexing bottleneck fixed
- ✅ **Intelligence Integration**: LLM-powered structured extraction working with OpenRouter API
- ✅ **Enhanced Search API**: Topics, entities, quality scores, sentiment in search results  
- ✅ **Database Schema**: Comprehensive insights schema (entities, quotes, topics, theses) operational
- ✅ **Process Monitoring**: Intelligent watchdog prevents resource waste, kills stuck processes

## 1) Execution Lifecycle (for each Task)
1. **Preflight** 
   - Read `tasks.md`; topologically sort tasks by `depends_on`.
   - Validate `.env` against `.env.template`; fail with missing keys listed.
   - Run `git status` must be clean on `main`. If not, commit/stash before proceeding.
   - **Preflight hard checks (extended)**
     - `scripts/preflight.sh` (ensures .env, OpenRouter defaults, budgets, policy).
     - **STORAGE CRISIS PREVENTION** (Added Aug 2025):
       - `df -h .` must show >5GB free before operations
       - `find . -name "*.log" -size +100M` must be empty (enforce log rotation)
       - Check background service resource usage, not just existence
     - Refresh index: `CURRENT_TASK_ID=<ID> scripts/update_index.sh`.
     - Budget check (estimate ok): `python3 scripts/budget_guard.py check --cost <est_cost_usd> --task <ID>`.
2. **Branch**
   - Create `task/<id>-<slug>` from `main`.
   - Commit message prefix standard: `task(<id>): ...`
3. **Execute**
   - Follow `steps` in the task block exactly, in order.
   - Make minimal, reviewable commits; reference the task id in each message.
4. **Verify Gates**
   - All task `success` criteria met.
   - Repo checks (choose what applies here; customize if needed):
     - Unit tests pass.
     - Lint/type checks pass.
     - Integration checks for the changed module pass.
5. **Log**
   - Append a new entry to `EXECUTION_LOG.md` with: task id, branch, commits, artifacts, status, notes.
6. **Merge**
   - Rebase or merge `main` into branch if needed, resolve conflicts.
   - Merge branch to `main` (no squash; preserve history).
   - Tag optional release `v0.<phase>.<seq>` if the task is a milestone.
7. **Post-Merge**
   - Update `tasks.md` status for that task.
   - If downstream tasks were blocked by this, unblocked tasks can now proceed.
   - Run `scripts/update_index.sh` and commit refreshed index:
     - `git add AGENT_INDEX.* && git commit -m "task(<ID>): refresh index" && git push`
   - Budget log: `python3 scripts/budget_guard.py log --cost <actual_or_est> --task <ID>`.
7. **Post-Merge**
   - Update `tasks.md` status for that task.
   - If downstream tasks were blocked by this, unblocked tasks can now proceed.

## 2) Storage Crisis Prevention (MANDATORY - Aug 2025 Learnings)
**NEVER REPEAT**: Background service + low disk space + no circuit breaker = 5.2GB log explosion

### Critical Implementation Requirements:
- **Pre-flight disk check**: `df -h . | awk 'NR==2{if($4+0<5) exit 1}'` before ANY background operation
- **Circuit breaker pattern**: Stop after 10 consecutive failures, don't retry indefinitely  
- **Log rotation enforcement**: No log file >100MB without rotation (check in preflight)
- **Failure rate monitoring**: If >50% operations fail, HALT and investigate immediately
- **Error deduplication**: Don't log identical errors repeatedly - summarize after 10 occurrences
- **Background service health**: Monitor CPU/memory/disk, not just process existence
- **Storage audits**: Weekly `du -sh` checks to identify bloat before crisis

### Root Cause Analysis (Aug 26, 2025):
- **error_log.jsonl**: 2.9GB, 7.3M lines (99.8% repeated "disk space" errors)  
- **ingest logs**: 2GB+ of failed retry attempts
- **System kept running**: No circuit breaker to stop futile operations
- **No monitoring**: 99.8% failure rate went unnoticed for days

## 3) Failure & Self-Repair
- On failure at any step:
  - Record failure details and artifacts in `EXECUTION_LOG.md`.
  - **STORAGE CHECK**: If disk <5GB, this is NOT a task failure - it's infrastructure crisis
  - Create a follow-up task `FIX-<id>-<slug>` with precise remediation steps.
  - Retry policy: up to 2 automated retries if clearly actionable; otherwise escalate by creating a fix task and halting the pipeline beyond dependent tasks.

## 4) Commit Conventions
- `task(<id>): <concise change>`
- Body: what/why; reference artifacts or doc sections.
- Footer: `Refs: task <id>`; use GitHub issue links if available.

## 5) Branch Naming
- `task/<id>-<slug>`
- Fixes: `fix/<id>-<slug>` (for follow-ups not tied to a specific task block).

## 6) Env Management
- Required keys listed in `.env.template`. Do not commit `.env`.
- If a key is optional, mark it `# optional` in `.env.template`.

## 7) Model Runtime Guidance (summary)
- Use the simplest capable model for mechanical edits.
- Chunk changes: favor small, verifiable commits over mega-diffs.
- On ambiguity, stop and add a clarification sub-task in `tasks.md`; do not guess silently.

## 8) Success Definition
- Can a new contributor, given this repo and no extra context, run the system as intended? If not, update docs before marking done.
<!-- BEGIN: PRE_FLIGHT_HARD_CHECKS_EXTENDED -->
- `scripts/preflight.sh` must pass (ensures `.env`, OpenRouter defaults, budgets, policy).
- Refresh index **before** changes: `CURRENT_TASK_ID=<ID> scripts/update_index.sh`.
- Budget gate (estimate): `python3 scripts/budget_guard.py check --cost <est_cost_usd> --task <ID>`.
- Then proceed with branch creation and task execution.
<!-- END: PRE_FLIGHT_HARD_CHECKS_EXTENDED -->
<!-- BEGIN: POST_MERGE_EXTENDED -->
- Refresh index and commit:
  - `scripts/update_index.sh`
  - `git add AGENT_INDEX.* && git commit -m "task(<ID>): refresh index" && git push`
- Budget log (actual or estimate): `python3 scripts/budget_guard.py log --cost <actual_or_est> --task <ID>`.
<!-- END: POST_MERGE_EXTENDED -->
<!-- BEGIN: TASK_SELECTION_POLICY -->
### Task Selection Policy (no user prompts)
- When you are about to ask “what next?”, run:
  - `python3 scripts/next_task.py pick` → JSON of the highest-priority **unblocked** task(s).
- For each selected task `<ID>` / `<slug>`:
  1) `scripts/preflight.sh`
  2) `CURRENT_TASK_ID=<ID> scripts/update_index.sh`
  3) Create branch: `git checkout -b task/<ID>-<slug>` from `main`
  4) Execute steps from `tasks.md`
  5) Verify gates (tests/lint/integration)
  6) Append `EXECUTION_LOG.md`
  7) Merge to `main` (no squash)
  8) Post-merge index + budget log per the anchored sections
- If `NO-READY-TASK`: rebuild index; if still none, create `PLAN-NEXT` task with concrete next steps and stop.
<!-- END: TASK_SELECTION_POLICY -->
<!-- BEGIN: ID_BASED_ADDRESSING -->
### ID-based addressing
- Prefer `fid` from `AGENT_INDEX.json` over filenames.
- To resolve:
  - `python3 scripts/resolve_id.py to-path <fid>` → path
  - `python3 scripts/resolve_id.py to-id <path>` → fid
- Always update the index before and after tasks to keep IDs accurate.
<!-- END: ID_BASED_ADDRESSING -->
<!-- BEGIN: GRACEFUL_FAILURE_POLICY -->
### Graceful failure policy
- `ON_ERROR=skip|halt|ask` (default `skip`).
  - **skip**: If non-blocking, open `FIX-<ID>-<slug>`, log details, continue.
  - **halt**: Stop immediately on failure; log and exit.
  - **ask**: Stop and emit: **"come help me please user"**.
- `STRICT_MODE=true` forces halt on ambiguity; otherwise create a small “clarify” task and continue.
<!-- END: GRACEFUL_FAILURE_POLICY -->
