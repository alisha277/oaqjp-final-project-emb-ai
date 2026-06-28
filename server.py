from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    return (
    f"For the given statement, the system response is "
    f"'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, "
    f"'joy': {response['joy']}, "
    f"'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}."
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

