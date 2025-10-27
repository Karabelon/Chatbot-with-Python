#Beginning of my chatbot, what it's about

print ("Welcome to the Big 4 Wild Cats Chatbot!")
print ("You can ask me anything about lions, cheetahs, leopards and tigers.")
print ("Type 'exit' to end the chat.\n")

#Facts about the Big 4 cats storing in my Dictionary

cat_facts = {
    "lion": "Lions are known as the 'King of the Jungle' and live in groups called prides.",
    "tiger": "Tigers are the largest wild cats and are known for their orange fur with black stripes.",
    "leopard": "Leopards are strong climbers and are known for their spotted coats called rosettes.",
    "cheetah": "Cheetahs are the most fastest cats, and they cannot roar unlikr other cats"
}

# Loop to keep the chatbot running
while True: # This is an infinite loop, the code will run over and over until the user stops it by typing exit as mentioned above
    user_input = input("You: ").lower() #'You' will be displayed for the user to type something then press enter
#lower, makes everything a lowercase so that it is for my dictionary to find the key word


# Control statement to exit loop
    if user_input == "exit":  
        print("Chatbot: Goodbye! 🐾 Stay fierce!")
        break

    # Conditionals to match user input with available data
    if user_input in cat_facts:
        print(f"Chatbot: {cat_facts[user_input]}")
    elif user_input in ["hello", "hi", "hey"]:
        print("Chatbot: Hello! Ask me about any of the Big 4 wild cats!")
    else:
        print("Chatbot: I don't know that one yet. Try asking about lion, tiger, leopard, or cheetah.")
