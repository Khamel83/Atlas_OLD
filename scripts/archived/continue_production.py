#!/usr/bin/env python3
"""
Continue Atlas Production - Next phase after initial startup
"""

import os
import sys
import time
import subprocess
from datetime import datetime

sys.path.append("/home/ubuntu/dev/atlas")

from cognitive_engine import CognitiveEngine
import glob
import json


def check_current_status():
    """Check what we have so far"""
    print("📊 Atlas Production Status Check")
    print("=" * 40)

    # Count articles
    articles = glob.glob("output/articles/markdown/*.md")
    metadata_files = glob.glob("output/articles/metadata/*.json")

    print(f"📄 Articles processed: {len(articles)}")
    print(f"📊 Metadata files: {len(metadata_files)}")

    # Check failed articles status
    try:
        with open("retries/queue.jsonl", "r") as f:
            failed_lines = f.readlines()
        print(f"❌ Failed articles remaining: {len(failed_lines)}")
    except Exception:
        print("❌ Failed articles: Could not read retry queue")

    # Check AI recovery progress
    try:
        with open("retry_log", "r") as f:
            log_lines = f.readlines()
        success_lines = [line for line in log_lines if "Successfully fetched" in line]
        print(f"🤖 AI Recovery successes: {len(success_lines)}")

        # Show recent progress
        if log_lines:
            print(f"📋 Last activity: {log_lines[-1].strip()[:100]}...")
    except Exception:
        print("🤖 AI Recovery: No log found")

    return len(articles), len(metadata_files)


def run_cognitive_processing_batch(article_count=100):
    """Run cognitive analysis on a batch of articles"""
    print(f"\n🧠 Running Cognitive Processing on {article_count} articles...")

    engine = CognitiveEngine()
    articles = glob.glob("output/articles/markdown/*.md")[:article_count]

    results = []
    insights_collected = []

    for i, article_path in enumerate(articles, 1):
        if i % 10 == 0:
            print(f"  [{i}/{len(articles)}] Processing...")

        try:
            analysis = engine.analyze_article(article_path)
            if analysis and "insights" in analysis:
                insights = analysis["insights"].get("insights", [])
                insights_collected.extend(insights)
                results.append(
                    {
                        "file": os.path.basename(article_path),
                        "word_count": analysis.get("word_count", 0),
                        "insights_count": len(insights),
                        "connections_count": len(analysis.get("connections", [])),
                    }
                )
        except Exception as e:
            print(f"  Error processing {article_path}: {e}")

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f"cognitive_batch_results_{timestamp}.json"

    with open(results_file, "w") as f:
        json.dump(
            {
                "processing_time": timestamp,
                "articles_processed": len(results),
                "total_insights": len(insights_collected),
                "results": results,
                "sample_insights": insights_collected[:20],  # First 20 insights
            },
            f,
            indent=2,
        )

    print("✅ Cognitive processing complete!")
    print(f"📊 Processed: {len(results)} articles")
    print(f"💡 Extracted: {len(insights_collected)} insights")
    print(f"💾 Results saved to: {results_file}")

    return results_file


def continue_ai_recovery():
    """Continue or restart AI recovery process"""
    print("\n🤖 AI Recovery Options:")
    print("1. Continue existing recovery process")
    print("2. Start new recovery batch")
    print("3. Skip recovery for now")

    choice = input("Choose option (1-3): ").strip()

    if choice == "1":
        print("🔄 Checking for existing recovery process...")
        result = subprocess.run(
            ["pgrep", "-f", "retry_failed_articles"], capture_output=True
        )
        if result.returncode == 0:
            print("✅ Recovery process still running")
            print("📋 Monitor with: tail -f retry_log")
        else:
            print("🚀 Starting new recovery process...")
            subprocess.Popen(
                [
                    "bash",
                    "-c",
                    "source atlas_venv/bin/activate && python retry_failed_articles.py --use-skyvern > recovery_output.log 2>&1 &",
                ]
            )
            print("✅ Recovery started in background")
            print("📋 Monitor with: tail -f recovery_output.log")

    elif choice == "2":
        print("🚀 Starting new AI recovery batch...")
        subprocess.Popen(
            [
                "bash",
                "-c",
                "source atlas_venv/bin/activate && python retry_failed_articles.py --use-skyvern > recovery_batch.log 2>&1 &",
            ]
        )
        print("✅ New recovery batch started")
        print("📋 Monitor with: tail -f recovery_batch.log")

    else:
        print("⏭️ Skipping recovery for now")


def start_web_dashboard():
    """Start the web dashboard for monitoring"""
    print("\n🌐 Starting Web Dashboard...")

    # Check if already running
    result = subprocess.run(["pgrep", "-f", "uvicorn"], capture_output=True)
    if result.returncode == 0:
        print("✅ Dashboard already running")
        print("🌐 Access at: http://localhost:8000")
        return

    print("🚀 Starting dashboard...")
    subprocess.Popen(
        [
            "bash",
            "-c",
            "cd web && source ../atlas_venv/bin/activate && uvicorn app:app --host 0.0.0.0 --port 8000 --reload > ../dashboard.log 2>&1 &",
        ]
    )

    time.sleep(3)
    print("✅ Dashboard started!")
    print("🌐 Access at: http://localhost:8000")
    print("📊 Cognitive API: http://localhost:8000/cognitive/status")
    print("📋 Monitor with: tail -f dashboard.log")


def run_comprehensive_ingestion():
    """Run comprehensive ingestion on remaining sources"""
    print("\n📥 Comprehensive Ingestion Options:")
    print("1. Process Instapaper articles")
    print("2. Process YouTube transcripts")
    print("3. Run podcast ingestion")
    print("4. Process all sources")
    print("5. Skip ingestion")

    choice = input("Choose option (1-5): ").strip()

    if choice == "1":
        print("📰 Starting Instapaper ingestion...")
        subprocess.Popen(
            [
                "bash",
                "-c",
                "source atlas_venv/bin/activate && python run_instapaper_simple.py > instapaper_batch.log 2>&1 &",
            ]
        )
        print("✅ Instapaper processing started")
        print("📋 Monitor with: tail -f instapaper_batch.log")

    elif choice == "2":
        print("📺 Starting YouTube processing...")
        subprocess.Popen(
            [
                "bash",
                "-c",
                "source atlas_venv/bin/activate && python helpers/youtube_ingestor.py > youtube_batch.log 2>&1 &",
            ]
        )
        print("✅ YouTube processing started")
        print("📋 Monitor with: tail -f youtube_batch.log")

    elif choice == "3":
        print("🎧 Starting podcast ingestion...")
        print("Note: This will process your 191 podcasts - this may take a while!")
        confirm = input("Continue? (y/n): ").strip().lower()
        if confirm == "y":
            subprocess.Popen(
                [
                    "bash",
                    "-c",
                    "source atlas_venv/bin/activate && python helpers/podcast_ingestor.py > podcast_batch.log 2>&1 &",
                ]
            )
            print("✅ Podcast processing started")
            print("📋 Monitor with: tail -f podcast_batch.log")
        else:
            print("⏭️ Skipping podcast ingestion")

    elif choice == "4":
        print("🚀 Starting comprehensive ingestion...")
        print("This will start all ingestion processes in parallel")
        confirm = input("Continue? (y/n): ").strip().lower()
        if confirm == "y":
            # Start all processes
            for script, log_file in [
                ("run_instapaper_simple.py", "instapaper_comprehensive.log"),
                ("helpers/youtube_ingestor.py", "youtube_comprehensive.log"),
                ("helpers/podcast_ingestor.py", "podcast_comprehensive.log"),
            ]:
                subprocess.Popen(
                    [
                        "bash",
                        "-c",
                        f"source atlas_venv/bin/activate && python {script} > {log_file} 2>&1 &",
                    ]
                )
            print("✅ All ingestion processes started!")
            print("📋 Monitor with: tail -f *_comprehensive.log")
        else:
            print("⏭️ Skipping comprehensive ingestion")

    else:
        print("⏭️ Skipping ingestion")


def main():
    """Main production continuation workflow"""
    print("🚀 Atlas Production Continuation")
    print("=" * 40)

    # Check current status
    article_count, metadata_count = check_current_status()

    print("\n🎯 Production Continuation Options:")


def run_cognitive_processing_batch(article_count=100):
    """Run cognitive analysis on a batch of articles"""
    print(f"\n🧠 Running Cognitive Processing on {article_count} articles...")

    engine = CognitiveEngine()
    articles = glob.glob("output/articles/markdown/*.md")[:article_count]

    results = []
    insights_collected = []

    for i, article_path in enumerate(articles, 1):
        if i % 10 == 0:
            print(f"  [{i}/{len(articles)}] Processing...")

        try:
            analysis = engine.analyze_article(article_path)
            if analysis and "insights" in analysis:
                insights = analysis["insights"].get("insights", [])
                insights_collected.extend(insights)
                results.append(
                    {
                        "file": os.path.basename(article_path),
                        "word_count": analysis.get("word_count", 0),
                        "insights_count": len(insights),
                        "connections_count": len(analysis.get("connections", [])),
                    }
                )
        except Exception as e:
            print(f"  Error processing {article_path}: {e}")

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f"cognitive_batch_results_{timestamp}.json"

    import json

    with open(results_file, "w") as f:
        json.dump(
            {
                "processing_time": timestamp,
                "articles_processed": len(results),
                "total_insights": len(insights_collected),
                "results": results,
                "sample_insights": insights_collected[:20],  # First 20 insights
            },
            f,
            indent=2,
        )

    print("✅ Cognitive processing complete!")
    print(f"📊 Processed: {len(results)} articles")
    print(f"💡 Extracted: {len(insights_collected)} insights")
    print(f"💾 Results saved to: {results_file}")

    return results_file


def continue_ai_recovery():
    """Continue or restart AI recovery process"""
    print("\n🤖 AI Recovery Options:")
    print("1. Continue existing recovery process")
    print("2. Start new recovery batch")
    print("3. Skip recovery for now")

    choice = input("Choose option (1-3): ").strip()

    if choice == "1":
        print("🔄 Checking for existing recovery process...")
        result = subprocess.run(
            ["pgrep", "-f", "retry_failed_articles"], capture_output=True
        )
        if result.returncode == 0:
            print("✅ Recovery process still running")
            print("📋 Monitor with: tail -f retry_log")
        else:
            print("🚀 Starting new recovery process...")
            subprocess.Popen(
                [
                    "bash",
                    "-c",
                    "source atlas_venv/bin/activate && python retry_failed_articles.py --use-skyvern > recovery_output.log 2>&1 &",
                ]
            )
            print("✅ Recovery started in background")
            print("📋 Monitor with: tail -f recovery_output.log")

    elif choice == "2":
        print("🚀 Starting new AI recovery batch...")
        subprocess.Popen(
            [
                "bash",
                "-c",
                "source atlas_venv/bin/activate && python retry_failed_articles.py --use-skyvern > recovery_batch.log 2>&1 &",
            ]
        )
        print("✅ New recovery batch started")
        print("📋 Monitor with: tail -f recovery_batch.log")

    else:
        print("⏭️ Skipping recovery for now")


def start_web_dashboard():
    """Start the web dashboard for monitoring"""
    print("\n🌐 Starting Web Dashboard...")

    # Check if already running
    result = subprocess.run(["pgrep", "-f", "uvicorn"], capture_output=True)
    if result.returncode == 0:
        print("✅ Dashboard already running")
        print("🌐 Access at: http://localhost:8000")
        return

    print("🚀 Starting dashboard...")
    subprocess.Popen(
        [
            "bash",
            "-c",
            "cd web && source ../atlas_venv/bin/activate && uvicorn app:app --host 0.0.0.0 --port 8000 --reload > ../dashboard.log 2>&1 &",
        ]
    )

    time.sleep(3)
    print("✅ Dashboard started!")
    print("🌐 Access at: http://localhost:8000")
    print("📊 Cognitive API: http://localhost:8000/cognitive/status")
    print("📋 Monitor with: tail -f dashboard.log")


def run_comprehensive_ingestion():
    """Run comprehensive ingestion on remaining sources"""
    print("\n📥 Comprehensive Ingestion Options:")
    print("1. Process Instapaper articles")
    print("2. Process YouTube transcripts")
    print("3. Run podcast ingestion")
    print("4. Process all sources")
    print("5. Skip ingestion")

    choice = input("Choose option (1-5): ").strip()

    if choice == "1":
        print("📰 Starting Instapaper ingestion...")
        subprocess.Popen(
            [
                "bash",
                "-c",
                "source atlas_venv/bin/activate && python run_instapaper_simple.py > instapaper_batch.log 2>&1 &",
            ]
        )
        print("✅ Instapaper processing started")
        print("📋 Monitor with: tail -f instapaper_batch.log")

    elif choice == "2":
        print("📺 Starting YouTube processing...")
        subprocess.Popen(
            [
                "bash",
                "-c",
                "source atlas_venv/bin/activate && python helpers/youtube_ingestor.py > youtube_batch.log 2>&1 &",
            ]
        )
        print("✅ YouTube processing started")
        print("📋 Monitor with: tail -f youtube_batch.log")

    elif choice == "3":
        print("🎧 Starting podcast ingestion...")
        print("Note: This will process your 191 podcasts - this may take a while!")
        confirm = input("Continue? (y/n): ").strip().lower()
        if confirm == "y":
            subprocess.Popen(
                [
                    "bash",
                    "-c",
                    "source atlas_venv/bin/activate && python helpers/podcast_ingestor.py > podcast_batch.log 2>&1 &",
                ]
            )
            print("✅ Podcast processing started")
            print("📋 Monitor with: tail -f podcast_batch.log")
        else:
            print("⏭️ Skipping podcast ingestion")

    elif choice == "4":
        print("🚀 Starting comprehensive ingestion...")
        print("This will start all ingestion processes in parallel")
        confirm = input("Continue? (y/n): ").strip().lower()
        if confirm == "y":
            # Start all processes
            for script, log_file in [
                ("run_instapaper_simple.py", "instapaper_comprehensive.log"),
                ("helpers/youtube_ingestor.py", "youtube_comprehensive.log"),
                ("helpers/podcast_ingestor.py", "podcast_comprehensive.log"),
            ]:
                subprocess.Popen(
                    [
                        "bash",
                        "-c",
                        f"source atlas_venv/bin/activate && python {script} > {log_file} 2>&1 &",
                    ]
                )
            print("✅ All ingestion processes started!")
            print("📋 Monitor with: tail -f *_comprehensive.log")
        else:
            print("⏭️ Skipping comprehensive ingestion")

    else:
        print("⏭️ Skipping ingestion")


def main():
    """Main production continuation workflow"""
    print("🚀 Atlas Production Continuation")
    print("=" * 40)

    # Check current status
    article_count, metadata_count = check_current_status()

    print("\n🎯 Production Continuation Options:")
    print("1. Run cognitive processing batch")
    print("2. Continue/start AI recovery")
    print("3. Start web dashboard")
    print("4. Run comprehensive ingestion")
    print("5. Start full production (all processes)")
    print("6. Custom selection")

    choice = input("\nChoose option (1-6): ").strip()

    if choice == "1":
        results_file = run_cognitive_processing_batch()
        print(f"\n✅ Cognitive processing complete! Results in {results_file}")

    elif choice == "2":
        continue_ai_recovery()

    elif choice == "3":
        start_web_dashboard()

    elif choice == "4":
        run_comprehensive_ingestion()

    elif choice == "5":
        print("🚀 Starting full production mode...")
        start_web_dashboard()
        time.sleep(2)
        continue_ai_recovery()
        time.sleep(2)
        run_cognitive_processing_batch(50)  # Smaller batch to start
        time.sleep(2)
        run_comprehensive_ingestion()

        print("\n✅ Full production mode started!")
        print("🌐 Dashboard: http://localhost:8000")
        print("📋 Monitor all processes with log files")

    elif choice == "6":
        print("🎛️ Custom selection mode...")
        print("Run commands individually as needed:")
        print("- Cognitive: python continue_production.py (option 1)")
        print("- Recovery: python continue_production.py (option 2)")
        print("- Dashboard: python continue_production.py (option 3)")
        print("- Ingestion: python continue_production.py (option 4)")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
