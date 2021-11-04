import pymongo as pm
import pandas as pd
import certifi

#클라이언트 연결
client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/testdb?retryWrites=true&w=majority', tlsCAFile=certifi.where())
for name in client.list_database_names():
    print(name)