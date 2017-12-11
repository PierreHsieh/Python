# coding:utf-8


class Student(object):
    score = 0
    passline = 60

    def __init__(self, score):
        self.score = score

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    @staticmethod
    def mycmp(obj1, obj2):
        # print(Student.score)
        return obj1.getScore() >= obj2.getScore()

    @classmethod
    def ispass(cls, obj):
        return obj.getScore() >= cls.passline


s1 = Student(80)
s2 = Student(90)
print(s1.getScore())
# 80
print(Student.getScore(s1))
# 80
print(s1.mycmp(s1, s2))
# False
print(Student.ispass(s1))
# True
