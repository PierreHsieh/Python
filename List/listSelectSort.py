# coding=utf-8
from random import randint


def select_sort(listm):
    print(listm)
    for index, value in enumerate(listm):
        mindex = index
        for i, val in enumerate(listm[index:]):
            if val < listm[mindex]:
                mindex = i+index
        if index != mindex:
            listm[index], listm[mindex] = listm[mindex], listm[index]
        print(listm)


listn = []
for i in range(20):
    listn.append(randint(0, 100))

select_sort(listn)
