import pymongo
import UPDT_crawl
import UNC_del
import get_regVec
import input_feature
import certifi
import pymongo as pm


#클라이언트 연결
client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/test?retryWrites=true&w=majority', tlsCAFile=certifi.where())

UPDT_crawl.UPDT_crawl(client)
UNC_del.UNC_del(client)
feature_data = get_regVec.get_regVec(client)
input_feature.input_feature(client, feature_data)
print("Update complete!")