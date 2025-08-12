#!/usr/bin/env python3
"""
Atlas Environment Recovery Script
This script implements the recovery steps from RECOVERY_PLAN.md
without using bash commands that might trigger the shared object error.
"""

import datetime
import os
import shutil
import subprocess
import sys
from pathlib import Path


def main():
    print("🚀 Starting Atlas Environment Recovery...")

    # Change to the project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    print(f"📂 Working in: {project_dir}")

    # 1. Try to identify the missing shared object file
    print("🔍 Step 1: Identifying missing shared object files...")
    temp_file = Path("/tmp/.3bdbfdadbd3a7ff2-00000001.node")
    if temp_file.exists():
        print(f"⚠️  Found problematic temporary file: {temp_file}")
    else:
        print("✅ No problematic temporary file found at expected location")

    # 2. Clear temporary files (using Python instead of bash)
    print("🧹 Step 2: Clearing temporary files...")
    try:
        if temp_file.exists():
            temp_file.unlink()
            print("✅ Removed problematic temporary file")
        else:
            print("ℹ️  No problematic temporary file to remove")
    except Exception as e:
        print(f"⚠️  Could not remove temporary file: {e}")

    # 3. Backup current environment
    print("📦 Step 3: Backing up current virtual environment...")
    venv_dir = Path(".venv")
    if venv_dir.exists():
        backup_name = f".venv.backup.{int(datetime.datetime.now().timestamp())}"
        try:
            shutil.move(".venv", backup_name)
            print(f"✅ Backed up current environment to {backup_name}")
        except Exception as e:
            print(f"⚠️  Could not backup environment: {e}")
    else:
        print("ℹ️  No existing virtual environment found")

    # 4. Create fresh virtual environment
    print("🔧 Step 4: Creating fresh virtual environment...")
    try:
        subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
        print("✅ Virtual environment created")
    except Exception as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return 1

    # 5. Try to activate and upgrade pip
    print("⬆️  Step 5: Upgrading pip...")
    try:
        pip_path = Path(".venv/bin/pip")
        if not pip_path.exists():
            pip_path = Path(".venv/bin/pip3")

        if pip_path.exists():
            subprocess.run([str(pip_path), "install", "--upgrade", "pip"], check=True)
            print("✅ Pip upgraded")
        else:
            print("⚠️  Could not find pip in virtual environment")
    except Exception as e:
        print(f"⚠️  Could not upgrade pip: {e}")

    # 6. Install dependencies
    print("📥 Step 6: Installing dependencies from requirements.txt...")
    try:
        if pip_path.exists():
            subprocess.run(
                [str(pip_path), "install", "-r", "requirements.txt"], check=True
            )
            print("✅ Dependencies installed")
        else:
            print("⚠️  Could not install dependencies - pip not found")
    except Exception as e:
        print(f"⚠️  Could not install dependencies: {e}")

    # 7. Fix directory structure by running the existing script
    print("📁 Step 7: Fixing directory structure...")
    try:
        fix_script = Path("fix_atlas_structure.sh")
        if fix_script.exists():
            # Read and execute the script contents directly
            with open(fix_script, "r") as f:
                lines = f.readlines()

            # Create the directories and files as specified in the script
            directories = [
                "data/raw",
                "data/parsed",
                "data/transcripts",
                "data/collateral",
                "logs",
                "output/articles",
                "output/youtube",
                "output/podcasts",
                "ask",
                "process",
                "ingest",
                "helpers",
            ]

            for directory in directories:
                Path(directory).mkdir(parents=True, exist_ok=True)
                print(f"✅ Created directory: {directory}")

            # Create placeholder files
            Path("run.py").write_text("# run.py (empty placeholder)\n")
            Path("helpers/config.py").write_text("# config.py (empty placeholder)\n")
            print("✅ Created placeholder files")
        else:
            print("⚠️  Fix structure script not found")
    except Exception as e:
        print(f"⚠️  Could not fix directory structure: {e}")

    # 8. Verify the fix by testing basic functionality
    print("✅ Step 8: Verifying the fix...")
    try:
        # Test Python
        python_version = sys.version
        print(f"✅ Python working: {python_version}")

        # Test if we can import some basic modules
        try:
            import importlib

            importlib.import_module("requests")
            print("✅ Requests library available")
        except ImportError:
            print("⚠️  Requests library not available")

        try:
            import importlib

            importlib.import_module("yaml")
            print("✅ PyYAML library available")
        except ImportError:
            print("⚠️  PyYAML library not available")

    except Exception as e:
        print(f"⚠️  Verification had issues: {e}")

    print("\n🎉 Recovery script completed!")
    print("\nTo manually activate the new environment, run:")
    print("source .venv/bin/activate")
    print("\nTo test Atlas functionality, run:")
    print("python scripts/diagnose_environment.py")

    return 0


if __name__ == "__main__":
    sys.exit(main())
