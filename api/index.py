from flask import Flask, request, jsonify
from backend.inference.client import OpenAIClient

app = Flask(__name__)

client = OpenAIClient(api_key="null", base_url="https://dev-hub.agentartificial.com")


@app.route('/get_chat_response', methods=['POST'])
def get_chat_response():
    data = request.json
    message = data.get('message')

    if not message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = client.get_chat_response(message)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
