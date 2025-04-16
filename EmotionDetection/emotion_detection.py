import requests
import json

def emotion_detector(text_to_analyze):

    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
          'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers=header, timeout=10)
    
    # If the response status code is 200, extract the scores from the response
    if response.status_code == 200:

        formatted_response = json.loads(response.text)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        emotions = {'anger': anger_score, 
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score
                    }
        dominant = max(emotions, key=emotions.get)

        # Add the dominant emotion to the dictionary
        emotions['dominant_emotion'] = dominant

    # If the response status code is 400, set emotions to None
    elif response.status_code == 400:
        
        emotions = {'anger': None, 
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                    }        

    return emotions