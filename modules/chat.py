# modules/chat.py

from transformers import pipeline

# Load the text generation model from Hugging Face
# You can replace 'gpt2' with any other model, e.g., 'mistralai/Mistral-7B-Instruct-v0.1'
generator = pipeline("text-generation", model="gpt2")

def generate_response(prompt: str, context_chunks=None) -> str:
    """
    Generate a response using the language model.
    If context_chunks (from RAG) are provided, include them in the prompt.
    """
    if context_chunks:
        # Add retrieved document chunks as additional context
        combined_context = "\n".join(context_chunks)
        prompt = f"Use the following context to answer:\n{combined_context}\n\nQuestion: {prompt}"

    # Generate a response using the language model
    response = generator(prompt, max_length=150, do_sample=True, temperature=0.7)[0]['generated_text']

    # Strip out the prompt to return only the model's reply
    return response.replace(prompt, "").strip()
