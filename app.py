from flask import Flask, request, jsonify
from deepface import DeepFace
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Home route to show API is live
@app.route('/')
def home():
    return jsonify({
        "message": "🎉 GENIE Emotion Detection API is Live and Ready 🚀",
        "usage": "Use POST /detect with an image to get emotion results."
    })

# ✅ Emotion detection route
@app.route('/detect', methods=['POST'])
def detect_emotion():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No image file uploaded"}), 400

        file = request.files['file']
        result = DeepFace.analyze(file.read(), actions=['emotion'])
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
