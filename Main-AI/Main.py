# This is a simplified version of a chatbot implemented in Python.
# The chatbot uses a basic response mechanism and can be terminated by typing 'bye'.

# Import the 'responses' module, which contains a set of predefined responses.
import responses

# Define the chatbot function, which manages the conversation.
def chatbot():
    # Print a welcome message to the user.
    print("Simple Chatbot - Type 'bye' to exit")

    # Start an infinite loop for continuous interaction with the user.
    while True:
        # Get user input and store it in the 'user_input' variable.
        user_input = input("You: ")
        
        # Check if the user wants to exit the chat by typing 'bye'.
        if user_input.lower() == "bye":
            # If the user says 'bye', print a farewell message and exit the loop.
            print("Chatbot: Goodbye!")
            break

        # Use the 'responses' module to get a response based on the user's input.
        response = responses.get_response(user_input)
        
        # Display the chatbot's response to the user.
        print(f"Chatbot: {response}")

# Check if this script is being run directly (not imported as a module).
if __name__ == "__main__":
    # Call the 'chatbot' function to start the chatbot interaction.
    chatbot()
