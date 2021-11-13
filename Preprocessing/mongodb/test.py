import pymongo as pm
import certifi
import pandas as pd
import get_regVec

client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/test?retryWrites=true&w=majority', tlsCAFile=certifi.where())

a = get_regVec.get_regVec(client)

print(a)