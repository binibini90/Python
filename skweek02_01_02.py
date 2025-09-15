class Student : 
    def __init__(self, name, kor, eng, mat) :
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
    
    def Total(self) :
        return self.kor + self.eng + self.mat

    def Average(self) :
        return self.Total() / 3

    def Grade(self) :
        avg = self.Average()
        if avg >= 90 :
            return 'A'
        elif avg >= 80 :
            return 'B'
        elif avg >= 70 :
            return 'C'
        elif avg >= 60 :
            return 'D'
        else :
            return 'F'
    def __str__(self) :
        return f'이름 : {self.name}, 총점 : {self.Total()}, 평균 : {self.Average():.2f}, 학점 : {self.Grade()}'
        

