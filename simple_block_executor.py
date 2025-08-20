#!/usr/bin/env python3
"""
Simplified Atlas Block Executor - No Git Branch Switching
Executes Blocks 8-16 automatically with strategic commits
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime


def load_progress():
    """Load execution progress from file"""
    progress_file = Path("simple_block_progress.json")
    if progress_file.exists():
        with open(progress_file, "r") as f:
            progress = json.load(f)
            if "blocks_completed" not in progress:
                progress["blocks_completed"] = []
            return progress
    return {
        "current_block": 8,
        "blocks_completed": [],
        "started_at": None,
        "last_updated": None,
    }


def save_progress(progress):
    """Save execution progress to file"""
    progress["last_updated"] = datetime.now().isoformat()
    with open("simple_block_progress.json", "w") as f:
        json.dump(progress, f, indent=2)


def strategic_commit(message):
    """Make strategic commit without complex git operations"""
    print(f"📝 Strategic commit: {message}")

    try:
        # Simple commit
        subprocess.run(
            "git add -A", shell=True, check=True, cwd="/home/ubuntu/dev/atlas"
        )
        commit_cmd = f'git commit -m "feat: {message}"'
        subprocess.run(commit_cmd, shell=True, check=True, cwd="/home/ubuntu/dev/atlas")
        print("✅ Commit successful")
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Commit failed (may be nothing to commit): {e}")
        return True  # Continue anyway


def implement_block(block_num, spec_file):
    """Implement a specific block using AI assistance"""
    print(f"🚀 Starting Block {block_num} implementation...")

    cmd = f"python3 helpers/ai_block_implementer.py {block_num} {spec_file}"
    try:
        result = subprocess.run(
            cmd, shell=True, cwd="/home/ubuntu/dev/atlas", timeout=300
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"❌ Block {block_num} implementation timed out")
        return False
    except Exception as e:
        print(f"❌ Block implementation failed: {e}")
        return False


def execute_blocks():
    """Execute all blocks in sequence"""
    progress = load_progress()

    if not progress.get("started_at"):
        progress["started_at"] = datetime.now().isoformat()

    print("📋 Starting block execution on current branch...")

    # Block specifications mapping
    block_specs = {
        8: "docs/specs/BLOCK_8_IMPLEMENTATION.md",
        9: "docs/specs/BLOCK_9_IMPLEMENTATION.md",
        10: "docs/specs/BLOCK_10_IMPLEMENTATION.md",
        11: "docs/specs/BLOCK_11_IMPLEMENTATION.md",
        12: "docs/specs/BLOCK_12_IMPLEMENTATION.md",
        13: "docs/specs/BLOCK_13_IMPLEMENTATION.md",
        15: "docs/specs/BLOCK_15_IMPLEMENTATION.md",
        16: "docs/specs/BLOCK_16_IMPLEMENTATION.md",
    }

    # Execute blocks starting from current
    for block_num in range(progress["current_block"], 17):
        if block_num == 14:  # Skip Block 14 (already complete)
            continue

        if block_num in progress["blocks_completed"]:
            print(f"✅ Block {block_num} already completed, skipping...")
            continue

        print(f"\n{'='*60}")
        print(f"🎯 EXECUTING BLOCK {block_num}")
        print(f"{'='*60}")

        # Strategic commit at block start
        strategic_commit(f"Block {block_num} - Starting implementation")

        # Get spec file (create basic one if missing)
        spec_file = block_specs.get(
            block_num, f"docs/specs/BLOCK_{block_num}_IMPLEMENTATION.md"
        )
        spec_path = Path(spec_file)

        if not spec_path.exists():
            print(f"📝 Creating basic spec for Block {block_num}...")
            spec_path.parent.mkdir(parents=True, exist_ok=True)
            spec_path.write_text(
                f"""# Block {block_num} Implementation

## Overview
Block {block_num} implementation for Atlas.

# Block {block_num}: Implementation Tasks
- [ ] Implement core functionality
- [ ] Add comprehensive testing
- [ ] Update documentation
- [ ] Integration with existing systems

This is a placeholder specification that will be enhanced during implementation.
"""
            )

        # Execute block implementation
        success = implement_block(block_num, str(spec_path))

        if success:
            # Mark as completed
            progress["blocks_completed"].append(block_num)
            progress["current_block"] = block_num + 1
            save_progress(progress)

            # Strategic commit at block completion
            strategic_commit(f"Block {block_num} implementation complete")

            print(f"✅ Block {block_num} completed successfully")
        else:
            print(f"❌ Block {block_num} implementation failed")
            save_progress(progress)
            return False

    print("\n🎉 ALL BLOCKS COMPLETED SUCCESSFULLY!")
    print("🎯 AUTOMATED EXECUTION COMPLETE!")
    print("Ready for comprehensive review.")

    return True


def main():
    """Main execution function"""
    print("🚀 Simple Automated Block Execution")
    print("=" * 60)

    os.chdir("/home/ubuntu/dev/atlas")

    success = execute_blocks()

    if success:
        print("🎉 Execution completed successfully!")
        sys.exit(0)
    else:
        print("❌ Execution failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
