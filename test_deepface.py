from deepface import DeepFace

print("🔍 Analyzing image... please wait (this may take 1–2 minutes the first time)")

# ✅ Path to your image inside 'test_images' folder
image_path = "test_images/happy.jpg"

result = DeepFace.analyze(img_path=image_path, actions=['emotion'])

# Print emotion clearly
print("\n✅ Analysis complete!")
print(f"🎯 Detected Emotion: {result[0]['dominant_emotion']}")