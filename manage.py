import json
import os
import random
import string

from utils import read_config, hash_filename
from process_input import flac_to_wav
from denoiser import denoise
from audio_separation import dprnn
from speechToText import speech_to_text

AUDIO_BASE_PATH = read_config(section="Paths")["AUDIO_BASE_PATH"]

class Manager:
    def __init__(self, audio):
        self.audio = audio
        filename = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))
    
        self.file = f"{filename}.flac"
        self.filename = filename

        if not os.path.exists(os.path.join(AUDIO_BASE_PATH, filename)):
            os.makedirs(os.path.join(AUDIO_BASE_PATH, filename))
        
        f = open(os.path.join(AUDIO_BASE_PATH, filename, f"{filename}.flac"), "wb")
        f.write(audio)

    def convert_audio(self):
        input_file = self.file
        input_filename = self.filename

        flac_to_wav(
            input_filename=input_filename,
            input_file=input_file,
            output_filename=f"{input_filename}.wav"
        )
    
    def denoise_input(self):
        input_filename = self.filename

        denoise(
            input_folder=os.path.join(AUDIO_BASE_PATH, self.filename),
            output_folder=os.path.join(AUDIO_BASE_PATH, self.filename, "denoised")
            )
    
    def separate(self):
        input_filename = self.filename

        dprnn(
            input_filename=os.path.join(AUDIO_BASE_PATH, self.filename, "denoised",f"{self.filename}.wav")
        )
    

    def create_transcript(self):
        files = []
        for root, dirs, f in os.walk(os.path.join(AUDIO_BASE_PATH, self.filename, "denoised")):
            for i in f:
                files.append(os.path.join(root, i))

        transcripts = []
        for idx, file in enumerate(files):
            r = speech_to_text(file)
            
            f = open(os.path.join(AUDIO_BASE_PATH, self.filename, f"transcript{idx}.json"), "w")
            data = r.json()
            transcripts.append(data)
            f.write(json.dumps(data))
        
    
        try:
            return transcripts[2]
        except:
            return transcripts[0]
