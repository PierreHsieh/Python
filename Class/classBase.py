# coding:utf-8


class people(object):
    name = 'X'
    age = 'X'
    gender = 'X'


p1 = people()
print(dir(people))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'gender', 'name']
print(p1, type(p1))
# <__main__.people object at 0x02013590> <class '__main__.people'>

p1.age = '10'
people.gender = 'x'
print(people.age, people.name, people.gender, id(people.age), id(people.name), id(people.gender))
# X X x 8240448 8240448 5695744
print(p1.age, p1.name, p1.gender, id(p1.age), id(p1.name), id(p1.gender))
# 10 X x 33173760 8240448 5695744

p1.name = 'Arvin'
p1.gender = 'man'
print(people.age, people.name, people.gender, id(people.age), id(people.name), id(people.gender))
# X X x 8240448 8240448 5695744
print(p1.age, p1.name, p1.gender, id(p1.age), id(p1.name), id(p1.gender))
# 10 Arvin man 33173760 33174016 33173920

people.name = 'y'
people.gender = 'y'
print(people.age, people.name, people.gender, id(people.age), id(people.name), id(people.gender))
# X y y 8240448 7254368 7254368
print(p1.age, p1.name, p1.gender, id(p1.age), id(p1.name), id(p1.gender))
# 10 Arvin man 33173760 33174016 33173920