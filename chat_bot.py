import random
responses = {
    "order status": "Please provide your order ID to track the status.",
    "return policy": "You can return products within 30 days with a valid receipt.",
    "payment issues": "We accept credit/debit cards, UPI, and PayPal. Any issue? Contact support.",
    "product recommendation": "What category are you looking for? (Electronics, Clothing, Books, etc.)",
    "default": "I'm sorry, I didn't understand. Can you rephrase?"
}


def chatbot_response(user_input):
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return responses["default"]


print("Welcome to our AI Customer Support! Type 'exit' to end chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Thank you for reaching out! Have a great day!")
        break
    print("Chatbot:", chatbot_response(user_input))