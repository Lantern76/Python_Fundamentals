import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the secret key from your .env file
load_dotenv()
api_key = os.getenv("XAI_API_KEY")

# 2. Connect to xAI
# xAI uses the standard OpenAI format but a different URL
client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")

print("Connecting to Grok...")

# 3. Send a message
completion = client.chat.completions.create(
    model="grok-4-1-fast-reasoning",  # Or "grok-2" depending on what your key has access to
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Explain quantum physics in one sentence."},
    ],
)

# 4. Print the answer
print(completion.choices[0].message.content)
