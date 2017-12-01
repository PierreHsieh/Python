# coding:utf-8


def myCount1(eng_msg):
    d = {}
    for key in eng_msg:
        if key.strip() == '':
            continue
        print(key)
        # t h i s i s p y t h o n

        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    print(d)
    return d


def myCount2(eng_msg):
    strc = ''
    for c in range(ord('a'), ord('z') + 1):
        strc += chr(c)
    print(strc, type(strc))
    # abcdefghijklmnopqrstuvwxyz <class 'str'>

    d = dict.fromkeys(strc, 0)
    print(d, type(d), "\n")
    # {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's':0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0} <class 'dict'>

    for key in eng_msg:
        if key.strip() == '':
            continue
        d[key] += 1
    print(d, type(d), "\n")
    # {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 2, 'i': 2, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 1, 'o': 1, 'p': 1, 'q': 0, 'r': 0, 's':2, 't': 2, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 1, 'z': 0} <class 'dict'>

    keys = list(d.keys())
    print(keys, type(keys), "\n")
    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] <class 'list'>

    for key in keys:
        if d[key] == 0:
            d.pop(key)
    print(d)
    # {'h': 2, 'i': 2, 'n': 1, 'o': 1, 'p': 1, 's': 2, 't': 2, 'y': 1}
    return d


msg = 'this is python'
print(msg, type(msg))
print("======")
result1 = myCount1(msg)
print("======")
result2 = myCount2(msg)
