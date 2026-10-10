
from utils import ask_ollama


def generate_reply(name, subject, email, intent, previous_reply):
    prompt = f"""
You are a professional customer support email assistant.

Write a polite, helpful, professional email reply.

Customer name: {name}
Email subject: {subject}
Customer email: {email}
Detected intent: {intent}
Reference reply from a previous interaction: {previous_reply}

Instructions:
- Address the customer politely.
- Acknowledge the issue.
- Use the previous reply as guidance, not as a reply to copy blindly.
- Do not invent order status, refunds, or actions already completed.
- Do not promise an outcome that is not confirmed.
- Include a greeting and a professional sign-off.
- Return only the email reply.
"""

    return ask_ollama(prompt)
