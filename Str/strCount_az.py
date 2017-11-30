# coding=utf-8


def countAZMax(strl):
    # a-z
    # ord('a')   => 97
    # chr(97)    => 'a'
    # unichr(97) => u'a'
    maxval = ''
    maxnum = 0
    for x in range(ord('a'), ord('z')+1):
        val = chr(x)
        num = strl.count(val)
        if maxnum < num:
            # print ('====>', maxval, maxnum)
            maxval = val
            maxnum = num
            # print ('====<', maxval, maxnum)
    print(maxval, maxnum)
    return maxval, maxnum


strl = 'aabbbccddddeeeee'
countAZMax(strl)
# e 5
