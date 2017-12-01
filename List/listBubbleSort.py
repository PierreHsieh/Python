# conding=utf-8
from random import randint


def bubble_sort(listn):
    lens = len(listn)
    for index in range(lens-1):
        flag = 0
        for i in range(lens-1-index):
            # print(i, lens)
            if listn[i] > listn[i+1]:
                listn[i], listn[i+1] = listn[i+1], listn[i]
                flag = 1
        print(i, listn)
        if flag == 0:
            break


listn = []
for i in range(20):
    listn.append(randint(0, 100))

bubble_sort(listn)
