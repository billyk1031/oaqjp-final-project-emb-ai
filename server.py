"""Main Server Module"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def render_index_page():
    """Render Index Page"""
    return render_template('index.html')


@app.route('/emotionDetector')
def emot_detector():
    """Emotion Detector Method"""

    text_to_analyze = request.args.get('textToAnalyze')
    emotion_data = emotion_detector(text_to_analyze)

    anger_score = emotion_data['anger']
    disgust_score = emotion_data['disgust']
    fear_score = emotion_data['fear']
    joy_score = emotion_data['joy']
    sadness_score = emotion_data['sadness']
    dominant_emotion = emotion_data['dominant_emotion']

    if dominant_emotion is None:
        return '<b>Invalid text! Please try again!</b>'

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )
    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
