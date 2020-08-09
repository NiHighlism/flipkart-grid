import os
import random
import string

from utils import read_config, hash_filename

AUDIO_FOLDER = read_config(section="Paths")["AUDIO_BASE_PATH"]
OUTPUT_BITRATE = read_config(section="Audio")["WAV_BITRATE"]

def flac_to_wav(input_filename, input_file, output_filename):

    temp_filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    command = f"ffmpeg -i {os.path.join(AUDIO_FOLDER, input_filename, input_file)} {os.path.join(AUDIO_FOLDER, input_filename, temp_filename)}.wav"
    print(command)
    os.system(command)
    
    command = f"sox {os.path.join(AUDIO_FOLDER, input_filename, temp_filename)}.wav -r {OUTPUT_BITRATE} {os.path.join(AUDIO_FOLDER, input_filename, output_filename)}"
    print(command)
    os.system(command)

    os.system(f"rm {os.path.join(AUDIO_FOLDER, input_filename, temp_filename)}.wav")
    return
