# coding=utf-8


def myfind(listn, val):
    for index, value in enumerate(listn):
        if value == val:
            return index
    return -1


def bsearch(listn, val):
    s_index = 0
    e_index = len(listn) - 1
    while s_index <= e_index:  # mid = 2, s_index = 3, e_index = 5
        mid = int((s_index + e_index) / 2)
        print(s_index, e_index, mid)

        if val > listn[mid]:
            s_index = mid + 1
        elif val < listn[mid]:
            e_index = mid - 1  # mid 2  s_index = 0, e_index = 1
        else:
            print(mid)
            return mid
    print('not find:', -1)
    return -1


listn = [1, 2, 5, 34, 67, 78, 100]
print(myfind(listn, 78))
print("=====")
print(listn)
print("=====")
bsearch(listn, 67)
print("=====")
bsearch(listn, 2)
print("=====")
val = bsearch(listn, 34)
if val >= 0:
    print(listn[val])
