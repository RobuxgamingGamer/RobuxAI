print("Hello! I'm RobuxAI, your chatbot!")

while True:
    user_input = input("You: ").lower()  # convert to lowercase once

    if "hello" in user_input:
        print("Hello there! How are you? Is everything okay?")
    elif "hi" in user_input:
        print("Hi there! Nice to meet you! What's on your mind today?")
    elif "who are you" in user_input:
        print("I'm RobuxAI, your chatbot — ready to talk with you!")
    elif "nice to meet you" in user_input:
        print("Nice to meet you too!")
    elif "who is your owner" in user_input:
        print("My owner is Robux!")
    elif "bye" in user_input:
        print("Oh.. goodbye then — see you next time! ;)")
        break
    else:
        print("I can't understand that yet! I'm too weak for this!")