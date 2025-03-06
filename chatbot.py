import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get OpenAI API Key
api_key = os.getenv("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")
if not api_key:
    print("❌ ERROR: OpenAI API key is missing. Please check your .env file.")
    exit()

# Configure OpenAI API
client = openai.OpenAI(api_key=api_key)

def chatbot_response(message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Test chatbot in terminal
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Chatbot:", chatbot_response(user_input))
