# this is a learner version of the main.py file feel free to change it or even completely re-do it, enjoy

# now later on down the line we will add a training set of data over the top of these preset responses

import random

# Define a list of greetings for the chatbot to use
greetings = ["hello", "hi", "hey", "greetings", "howdy"]

# Define responses to greetings
greeting_responses = ["Hello! How can I assist you?", "Hi there! What can I do for you today?"]

# Define a list of questions for the chatbot to use
questions = ["how are you", "what's up", "how's it going", "how's your day"]

# Define responses to questions
question_responses = ["I'm just a computer program, so I don't have feelings, but thanks for asking!", "I'm here to help you. What can I assist you with?"]

# Define a default response for the chatbot
default_response = "I'm not sure how to respond to that. Can you please rephrase your question?"

# Function to generate a response
def generate_response(user_input):
    user_input = user_input.lower()

    for greeting in greetings:
        if greeting in user_input:
            return random.choice(greeting_responses)

    for question in questions:
        if question in user_input:
            return random.choice(question_responses)

    return default_response

# Main loop for the chatbot
if __name__ == "__main__":
    print("Chatbot: Hello! I'm a simple chatbot. You can start a conversation with me or type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)
