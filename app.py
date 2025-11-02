from flask import Flask, request, jsonify
from flask_cors import CORS
from deepface import DeepFace

app = Flask(__name__)
CORS(app)

# ✅ Home route - this fixes the "Not Found" error
@app.route('/')
def home():
    return "🎉 GENIE Emotion Detection API is Live and Ready 🚀"

# ✅ Emotion detection route
@app.route('/detect', methods=['POST'])
def detect_emotion():
    try:
        # check if image is sent in request
        if 'image' not in request.files:
            return jsonify({'error': 'No image file found in request'}), 400

        image = request.files['image']

        # use DeepFace to analyze the emotion
        result = DeepFace.analyze(image.read(), actions=['emotion'], enforce_detection=False)

        # extract the emotion
        emotion = result[0]['dominant_emotion']

        return jsonify({'emotion': emotion})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
