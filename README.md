# Flipkart-GRiD 2.0

# Team Nihighlism

Repository for Implementation stage (Level 3) for Flipkart GRiD 2.0

We have taken the following approach to acquire and process the audio files, in order to identify the primary speaker audio.

1. **Conversion of all given audio formats into .wav format**:
   We used FFmpeg to convert the various input formats into a standardized .wav type.

2. **Denoising of .wav audio**:
   All audio files were found to have some extent of background noise/ interference, which lowers the model's performance. We therefore engineered a LSTM based Deep Learning model that would filter out the background noise, that too in real time. This would serve as pre-processing for each and every audio file.
3. **Primary speaker identification**:
   We employed a Dual Path Recurrent Neural Network (DPRNN) model to separate the primary speaker audio data from the given audio. This model was further modified to provide output in real time, without any compromise on performance.
4. **Transcription of Primary speaker audio**:
   Lastly, the audio is transcribed via the ASR API provided and the transcription is saved as a .json file.
