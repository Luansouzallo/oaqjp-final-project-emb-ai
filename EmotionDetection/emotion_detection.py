import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=input_json, headers=header)
    
    # Se a requisição retornar status 400 (ex: texto vazio), retorna valores None
    if response.status_code == 400:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }
    
    # Converte a resposta para dicionário
    formatted_response = json.loads(response.text)
    
    # Extrai as emoções do dicionário de resposta da API
    # (Baseado na estrutura que a API retornou anteriormente)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Encontra a emoção dominante (aquela com o maior score)
    # Criamos um dicionário apenas com as pontuações para achar o maior valor com max()
    score_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(score_dict, key=score_dict.get)
    
    # Retorna o dicionário no formato exato exigido pelo projeto
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }