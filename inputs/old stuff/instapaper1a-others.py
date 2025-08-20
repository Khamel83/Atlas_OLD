import requests
from bs4 import BeautifulSoup
import csv
import os

# Define login details
login_url = "https://www.instapaper.com/user/login"
username = "khamel83@gmail.com"
password = "volvo87"

# Start a session
session = requests.Session()

# Fetch the login page to get the CSRF token
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")

# Extract the CSRF token
csrf_token_element = soup.find("input", {"name": "csrf_token"})
if csrf_token_element:
    csrf_token = csrf_token_element["value"]
else:
    # If CSRF token is not found, try to find it in other ways
    csrf_token = None
    # Look for a script tag that might contain the CSRF token
    script_tags = soup.find_all("script")
    for script in script_tags:
        if "csrf_token" in script.text:
            # Extract the CSRF token from the script content
            # This is a simple example, you might need to adjust the extraction logic
            csrf_token = script.text.split("csrf_token")[1].split("'")[1]
            break

    if not csrf_token:
        print("CSRF token not found. Exiting.")
        exit()

# Prepare the login payload
payload = {
    "username": username,
    "password": password,
    "csrf_token": csrf_token,
    "keep_logged_in": "1",
}

# Set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": login_url,
}

# Perform login
login_response = session.post(
    login_url, data=payload, headers=headers, allow_redirects=True
)

# Check if login was successful
if "Logout" in login_response.text:
    print("Login successful.")
else:
    print("Login failed.")
    exit()

# List of URLs to scrape
urls = [
    "https://www.instapaper.com/read/1685464308",
    "https://www.instapaper.com/read/1685191490",
    "https://www.instapaper.com/read/1684799827",
    "https://www.instapaper.com/read/1684456603",
    "https://www.instapaper.com/read/1684241687",
    "https://www.instapaper.com/read/1684058802",
    "https://www.instapaper.com/read/1684010322",
    "https://www.instapaper.com/read/1683309118",
    "https://www.instapaper.com/read/1683070238",
    "https://www.instapaper.com/read/1682912367",
    "https://www.instapaper.com/read/1682650333",
    "https://www.instapaper.com/read/1682641946",
    "https://www.instapaper.com/read/1682400191",
    "https://www.instapaper.com/read/1682045240",
    "https://www.instapaper.com/read/1681660568",
    "https://www.instapaper.com/read/1681202506",
    "https://www.instapaper.com/read/1681103810",
    "https://www.instapaper.com/read/1680544720",
    "https://www.instapaper.com/read/1680206176",
    "https://www.instapaper.com/read/1679847403",
    "https://www.instapaper.com/read/1679792798",
    "https://www.instapaper.com/read/1679590035",
    "https://www.instapaper.com/read/1679489498",
    "https://www.instapaper.com/read/1679486154",
    "https://www.instapaper.com/read/1679215007",
    "https://www.instapaper.com/read/1678916832",
    "https://www.instapaper.com/read/1678833135",
    "https://www.instapaper.com/read/1678421386",
    "https://www.instapaper.com/read/1678049576",
    "https://www.instapaper.com/read/1677880833",
    "https://www.instapaper.com/read/1677548453",
    "https://www.instapaper.com/read/1677144292",
    "https://www.instapaper.com/read/1676959948",
    "https://www.instapaper.com/read/1676290807",
    "https://www.instapaper.com/read/1676238377",
    "https://www.instapaper.com/read/1676237492",
    "https://www.instapaper.com/read/1675891110",
    "https://www.instapaper.com/read/1675727505",
    "https://www.instapaper.com/read/1675321888",
    "https://www.instapaper.com/read/1674984820",
    # Add more URLs here
]

# Open a CSV file to write the results
output_path = os.path.join(os.path.expanduser("~"), "Desktop", "scraped_articles.csv")
with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["URL", "Title"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for url in urls:
        # Send a GET request to the URL using the session
        response = session.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the title of the article
        title = soup.find("title").get_text()

        # Write the URL and title to the CSV file
        writer.writerow({"URL": url, "Title": title})

print(f"Scraping completed. Data saved to {output_path}")
