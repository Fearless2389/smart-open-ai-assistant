import streamlit as st
from modules.chat import generate_response
from modules.memory import load_memory, save_memory
from modules.retriever import rag_answer
from modules.voice import speech_to_text, speak_text
from modules.vision import analyze_image
from modules.persona import apply_persona

st.set_page_config(page_title="Smart AI Assistant", layout="wide")

# Initialize session memory
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🤖 Smart AI Assistant")

# Sidebar: Mode Selector
mode = st.sidebar.radio("Choose Input Mode", ["📝 Text", "🎙️ Voice", "🖼️ Image"])
persona = st.sidebar.selectbox("Choose Assistant Persona", ["Default", "Study Buddy", "Coder", "Motivator"])

# File Uploads
uploaded_file = st.file_uploader("Upload a PDF/Text File for RAG (optional)", type=["pdf", "txt"])

# Load file content for RAG
context_chunks = []
if uploaded_file:
    context_chunks = rag_answer(uploaded_file)

# Input Section
if mode == "📝 Text":
    user_input = st.text_input("Ask me anything:")
elif mode == "🎙️ Voice":
    st.info("Click the button and speak your question.")
    if st.button("🎙️ Record Voice"):
        user_input = speech_to_text()
        st.write(f"You said: `{user_input}`")
else:
    image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if image_file:
        user_input = analyze_image(image_file)
        st.write(f"Question from image: `{user_input}`")
    else:
        user_input = None

# Process Input
if user_input:
    full_input = apply_persona(user_input, persona)
    response = generate_response(full_input, context_chunks)

    # Show messages
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)

    # Save to memory
    st.session_state.history.append((user_input, response))
    save_memory(st.session_state.history)

    # Speak response
    speak_text(response)

# Chat history viewer
with st.expander("🧠 View Conversation History"):
    for user_msg, bot_msg in st.session_state.history:
        st.markdown(f"**You:** {user_msg}")
        st.markdown(f"**Bot:** {bot_msg}")
