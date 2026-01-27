import os
import json
import random
import datetime
from openai import OpenAI
from dotenv import load_dotenv

# --- SETUP ---
load_dotenv()
client = OpenAI(api_key=os.getenv("XAI_API_KEY"), base_url="https://api.x.ai/v1")

memory_file = "chat_history.json"

# Load Memory
if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        chat_history = json.load(f)
    print("🧠 Memory loaded successfully!")
else:
    chat_history = [{"role": "system", "content": "You are a helpful AI assistant."}]
    print("✨ Starting a new conversation.")

print("--- Hybrid Grok Bot (Type 'quit' to exit) ---")

# --- MAIN LOOP ---
while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break

    # --- REFLEX 1: TIME ---
    if "time" in user_input.lower():
        now = datetime.datetime.now().strftime("%I:%M %p")
        bot_reply = f"It is currently {now}"
        print(f"Bot (Local): {bot_reply}")

        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": bot_reply})

        with open(memory_file, "w") as f:
            json.dump(chat_history, f, indent=4)
        continue

    # --- REFLEX 2: DICE ---
    if "roll" in user_input.lower():
        die_roll = random.randint(1, 6)
        bot_reply = f"You rolled a {die_roll}"
        print(f"Bot (Local): {bot_reply}")

        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": bot_reply})

        with open(memory_file, "w") as f:
            json.dump(chat_history, f, indent=4)
        continue

    # --- PART 3: THE CLOUD (Grok) ---

    # 1. Append User Input FIRST (So Grok sees it)
    chat_history.append({"role": "user", "content": user_input})

    try:
        completion = client.chat.completions.create(
            model="grok-4-fast",  # Ensure this matches your API access
            messages=chat_history,
        )
        bot_reply = completion.choices[0].message.content
        print(f"Grok: {bot_reply}")

        # 2. Append Bot Reply
        chat_history.append({"role": "assistant", "content": bot_reply})

        # 3. Save to File
        with open(memory_file, "w") as f:
            json.dump(chat_history, f, indent=4)

    except Exception as e:
        print(f"❌ Error connecting to Grok: {e}")
