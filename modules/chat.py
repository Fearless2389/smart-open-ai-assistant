# modules/chat.py — using Hugging Face LLaMA 3 Inference API
import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def generate_response(user_input, history):
    # Format history as a conversation string
    history_text = ""
    for i in range(0, len(history), 2):
        history_text += f"<|user|>: {history[i]}\n<|assistant|>: {history[i+1]}\n"
    prompt = history_text + f"<|user|>: {user_input}\n<|assistant|>:"

    data = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.7,
            "top_p": 0.9,
            "repetition_penalty": 1.1,
            "do_sample": True
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()

        if "error" in result:
            reply = f"⚠️ LLaMA Error: {result['error']}"
        else:
            reply = result[0]["generated_text"].split("<|assistant|>:")[-1].strip()

    except Exception as e:
        reply = f"⚠️ API call failed: {str(e)}"

    history.append(user_input)
    history.append(reply)
    return reply, history
