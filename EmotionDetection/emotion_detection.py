""" emotion prodiction """
import json
import requests

def emotion_detector(text_to_analyze):
    """ calls watson with 'text_to_anlyze' and returns watson's response """
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputObject = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = inputObject, headers = headers)
    
    if response.status_code == 400:
        emotion_scores = {}
        emotion_scores['anger'] = None
        emotion_scores['disgust'] = None
        emotion_scores['fear'] = None
        emotion_scores['joy'] = None
        emotion_scores['sadness'] = None
        emotion_scores['dominant_emotion'] = None
        return emotion_scores
    
    responseJson = response.json()      
    emotionPredictions = responseJson["emotionPredictions"][0]["emotion"]
    anger_score = emotionPredictions["anger"]
    disgust_score = emotionPredictions["disgust"]
    fear_score = emotionPredictions["fear"]
    joy_score = emotionPredictions["joy"]
    sadness_score = emotionPredictions["sadness"]

    emotion_scores = {}
    emotion_scores['anger'] = anger_score
    emotion_scores['disgust'] = disgust_score
    emotion_scores['fear'] = fear_score
    emotion_scores['joy'] = joy_score
    emotion_scores['sadness'] = sadness_score

    dominant_emotion_name = ""
    dominant_emotion_score = -1.0
    for key in emotion_scores.keys():
        if emotion_scores[key]> dominant_emotion_score:
           dominant_emotion_name = key
           dominant_emotion_score = emotion_scores[key]
    
    emotion_scores['dominant_emotion'] = dominant_emotion_name

    
    return emotion_scores