import json, requests 

url = requests.get("osspcoconut.dothome.co.kr/get_Json.php")
text = url.text
print(text)
data = json.loads(text)

print(data[0])