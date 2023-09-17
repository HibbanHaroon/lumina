# Imports
from utils.get_audio_file import get_audio_file
from utils.get_transcription import get_transcription
from utils.get_quiz_array import get_quiz_array

url = "https://www.youtube.com/watch?v=rs9AFEebHsk"
get_audio_file(url)

text = get_transcription()

result = get_quiz_array(text)
print(result)