# Imports
import assemblyai as aai

# Audio to Text
def get_transcription():
    aai.settings.api_key = f"50905bbd768d489eb14b8ac6b0f45d36"

    # URL of the file to transcribe
    FILE_URL = "audio.mp3"

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)

    print("Audio to Text Converted.")

    return transcript.text