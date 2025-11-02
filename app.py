from flask import Flask, request, jsonify
from deepface import DeepFace
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Home route (so your Render URL won't show "Not Found")
@app.route('/')
def home():
    return "🎉 GENIE Emotion Detection API is Live and Ready 🚀"

# ✅ Emotion detection route
@app.route('/detect', methods=['POST'])
def detect_emotion():
    try:
        # Get image from request
        if 'file' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        file = request.files['file']
        file_path = "temp.jpg"
        file.save(file_path)

        # Analyze the emotion using DeepFace
        result = DeepFace.analyze(img_path=file_path, actions=['emotion'])
        emotion = result[0]['dominant_emotion']

        return jsonify({"emotion": emotion}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
