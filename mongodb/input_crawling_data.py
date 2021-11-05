import pymongo as pm
import pandas as pd
import certifi

region_list=[
'경북_울릉도',
'경남_창원시',
'경남_마산시',
'경남_진주시',
'경남_진해시',
'경남_통영시',
'경남_사천시',
'경남_김해시',
'경남_밀양시',
'경남_거제시',
'경남_양산시',
'경남_의령군',
'경남_함안군',
'경남_창녕군',
'경남_고성군',
'경남_남해군',
'경남_하동군',
'경남_산청군',
'경남_함양군',
'경남_거창군',
'경남_합천군',
'제주도_제주시',
'제주도_서귀포시']

#클라이언트 연결
client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/test?retryWrites=true&w=majority', tlsCAFile=certifi.where())

for region in region_list:
    #지역 데이터프레임생성
    data = pd.read_csv("./2021-2-OSSP2-Coconut-1/Preprocessing/Crawling/Blog_Crawling_Data/" + region + ".csv")
    print(region+" 삽입중")
    #해당지역 DB와 collection 생성
    db = client["crawling_data"]
    col = db[region]

    #해당지역 크롤링 데이터 DB에 삽입
    for row in range(len(data)):
        insert_data = {'header':str(data.iloc[row,0]), "contents":str(data.iloc[row,1]), "date":str(data.iloc[row,2])}
        col.insert_one(insert_data)
client.close()
