# -*- coding: utf-8 -*-
class student() :
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self) :
        return self._age 
    @age.setter
    def age(self, value) :
        self._age = value


st1 = student('홍길동', 90)
st2 = student('홍길동', 90)
st1 == st2
print(st1)