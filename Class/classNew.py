# coding:utf-8


class myInt(int):
    def __new__(cls, num):
        print('myInt __new__', num)
        obj = int.__new__(cls, abs(num))
        return obj


class single(object):
    obj = None

    def __new__(cls, num):
        print('single __new__', num)
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj

    def __init__(self, num):
        print('call single init', num)
        self.arg = num


s1 = single(1)
# single __new__ 1
# call single init 1

s2 = single(2)
# single __new__ 2
# call single init 2

print(id(s1), id(s2), id(single(3)), id(single(4)))
# single __new__ 3
# call single init 3
# single __new__ 4
# call single init 4
# 35471920 35471920 35471920 35471920

print(s1.arg)
# 4

a = myInt(10)
# myInt __new__ 10
b = myInt(-10)
# myInt __new__ -10
print(type(a), id(a), id(b))
# <class '__main__.myInt'> 35506696 35506736
