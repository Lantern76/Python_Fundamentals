import os
import json
import random
import datetime
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import pandas as pd

# Step 1: set page title
st.set_page_config(page_title="My Bot")
memory_file = "chat_history.json"
# Add sidebar
# --- NEW: SIDEBAR FOR FILES ---
# [ADD THIS IMPORT AT THE TOP]
import pandas as pd

# ... [Keep your setup code same as before] ...

# 3. THE LIBRARIAN (Sidebar)
with st.sidebar:
    st.header("📚 The Librarian")
    # Update: Allow both 'txt' and 'csv'
    uploaded_file = st.file_uploader("Upload a file", type=["txt", "csv"])

    if uploaded_file is not None:
        file_name = uploaded_file.name

        # --- PATH A: Text Files ---
        if file_name.endswith(".txt"):
            file_content = uploaded_file.read().decode("utf-8")
            st.success(f"Loaded Text: {file_name}")
            st.text(file_content[:500] + "...")  # Preview

            # Prepare for Injection
            injection_text = file_content

        # --- PATH B: CSV (Data) Files ---
        elif file_name.endswith(".csv"):
            # Load into a Pandas DataFrame
            df = pd.read_csv(uploaded_file)
            st.success(f"Loaded Data: {file_name}")

            # Show the data table
            st.dataframe(df.head(5))  # Show first 5 rows

            # Draw a quick chart!
            st.caption("Quick Visual:")
            st.line_chart(df)

            # Convert data to string so Grok can read it
            injection_text = df.to_csv(index=False)

        # --- THE INJECTION 💉 (Common to both) ---
        file_id = f"file_read_{file_name}"

        if file_id not in st.session_state:
            system_note = {
                "role": "system",
                "content": f"The user uploaded a file '{file_name}'. Here is the content:\n\n{injection_text}",
            }
            st.session_state.message.append(system_note)
            st.session_state[file_id] = True

            # Save to JSON
            with open(memory_file, "w") as f:
                json.dump(st.session_state.message, f, indent=4)

            st.toast(f"🧠 I have analyzed {file_name}!")

            # 2. Add to backpack
            st.session_state.message.append(system_note)

            # 3. Mark this file as 'read' so we don't add it again
            st.session_state[file_id] = True

            # 4. Save to JSON
            with open(memory_file, "w") as f:
                json.dump(st.session_state.message, f, indent=4)

            # 5. Tell the user
            st.toast(f"🧠 I have memorized {uploaded_file.name}!")

# Step 2: load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("XAI_API_KEY"), base_url="https://api.x.ai/v1")

memory_file = "chat_history.json"


# Step 3: Load Memory
if "message" not in st.session_state:
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            st.session_state.message = json.load(f)

    else:
        st.session_state.message = [
            {"role": "system", "content": "You are a helpful AI assistant."}
        ]

# Step 4: Loop through message in backpack
for message in st.session_state.message:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


# Step 5: Handle User Input
if prompt := st.chat_input("What is on your mind?"):
    # 5a. Display User Message immediately
    with st.chat_message("user"):
        st.markdown(prompt)

    # 5b. Add User to Backpack
    st.session_state.message.append({"role": "user", "content": prompt})

    # --- THE BRAIN (Logic) ---
    bot_reply = ""

    # REFLEX 1: TIME
    if "time" in prompt.lower():
        now = datetime.datetime.now().strftime("%I:%M %p")
        bot_reply = f"It is currently {now}"

    # REFLEX 2: DICE
    elif "roll" in prompt.lower():
        die_roll = random.randint(1, 6)
        bot_reply = f"You rolled a {die_roll}"
        pass

    # FALLBACK (Grok) - We will add this in the next step
    else:
        try:
            completion = client.chat.completions.create(
                model="grok-4-fast", messages=st.session_state.message
            )
            bot_reply = completion.choices[0].message.content
        except Exception as e:
            bot_reply = "Error connecting to Grok: {e}"

    # 5c. Display Bot Response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # 5d. Add Bot to Backpack & Save to File
    st.session_state.message.append({"role": "assistant", "content": bot_reply})

    with open(memory_file, "w") as f:
        json.dump(st.session_state.message, f, indent=4)
