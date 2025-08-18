#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from requests.exceptions import RequestException
from datetime import date

# Define login details
login_url = 'https://www.instapaper.com/user/login'
username = 'khamel83@gmail.com'
password = 'volvo87'

# Start a session
session = requests.Session()

# Create payload for login
payload = {
    'username': username,
    'password': password
}

# Perform login
try:
    login_response = session.post(login_url, data=payload)
    login_response.raise_for_status()
    print('Login successful.')
    time.sleep(5)  # Add a 5-second delay after login
except RequestException as e:
    print(f'Login failed: {e}')
    exit(1)

# Read the CSV file
csv_path = "/Users/khamel83/Desktop/articles_test.csv"
df = pd.read_csv(csv_path)

print(df.columns)
print(df.head())

required_columns = ['URL', 'Title', 'Summary']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print(f"Error: The following required columns are missing from the CSV: {missing_columns}")
    exit(1)

# Create output directory if it doesn't exist
output_dir = '/Users/khamel83/Desktop/Docs'
os.makedirs(output_dir, exist_ok=True)

# Create working CSV file
working_csv_path = "/Users/khamel83/Desktop/articles_test_working.csv"
working_df = df.copy()
working_df['status'] = ''
working_df['error_message'] = ''

# Function to sanitize filename
def sanitize_filename(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()

# Process articles
for index, row in df.iterrows():
    url = row['URL']
    title = row['Title']
    summary = row['Summary']

    try:
        # Fetch the article
        response = session.get(url)
        response.raise_for_status()
        
        # Check if we're redirected to the login page
        if 'login' in response.url.lower():
            print(f"Redirected to login page for article {index + 1}. Re-attempting login.")
            login_response = session.post(login_url, data=payload)
            login_response.raise_for_status()
            time.sleep(5)
            response = session.get(url)
            response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the article content
        article_content = soup.find('div', id='story')
        if not article_content:
            article_content = soup.find('div', class_='story')
        if not article_content:
            article_content = soup.find('article')

        if article_content:
            # Create HTML content
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{title}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }}
                    h1 {{ color: #333; }}
                    .metadata {{ margin-bottom: 20px; }}
                    .metadata p {{ margin: 5px 0; }}
                    .content {{ margin-top: 20px; }}
                </style>
            </head>
            <body>
                <h1>{title}</h1>
                <div class="metadata">
                    <p><strong>URL:</strong> {url}</p>
                    <p><strong>Title:</strong> {title}</p>
                    <p><strong>Summary:</strong> {summary}</p>
                </div>
                <div class="content">
                    {str(article_content)}
                </div>
            </body>
            </html>
            """

            # Save HTML file
            today = date.today().strftime("%Y-%m-%d")
            filename = f"{sanitize_filename(title)}_{today}.html"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)

            working_df.at[index, 'status'] = 'completed'
            print(f"Processed article {index + 1}: {title}")
        else:
            working_df.at[index, 'status'] = 'error'
            error_message = 'Article content not found. HTML structure:'
            error_message += str(soup.prettify())[:500]  # First 500 characters of the HTML
            working_df.at[index, 'error_message'] = error_message
            print(f"Error processing article {index + 1}: {error_message}")

    except RequestException as e:
        working_df.at[index, 'status'] = 'error'
        working_df.at[index, 'error_message'] = str(e)
        print(f"Error processing article {index + 1}: {str(e)}")

    # Save progress every 10 articles
    if (index + 1) % 10 == 0:
        working_df.to_csv(working_csv_path, index=False)
        print(f"Saved progress after processing {index + 1} articles")

    # Sleep to avoid overloading the server
    time.sleep(10)  # Increased from 5 to 10 seconds

# Save final results
working_df.to_csv(working_csv_path, index=False)
print("Processing completed")