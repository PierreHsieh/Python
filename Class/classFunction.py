# coding:utf-8


class people(object):
    name = 'X'
    age = 'X'
    gender = 'X'
    __privatedata = 'y'

    def getSelf(self):
        return (id(self))

    def getPrivatedata(self):
        print(id(self.__privatedata))
        return self.__privatedata

    def setPrivatedata(self, Privatedata):
        self.__privatedata = Privatedata

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
print(dir(people))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
#  '_people__privatedata', 'age', 'eat', 'gender', 'getAge', 'getGender', 'getName', 'getSelf', 'name', 'setAge', 'setGender', 'setName', 'sleep']
print(dir(p1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
#  '_people__privatedata', 'age', 'eat', 'gender', 'getAge', 'getGender', 'getName', 'getSelf', 'name', 'setAge', 'setGender', 'setName', 'sleep']

print(id(p1))
# 7747888
print(p1.getSelf())
# 7747888

print(p1._people__privatedata, id(p1._people__privatedata))
# y 5419360
print(p1.getPrivatedata())
# 5419360
# y

p1.__privatedata = 'z'
print(p1.__privatedata, id(p1.__privatedata))
# z 36452544
print(dir(p1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#  '__privatedata', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
#  '_people__privatedata', 'age', 'eat', 'gender', 'getAge', 'getGender', 'getName', 'getPrivatedata', 'getSelf', 'name', 'setAge', 'setGender', 'setName', 'setPrivatedata', 'sleep']

p1._people__privatedata = 'w'
print(p1._people__privatedata, id(p1._people__privatedata))
# w 5563200
print(p1.getPrivatedata())
# 5563200
# w

p1.setPrivatedata('v')
print(p1._people__privatedata, id(p1._people__privatedata))
# v 5479296
print(p1.getPrivatedata())
# 5479296
# v

p1.setAge(20)
p1.setGender('man')
p1.setName('Addison')
print(p1.getName(), p1.getAge(), p1.getGender())
# Addison 20 man