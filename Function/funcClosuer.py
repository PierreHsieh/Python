# coding:utf-8


def strToint2(strn):
    return int(strn, 2)


def strToint10(strn):
    return int(strn, 10)


def strToint16(strn):
    return int(strn, 16)


def getFuncByN(n):
   def strTointN(strn):
       return int(strn, n)
   return strTointN


strToint_2 = getFuncByN(2)
strToint_16 = getFuncByN(16)
print(type(strToint2))
# <class 'function'>
print(strToint_2('10'))
# 2
print(strToint_16('10'))
# 16
print(hex(id(2)))
# 0x572ad740
print(strToint_2.__closure__)
# (<cell at 0x007341D0: int object at 0x572AD740>,)

