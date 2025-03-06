from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load .env file
dotenv_path = "D:/documents/GitHub/al-chatbot-1/.env"
load_dotenv(dotenv_path, override=True)


# Get OpenAI API Key
api_key = os.getenv("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")
if not api_key:
    print("❌ ERROR: OpenAI API key is missing. Please check your .env file.")
    exit()

# Configure OpenAI API
client = openai.OpenAI(api_key=api_key)

# Initialize Flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        response = chat_with_openai(user_message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def chat_with_openai(message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Ensure Flask runs properly
if __name__ == "__main__":
    print("🚀 Starting Flask server with OpenAI API...")
    app.run(debug=True)
