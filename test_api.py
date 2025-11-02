import base64
import requests

# 1️⃣ Convert test image to base64
with open("test_images/happy.jpg", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

# 2️⃣ Send POST request to Flask server
response = requests.post("http://127.0.0.1:5000/detect", json={"image": img_b64})

# 3️⃣ Print API response
print(response.json())
