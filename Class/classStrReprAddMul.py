# conding:utf-8


class Flower(object):
    name = ''
    color = ''

    def grew(self):
        print('Flower: grew')

    def __init__(self, name, color):
        print('Flower: __init__', name, color)
        self.name = name
        self.color = color


class Lily(Flower):
    pass


class Rose(Flower):
    price = 0

    def __init__(self, name, color, price):
        print('Rose: __init__', name, color, price)
        self.price = price
        super(Rose, self).__init__(name, color)

    def grew(self):
        print('Rose: grew')

    def show(self):
        print(self.name, self.color, self.price)

    def __str__(self):
        print('call __str__')
        return (self.color + ' ' + str(self.price))

    def __repr__(self):
        return 'Rose Class Object'

    def __add__(self, other):
        return self.price + other.price

    def __mul__(self, other):
        return self.price * other

    def __sub__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

listl = list('123')
print(listl, ':', repr(listl))
# ['1', '2', '3'] : ['1', '2', '3']

rose = Rose('rose', 'red', 5)
# Rose: __init__ rose red 5
# Flower: __init__ rose red

print(str(rose))
# call __str__
# red 5

print(rose, ':', repr(rose))
# call __str__
# red 5 : Rose Class Object

r = rose + rose
print(r, rose * 5)
# 10 25
