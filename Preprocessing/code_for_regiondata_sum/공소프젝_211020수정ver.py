#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


region_list=['서울_종로구',
'서울_중구',
'서울_용산구',
'서울_성동구',
'서울_광진구',
'서울_동대문구',
'서울_중랑구',
'서울_성북구',
'서울_강북구',
'서울_도봉구',
'서울_노원구',
'서울_은평구',
'서울_서대문구',
'서울_마포구',
'서울_양천구',
'서울_강서구',
'서울_구로구',
'서울_금천구',
'서울_영등포구',
'서울_동작구',
'서울_관악구',
'서울_서초구',
'서울_강남구',
'서울_송파구',
'서울_강동구',
'부산_중구',
'부산_서구',
'부산_동구',
'부산_영도구',
'부산_부산진구',
'부산_동래구',
'부산_남구',
'부산_북구',
'부산_해운대구',
'부산_사하구',
'부산_금정구',
'부산_강서구',
'부산_연제구',
'부산_수영구',
'부산_사상구',
'부산_기장군',
'대구_중구',
'대구_동구',
'대구_서구',
'대구_남구',
'대구_북구',
'대구_수성구',
'대구_달서구',
'대구_달성군',
'인천_중구',
'인천_동구',
'인천_미추홀구',
'인천_연수구',
'인천_남동구',
'인천_부평구',
'인천_계양구',
'인천_서구',
'인천_강화군',
'인천_옹진군',
'광주_동구',
'광주_서구',
'광주_남구',
'광주_북구',
'광주_광산구',
'대전_동구',
'대전_중구',
'대전_서구',
'대전_유성구',
'대전_대덕구',
'강원_춘천시',
'강원_원주시',
'강원_강릉시',
'강원_동해시',
'강원_태백시',
'강원_속초시',
'강원_삼척시',
'강원_홍천군',
'강원_횡성군',
'강원_영월군',
'강원_평창군',
'강원_정선군',
'강원_철원군',
'강원_화천군',
'강원_양구군',
'강원_인제군',
'강원_고성군',
'강원_양양군',
'울산_중구',
'울산_남구',
'울산_동구',
'울산_북구',
'울산_울주군',
'세종_세종시',
'경기_수원시',
'경기_성남시',
'경기_의정부시',
'경기_안양시',
'경기_부천시',
'경기_광명시',
'경기_평택시',
'경기_동두천시',
'경기_안산시',
'경기_고양시',
'경기_과천시',
'경기_구리시',
'경기_남양주시',
'경기_오산시',
'경기_시흥시',
'경기_군포시',
'경기_의왕시',
'경기_하남시',
'경기_용인시',
'경기_파주시',
'경기_이천시',
'경기_안성시',
'경기_김포시',
'경기_화성시',
'경기_광주시',
'경기_양주시',
'경기_포천시',
'경기_여주시',
'경기_연천군',
'경기_가평군',
'경기_양평군',
'충북_청주시',
'충북_충주시',
'충북_제천시',
'충북_보은군',
'충북_옥천군',
'충북_영동군',
'충북_진천군',
'충북_괴산군',
'충북_음성군',
'충북_단양군',
'충북_증평군',
'충남_천안시',
'충남_공주시',
'충남_보령시',
'충남_아산시',
'충남_서산시',
'충남_논산시',
'충남_계룡시',
'충남_당진시',
'충남_금산군',
'충남_연기군',
'충남_부여군',
'충남_서천군',
'충남_청양군',
'충남_홍성군',
'충남_예산군',
'충남_태안군',
'전북_전주시',
'전북_군산시',
'전북_익산시',
'전북_정읍시',
'전북_남원시',
'전북_김제시',
'전북_완주군',
'전북_진안군',
'전북_무주군',
'전북_장수군',
'전북_임실군',
'전북_순창군',
'전북_고창군',
'전북_부인군',
'전남_목포시',
'전남_여수시',
'전남_순천시',
'전남_나주시',
'전남_광양시',
'전남_담양군',
'전남_곡성군',
'전남_구례군',
'전남_고흥군',
'전남_보성군',
'전남_화순군',
'전남_장흥군',
'전남_강진군',
'전남_해남군',
'전남_영암군',
'전남_무안군',
'전남_함평군',
'전남_영광군',
'전남_장성군',
'전남_완도군',
'전남_진도군',
'전남_신안군',
'경북_포항시',
'경북_경주시',
'경북_김천시',
'경북_안동시',
'경북_구미시',
'경북_영주시',
'경북_영천시',
'경북_상주시',
'경북_경산시',
'경북_군위군',
'경북_의성군',
'경북_청송군',
'경북_영양군',
'경북_영덕군',
'경북_청도군',
'경북_고령군',
'경북_성주군',
'경북_칠곡군',
'경북_예천군',
'경북_봉화군',
'경북_울진군',
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


# In[ ]:


#최종_code

#빈 데이터프레임 생성
matrix_232x2 = pd.DataFrame(index=range(0,232), columns=['region', 'sentences']) 
#행 카운팅할 row변수생성
row=0
#반복(각 지역에 대해)
for region in region_list:
    region_data=pd.read_csv(region+".csv",encoding="utf-8")
    
    matrix_232x2.iloc[row,0]=region
    matrix_232x2.iloc[row,1]=region_data.iloc[0,0]+region_data.iloc[0,1]
    
    #반복(각 지역의 크롤링 데이터 1050행에 대해)
    for i in range(1,1050):
        if ( matrix_232x2.iloc[i,0] in list(matrix_232x2.iloc[range(0,i),0]) ):
            break
        
        matrix_232x2.iloc[row,1]=matrix_232x2.iloc[row,1] + region_data.iloc[i,0] + region_data.iloc[i,1]
    
    #matrix_232x2 다음행으로 row 업데이트        
    row += 1

#데이터확인
print(matrix_232x2.head())
print(matrix_232x2.tail())
#행렬 csv파일로 저장
matrix_232x2.to_csv("matrix_232x2.csv",encoding='utf-8-sig',index=False,header=True, sep=',')

