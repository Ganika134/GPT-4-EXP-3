
def get_customer_input():
    print("\n--- Customer Email Details ---")

    name = input("Enter customer name: ").strip()
    subject = input("Enter email subject: ").strip()
    email = input("Enter customer email: ").strip()

    if not name or not subject or not email:
        print("All fields are required.")
        return None

    print("\n--- Entered Details ---")
    print("Customer Name:", name)
    print("Subject:", subject)
    print("Customer Email:", email)

    return {
        "name": name,
        "subject": subject,
        "email": email
    }
