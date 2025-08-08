import subprocess
import tempfile
import os
from gtts import gTTS

def say(text):
    print("T800:", text)
    tts = gTTS(text=text, lang='es')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        print(f"Reproduciendo: {fp.name}")
        subprocess.run(["termux-media-player", "play", fp.name])
        os.remove(fp.name)
