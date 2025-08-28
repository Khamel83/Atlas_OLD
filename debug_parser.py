#!/usr/bin/env python3
import re, yaml
from pathlib import Path

HDR = re.compile(r"^### \*\*(?P<id>ATLAS-COMPLETE-\d+):\s*(?P<title>[^*]+)\*\*$")

content = Path("TASKS.md").read_text()
lines = content.splitlines()

print("Looking for task headers...")
for i, line in enumerate(lines):
    if "ATLAS-COMPLETE-001" in line:
        print(f"Line {i+1}: {repr(line)}")
        m = HDR.match(line.strip())
        if m:
            print(f"  ✓ Matched! ID: {m.group('id')}, Title: {m.group('title')}")
        else:
            print(f"  ✗ No match")
            
# Test the exact line
test_line = "### **ATLAS-COMPLETE-001: Replace Dangerous Subprocess Calls**"
print(f"\nTesting: {repr(test_line)}")
m = HDR.match(test_line)
if m:
    print(f"✓ Matched! ID: {m.group('id')}, Title: {m.group('title')}")
else:
    print("✗ No match")