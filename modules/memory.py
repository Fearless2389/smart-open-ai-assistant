# modules/memory.py

import os
import json

# Path to store conversation history (in local file)
MEMORY_FILE = "chat_history.json"

def save_memory(history: list):
    """
    Save the chat history to a local JSON file.
    This allows persistence between sessions (optional).
    """
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        print(f"[Memory Save Error] {e}")

def load_memory() -> list:
    """
    Load the previous chat history from the local JSON file.
    Returns an empty list if file doesn't exist or can't be read.
    """
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Memory Load Error] {e}")
        return []
