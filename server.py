from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

@app.route("/")
def render_index_page():
    return render_template('index.html')