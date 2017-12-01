# coding:utf-8
from random import randint


def genList(num):
    lm = []
    for x in range(num):
        lm.append(randint(0, 10))
    # print(lm)
    return lm


def listRmSame(tlist):
    dlist = []
    for val in tlist:
        if tlist.count(val) > 1 and val not in dlist:
            dlist.append(val)
    print(dlist)
    # [7, 5, 2]
    for dval in dlist:
        n = tlist.count(dval)
        while n > 1:
            tlist.remove(dval)
            n -= 1


listn = genList(10)
print(listn)
# [9, 6, 8, 7, 5, 1, 7, 5, 2, 2]
listRmSame(listn)
print(listn)
# [9, 6, 8, 1, 7, 5, 2]
