import requests
from bs4 import BeautifulSoup
import csv

# --- STAGE 1: THE REQUEST ---
url = "https://news.ycombinator.com/"
print(f"🚀 Visiting {url}...")
response = requests.get(url)

# --- STAGE 2: THE PARSING ---
# Turn the raw HTML into a 'Soup' object we can search
soup = BeautifulSoup(response.text, "html.parser")

# Find all the tags that contain headlines
# Note: "titleline" is the specific class Hacker News uses
headlines = soup.find_all("span", class_="titleline")

# --- STAGE 3: THE SAVE ---
filename = "tech_news.csv"

# Open the file in WRITE mode
with open(filename, "w", newline="", encoding="utf-8") as f:
    # Create the CSV writer tool
    writer = csv.writer(f)

    # Write the Header row
    writer.writerow(["Rank", "Headline", "Link"])

    print(f"💾 Saving {len(headlines)} articles to {filename}...")

    # Loop through each headline we found
    for index, tag in enumerate(headlines, 1):
        # 1. Get the text
        headline = tag.get_text()

        # 2. Find the link inside the headline tag
        link_tag = tag.find("a")
        link = link_tag["href"]

        # 3. Write the row to the file
        writer.writerow([index, headline, link])

print("✨ Done! Go check your folder.")
