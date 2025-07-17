import requests
import json 

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(URL, json=input_json, headers=HEADERS)
    if res.status_code == 200:
        result = res.json()
        emotions = result['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=lambda k: emotions[k])
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    elif res.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
    else:
        return {"error": f"Request failed with status code {res.status_code}"}