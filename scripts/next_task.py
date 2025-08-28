#!/usr/bin/env python3
import re, sys, json, pathlib
from collections import defaultdict, deque

ROOT = pathlib.Path(__file__).resolve().parent.parent
TASKS_MD = ROOT / "tasks.md"

HDR = re.compile(r"^### \[(?P<id>[^\]]+)\]\s*(?P<title>.+)$")
FIELD = re.compile(r"^\\*\\*(?P<key>[^:]+):\\*\\*\\s*(?P<val>.+)$")

PRIO_ORDER = {"P0":0,"P1":1,"P2":2,"P3":3}
STATUS_DONE = {"done"}
STATUS_READY = {"todo","in_progress"}
def slug(s):
    import re
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+","-",s).strip("-")
    return s[:60] or "task"

def parse_tasks(text):
    lines = text.splitlines()
    tasks, curr, buf = [], None, []
    def flush():
        nonlocal curr, buf
        if curr:
            block = "\n".join(buf)
            curr["block"] = block
            # parse common fields
            fields = {}
            for ln in block.splitlines():
                m = FIELD.match(ln.strip())
                if m:
                    k = m.group("key").strip().lower()
                    v = m.group("val").strip()
                    fields[k] = v
            # normalize
            curr["phase"] = int(re.findall(r"\d+", fields.get("phase","0"))[0]) if re.findall(r"\d+", fields.get("phase","0")) else 0
            curr["status"] = fields.get("status","todo").strip().lower()
            deps = fields.get("depends on"," ").strip()
            dep_ids = []
            if deps:
                dep_ids = [d.strip().strip("[],") for d in re.split(r"[,\\s]+", deps) if d.strip() and d.strip() not in {"[]"}]
            curr["deps"] = dep_ids
            pr = fields.get("priority","P2").upper().strip()
            curr["priority"] = pr if pr in PRIO_ORDER else "P2"
            tasks.append(curr)
        curr, buf = None, []
    for ln in lines:
        m = HDR.match(ln.strip())
        if m:
            flush()
            curr = {"id": m.group("id").strip(), "title": m.group("title").strip(), "slug": slug(m.group("title"))}
        elif curr:
            buf.append(ln)
    flush()
    return tasks

def topo_ready(tasks):
    by_id = {t["id"]: t for t in tasks}
    done = {t["id"] for t in tasks if t["status"] in STATUS_DONE}
    # treat unknown deps as not done -> blocks
    indeg = {t["id"]: 0 for t in tasks}
    graph = defaultdict(list)
    for t in tasks:
        for d in t["deps"]:
            if d in by_id:
                graph[d].append(t["id"])
                indeg[t["id"]] += 1
            else:
                # unknown dep -> consider permanently blocked
                indeg[t["id"]] += 1
    # a task is runnable if ALL deps are in done
    runnable = []
    for t in tasks:
        if t["status"] in STATUS_READY and all((d in done) for d in t["deps"]):
            runnable.append(t)
    # sort by (priority, phase, FIX boost, id)
    def score(t):
        prio = PRIO_ORDER.get(t["priority"], 2)
        fix_boost = 0 if t["id"].upper().startswith("FIX-") else 1
        return (prio, t["phase"], fix_boost, t["id"])
    runnable.sort(key=score)
    return runnable

def pick(tasks, n=1):
    r = topo_ready(tasks)
    return r[:n]

def main():
    if not TASKS_MD.exists():
        print("tasks.md not found", file=sys.stderr); sys.exit(2)
    tasks = parse_tasks(TASKS_MD.read_text(encoding="utf-8"))
    if len(sys.argv) == 1 or sys.argv[1] in {"pick","next"}:
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        sel = pick(tasks, n=n)
        if not sel:
            print("NO-READY-TASK", file=sys.stderr); sys.exit(3)
        # print machine-friendly JSON for agents
        out = [{"id": t["id"], "slug": t["slug"], "title": t["title"], "phase": t["phase"], "priority": t["priority"]} for t in sel]
        print(json.dumps(out))
    elif sys.argv[1] == "list":
        out = [{"id": t["id"], "title": t["title"], "status": t["status"], "deps": t["deps"], "priority": t["priority"], "phase": t["phase"]} for t in tasks]
        print(json.dumps(out, indent=2))
    else:
        print("Usage: next_task.py [pick [N]|list]", file=sys.stderr); sys.exit(2)

if __name__ == "__main__":
    main()
