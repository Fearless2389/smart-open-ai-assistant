# ✅ Updated Streamlit App with Chat Memory and Better UI
# File: app.py

import streamlit as st
from modules.chat import generate_response
from modules.voice import speech_to_text, speak_text

st.set_page_config(page_title="Smart AI Assistant")
st.title("🤖 Smart AI Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

# Display chat history using Streamlit's chat layout
for i in range(0, len(st.session_state.history), 2):
    st.chat_message("user").write(st.session_state.history[i])
    st.chat_message("assistant").write(st.session_state.history[i + 1])

input_mode = st.sidebar.radio("Input method", ["Type", "Speak"])

if input_mode == "Type":
    user_input = st.chat_input("Ask me something...")
else:
    if st.button("🎙️ Speak"):
        user_input = speech_to_text()
        st.chat_message("user").write(user_input)
    else:
        user_input = ""

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    response, updated_history = generate_response(user_input, st.session_state.history)
    st.session_state.history = updated_history

    with st.chat_message("assistant"):
        st.write(response)

    speak_text(response)
