import pymongo as pm
import pandas as pd
import certifi
import time
import selenium
from selenium import webdriver
import regions
from datetime import datetime

def get_post_info(keyword: str, start_date: str, end_date: str, pages: int) -> pd.DataFrame:
    total_header = []
    total_contents = []
    total_date = []
    driver = webdriver.Chrome("./2021-2-OSSP2-Coconut-1/Preprocessing/Crawling/Driver/chromedriver_94.exe")


    for j in range(1, pages + 1):
        # first page
        first_url = f"https://section.blog.naver.com/Search/Post.nhn?pageNo=1&rangeType=PERIOD&orderBy=sim&startDate="                     f"{start_date}&endDate={end_date}&keyword={keyword}"
        # After first page
        loop_url = f"https://section.blog.naver.com/Search/"                    f"Post.nhn?pageNo={j}&rangeType=PERIOD&orderBy=sim&startDate="                    f"{start_date}&endDate={end_date}&keyword={keyword}"
        driver.get(first_url)

        if j != 1:
            driver.get(loop_url)

        # loading...
        time.sleep(1.5)

        # crawling informations on each 7 contents
        # if any selector does not exist, that selector returns blank string
        for i in range(1, 8):
            time.sleep(1)
            try:
                head = driver.find_element_by_css_selector(
                    f"#content > section > div.area_list_search > div:nth-child({i}) > div > div.info_post > div.desc > a.desc_inner > strong > span").text
            except selenium.common.exceptions.NoSuchElementException:
                head = " "
            try:
                contents = driver.find_element_by_css_selector(
                    f"#content > section > div.area_list_search > div:nth-child({i}) > div > div.info_post > div.desc > a.text").text
            except selenium.common.exceptions.NoSuchElementException:
                contents = " "
            try:
                date = driver.find_element_by_css_selector(
                    f"#content > section > div.area_list_search > div:nth-child({i}) > div > div.info_post > div.writer_info > span.date").text
            except selenium.common.exceptions.NoSuchElementException:
                date = " "

            time.sleep(1)
            print(head)
            print(contents)
            print(date)
            total_header.append(head)
            total_contents.append(contents)
            total_date.append(date)

    return total_header, total_contents, total_date



region_list = regions.get_regions()

#클라이언트 연결
client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/test?retryWrites=true&w=majority', tlsCAFile=certifi.where())

#지역별 업데이트
for region in region_list:
    db = client["crawling_data"]
    col = db[region]
    
    s = region.split('_')
    keyword = s[0] + " " + s[1] + " " + "여행"
    pages = 150

    ealiest_date=col.find({'date':1}).sort({'date',-1})[0]

    start_date = '2020-01-01'
    end_date = '2021-10-11'

    total_header, total_contents, total_date = get_post_info(keyword, start_date, end_date, pages)

    for data in zip(total_header,total_contents,total_date):

    data = {"header": total_header, "contents": total_contents, "date": total_date}
    df = pd.DataFrame(data, columns=["header", "contents", "date"])
    keyword = keyword[:-3].split()
    title = keyword[0]+"_"+keyword[1]+".csv"
    df.to_csv("./2021-2-OSSP2-Coconut-1/Preprocessing/Crawling/Blog_Crawling_Data/"+title, index=False, encoding='utf-8-sig')