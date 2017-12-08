# coding:utf-8


class people(object):
    name = 'X'
    age = 'X'
    gender = 'X'


p1 = people()
p1.name = 'Arvin'
p1.gender = 'man'

people.name = 'x'
p1.age = '10'
people.gender = 'x'

print(people.age, people.name, people.gender)
print(p1.age, p1.name, p1.gender)
# X x x
# 10 Arvin man
