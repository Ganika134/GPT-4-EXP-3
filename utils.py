
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"


def ask_ollama(prompt):
    """Send a prompt to the local Ollama model."""
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()
        return response.json()["response"].strip()

    except requests.RequestException as error:
        return f"ERROR: Could not connect to Ollama: {error}"
