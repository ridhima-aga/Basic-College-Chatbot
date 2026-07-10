print("="*35)
print("      COLLEGE CHATBOT")
print("="*35)

print("Type 'bye' anytime to exit.\n")

while True:

    user = input("You: ").lower()

    if "hi" in user or "hello" in user:
        print("Bot: Hello! Welcome to ABC College.")

    elif "fees" in user:
        print("Bot: Annual fees are ₹80,000.")

    elif "admission" in user:
        print("Bot: Admissions begin in June every year.")

    elif "hostel" in user:
        print("Bot: Separate hostels are available for boys and girls.")

    elif "library" in user:
        print("Bot: Library timings are 8 AM to 8 PM.")

    elif "courses" in user:
        print("Bot: We offer B.Tech, MBA, MCA and BCA.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")