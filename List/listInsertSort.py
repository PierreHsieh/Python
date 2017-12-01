# conding=utf-8
from random import randint


def insert1_sort(listm):
    result = []
    for val in listm:
        index = -1
        for i, v in enumerate(result):
            if val < v:
                index = i
                result.insert(i, val)
                break
        if index < 0:
            result.append(val)
        print(result)
    return result


def insert2_sort(listm):
    for index, val in enumerate(listm):
        for i in range(index):
            if val <= listm[i]:
                listm.pop(index)
                listm.insert(i, val)
                break
        print(listm)


listn = []
for i in range(20):
    listn.append(randint(0, 100))

insert1_sort(listn)
print("================")
insert2_sort(listn)
