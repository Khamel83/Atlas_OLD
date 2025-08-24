# Atlas — Overview

Atlas is a local-first, cost-aware personal knowledge system. This repo is now structured so that:
- A simpler agent can execute tasks end-to-end.
- Every change is auditable (branch-per-task).
- Docs are human-readable; agent specifics live in `agents.md`.

## Quick Start
1. Copy `.env.template` to `.env` and fill in values you actually use.
2. Read `agents.md` for execution lifecycle, branching, and logging.
3. See `tasks.md` for the current roadmap and Phase 1 task list.
4. To run a task: follow the “Execution Lifecycle” in `agents.md`.

## Project Structure
- `README.md` — You are here; human-readable summary.
- `agents.md` — Single source of truth for agent execution.
- `tasks.md` — Roadmap and atomic tasks (Phase 1 detailed).
- `claude.md`, `gemini.md`, `qwen.md` — Model-specific deltas; defer to `agents.md`.
- `EXECUTION_LOG.md` — Append-only run log linking to commits/branches.
- `scripts/task_runner.sh` — Branch/commit/merge scaffolding.
- `.env.template` — Required env keys.

## Principles
- **Zero-questions**: Docs stand alone.
- **Idempotent**: Repeatable runs produce the same results.
- **Auditable**: Every task is branched, verified, logged, then merged.

## Status
- Phase 1: Detailed and ready to execute.
- Future phases: High-level; will be detailed as we progress.
