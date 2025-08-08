import speech_recognition as sr

def transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="es-MX")
            print(f"Reconocido: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return "No entendí lo que dijiste."
        except sr.RequestError:
            return "Error con el servicio de reconocimiento."