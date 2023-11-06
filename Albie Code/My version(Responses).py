import random

def get_response(user_input):
    user_input = user_input.lower()
    
greetings = ["hello", "hi", "hey"]
farewells = ["bye", "goodbye", "see you later"]

if any(word in user_input for word in greetings):
    return "Hello, I am a chatbot. How may I assist you?"
elif any(word in user_input for word in farewells):
    return "Goodbye!"
elif "how are you" in user_input:
    return "I am a computer program, I do not experience feelings. Thank you for asking though!"
elif "are you a robot" in user_input:
    return "I am a robot, I cannot say the phrase 'I am not a robot'."
else:
    return "I am sorry, I do not understand your question, please rephrase!"
