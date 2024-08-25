""" emotion prodiction """

import requests

def sentiment_analyzer(text_to_analyze):
    """ calls watson with 'text_to_anlyze' and returns watson's response """
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputObject = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = inputObject, headers = headers)

    return response.text