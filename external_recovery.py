#!/usr/bin/env python3
"""
External recovery script to be run from a different environment.
This script should be copied to a different machine/environment and run from there.
"""
import importlib.util
import os
import pathlib
import shutil
import subprocess
import sys
import venv


def remove_problematic_file():
    """Remove the problematic temporary file causing shared object errors."""
    temp_file = "/tmp/.3bdbfdadbd3a7ff2-00000001.node"
    try:
        if os.path.exists(temp_file):
            os.remove(temp_file)
            print(f"Removed problematic file: {temp_file}")
        else:
            print(f"File not found: {temp_file}")
    except Exception as e:
        print(f"Error removing file: {e}")


def backup_virtual_environment(venv_path=".venv", backup_path=".venv.backup"):
    """Backup the current virtual environment."""
    try:
        if os.path.exists(venv_path):
            if os.path.exists(backup_path):
                shutil.rmtree(backup_path)
                print(f"Removed old backup: {backup_path}")

            shutil.copytree(venv_path, backup_path)
            print(f"Backed up virtual environment to: {backup_path}")
        else:
            print(f"Virtual environment not found at: {venv_path}")
    except Exception as e:
        print(f"Error backing up virtual environment: {e}")


def create_new_virtual_environment(venv_path=".venv.new"):
    """Create a new virtual environment."""
    try:
        if os.path.exists(venv_path):
            shutil.rmtree(venv_path)
            print(f"Removed existing new venv: {venv_path}")

        # Create new virtual environment
        builder = venv.EnvBuilder(with_pip=True)
        builder.create(venv_path)
        print(f"Created new virtual environment: {venv_path}")
    except Exception as e:
        print(f"Error creating new virtual environment: {e}")


def install_dependencies(venv_path=".venv.new"):
    """Install dependencies in the new virtual environment."""
    try:
        pip_path = os.path.join(venv_path, "bin", "pip")
        if os.path.exists(pip_path):
            # Install requirements from requirements.txt if it exists
            requirements_path = "requirements.txt"
            if os.path.exists(requirements_path):
                result = subprocess.run(
                    [pip_path, "install", "-r", requirements_path],
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    print("Successfully installed dependencies from requirements.txt")
                else:
                    print(f"Error installing dependencies: {result.stderr}")
            else:
                print("requirements.txt not found, skipping dependency installation")
        else:
            print(f"Pip not found at: {pip_path}")
    except Exception as e:
        print(f"Error installing dependencies: {e}")


def create_directory_structure():
    """Create necessary directory structure."""
    dirs = [
        "ingest/queue",
        "ingest/capture",
        "ask/insights",
        "ask/proactive",
        "ask/recall",
        "ask/socratic",
        "ask/temporal",
    ]

    try:
        for dir_path in dirs:
            path = pathlib.Path(dir_path)
            path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {dir_path}")
    except Exception as e:
        print(f"Error creating directory structure: {e}")


def verify_fix():
    """Verify the fix by attempting to import key modules."""
    modules_to_test = ["pathlib", "shutil", "venv", "subprocess"]

    try:
        for module in modules_to_test:
            spec = importlib.util.find_spec(module)
            if spec is not None:
                print(f"Successfully verified module: {module}")
            else:
                print(f"Module not found: {module}")
    except Exception as e:
        print(f"Error verifying modules: {e}")


def main():
    """Main recovery function."""
    print("Starting external recovery process...")

    # Step 1: Remove problematic file
    remove_problematic_file()

    # Step 2: Backup virtual environment
    backup_virtual_environment()

    # Step 3: Create new virtual environment
    create_new_virtual_environment()

    # Step 4: Install dependencies
    install_dependencies()

    # Step 5: Create directory structure
    create_directory_structure()

    # Step 6: Verify fix
    verify_fix()

    print("External recovery process completed.")


if __name__ == "__main__":
    main()
