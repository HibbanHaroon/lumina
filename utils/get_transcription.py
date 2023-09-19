# Imports
import assemblyai as aai
import streamlit as st

# Audio to Text
def get_transcription():
    AAI_API_KEY = st.secrets["AAI_API_KEY"]

    # URL of the file to transcribe
    FILE_URL = "audio.mp3"

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)

    print("Audio to Text Converted.")

    return transcript.text