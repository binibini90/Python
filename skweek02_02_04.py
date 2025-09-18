# -*- coding: utf-8 -*-
# 직원 Employee - 아이디, 이름, 기본급
class Employee(object):
    def __init__(self, emp_id, name, base_pay):
        self.emp_id = emp_id
        self.name = name
        self.base_pay = base_pay

    @property
    def base_pay(self):
        return self._base_pay

    @base_pay.setter
    def base_pay(self, value):
        if value >= 0:  # 0도 허용
            self._base_pay = value
        else:
            raise ValueError("기본급은 0보다 커야 합니다.")

    @property
    def get_total_pay(self):
        return self.base_pay

    def __str__(self):
        return '아이디: {}, 이름: {}, 기본급: {}'.format(self.emp_id, self.name, self.base_pay)
    def emp(self) :
        print('직원 클래스')
    
# 정규직 FullTimeEmployee - 보너스
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, base_pay, bonus):
        super(FullTimeEmployee, self).__init__(emp_id, name, base_pay)
        self.bonus = bonus

    def __str__(self):
        return '이름: {}, 기본급: {}, 보너스: {}'.format(self.name, self.base_pay, self.bonus)
    
    def fte(self) :
        print('정규직 클래스')
# 계약직 PartTimeEmployee - 시급, 기본금 없음
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours):
        super(PartTimeEmployee, self).__init__(emp_id, name, 0)  # 기본급은 0으로 설정
        self.hourly_rate = hourly_rate
        self.hours = hours
    def __str__(self):
        return '이름: {}, 시급: {}, 근무시간: {}'.format(self.name, self.hourly_rate, self.hours)
    def pte(self) :
        print('계약직 클래스')
    
#인턴 Intern - 고정수당
class Intern(Employee):
    def __init__(self, emp_id, name, fixed_salary) :
        super(Intern, self).__init__(emp_id, name, 0)  # 기본급은 0으로 설정
        self.fixed_salary = fixed_salary
    def __str__(self):
        return '이름: {}, 고정수당: {}'.format(self.name, self.fixed_salary)
    def it(self) :
        print('인턴 클래스')
    

emp = [
    FullTimeEmployee(1, "김철수", 3000000, 500000),
    PartTimeEmployee(2, "이영희", 20000, 120),
    Intern(3, "박민수", 1000000)
]

#emp에 들어있는 직원이 각각 어떤 클래스인지 순환을 이용해서 각 클래스의 it, pte, fte 메서드를 호출
for e in emp:
    if isinstance(e, FullTimeEmployee):
        e.fte()
    elif isinstance(e, PartTimeEmployee):
        e.pte()
    elif isinstance(e, Intern):
        e.it()
    print(e)