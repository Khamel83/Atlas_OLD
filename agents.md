# Agents — Single Source of Truth

This file governs how any agent (Gemini, Claude, Qwen, etc.) executes work. Model-specific nuances belong in their respective files and do not override this lifecycle.

## 1) Execution Lifecycle (for each Task)
1. **Preflight**
   - Read `tasks.md`; topologically sort tasks by `depends_on`.
   - Validate `.env` against `.env.template`; fail with missing keys listed.
   - Run `git status` must be clean on `main`. If not, commit/stash before proceeding.
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
