import requests

def emotion_detector(text_to_analyze):
    # Definizione dell'URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Intestazioni (Headers) - Usa il segno '=' per assegnare
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Payload (Input JSON)
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Esecuzione della chiamata POST
    response = requests.post(url, json=myobj, headers=headers)
    
    return response.text