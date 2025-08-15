#!/usr/bin/env python3
"""
Debug NYTimes login page to find correct selectors
"""

import sys
sys.path.append('/home/ubuntu/dev/atlas')

from playwright.sync_api import sync_playwright

def debug_nytimes_login():
    """Debug NYTimes login page structure"""
    print("🔍 Debugging NYTimes login page structure...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto("https://myaccount.nytimes.com/auth/login", timeout=30000)
            page.wait_for_load_state("domcontentloaded")
            
            # Take a screenshot for debugging
            page.screenshot(path="nytimes_login_debug.png")
            print("📸 Screenshot saved as nytimes_login_debug.png")
            
            # Find all input fields
            inputs = page.query_selector_all('input')
            print(f"\n📝 Found {len(inputs)} input fields:")
            
            for i, input_elem in enumerate(inputs):
                name = input_elem.get_attribute('name')
                id_attr = input_elem.get_attribute('id')
                type_attr = input_elem.get_attribute('type')
                placeholder = input_elem.get_attribute('placeholder')
                
                print(f"  Input {i+1}:")
                print(f"    name: {name}")
                print(f"    id: {id_attr}")
                print(f"    type: {type_attr}")
                print(f"    placeholder: {placeholder}")
                print()
            
            # Find all buttons
            buttons = page.query_selector_all('button')
            print(f"🔘 Found {len(buttons)} buttons:")
            
            for i, button in enumerate(buttons):
                text = button.inner_text()
                type_attr = button.get_attribute('type')
                class_attr = button.get_attribute('class')
                
                print(f"  Button {i+1}:")
                print(f"    text: '{text}'")
                print(f"    type: {type_attr}")
                print(f"    class: {class_attr}")
                print()
            
            # Wait a bit to see the page
            page.wait_for_timeout(5000)
            
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    debug_nytimes_login()