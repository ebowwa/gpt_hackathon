from flask import Flask, request, jsonify
from backend.inference.client import OpenAIClient
from backend.resemble.speech import create_audio_clip

app = Flask(__name__)

client = OpenAIClient(api_key="null", base_url="https://dev-hub.agentartificial.com")
# collect user input 

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
      
# TODO (backend edition):        
# Search for relevant clips for twelvelabs
# - track the added content to twelvelabs uuid all videos with url to extract afterward.
# API CALLS TO MISTRAL to narrate clips/content
# - prompting mistral for (potential various styles) narration:
# 
# API calls to resemble to generate audio on the narration
# ffmpeg to stitch it all together
# Share Download/Preview 
# update the OPENAPI spec for gpts access to the workflow


if __name__ == "__main__":
    app.run(debug=True, port=5000)
