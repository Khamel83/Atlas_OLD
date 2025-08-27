# Atlas Development Philosophy

This document outlines the development philosophy and processes for the Atlas project. It is intended to be a living document that evolves with the project.

## Guiding Principles

- **Agent-First Development:** The primary audience for our code, documentation, and processes is AI agents. Humans are the second audience. This means that everything we do should be optimized for clarity, simplicity, and machine-readability.
- **Zero-Questions Standard:** Our goal is to create a project that can be understood and used by a new developer with no prior context, just by reading the documentation. If a question needs to be asked, the documentation has failed.
- **Transactional and Auditable:** Every change to the codebase should be a small, atomic, and verifiable transaction. This creates a detailed audit trail and makes it easy to recover from errors.
- **Mission-Driven:** All decisions should be made with the Atlas mission and vision in mind. When in doubt, choose the path that best advances the mission.

## AI-First Git & Commit Hygiene
- Optimize for **LLMs reading diffs**: many small commits > one giant diff.
- Commit prefix: `task(<ID>): <change>`; body = what/why; reference files and task ID.
- Push early/often. Humans can be messy; **the LLM must never be confused**.

## Continuous Preflight (Measure Twice, Cut Once)
- Before any task: run `scripts/preflight.sh`.
- Guarantees:
  - `.env` exists; required keys from `.env.template` are non-empty.
  - Python venv is present (`.venv`) and deps are installed.
  - Git workspace is clean on `main` (or committed/stashed).
  - **DISK SPACE CHECK**: Minimum 5GB free before operations
  - **LOG SIZE CHECK**: No single log file >100MB without rotation
- If any check fails: STOP, log to `EXECUTION_LOG.md`, open a `FIX-` task.

## Storage Crisis Prevention (Critical Learnings Aug 2025)
- **MANDATORY pre-flight disk checks** before background operations
- **Circuit breaker pattern** - Stop after 10 consecutive failures, don't retry indefinitely
- **Log rotation enforcement** - Size-based (50MB max) and time-based (daily) cleanup
- **Failure rate monitoring** - Alert if >50% operations fail, investigate immediately  
- **Error log deduplication** - Don't log identical errors repeatedly
- **Background service health** - Monitor resource usage, not just process existence
- **Storage audits** - Regular `du -sh` checks to identify bloat before crisis

## Agentic File Index (Transactional)
- Source of truth lives at `AGENT_INDEX.json` (machine-readable) and `AGENT_INDEX.md` (human).
- Rebuilt **before** executing a task and **after** merging a task via `scripts/update_index.sh`.
- Each entry includes: `path`, `type`, `size`, `sha256`, `mtime`, `tags` (by extension), `module`, `last_commit`, `last_task_id`.
- This index enables agents to discover what exists, where it is, and relevant metadata without guessing.

## Decision Records (ADR)
- For non-trivial changes, create an ADR in `docs/adr/` with `scripts/new_adr.sh "<title>"`.
- Each ADR states the decision, alternatives, and alignment to Atlas mission/vision.

## Agent Readability Conventions
- Use stable section markers in generated docs:
  - `<!-- BEGIN: AUTO-GENERATED <name> -->` … `<!-- END: AUTO-GENERATED <name> -->`
- Prefer deterministic formats (JSON, YAML, Markdown tables).
- Avoid silent renames. If renaming paths, update the index and note in `EXECUTION_LOG.md`.

## North Star: Atlas Mission & Vision
- When in doubt, choose the path that best advances an Atlas’ mission/vision and shortens time to a durable, low-ops product.

## Secrets & Environment
- Secrets are loaded via `.env` (auto-sourced in `scripts/preflight.sh`).
- Only *required* secret to run is an API key. All else is configuration with sensible defaults.
- Paths and toggles must be environment-driven (no hardcoded paths). Keep `.env.template` authoritative.

## AI Budget & Cost Guard
- Caps: `$AI_BUDGET_DAILY_USD` (default 1.00), `$AI_BUDGET_MONTHLY_USD` (default 10.00).
- Gate before tasks: `python3 scripts/budget_guard.py check --cost <est> --task <ID>`
- Log after tasks: `python3 scripts/budget_guard.py log --cost <actual_or_est> --task <ID>`
- Goal: stay far below caps; fail early if we’d exceed.

## ID-First File Addressing
- Agents should **not** parse filenames. Use `fid` from `AGENT_INDEX.json`.
- Resolve IDs with `scripts/resolve_id.py` and update the index before/after tasks.

## Graceful Degradation
- If recoverable: skip, open a `FIX-` task, continue.
- If terminal: stop and say **"come help me please user"**.
- Keep runs idempotent; always update the index and append to the execution log.

## North Star
- Decisions prioritize Atlas mission/vision and reduce time to a durable, low-ops product.