from wakeword import listen_for_wakeword
from tts import say
from stt import transcribe
from actions import execute_command

def main():
    say("T800 iniciado. Esperando a que digas 'Atila'.")

    while True:
        if listen_for_wakeword():
            say("Te escucho.")
            comando = transcribe()
            if comando:
                respuesta = execute_command(comando)
                say(respuesta)