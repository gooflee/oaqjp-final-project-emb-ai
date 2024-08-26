""" Server code for emotion detection """

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector_details():
    """ recieve text to process and send it to watson and return formated string """

    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)
    dominant_emotion = emotions["dominant_emotion"]

    if dominant_emotion is None:
        return "<B> Invalid text! Please try again!</B>"

    del emotions["dominant_emotion"]
    formated_emotions = ""
    for emotion, score  in emotions:
        formated_emotions += "\'" + emotion + "\': " +  str(score) + ", "

    formated_emotions = formated_emotions[:-2] + ".  "
    message = f'For the given statement, the system response is {formated_emotions}'
    message = message + f'The dominant emotion is <B>{dominant_emotion}</B>'

    return message

@app.route("/")
def render_index_page():
    """ Loads index.hmtl """

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
