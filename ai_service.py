import os
import requests
from dotenv import load_dotenv

# Cargar la clave de API
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# URL de la API de Mistral (verifica la documentación oficial para el endpoint correcto)
API_URL = "https://api.mistral.ai/v1/chat/completions"

def create_simple_tasks(description):
    if not MISTRAL_API_KEY:
        return ['Mistral API key not found. Please set the MISTRAL_API_KEY environment variable.']

    try:
        prompt = f"""Desglosa la siguiente tarea compleja en una lista de 2 o 3 subtareas simples y accionables.

        Tarea: {description}
        Formato de respuesta:
        - Subtarea 1
        - Subtarea 2
        - Subtarea 3
        - etc.
        Responde solo con la lista de subtareas, una por línea, empezando cada línea con un guion y en español."""

        headers = {
            "Authorization": f"Bearer {MISTRAL_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistral-tiny",  # Cambia al modelo que prefieras (ej: mistral-small, mistral-medium)
            "messages": [
                {"role": "system", "content": "Eres un asistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 300
        }

        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Verifica si hay errores en la respuesta
        content = response.json()["choices"][0]["message"]["content"].strip()

        subtasks = []
        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return subtasks if subtasks else [f"Error, no se pudieron generar subtareas."]

    except Exception as e:
        return [f"Error: {str(e)}"]
