#!/usr/bin/env python3

# Simple test to verify Python functionality
print("Python is working!")
print("Basic math: 2 + 2 =", 2 + 2)

# Test importing a built-in module
try:
    import os

    print("Importing os module: SUCCESS")
except Exception as e:
    print("Importing os module: FAILED -", e)

# Test file operations
try:
    with open("/tmp/test.txt", "w") as f:
        f.write("File operation test")
    print("File write: SUCCESS")

    with open("/tmp/test.txt", "r") as f:
        content = f.read()
    print("File read: SUCCESS - Content:", content)

    os.remove("/tmp/test.txt")
    print("File cleanup: SUCCESS")
except Exception as e:
    print("File operations: FAILED -", e)

print("Test completed.")
