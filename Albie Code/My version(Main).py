import responses

def chatbot():
  print("Simple chatbot ai - If you want to exit, just type 'bye'.")

while true():
  user_input = input("You: ")
  if user_input.lower() == "bye":
    print("
