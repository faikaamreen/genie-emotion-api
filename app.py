from flask import Flask, request, jsonify
from deepface import DeepFace
import numpy as np, cv2, base64

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "🐾 GENIE Emotion Detection API is Live and Ready ✨",
        "usage": "Use POST /detect with a JSON body containing 'image' (base64)"
    })

@app.route('/detect', methods=['POST'])
def detect_emotion():
    try:
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({"error": "No image data provided"}), 400

        img_data = data['image']
        img_bytes = base64.b64decode(img_data)
        np_arr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        result = DeepFace.analyze(img, actions=['emotion'])
        emotion = result[0]['dominant_emotion']

        return jsonify({"emotion": emotion})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
