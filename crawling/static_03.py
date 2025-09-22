# -*- coding: utf-8 -*-
import pymysql
from dotenv import load_dotenv
import os   

load_dotenv()
def get_connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database = 'shopinfo'
    )

import crawlingcoffe

for kk in range(1, 47) : 
    with get_connection() as conn :
        with conn.cursor() as cur :
            sql = '''
                insert into shop_base_tbl
                    values(null, %s,%s,%s,%s,%s)
                '''
            cur.executemany(sql,crawlingcoffe.get_data(kk))
        conn.commit()