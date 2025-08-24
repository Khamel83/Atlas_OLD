# Agents — Single Source of Truth

This file governs how any agent (Gemini, Claude, Qwen, etc.) executes work. Model-specific nuances belong in their respective files and do not override this lifecycle.

## 1) Execution Lifecycle (for each Task)
1. **Preflight**
   - Read `tasks.md`; topologically sort tasks by `depends_on`.
   - Validate `.env` against `.env.template`; fail with missing keys listed.
   - Run `git status` must be clean on `main`. If not, commit/stash before proceeding.
   - **Preflight hard checks (extended)**
     - `scripts/preflight.sh` (ensures .env, OpenRouter defaults, budgets, policy).
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

## 2) Failure & Self-Repair
- On failure at any step:
  - Record failure details and artifacts in `EXECUTION_LOG.md`.
  - Create a follow-up task `FIX-<id>-<slug>` with precise remediation steps.
  - Retry policy: up to 2 automated retries if clearly actionable; otherwise escalate by creating a fix task and halting the pipeline beyond dependent tasks.

## 3) Commit Conventions
- `task(<id>): <concise change>`
- Body: what/why; reference artifacts or doc sections.
- Footer: `Refs: task <id>`; use GitHub issue links if available.

## 4) Branch Naming
- `task/<id>-<slug>`
- Fixes: `fix/<id>-<slug>` (for follow-ups not tied to a specific task block).

## 5) Env Management
- Required keys listed in `.env.template`. Do not commit `.env`.
- If a key is optional, mark it `# optional` in `.env.template`.

## 6) Model Runtime Guidance (summary)
- Use the simplest capable model for mechanical edits.
- Chunk changes: favor small, verifiable commits over mega-diffs.
- On ambiguity, stop and add a clarification sub-task in `tasks.md`; do not guess silently.

## 7) Success Definition
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
