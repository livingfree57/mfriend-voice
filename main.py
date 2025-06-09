from flask import Flask, request, jsonify
from flask import render_template


import requests
import os

app = Flask(__name__)

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID")  # Your cloned voice


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/speak", methods=["POST"])
def speak():
    text = request.json.get("text", "")
    if not text:
        return jsonify({"error": "No text received"}), 400

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
        headers=headers,
        json=data
    )

    if response.status_code != 200:
        return jsonify({"error": "Failed to generate speech"}), 500

    audio = response.content
    with open("static/response.mp3", "wb") as f:
        f.write(audio)

    return jsonify({"url": "/static/response.mp3"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)