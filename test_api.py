import base64
import requests

# Deployed Render URL
API_URL = "https://genie-emotion-api-1.onrender.com/detect"

# Path to local image
IMAGE_PATH = "test_images/happy.jpg"

# Encode image as base64
with open(IMAGE_PATH, "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode("utf-8")

# Send POST request
response = requests.post(API_URL, json={"image": img_b64})

# Show results
print("Status Code:", response.status_code)
print("Response:", response.text)
