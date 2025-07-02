import streamlit as st
from modules.chat import generate_response
from modules.voice import speech_to_text, speak_text

st.set_page_config(page_title="Smart AI Assistant")
st.title("💬 Smart AI Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

# Text Input or Voice
input_mode = st.radio("Input method", ["Type", "Speak"])

if input_mode == "Type":
    user_input = st.text_input("Ask me something:")
else:
    if st.button("🎙️ Speak"):
        user_input = speech_to_text()
        st.write(f"You said: {user_input}")
    else:
        user_input = ""

# Generate Response
if user_input:
    reply, updated_history = generate_response(user_input, st.session_state.history)
    st.session_state.history = updated_history
    st.markdown(f"**Assistant**: {reply}")
    speak_text(reply)
# Display Chat History
if st.session_state.history:
    st.subheader("Chat History")
    for i, message in enumerate(st.session_state.history):
        if i % 2 == 0:
            st.markdown(f"**You**: {message}")
        else:
            st.markdown(f"**Assistant**: {message}")