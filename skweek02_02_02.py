# -*- coding: utf-8 -*-
class Parents : 
    def __init__(self, name):
        self.p_name = name
        print('부모 생성자')
    def parent_method(self):
        print('부모 메서드')

class Child(Parents) : 
    def __init__(self,name, age):
        Parents.__init__(self,name)
        self.age = age
        print('자식 생성자')
    def child_method(self):
        print('자식 메서드')

c = Child('홍길동', 20)
print(c.p_name, c.age)