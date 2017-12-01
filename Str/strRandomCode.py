# coding=utf-8
from random import randint
from random import choice


def switchCode(rcode, swnum):
    return ''.join([rcode[x:x+swnum][::-1] for x in range(0, len(rcode), swnum)])


def getRandomCode(N):
    rcode = ''
    # listc = 'a...z'
    # listn = '0...9'
    listn = '0123456789'
    listc = ''
    for val in range(97, 122+1):
        listc += (chr(val))
    print(listc)
    numc = randint(1, N-1)
    numn = N - numc
    print('numc=%d, numn=%d' % (numc, numn))

    for val in range(numc):
        rcode += choice(listc)

    for val in range(numn):
        rcode += str(randint(0, 9))
        # rcode += str(randint(1, 9))

    """
    print("====")
    for x in range(0, len(rcode), 2):
        print(x)
    # 0 2 4 6 ...
    print(rcode)
    print(rcode[2:2+2][::-1])
    # [a0964038] => 69
    rcode = ''.join([ rcode[x:x+2][::-1] for x in range(0, len(rcode), 2) ])
    print("====")
    """

    print(rcode)
    rcode = switchCode(rcode, 2)
    rcode = switchCode(rcode, 3)
    rcode = switchCode(rcode, 4)
    rcode = switchCode(rcode, 3)
    rcode = switchCode(rcode, 2)
    print(rcode, type(rcode))
    # rukbw451 => ur5wb1k4
    return rcode


getRandomCode(5)
getRandomCode(8)
