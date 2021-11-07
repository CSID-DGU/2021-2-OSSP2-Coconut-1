import pymongo as pm
import certifi
import datetime

#클라이언트 연결
client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/test?retryWrites=true&w=majority', tlsCAFile=certifi.where())

db = client["crawling_data"]
col = db["강원_강릉시"]
print(len(list(col.find({},{'date':1}).sort('date',-1))))
print(col.find({},{'date':1}).sort('date',-1)[0]['date'])


latest_date = col.find({},{'date':1}).sort('date',-1)[0]['date'].split('.')
start_date = (datetime.date(int(latest_date[0]), int(latest_date[1]), int(30))+datetime.timedelta(days=1)).isoformat()

end_date = datetime.datetime.now().strftime("%Y-%m-%d")
print(start_date)
print(end_date)