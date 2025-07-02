from transformers import pipeline, Conversation

# DialoGPT or Mistral-like conversational pipeline
chat_pipeline = pipeline("conversational", model="microsoft/DialoGPT-large")

# Track session history
def generate_response(user_input, chat_history):
    if not chat_history:
        chat_history = []
    conversation = Conversation(text=user_input, past_user_inputs=chat_history)
    result = chat_pipeline(conversation)
    reply = result.generated_responses[-1]
    chat_history.append(user_input)
    return reply, chat_history
