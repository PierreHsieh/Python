# coding:utf-8
from functools import reduce


def func(result, info):
    info = list(map(float, info))
    result += reduce(lambda x, y: x*y, info)
    return result


listnum = list(range(1, 5))
print(listnum)
# [1, 2, 3, 4]
print(sum(listnum))
# 10
result = reduce(lambda x, y: x+y, listnum)
print(result)
# 10

liststr = [str(val) for val in listnum]
print(liststr)
# ['1', '2', '3', '4']

print(int((reduce(lambda x, y: x+y, liststr))), type(int((reduce(lambda x, y: x+y, liststr)))))
# 1234 <class 'int'>
print(reduce(lambda x, y: x*10+y, map(int, liststr)), type(reduce(lambda x, y: x*10+y, map(int, liststr))))
# 1234 <class 'int'>
print(reduce(lambda x, y: x*10+y, listnum), type(reduce(lambda x, y: x*10+y, listnum)))
# 1234 <class 'int'>

fpath = r'.\file\order.txt'
f = open(fpath, encoding='utf8')
mlist = map(lambda line: line.strip().split()[1:], f.readlines())
# print(mlist, type(mlist))
# <map object at 0x01E8B990> <class 'map'>
result = reduce(lambda tmp, info: tmp + reduce(lambda x, y: x*y, map(float, info)), mlist, 0)
print(result)
# 138920.85000000003
