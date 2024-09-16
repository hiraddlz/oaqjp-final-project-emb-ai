import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
        # Convert response to dictionary
        response_dict = response.json()
        response_dict = response_dict['emotionPredictions'][0]['emotion']
        
        # Extract emotions and their scores
        emotions = {
            'anger': response_dict.get('anger', 0),
            'disgust': response_dict.get('disgust', 0),
            'fear': response_dict.get('fear', 0),
            'joy': response_dict.get('joy', 0),
            'sadness': response_dict.get('sadness', 0)
        }
        emotions = {k: v for k, v in sorted(emotions.items(), key=lambda item: item[1], reverse=True)}
        
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        emotions['dominant_emotion'] = dominant_emotion
        # Create the result dictionary
       
        
        return emotions
    else:
        return {"error": f"Error: {response.status_code}"}

# Example usage:
if __name__ == "__main__":
    text = "I am so happy I am doing this."
    print(emotion_detector(text))