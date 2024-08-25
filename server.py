from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotionDetector():
    """ recieve text to process and send it to watson and return formated string """

    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)
    dominant_emotion = emotions["dominant_emotion"]
    del emotions["dominant_emotion"]
    formated_emotions = ""
    for key in emotions.keys():
        formated_emotions += "\'" + key + "\': " +  str(emotions[key]) + ", "
    
    formated_emotions = formated_emotions[:-2] + "."
    message = f'For the given statement, the system response is {formated_emotions} The dominant emotion is <B>{dominant_emotion}</B>'

    return message

@app.route("/")
def render_index_page():
    """ This function initiates the rendering of the main application page over the Flask channel """

    return render_template("index.html")


if __name__ == "__main__":
    app.run()