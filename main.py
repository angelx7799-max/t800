from wakeword import listen_for_wakeword
from tts import say
from stt import transcribe
from actions import execute_command

def main():
    say("T800 iniciado. Esperando a que digas 'Atila'.")
    print("Entrando al loop principal...")

    while True:
        print("Escuchando wakeword...")
        if listen_for_wakeword():
            print("Wakeword detectado!")
            say("Te escucho.")
            comando = transcribe()
            if comando:
                print(f"Comando recibido: {comando}")
                respuesta = execute_command(comando)
                say(respuesta)
        else:
            print("Wakeword no detectado.")

if __name__ == "__main__":
    main()