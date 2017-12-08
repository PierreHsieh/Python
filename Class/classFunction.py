# coding:utf-8


class people(object):
    name = 'X'
    age = 'X'
    gender = 'X'

    def getName(self):
        return self.name

    def setName(self, Name):
        self.name = Name

    def getAge(self):
        return self.age

    def setAge(self, Age):
        self.age = Age

    def getGender(self):
        return self.gender

    def setGender(self, Gender):
        self.gender = Gender

    def eat(self, food):
        print('eat', food)

    def sleep(self, times):
        pass


p1 = people()
p1.setAge(20)
p1.setGender('man')
p1.setName('Addison')
print(p1.getName(), p1.getAge(), p1.getGender())
# Addison 20 man