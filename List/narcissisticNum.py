# coding=utf-8


def intToList(num):
    result = []
    strm = str(num)
    for val in strm:
        result.append(int(val))
    return result


def countval(listnum):
    n = len(listnum)
    result = 0
    for val in listnum:
        result += val ** n
    return result


def flower(n_start, n_end):
    result = []
    for n in range(n_start, n_end):
        tmp = intToList(n)
        # print(tmp, type(tmp))
        if countval(tmp) == n:
            result.append(n)
    print(result)
    return result


flower(0, 10000)
