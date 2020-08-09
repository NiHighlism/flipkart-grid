from utils import hash_filename, write_wav, read_wav


def read_audio_files():
    FOLDER_NAME = "separated_audios"
    
    audios = []
    for file in os.walk(FOLDER_NAME):
        audio = read_wav(file)
        audios.append(audio)
    
    return audios


def primary_speaker_detection(audios):
    pass

def detect_primary_speaker():
    OUTPUT_FOLDER = "speakers"

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    audios = read_audio_files()

    if len(audios) == 1:
        write_wav(audios[0], os.path.join(OUTPUT_FOLDER, "primary.wav"))
        return        
    else:
        primary_audio = primary_speaker_detection(audios)
        write_wav(primary_audio, os.path.join(OUTPUT_FOLDER, "primary.wav"))
        return
