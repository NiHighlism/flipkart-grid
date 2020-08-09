import os
import requests
from utils import read_wav
from dotenv import load_dotenv


def speech_to_text(input_filename):
    load_dotenv()
    headers = {'Authorization' : f"Token {os.getenv('API_KEY')}"}
    data = {'user' : os.getenv('USER_ID') ,'language' : 'HI'}
    files = {'audio_file' : open(input_filename, "rb")}
    url = 'https://dev.liv.ai/liv_transcription_api/recordings/'
    res = requests.post(url, headers = headers, data = data, files = files)

    return res

