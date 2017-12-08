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


rose = Rose('rose', 'red', 5)
# Rose: __init__ rose red 5
# Flower: __init__ rose red
rose.grew()
# Rose: grew
rose.show()
# rose red 5
