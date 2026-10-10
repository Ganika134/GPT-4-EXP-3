
from datetime import datetime
from pathlib import Path

from input_module import get_customer_input
from intent_module import detect_intent
from retrieval_module import retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import summarize_conversation


OUTPUT_FILE = (
    Path(__file__).parent
    / "outputs"
    / "generated_reply.txt"
)


def process_email():
    # Part A: Read customer input
    customer = get_customer_input()

    if customer is None:
        return

    # Part B: Detect intent
    print("\n--- Intent Detection ---")
    intent = detect_intent(customer["email"])

    if intent.startswith("ERROR:"):
        print(intent)
        return

    print("Detected Intent:", intent)

    # Part C: Retrieve a similar historical email
    print("\n--- Similar Email Retrieval ---")

    try:
        previous = retrieve_similar_email(customer["email"])
    except (OSError, ValueError, KeyError) as error:
        print("Retrieval error:", error)
        return

    print("Previous Email:", previous["email"])
    print("Previous Reply:", previous["reply"])
    print("Similarity Score:", round(previous["similarity"], 3))

    # Part D: Generate a professional reply
    print("\n--- AI Reply Generation ---")

    reply = generate_reply(
        customer["name"],
        customer["subject"],
        customer["email"],
        intent,
        previous["reply"]
    )

    if reply.startswith("ERROR:"):
        print(reply)
        return

    print("\nGenerated Reply:\n")
    print(reply)

    # Part E: Improve the tone
    while True:
        print("\n--- Tone Improver ---")
        print("1. Friendly Tone")
        print("2. Formal Tone")
        print("3. Empathetic Tone")
        print("4. Keep Original Reply")

        choice = input("Choose tone: ").strip()

        tone_options = {
            "1": "Friendly",
            "2": "Formal",
            "3": "Empathetic"
        }

        if choice == "4":
            break

        if choice in tone_options:
            revised_reply = improve_tone(
                reply, tone_options[choice]
            )

            if revised_reply.startswith("ERROR:"):
                print(revised_reply)
                continue

            reply = revised_reply
            print("\nRevised Reply:\n")
            print(reply)
            break

        print("Invalid choice. Try again.")

    # Part F: Summarize the issue
    print("\n--- Conversation Summary ---")
    summary = summarize_conversation(customer["email"])

    if summary.startswith("ERROR:"):
        print(summary)
        summary = "Summary generation failed."

    print(summary)

    # Part G: Save the reply
    save_choice = input(
        "\nSave customer email and reply? (y/n): "
    ).strip().lower()

    if save_choice == "y":
        OUTPUT_FILE.parent.mkdir(
            parents=True, exist_ok=True
        )

        with OUTPUT_FILE.open(
            "a", encoding="utf-8"
        ) as file:
            file.write("\n" + "=" * 60 + "\n")
            file.write(
                f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            file.write(f"Customer: {customer['name']}\n")
            file.write(f"Subject: {customer['subject']}\n")
            file.write(f"Intent: {intent}\n")
            file.write(f"Customer Email: {customer['email']}\n")
            file.write(f"Generated Reply:\n{reply}\n")
            file.write(f"Summary: {summary}\n")

        print("Reply saved to:", OUTPUT_FILE)

    else:
        print("Reply was not saved.")


def main():
    while True:
        print("\n" + "=" * 45)
        print("   INTELLIGENT EMAIL ASSISTANT")
        print("=" * 45)
        print("1. Process a customer email")
        print("2. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                process_email()
            except (OSError, ValueError, KeyError) as error:
                print("Application error:", error)

        elif choice == "2":
            print("Thank you for using Email Assistant!")
            break

        else:
            print("Invalid choice. Enter 1 or 2.")


if __name__ == "__main__":
    main()
