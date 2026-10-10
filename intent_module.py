
from utils import ask_ollama


def detect_intent(email):
    prompt = f"""
Classify the customer email into exactly ONE category.

Allowed categories:
Delivery Issue
Refund Request
Product Complaint
Technical Support
Order Cancellation
General Inquiry

Return only the category name.
Do not explain your answer.

Customer email:
{email}
"""

    result = ask_ollama(prompt)

    if result.startswith("ERROR:"):
        return result

    categories = [
        "Delivery Issue",
        "Refund Request",
        "Product Complaint",
        "Technical Support",
        "Order Cancellation",
        "General Inquiry"
    ]

    for category in categories:
        if category.lower() in result.lower():
            return category

    return "General Inquiry"
