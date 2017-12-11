# coding:utf-8


def func(d, key):
    try:
        key = int(key)
        print('call here')
        return d[key]
    except (KeyError, ValueError) as e:
    # except Exception as e:
    # except:
        # print('catch an exception')
        print('catch an exception', e)
        return 0


d = {10: 100}
print(func(d, '10d'))
# catch an exception
# 0