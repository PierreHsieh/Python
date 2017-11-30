# coding=utf-8


def myCount(strs, subs):
    num = 0
    index = 0
    lens = len(strs)
    sublens = len(subs)
    print(lens, sublens)
    # while (lens-index) >= sublens:
    while index < lens:
        tmp = strs[index:index+sublens]
        print(index, index+sublens, tmp, subs)
        # [0,2], [1,3], [2,4] ...
        if tmp == subs:
            num += 1
        index += 1
    # print(num)
    return num


teststr = 'abcdefcdefcdefxyz'

print(myCount(teststr, 'cde'))
print(teststr.count('cde'))
