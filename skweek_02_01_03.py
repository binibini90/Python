# -*- coding: utf-8 -*-
import random

class RCP :
    scissors = 1
    rock = 2
    paper = 3

    def __init__(self, choice, comp_choice) :
        self.choice = choice
        self.comp_choice = comp_choice
    
    def result(self) :
        if self.choice == self.comp_choice :
            return '비겼습니다.'
        elif (self.choice == self.scissors and self.comp_choice == self.paper) or \
             (self.choice == self.rock and self.comp_choice == self.scissors) or \
             (self.choice == self.paper and self.comp_choice == self.rock) :   
            return '이겼습니다.'
        else :
            return '졌습니다.'  
    def __str__(self) :
        choices = {1: '가위', 2: '바위', 3: '보'}
        return '사용자 : {}, 컴퓨터 : {} => {}'.format(
            choices[self.choice], choices[self.comp_choice], self.result())
    
    @classmethod
    def play(cls):
        for _ in range(10) :
            user_choice = int(input('가위(1), 바위(2), 보(3) 중 하나를 선택하세요: '))
            comp_choice = random.randint(1, 3)
            game = cls(user_choice, comp_choice)
            print(game)
            if input('계속하시겠습니까? (y/n): ').lower() != 'y':
                break

RCP.play()