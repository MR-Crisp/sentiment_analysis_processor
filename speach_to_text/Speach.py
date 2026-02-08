import sounddevice as sd
import soundfile as sf

import whisper


def record_aduio(seconds):

    fs = 44100
    print("Recording...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()

    sf.write("output3.wav", recording, fs)
    print("Done.")

def transcribe_aduio(filename):
    model = whisper.load_model("base")  # tiny, base, small, medium, large
    result = model.transcribe(filename)

    return result["text"]

