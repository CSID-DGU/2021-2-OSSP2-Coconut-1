import json, requests 

def get_f(region):
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_f?region="+region)
    text = url.text
    data = json.loads(text)
    return data['features']

"""
사용예시
print(get_f("강원_강릉시"))
"""