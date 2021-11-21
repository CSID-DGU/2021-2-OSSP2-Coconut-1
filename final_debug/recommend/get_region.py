import json, requests 

def get_r(features):
    features = '_'.join(features)
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_r?features="+features)
    text = url.text
    data = json.loads(text)
    return data['regions']