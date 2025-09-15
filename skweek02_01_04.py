# -*- coding: utf-8 -*-
import random

class NumberGuessingGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

    def guess(self, user_guess):
        self.attempts += 1
        if user_guess < self.number_to_guess:
            return "너무 낮습니다!"
        elif user_guess > self.number_to_guess:
            return "너무 높아요!"
        else:
            return "Correct!"
        
    @classmethod
    def play(cls):
        game = cls()
        print("1부터 100 사이의 숫자를 맞춰보세요!")
        while True:
            try:
                user_input = int(input("숫자를 입력하세요: "))
                result = game.guess(user_input)
                print(result)
                if result == "Correct!":
                    print("축하합니다! {}번 만에 맞추셨습니다.".format(game.attempts))
                    break
            except ValueError:
                print("유효한 숫자를 입력하세요.")
    
NumberGuessingGame.play()