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

## Database Schema Optimization Patterns (Aug 27, 2025)
- **Cross-database queries**: Use `ATTACH DATABASE` for joining search indexes with main content
- **JSON field parsing**: Safe handling with `json.loads()` + `isinstance()` checks for list/dict structures
- **Graceful fallback**: Design search APIs to work with/without enhanced insights data
- **Batch processing**: Use `executemany()` for bulk operations, commit in batches of 100
- **Schema validation**: Always check table existence before complex joins

## LLM Integration Patterns (Aug 27, 2025)
- **Router-based selection**: Economy → Balanced → Premium model progression for cost optimization
- **JSON truncation issues**: Common LLM output problem - implement retry logic with shorter context
- **Pydantic validation**: Strong typing prevents malformed LLM responses from breaking system
- **Error handling**: Distinguish between extraction failures vs validation failures for better debugging
- **Processing time tracking**: Log extraction duration for performance monitoring

## Search Integration Architecture (Aug 27, 2025)
- **Enhanced SearchResult models**: Include AI-generated fields (summary, topics, entities, sentiment)
- **Database attachment strategy**: Use `ATTACH DATABASE` for cross-database joins in single queries
- **Graceful enhancement**: Design APIs to work with basic data + optional AI insights
- **JSON parsing safety**: Handle string/object conversion with proper error handling
- **Performance optimization**: Batch index population for 100k+ items without memory issues

## Virtual Environment Management (CRITICAL - Aug 27, 2025)
**STOP THE MADNESS**: Venv paths keep breaking background processes!

### **Definitive Solution Pattern:**
```python
# NEVER use sys.executable or hardcoded venv paths
class BackgroundService:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent
        # ALWAYS use this pattern for subprocess calls
        self.python_executable = str(self.project_root / "atlas_venv" / "bin" / "python3")
        
    def run_subprocess(self, script_name):
        subprocess.run([self.python_executable, script_name], cwd=self.project_root)
```

### **Common Failure Patterns to AVOID:**
- ❌ `sys.executable` - Points to system Python, not venv
- ❌ `/venv/bin/python3` - Wrong venv name  
- ❌ Hardcoded absolute paths - Break on deployment
- ❌ Assuming `python3` command uses venv - Uses system Python

### **Mandatory Checks in All Background Services:**
1. **Verify venv exists**: Check `atlas_venv/bin/python3` before subprocess calls
2. **Use project-relative paths**: Calculate from `Path(__file__).parent`
3. **Log the actual executable**: Log which Python is being used for debugging
4. **Test subprocess calls**: Ensure they load correct dependencies

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

## Qwen Autonomous Execution Rules (Aug 2025)

### **Task Structure Requirements for Autonomous Models**
All tasks in `TASKS.md` must follow these rules for successful Qwen execution:

#### **1. Concrete Deliverables Only**
```yaml
# ❌ BAD (vague, untestable)
- "Create user-friendly documentation with screenshots"
- "Test on real devices and gather feedback"

# ✅ GOOD (concrete, verifiable)
- "Create docs/user-guides/SETUP.md with sections: Installation (min 200 words), Configuration (min 150 words)"
- "Generate browser bookmarklet JavaScript code and save to web/static/bookmarklets.js"
```

#### **2. Mandatory Verification Commands**
Every task MUST include `verification_command` with bash tests:
```yaml
verification_command: |
  test -f docs/user-guides/SETUP.md && 
  wc -w docs/user-guides/SETUP.md | awk '{if($1<350) exit 1}' &&
  grep -q "Installation" docs/user-guides/SETUP.md
```

#### **3. No Manual Testing or Device Access**
Qwen cannot:
- Test on iOS/macOS devices
- Take screenshots or record videos  
- Interact with browser extensions
- Perform user experience testing
- Access external APIs without credentials

Replace with:
- Code generation with examples
- Documentation with code snippets
- Automated file structure validation
- Content verification via text analysis

#### **4. Specific File Path Requirements**
Always specify exact paths and directory structures:
```yaml
# ❌ BAD
- "Create documentation files"

# ✅ GOOD  
- "Create docs/user-guides/MAC_GUIDE.md"
- "Generate apple_shortcuts/shortcuts/save-to-atlas.shortcut"
- "Update web/templates/dashboard.html with new sections"
```

#### **5. Content Specifications**
Include minimum requirements for generated content:
```yaml
# Content requirements
min_word_count: 500
required_sections: ["Installation", "Configuration", "Troubleshooting"]
required_code_blocks: ["JavaScript bookmarklet", "Python API example"]
required_keywords: ["Atlas", "setup", "configuration"]
```

#### **6. Self-Validating Steps**
Each step should be verifiable by the model itself:
```bash
# Good verification steps
ls -la docs/user-guides/ | grep -c "\.md$" | awk '{if($1<5) exit 1}'  # At least 5 guides
python3 -c "import json; json.load(open('config/settings.json'))"      # Valid JSON
curl -s http://localhost:8000/health | grep -q "healthy"               # API responsive
```

#### **7. AgentOS Lifecycle Compliance**
Follow the agents.md execution pattern:
```yaml
preflight_checks:
  - "test -f .env || cp .env.template .env"
  - "python3 -c 'import requests' || pip install requests"
  
git_workflow:
  branch_name: "task/ATLAS-COMPLETE-XXX-description"
  commit_prefix: "task(ATLAS-COMPLETE-XXX):"
  
post_completion:
  - "git add . && git commit -m 'task(ATLAS-COMPLETE-XXX): completed task'"
  - "python3 scripts/update_index.sh"
```

### **Task Quality Checklist**
Before adding any task to `TASKS.md`, verify:

- [ ] All steps are concrete file/code operations
- [ ] Verification command tests actual deliverables  
- [ ] No manual testing or device access required
- [ ] File paths and structures explicitly specified
- [ ] Content requirements quantified (word counts, sections)
- [ ] Success criteria measurable via bash commands
- [ ] Dependencies clearly listed in `depends_on`
- [ ] AgentOS lifecycle steps included

### **Common Anti-Patterns to Avoid**
```yaml
# ❌ These will fail in autonomous mode:
- "Create engaging user experience"
- "Test thoroughly on multiple devices"  
- "Gather user feedback and iterate"
- "Make it look professional"
- "Optimize for best practices"
- "Create compelling screenshots"
- "Record demonstration videos"

# ✅ Replace with concrete alternatives:
- "Create docs/UX_GUIDE.md with 5 workflow examples (min 100 words each)"
- "Generate test data in tests/fixtures/ and validate with pytest"
- "Create docs/FAQ.md addressing 10 common user questions"
- "Apply consistent CSS styling to web/static/css/main.css"
- "Implement PEP 8 formatting and validate with ruff check"
- "Generate ASCII diagrams in docs/ARCHITECTURE.md using text"
- "Create step-by-step text tutorials with code examples"
```

## North Star
- Decisions prioritize Atlas mission/vision and reduce time to a durable, low-ops product.