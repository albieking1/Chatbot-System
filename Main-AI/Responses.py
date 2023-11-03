import random

def get_response(user_input):
    user_input = user_input.lower()
    
    # Predefined responses
    greetings = ["hello", "hi", "hey"]
    farewells = ["bye", "goodbye", "see you later"]
    
    if any(word in user_input for word in greetings):
        return "Hello! How can I assist you?"
    elif any(word in user_input for word in farewells):
        return "Goodbye! Feel free to come back anytime if you have more questions."
    elif "how are you" in user_input:
        return "I'm just a computer program, but I'm here to help. How can I assist you today?"
    elif "what's your name" in user_input:
        return "I'm a chatbot, so I don't have a name, but you can call me Chatbot!"
    else:
        return "I'm not sure what you mean. Can you please rephrase your question?"
