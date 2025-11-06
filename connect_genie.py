import base64
import requests

# 🔹 1. Path to your test image
image_path = "test_images/happy.jpg"

# 🔹 2. Convert image to Base64
with open(image_path, "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

# 🔹 3. Send request to your deployed API on Render
api_url = "https://genie-emotion-api-1.onrender.com/detect"

# Send the image as JSON
response = requests.post(api_url, json={"image": img_b64})

# 🔹 4. Print the response from your API
print("Status Code:", response.status_code)
print("Response:", response.json())
