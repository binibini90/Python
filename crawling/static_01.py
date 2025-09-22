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
print(response.text[:500])