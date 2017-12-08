# coding:utf-8
class people(object):
    name = 'X'
    __age = 'X'
    gender = 'X'

    def __new__(cls, *args, **kwargs):
        print('call __new__', args, kwargs)
        obj = object.__new__(cls)
        return obj

    def __init__(self, Name, Age, Gender):
        print('call __init__', Name, Age, Gender)
        self.name = Name
        self.__age = Age
        self.gender = Gender

    def __del__(self):
        print('call __del__')

    def getName(self):
        return self.name

    def setName(self, Name):
        self.name = Name

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, age):
        self.__age = age

    def getGender(self):
        return self.gender

    def setGender(self, Gender):
        self.gender = Gender

    def eat(self, food):
        print('eat', food)

    def sleep(self, times):
        pass


p1 = people('Alvis', 20, 'man')
# call __new__ ('Alvis', 20, 'man') {}
# call __init__ Alvis 20 man

print(type(p1))
# <class '__main__.people'>

print(p1.name, p1.Age, p1.gender)
# Alvis 20 man
# call __del__
