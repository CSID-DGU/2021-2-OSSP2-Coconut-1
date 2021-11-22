import json, requests 

def get_r(features):
    features = '-'.join(features)
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_r?features="+features)
    text = url.text
    data = json.loads(text)
    return data['regions']

"""
사용예시
print(get_r(['강원_강릉시','비치', '바다', '동해', '해변']))
"""