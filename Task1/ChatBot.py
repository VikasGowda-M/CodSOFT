while True:
    user = input("You: ").strip().lower()
    if "hello" in user or "hi" in user:
         print("Bot: Hi there! I am your chatbot,Type 'bye' to exit.")
    elif "how are you" in user:
        print("Bot: I am fine!")
    elif "bye" in user:
        print("Bot: Bye Buddy,Have a nice day!")
        break
    else:
        print("Bot: I don't understand ")