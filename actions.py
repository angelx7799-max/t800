from datetime import datetime
# from config import OPENAI_API_KEY, GEMINI_API_KEY, etc

def execute_command(command):
    if "hora" in command:
        return f"Son las {datetime.now().strftime('%H:%M')}"
    elif "enciende la luz" in command:
        return "Encendiendo luz (aquí conectar Arduino)"
    elif "usa gpt" in command:
        return usar_gpt(command)
    elif "usa gemini" in command:
        return usar_gemini(command)
    elif "livekit" in command:
        return usar_livekit(command)
    else:
        return "No entiendo ese comando... todavía."

def usar_gpt(prompt):
    # Aquí integras GPT
    return "[GPT] Respuesta simulada"

def usar_gemini(prompt):
    # Aquí integras Gemini
    return "[Gemini] Respuesta simulada"

def usar_livekit(prompt):
    # Aquí se comunicaría con tu agente de LiveKit
    return "[LiveKit] Acción no implementada aún"