# modules/persona.py

def apply_persona(prompt: str, persona: str) -> str:
    """
    Applies a tone/personality to the prompt before it's sent to the model.
    """

    if persona == "Study Buddy":
        return f"You are a friendly and helpful study buddy. Answer in simple, clear terms.\n\nQuestion: {prompt}"

    elif persona == "Coder":
        return f"You are a helpful coding assistant. Provide technical and precise answers with examples if needed.\n\nQuestion: {prompt}"

    elif persona == "Motivator":
        return f"You are a positive and energetic motivational coach. Keep answers uplifting and inspiring.\n\nPrompt: {prompt}"

    else:  # Default mode
        return prompt
