# coding='utf-8'


def mul1to9():
    # 1x1=1
    # 1x2=2 .....
    # 1x9=9....9x9=81
    for val in range(1, 10):
        f = '{x}x{y}={z} '
        # print(type(f)); # <class 'str'>
        result = ''
        for tmp in range(1, val+1):
            result += f.format(x=tmp, y=val, z=val*tmp)
        print(result)


mul1to9()
