
from utils import ask_ollama


def improve_tone(reply, tone):
    allowed_tones = [
        "Friendly",
        "Formal",
        "Empathetic"
    ]

    if tone not in allowed_tones:
        raise ValueError("Choose Friendly, Formal, or Empathetic.")

    prompt = f"""
Rewrite the following customer support email in a {tone.lower()} tone.

Keep the original meaning and important facts.
Do not invent promises or new information.
Return only the rewritten email.

Original email:
{reply}
"""

    return ask_ollama(prompt)
