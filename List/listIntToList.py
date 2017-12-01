# coding:utf-8


def intToList1(num):
    result = []
    while num > 0:
        m = num % 10
        result.insert(0, m)
        num = int(num / 10)
        print(num)
    print(result)
    return result


def intToList2(num):
    result = []
    strm = str(num)
    for val in strm:
        print(val)
        result.append(int(val))
    print(result)
    return result


num = 1234
listm = intToList1(num)
listn = intToList2(num)
