from gtts import gTTS
import tempfile
import os

def say(text):
    print("T800:", text)
    tts = gTTS(text=text, lang='es')
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        tts.save(fp.name)
        os.system(f"mpg123 {fp.name}")