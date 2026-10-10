
from utils import ask_ollama


def summarize_conversation(email):
    prompt = f"""
Summarize the customer's issue in no more than 50 words.
Include the main problem and any request made.
Do not invent facts.
Return only the summary.

Customer email:
{email}
"""

    return ask_ollama(prompt)
