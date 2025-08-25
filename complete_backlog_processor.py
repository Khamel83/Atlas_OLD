#!/usr/bin/env python3
"""
Complete Backlog Processor - Process ALL remaining files in inputs/

Process every single HTML, email, and markdown file in all subdirectories.
"""

import csv
import email
import hashlib
import os
import shutil
from pathlib import Path
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


def clean_filename(text, max_length=100):
    """Convert text to safe filename"""
    cleaned = "".join(c if c.isalnum() or c in ' -_.' else '_' for c in text)
    cleaned = ' '.join(cleaned.split())[:max_length]
    return cleaned.strip() or "untitled"


def html_to_text(html_content):
    """Extract clean text from HTML"""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Remove script, style, nav, footer, etc.
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'advertisement']):
            tag.decompose()
            
        # Get title
        title_tag = soup.find('title')
        title = title_tag.text.strip() if title_tag else "Untitled"
        
        # Get main content
        content = None
        for selector in ['article', '[role="main"]', 'main', '.content', '#content', '.post', '.entry']:
            content = soup.select_one(selector)
            if content:
                break
        
        # Fallback to body
        if not content:
            content = soup.find('body') or soup
            
        # Convert to markdown
        markdown = markdownify(str(content), heading_style="ATX")
        
        return title, markdown
        
    except Exception as e:
        return "Error extracting content", f"Error: {str(e)}"


def process_html_file(html_path, output_dir="processed_backlog"):
    """Process a single HTML file"""
    try:
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
            
        title, text = html_to_text(html_content)
        
        # Create output filename
        safe_title = clean_filename(title)
        output_file = Path(output_dir) / "html" / f"{safe_title}.md"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write markdown
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Source:** {html_path}\n")
            f.write(f"**Processed:** {datetime.now().isoformat()}\n\n")
            f.write(text)
            
        # Move original to processed
        processed_dir = Path("inputs/PROCESSED/html")
        processed_dir.mkdir(parents=True, exist_ok=True)
        
        # Create unique filename if exists
        dest_file = processed_dir / Path(html_path).name
        counter = 1
        while dest_file.exists():
            name_parts = Path(html_path).name.rsplit('.', 1)
            dest_file = processed_dir / f"{name_parts[0]}_{counter}.{name_parts[1]}"
            counter += 1
            
        shutil.move(html_path, dest_file)
        
        return True, str(output_file)
        
    except Exception as e:
        return False, str(e)


def process_email_file(email_path, output_dir="processed_backlog"):
    """Process a single email file"""
    try:
        with open(email_path, 'rb') as f:
            msg = email.message_from_bytes(f.read())
            
        # Extract email content
        subject = msg.get('Subject', 'No Subject')
        sender = msg.get('From', 'Unknown Sender')
        date = msg.get('Date', 'Unknown Date')
        
        # Get body
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    break
                elif part.get_content_type() == "text/html":
                    html_body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    _, body = html_to_text(html_body)
        else:
            if msg.get_content_type() == "text/plain":
                body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
            elif msg.get_content_type() == "text/html":
                html_body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                _, body = html_to_text(html_body)
                
        # Create output filename
        safe_subject = clean_filename(subject)
        output_file = Path(output_dir) / "emails" / f"{safe_subject}.md"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write markdown
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {subject}\n\n")
            f.write(f"**From:** {sender}\n")
            f.write(f"**Date:** {date}\n")
            f.write(f"**Source:** {email_path}\n")
            f.write(f"**Processed:** {datetime.now().isoformat()}\n\n")
            f.write(body)
            
        # Move original to processed
        processed_dir = Path("inputs/PROCESSED/emails")
        processed_dir.mkdir(parents=True, exist_ok=True)
        
        # Create unique filename if exists
        dest_file = processed_dir / Path(email_path).name
        counter = 1
        while dest_file.exists():
            name_parts = Path(email_path).name.rsplit('.', 1)
            dest_file = processed_dir / f"{name_parts[0]}_{counter}.{name_parts[1]}"
            counter += 1
            
        shutil.move(email_path, dest_file)
        
        return True, str(output_file)
        
    except Exception as e:
        return False, str(e)


def process_markdown_file(md_path, output_dir="processed_backlog"):
    """Process a markdown file (copy with metadata)"""
    try:
        with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Extract title from first line or filename
        lines = content.split('\n')
        title = "Untitled"
        for line in lines[:5]:
            if line.startswith('# '):
                title = line[2:].strip()
                break
        if title == "Untitled":
            title = Path(md_path).stem
        
        # Create output filename
        safe_title = clean_filename(title)
        output_file = Path(output_dir) / "markdown" / f"{safe_title}.md"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Write markdown with metadata
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Source:** {md_path}\n")
            f.write(f"**Processed:** {datetime.now().isoformat()}\n\n")
            f.write(content)
            
        # Move original to processed
        processed_dir = Path("inputs/PROCESSED/markdown")
        processed_dir.mkdir(parents=True, exist_ok=True)
        
        # Create unique filename if exists
        dest_file = processed_dir / Path(md_path).name
        counter = 1
        while dest_file.exists():
            name_parts = Path(md_path).name.rsplit('.', 1)
            dest_file = processed_dir / f"{name_parts[0]}_{counter}.{name_parts[1]}"
            counter += 1
            
        shutil.move(md_path, dest_file)
        
        return True, str(output_file)
        
    except Exception as e:
        return False, str(e)


def find_all_files():
    """Find all files to process"""
    files_to_process = {
        'html': [],
        'email': [],
        'markdown': []
    }
    
    # Skip PROCESSED directory
    skip_dirs = {'PROCESSED', 'processed'}
    
    for root, dirs, files in os.walk("inputs"):
        # Skip processed directories
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for file in files:
            file_path = Path(root) / file
            
            if file.endswith('.html'):
                files_to_process['html'].append(file_path)
            elif file.endswith('.eml'):
                files_to_process['email'].append(file_path)
            elif file.endswith('.md'):
                files_to_process['markdown'].append(file_path)
    
    return files_to_process


def process_all_remaining():
    """Process ALL remaining files in inputs/"""
    print("🚀 Starting COMPLETE backlog processing...")
    print("   Finding all files to process...")
    
    files = find_all_files()
    
    print(f"📊 Files found:")
    print(f"   HTML: {len(files['html'])}")
    print(f"   Email: {len(files['email'])}")
    print(f"   Markdown: {len(files['markdown'])}")
    
    total_files = len(files['html']) + len(files['email']) + len(files['markdown'])
    print(f"   TOTAL: {total_files} files to process")
    
    if total_files == 0:
        print("✅ No files to process!")
        return
    
    stats = {
        "html_success": 0, "html_failed": 0,
        "email_success": 0, "email_failed": 0,
        "markdown_success": 0, "markdown_failed": 0
    }
    
    processed_count = 0
    
    # Process HTML files
    if files['html']:
        print(f"\n📄 Processing {len(files['html'])} HTML files...")
        for html_file in files['html']:
            processed_count += 1
            print(f"[{processed_count}/{total_files}] HTML: {html_file.name[:50]}...")
            success, result = process_html_file(html_file)
            if success:
                stats["html_success"] += 1
                print(f"✅")
            else:
                stats["html_failed"] += 1
                print(f"❌ {result}")
    
    # Process email files
    if files['email']:
        print(f"\n📧 Processing {len(files['email'])} email files...")
        for email_file in files['email']:
            processed_count += 1
            print(f"[{processed_count}/{total_files}] Email: {email_file.name[:50]}...")
            success, result = process_email_file(email_file)
            if success:
                stats["email_success"] += 1
                print(f"✅")
            else:
                stats["email_failed"] += 1
                print(f"❌ {result}")
    
    # Process markdown files
    if files['markdown']:
        print(f"\n📝 Processing {len(files['markdown'])} markdown files...")
        for md_file in files['markdown']:
            processed_count += 1
            print(f"[{processed_count}/{total_files}] Markdown: {md_file.name[:50]}...")
            success, result = process_markdown_file(md_file)
            if success:
                stats["markdown_success"] += 1
                print(f"✅")
            else:
                stats["markdown_failed"] += 1
                print(f"❌ {result}")
    
    print(f"\n✅ COMPLETE backlog processing finished!")
    print(f"📊 Final Results:")
    print(f"   HTML: {stats['html_success']} success, {stats['html_failed']} failed")
    print(f"   Email: {stats['email_success']} success, {stats['email_failed']} failed")
    print(f"   Markdown: {stats['markdown_success']} success, {stats['markdown_failed']} failed")
    
    total_success = stats["html_success"] + stats["email_success"] + stats["markdown_success"]
    total_failed = stats["html_failed"] + stats["email_failed"] + stats["markdown_failed"]
    
    print(f"🎯 TOTAL: {total_success} successful, {total_failed} failed")


if __name__ == "__main__":
    process_all_remaining()