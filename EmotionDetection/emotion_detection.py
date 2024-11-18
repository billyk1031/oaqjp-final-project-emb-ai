import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = jsonobj, headers=headers)
    
    # check error code
    if response.status_code == 400:
        return {'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None}
                
    # retrieving emotion scores from response
    formatted_response = json.loads(response.text)
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    emotion_dict = {'anger': anger_score,
                    'disgust': disgust_score,
                    'fear' : fear_score,
                    'joy' : joy_score,
                    'sadness' : sadness_score}

    # find the dominant emotion
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = dominant_emotion

    return emotion_dict
