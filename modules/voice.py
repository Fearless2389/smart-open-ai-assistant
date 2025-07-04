import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception:
        return ""

def speak_text(text):
    if not text:
        print("No text to speak.")
        return

    # Save the MP3 to a named file properly
    temp_path = tempfile.gettempdir() + "/tts_output.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(temp_path)
    sound = AudioSegment.from_file(temp_path, format="mp3")
    play(sound)
    os.remove(temp_path)

