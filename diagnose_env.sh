#!/bin/bash

echo "=== Atlas Environment Diagnostic Script ==="
echo "Date: $(date)"
echo "User: $(whoami)"
echo "Working Directory: $(pwd)"
echo

echo "=== Container Detection ==="
if [ -f /.dockerenv ]; then
    echo "✓ Running in Docker container"
else
    echo "○ Not in Docker container"
fi

if grep -q container /proc/1/cgroup 2>/dev/null; then
    echo "✓ Container environment detected in cgroup"
else
    echo "○ No container detected in cgroup"
fi

echo

echo "=== System Tools Check ==="
tools=("ls" "cat" "ps" "grep" "find" "which" "python" "python3" "pip" "pip3" "git" "curl" "wget")
for tool in "${tools[@]}"; do
    if command -v "$tool" >/dev/null 2>&1; then
        echo "✓ $tool: $(command -v "$tool")"
    else
        echo "✗ $tool: Not found"
    fi
done
echo

echo "=== Filesystem Structure ==="
echo "Root directory:"
ls -la / | head -20
echo
echo "Home directory:"
ls -la ~ | head -20
echo
echo "Project directory:"
ls -la . | head -20
echo

echo "=== Environment Variables ==="
echo "PATH: $PATH"
echo "PYTHONPATH: $PYTHONPATH"
echo "VIRTUAL_ENV: $VIRTUAL_ENV"
echo "HOME: $HOME"
echo "USER: $USER"
echo "SHELL: $SHELL"
echo

echo "=== Python Environment ==="
if command -v python3 >/dev/null 2>&1; then
    echo "Python3 version: $(python3 --version 2>/dev/null || echo 'Failed to get version')"
    echo "Python3 location: $(command -v python3)"
fi

if command -v python >/dev/null 2>&1; then
    echo "Python version: $(python --version 2>/dev/null || echo 'Failed to get version')"
    echo "Python location: $(command -v python)"
fi

if [ -d ".venv" ]; then
    echo "✓ Virtual environment directory exists"
    ls -la .venv/bin/ | head -10
else
    echo "○ No virtual environment directory found"
fi
echo

echo "=== Shared Object Issues ==="
echo "Checking for missing shared libraries..."
ldd --version 2>/dev/null || echo "ldd not available"
echo

echo "Checking for common library paths:"
for path in "/lib" "/lib64" "/usr/lib" "/usr/lib64" "/usr/local/lib"; do
    if [ -d "$path" ]; then
        echo "✓ $path exists ($(ls $path | wc -l) files)"
    else
        echo "✗ $path does not exist"
    fi
done
echo

echo "=== Process Information ==="
echo "Current processes:"
ps aux | head -10
echo

echo "=== Memory Information ==="
free -h 2>/dev/null || echo "Memory info not available"
echo

echo "=== Disk Space ==="
df -h 2>/dev/null || echo "Disk info not available"
echo

echo "=== Diagnostic Complete ==="