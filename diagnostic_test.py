#!/usr/bin/env python3

import datetime
import json
import os
import pathlib
import sys


def test_basic_python():
    """Test basic Python functionality"""
    try:
        result = 2 + 2
        return result == 4, "Basic arithmetic works"
    except Exception as e:
        return False, f"Basic arithmetic failed: {e}"


def test_imports():
    """Test importing standard library modules"""
    modules_to_test = ["os", "pathlib", "json", "datetime", "sys"]
    results = {}

    for module in modules_to_test:
        try:
            __import__(module)
            results[module] = True
        except Exception as e:
            results[module] = f"Failed: {e}"

    return results


def test_file_operations():
    """Test file read/write operations"""
    test_file = "/tmp/diagnostic_test.txt"
    test_content = "Hello, World!"

    try:
        # Write test
        with open(test_file, "w") as f:
            f.write(test_content)

        # Read test
        with open(test_file, "r") as f:
            content = f.read()

        # Cleanup
        os.remove(test_file)

        return content == test_content, "File operations work"
    except Exception as e:
        return False, f"File operations failed: {e}"


def test_pathlib():
    """Test pathlib functionality"""
    try:
        p = pathlib.Path("/tmp")
        exists = p.exists()
        return exists, "Pathlib works"
    except Exception as e:
        return False, f"Pathlib failed: {e}"


def main():
    results = {
        "timestamp": datetime.datetime.now().isoformat(),
        "python_version": sys.version,
        "tests": {},
    }

    # Run tests
    results["tests"]["basic_python"] = test_basic_python()
    results["tests"]["imports"] = test_imports()
    results["tests"]["file_operations"] = test_file_operations()
    results["tests"]["pathlib"] = test_pathlib()

    # Save results
    output_file = "/tmp/diagnostic_results.json"
    try:
        with open(output_file, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Diagnostic results saved to {output_file}")
    except Exception as e:
        print(f"Failed to save results: {e}")

    # Also print to stdout
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
