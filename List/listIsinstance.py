# coding:utf-8

listl = [1, 2, 3, 4, 5, 'abc', [6, 7, 8], (9, 10, 11), (12,)]

for val in listl:
    if isinstance(val, (str, list)):
        for v in val:
            print(v)
    else:
        print(val)
