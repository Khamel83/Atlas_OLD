#!/usr/bin/env python3
import os, sys, json, hashlib, subprocess, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IGNORE_DIRS = {'.git', '.venv', 'node_modules', '__pycache__', '.cache', '.idea', '.vscode'}
INDEX_JSON = ROOT / 'AGENT_INDEX.json'
INDEX_MD   = ROOT / 'AGENT_INDEX.md'

EXT_TAGS = {
    '.py': ['code','python'], '.md': ['doc','markdown'], '.json': ['data','json'],
    '.yaml': ['config','yaml'], '.yml': ['config','yaml'], '.sh': ['script','bash'],
    '.ipynb': ['notebook'], '.txt': ['text'], '.csv': ['data','csv']
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def last_commit_for(path: Path) -> str:
    try:
        out = subprocess.check_output(['git','log','-1','--format=%H','--','{0}'.format(str(path))], cwd=ROOT, stderr=subprocess.DEVNULL)
        return out.decode().strip()
    except subprocess.CalledProcessError:
        return ''

def guess_module(path: Path) -> str:
    p = str(path)
    if p.startswith('scripts/'): return 'scripts'
    if p.startswith('docs/'): return 'docs'
    if p.startswith('tests/'): return 'tests'
    return 'core'

def tags_for(path: Path) -> list:
    return EXT_TAGS.get(path.suffix.lower(), ['other'])

def build():
    entries = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # prune ignored dirs
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith('.git')]
        rel_dir = Path(dirpath).relative_to(ROOT)
        for name in filenames:
            p = (Path(dirpath)/name).relative_to(ROOT)
            if p.parts and (p.parts[0] in IGNORE_DIRS): continue
            if p.name in {INDEX_JSON.name, INDEX_MD.name}: continue
            abspath = ROOT / p
            try:
                stat = abspath.stat()
            except FileNotFoundError:
                continue
            entry = {
                "path": str(p).replace('','/'),
                "type": "file",
                "size": stat.st_size,
                "mtime": int(stat.st_mtime),
                "sha256": sha256(abspath),
                "module": guess_module(p),
                "tags": tags_for(p),
                "last_commit": last_commit_for(p),
                "last_task_id": os.environ.get("CURRENT_TASK_ID", ""),
            }
            entries.append(entry)
    entries.sort(key=lambda e: e["path"])
    return {"generated_at": int(time.time()), "count": len(entries), "entries": entries}

def write_md(index):
    lines = []
    lines.append("# Agentic File Index")
    lines.append("")
    lines.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(index['generated_at']))} UTC")
    lines.append(f"Count: {index['count']}")
    lines.append("")
    lines.append("| path | size | module | tags | last_commit |")
    lines.append("|---|---:|---|---|---|")
    for e in index['entries']:
        tags = ",".join(e['tags'])
        lines.append(f"| `{e['path']}` | {e['size']} | {e['module']} | {tags} | `{e['last_commit'][:8]}` |")
    INDEX_MD.write_text("\n".join(lines), encoding='utf-8')

def main():
    idx = build()
    INDEX_JSON.write_text(json.dumps(idx, indent=2), encoding='utf-8')
    write_md(idx)
    print(f"Wrote {INDEX_JSON} and {INDEX_MD}")

if __name__ == "__main__":
    main()
