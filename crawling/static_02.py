# -*- coding: utf-8 -*-

import requests
#데이터를 요청 할 주소
url = 'https://www.hollys.co.kr/store/korea/korStore2.do?'
#서버에 보낼 데이터
from_data = {
    'pageNo' : 1,
    'sido' : '',
    'gugun' : '',
    'store' : ''
}

response = requests.post(url, data = from_data)
from bs4 import BeautifulSoup
# response에 있는 문자열로 된 데이터를 BeautifulSoup 객체로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# 원하는 정보를 추출
#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody >tr
str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr'
sotre_rows = soup.select(str_table_rows)
# print(sotre_rows[:])
# print(soup.select('td')[0].text.strip()) #지역
# print(soup.select('td')[1].text.strip()) #매장명
# print(soup.select('td')[2].text.strip()) #현황
# print(soup.select('td')[3].text.strip()) #주소
# print(soup.select('td')[5].text.strip()) #전화번호

# for idx, row in enumerate(sotre_rows) : 
#     print(idx + 1)
#     print(row.select('td')[0].text.strip()) #지역
#     print(row.select('td')[1].text.strip()) #매장명
#     print(row.select('td')[2].text.strip()) #현황
#     print(row.select('td')[3].text.strip()) #주소
#     print(row.select('td')[5].text.strip()) #전화번호
#     print('------------------')

store_list = []
for row in sotre_rows : 
    store_list.append(
        (
        row.select('td')[0].text.strip(), #지역
        row.select('td')[1].text.strip(), #매장명
        row.select('td')[2].text.strip(), #현황
        row.select('td')[3].text.strip(), #주소
        row.select('td')[5].text.strip() #전화번호
        )
    )
print(store_list)