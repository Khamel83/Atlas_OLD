import requests
import pandas as pd
import time
import os
from requests.exceptions import RequestException
from datetime import datetime

# Define login details
login_url = "https://www.instapaper.com/user/login"
username = "khamel83@gmail.com"
password = "volvo87"

# Start a session
session = requests.Session()

# Create payload for login
payload = {"username": username, "password": password}

# Perform login
try:
    login_response = session.post(login_url, data=payload)
    login_response.raise_for_status()
    print("Login successful.")
    time.sleep(5)  # Add a 5-second delay after login
except RequestException as e:
    print(f"Login failed: {e}")
    exit(1)


# Function to sanitize filename
def sanitize_filename(filename):
    return "".join(
        [c for c in filename if c.isalpha() or c.isdigit() or c == " "]
    ).rstrip()


# Read the CSV file
csv_path = "/Users/hr-svp-mac12/Library/Mobile Documents/com~apple~CloudDocs/Code/instapaper/articles.csv"
df = pd.read_csv(csv_path)

print(df.columns)
print(df.head())

required_columns = ["URL", "Title", "Summary", "Source", "Folder", "Timestamp"]
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print(
        f"Error: The following required columns are missing from the CSV: {missing_columns}"
    )
    exit(1)

# Create output directory if it doesn't exist
output_dir = "/Users/hr-svp-mac12/Library/Mobile Documents/com~apple~CloudDocs/Code/instapaper/Docs"
os.makedirs(output_dir, exist_ok=True)

# Create working CSV file
working_csv_path = "/Users/hr-svp-mac12/Library/Mobile Documents/com~apple~CloudDocs/Code/instapaper/articles_working.csv"
working_df = df.copy()
working_df["status"] = ""
working_df["error_message"] = ""

# Process articles
for index, row in df.iterrows():
    url = row["URL"]
    title = row["Title"]
    summary = row["Summary"]
    source = row["Source"]
    folder = row["Folder"]
    timestamp = row["Timestamp"]

    try:
        # Fetch the article
        response = session.get(url)
        response.raise_for_status()

        # Check if we're redirected to the login page
        if "login" in response.url.lower():
            print(
                f"Redirected to login page for article {index + 1}. Re-attempting login."
            )
            login_response = session.post(login_url, data=payload)
            login_response.raise_for_status()
            time.sleep(5)
            response = session.get(url)
            response.raise_for_status()

        # Extract the article content
        article_content = response.text

        # Format the timestamp
        formatted_date = datetime.fromtimestamp(int(timestamp)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Create HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
        </head>
        <body>
            <br><br><br>
            <p><strong>Title:</strong> {title}</p>
            <p><strong>Source:</strong> <a href="{source}">{source}</a></p>
            <p><strong>Timestamp:</strong> {formatted_date}</p>
            <p><strong>Summary:</strong> {summary}</p>
            <p><strong>Folder:</strong> {folder}</p>
            <p><strong>URL:</strong> <a href="{url}">{url}</a></p>
            <div>{article_content}</div>
        </body>
        </html>
        """

        # Create filename using the Unix timestamp
        formatted_timestamp = datetime.fromtimestamp(int(timestamp)).strftime("%m%d%y")
        filename = f"{sanitize_filename(title)}_{formatted_timestamp}.html"
        filepath = os.path.join(output_dir, filename)

        # Save HTML file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)

        working_df.at[index, "status"] = "completed"
        print(f"Processed article {index + 1}: {title}")
    except RequestException as e:
        working_df.at[index, "status"] = "error"
        working_df.at[index, "error_message"] = str(e)
        print(f"Error processing article {index + 1}: {str(e)}")

    # Save progress every 10 articles
    if (index + 1) % 10 == 0:
        working_df.to_csv(working_csv_path, index=False)
        print(f"Saved progress after processing {index + 1} articles")

    # Sleep to avoid overloading the server
    time.sleep(10)

# Save final results
working_df.to_csv(working_csv_path, index=False)
print("Processing completed")
