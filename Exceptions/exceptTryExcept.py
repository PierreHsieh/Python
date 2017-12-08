# coding:utf-8


def func(d, key):
    try:
        key = int(key)
        print('call here')
        return d[key]
    except:
        print('catch an exception')
        return 0


d = {10: 100}
print(func(d, '10d'))
# catch an exception
# 0