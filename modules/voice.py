# modules/voice.py

import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import playsound

def speech_to_text() -> str:
    """
    Records audio from the microphone and converts it to text.
    Uses SpeechRecognition + Google Web Speech API.
    """
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "API unavailable or quota exceeded."

def speak_text(text: str):
    """
    Converts a text response into speech and plays it.
    Uses gTTS (Google Text-to-Speech) + temporary audio file.
    """
    try:
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            playsound.playsound(fp.name)
    except Exception as e:
        print(f"[TTS Error] {e}")
