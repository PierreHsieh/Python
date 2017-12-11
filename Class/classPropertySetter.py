# coding:utf-8


class people(object):
    name = 'X'
    __age = 'X'
    gender = 'X'
    __privatedata = 'X'

    def getName(self):
        return self.name

    def setName(self, Name):
        self.name = Name

    def getAge(self):
        return self.__age

    def setAge(self, Age):
        self.__age = Age

    def privatedata(self):
        return self.privatedata

    @property
    def Age(self):
        print('call Age()')
        return self.__age

    @Age.setter
    def Age(self, age):
        print('call set age')
        self.__age = age

    def getGender(self):
        return self.gender

    def setGender(self, Gender):
        self.gender = Gender

    def eat(self, food):
        print('eat', food)

    def sleep(self, times):
        pass


p1 = people()
p1.name = 'Alan'
p1.setAge(20)
print(p1.name, p1.gender, p1.getAge())
# Alan X 20

print(p1.privatedata)
# <bound method people.privatedata of <__main__.people object at 0x01F83950>>

p1.Age = 30
# call set age
print(p1.Age)
# call Age()
# 30
