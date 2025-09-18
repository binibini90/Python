# pip install mysql
import mysql.connector as mydb
# 1. DB 연결
conn = mydb.connect(host = '127.0.0.1',
             user = 'root',
             password = 'qweqwe8422~',
             database = 'shopdb'
             )
print('DB 연결 성공')
conn.close()
# 2. CRUD 
#     C - insert
#     R - select
#     U - update
#     D - delete
# 3. 메소드
#     회원가입
#     상품정보 출력
#     상품구입
#     상품정보 입력
#     대쉬보드 : 고객별 상품별 구매회수, 평균구매액
# 4. 기능구현과 테스트가 되면.. streamlit으로 ui구성