''' module to analyze text emotion '''

import json
import requests

# NOTE: THIS ONLY WORKS INSIDE IBM LAB

#text_to_analyse = input("Insert text to analyse: ")

# Define a function named emotion_analyzer that takes a string input (text_to_analyse)
def emotion_analyzer(text_to_analyse):
    ''' ANALYZES EMOTION '''
    # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header, timeout=1.5)
    result = response.text
    formatted_response = json.loads(result)
    if text_to_analyse != "":
        if response.status_code == 500:
            label = None
        elif response.status_code == 200:
            anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
            disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
            fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
            joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
            sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
            emotions = formatted_response["emotionPredictions"][0]["emotion"]
            sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
            dominant_emotion = sorted_emotions[0]
    else:
        anger_score = ""
        disgust_score = ""
        fear_score = ""
        joy_score = ""
        sadness_score = ""
        dominant_emotion = ""
    return print('anger:', anger_score,
            'disgust:', disgust_score,
            'fear:', fear_score,
            'joy:', joy_score,
            'sadness:', sadness_score,
            'dominant_emotion:', dominant_emotion
            )  # Return the response text from the API

#emotion_analyzer(text_to_analyse)