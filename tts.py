from gtts import gTTS
from playsound import playsound
import tempfile

def say(text):
    print("T800:", text)
    tts = gTTS(text=text, lang='es')
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        tts.save(fp.name)
        playsound(fp.name)