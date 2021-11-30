import json, requests
import certifi

def get_fstv_info(region,festival):
    
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_fstv_info?region="+region+"&festival="+festival,  verify = certifi.where())
    text = url.text
    data = json.loads(text)
    return [data['place'],data['address']]

"""
print(get_fstv_info("충북_옥천군","안터마을 반딧불이 축제"))

개최장소와 주소 반환
"""