# -*- coding: utf-8 -*-
class Review :
    # 클래스 변수 생성
    count = 0
    # 생성자 메소드
    def __init__(self) :
        self.name = ""

# 인스턴스 생성
r1 = Review()
r2 = Review()
# 인스턴스 변수 변경
r1.name = "첫번째 리뷰 "
print(f'r1인스턴스 변수 : {r1.name}, r2인스턴스 변수 : {r2.name}')
print(f'클래스 변수 : {Review.count}')