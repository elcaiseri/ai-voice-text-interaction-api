import speech_recognition as sr
from gtts import gTTS
import io

def speech_to_text(audio_bytes):
    recognizer = sr.Recognizer()
    audio_file = io.BytesIO(audio_bytes)
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            text = ""
        except sr.RequestError:
            text = ""
    return text

def text_to_speech(text):
    tts = gTTS(text, lang='en')
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file.read()