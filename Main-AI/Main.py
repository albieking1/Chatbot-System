# this is a learner version of the main.py file feel free to change it or even completely re-do it, enjoy

# now later on down the line we will add a training set of data over the top of these preset responses

import responses

def chatbot():
    print("Simple Chatbot - Type 'bye' to exit")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = responses.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
