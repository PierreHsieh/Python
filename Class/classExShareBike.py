# coding:utf-8
from time import time
from time import sleep


class shareBike(object):
    fname = ''
    price = ''
    s_time = 0
    e_time = 0
    isfree = False

    def __init__(self, Name, Price):
        self.fname = Name
        self.price = Price

    @property
    def free(self):
        return self.isfree

    @free.setter
    def free(self, value):
        self.isfree = value

    def unlock(self):
        self.s_time = time()

    def lock(self):
        self.e_time = time()

    def pay(self):
        if self.free:
            return 0
        tlens = self.e_time - self.s_time
        money = (1+int(tlens/3600))*self.price
        return money

    def getTimes(self):
        return str(int((self.e_time - self.s_time) / 60)) + ':'\
               + str(int((self.e_time - self.s_time) % 60))


ofo = shareBike('ofo', 1)
ofo.unlock()
sleep(2)
ofo.lock()
ofo.free = True
print(ofo.getTimes())
# 0:2
print(ofo.pay())
# 0
