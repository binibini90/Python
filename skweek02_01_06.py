# -*- coding: utf-8 -*-
class Product : 
    def __init__(self, product_name, product_price, product_stock):  # 오타 수정
        self.product_name = product_name
        self.product_price = product_price  # 오타 수정
        self.product_stock = product_stock
    
    def __str__(self) :
        return '상품명 : {}, 가격 : {}, 재고 : {}'.format(
            self.product_name, self.product_price, self.product_stock)
    def __eq__(self, other) :
        return self.product_name == other.product_name
    def __ne__(self, value):
        return self.product_name != value.product_name
    def __lt__(self, value):
        return self.product_price < value.product_price
    def __le__(self, value):
        return self.product_price <= value.product_price
    def __gt__(self, value):
        return self.product_price > value.product_price
    def __ge__(self, value):
        return self.product_price >= value.product_price
    @property
    def price(self) :
        return self.product_price
    @price.setter
    def price(self, value) :
        self.product_price = value 

p1 = Product('사과', 1000, 10)
p2 = Product('사과', 2000, 20)

print(p1 == p2)
print(p1 != p2)
print(p1 < p2)
print(p1 <= p2)
print(p1 > p2)
print(p1 >= p2) 
price = p1.price
print(price)
p1.price = 3000
print(p1)