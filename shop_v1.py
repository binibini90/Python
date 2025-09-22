# pip install mysql
import mysql.connector as mydb
from dotenv import load_dotenv
import os


#.env 파일 로드
load_dotenv()
# 1. DB 연결
conn = mydb.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME')
)
print('DB 연결 성공')
# 2. CRUD 
#     C - insert
#     R - select
#     U - update
#     D - delete
# 고객 - customer
def create_customer(name):
    sql = 'insert into customer values(null, %s)'
    cur = conn.cursor()
    cur.execute(sql, (name,))
    conn.commit()
    print('고객 등록 완료')
sql = 'select * from customer'
cur = conn.cursor()
cur.execute(sql)
for row in cur.fetchall():
    print(row)
print('고객 조회 완료')

def readAll_customer(isDict=False):
    sql = 'select * from customer'
    if isDict:
        with conn.cursor(dictionary=True) as cur:
            cur.execute(sql)
            for c in  cur.fetchall() :
                print(c['customer_id'], c['name'])
    else:
        with conn.cursor() as cur:
            cur.execute(sql)
            for c in  cur.fetchall() :
                print(c[0], c[1])
    print('고객 조회 완료')

def update_customer(customer_id, name):
    sql = '''
    update customer
        set name = %s
    where customer_id = %s
    '''

    with conn.cursor() as cur:
        cur.execute(sql, (name, customer_id))
    conn.commit()

def delete_customer(customer_id):
    sql = 'delete from customer where customer_id = %s'
    with conn.cursor() as cur:
        cur.execute(sql, (customer_id,))
    conn.commit()
    print('고객 삭제 완료')

# create_customer('abc')
# readAll_customer()
# update_customer(1, '임꺽정')
# readAll_customer(True)
# delete_customer(1)
# readAll_customer()
# 3. 메소드
#     회원가입
#     상품정보 출력
#     상품구입
#     상품정보 입력
#     대쉬보드 : 고객별 상품별 구매회수, 평균구매액
# 4. 기능구현과 테스트가 되면.. streamlit으로 ui구성
import streamlit as st

# session_state edit_id 초기화
if 'edit_id' not in st.session_state:
    st.session_state.edit_id = None

st.title('Shop Management System')

customer_name = st.text_input('고객명')
if st.button('고객 등록'):
    create_customer(customer_name)
    st.success('고객 등록 완료!')
    st.rerun()

st.write('### 고객 목록')

import pandas as pd

# DB에서 고객 리스트 가져오기
def get_customers():
    sql = 'select * from customer'
    with conn.cursor(dictionary=True) as cur:
        cur.execute(sql)
        return cur.fetchall()

customers = get_customers()

# 표 형태로 출력
if customers:
    df = pd.DataFrame(customers)
    df = df[['customer_id', 'name']]
    df.columns = ['회원아이디', '이름']
    st.table(df)
else:
    st.info('등록된 고객이 없습니다.')

# 기존 수정/삭제 버튼 로직은 그대로 아래에 유지
for customer in customers:
    col1, col2, col3 = st.columns([2, 2, 1])
    col1.write(f"{customer['customer_id']}")
    col2.write(f"{customer['name']}")
    if col3.button('수정', key=f"edit_{customer['customer_id']}"):
        st.session_state.edit_id = customer['customer_id']
    if col3.button('삭제', key=f"delete_{customer['customer_id']}"):
        delete_customer(customer['customer_id'])
        st.success('고객이 삭제되었습니다.')
        st.rerun()

# 수정 입력창 및 버튼
if st.session_state.edit_id is not None:
    new_name = st.text_input('새 이름 입력', key='newname_input')
    if st.button('이름 변경', key='update_btn'):
        update_customer(st.session_state.edit_id, new_name)
        st.success('이름이 변경되었습니다.')
        st.session_state.edit_id = None
        st.rerun()