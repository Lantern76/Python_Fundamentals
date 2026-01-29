# --- 1. SETUP ---
# Import the pandas library
import pandas as pd

# Create file

# Create dummy data
data = {
    "Rank": [1, 2, 3, 4, 5],
    "Headline": [
        "AI takes over the world of coding",
        "New iPhone released today",
        "Google releases new AI model",
        "Best chocolate chip cookie recipes",
        "TechCrunch: The future of Generative AI",
    ],
    "Link": [
        "https://www.theverge.com/2024/01/ai-news",
        "https://www.wired.com/2024/02/iphone-review",
        "https://techcrunch.com/2024/03/google-ai-gemini",
        "https://www.nytimes.com/2024/food/cookies",
        "https://techcrunch.com/2024/04/generative-ai",
    ],
}

# Create the DataFrame
df_dummy = pd.DataFrame(data)
df_dummy.to_csv("daily_headlines.csv", index=False)
df = pd.read_csv("daily_headlines.csv")
# Save to CSV
df = pd.read_csv("daily_headlines.csv")
print("File 'daily_headlines.csv' created successfully!")

# Load 'daily_headlines.csv' into a variable called df


# --- 3. PROCESS ---
# Filter for "AI" and save to 'ai_news'
# Extract domains and count them
ai_news = df[df["Headline"].str.contains("AI")]
counts = ai_news["Link"].str.split("/").str[2].value_counts()

# --- 4. OUTPUT ---
# Save the filtered CSV
# Create and save the bar chart

ai_news.to_csv("ai_news.csv")

counts.plot(kind="bar").figure.savefig("ai_sources.png")
