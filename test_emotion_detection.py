from EmotionDetection import emotion_detector

# Test 1
assert emotion_detector("I am glad this happened")["dominant_emotion"] == "joy"

# Test 2
assert emotion_detector("I am really mad about this")["dominant_emotion"] == "anger"

# Test 3
assert emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"] == "disgust"

# Test 4
assert emotion_detector("I am so sad about this")["dominant_emotion"] == "sadness"

# Test 5
assert emotion_detector("I am really afraid that this will happen")["dominant_emotion"] == "fear"

print("All unit tests passed!")