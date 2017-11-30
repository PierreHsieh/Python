# coding=utf-8


def myStrip(src, chars=' '):
    s_index = 0
    e_index = len(src)
    # val in chars:continue s_index+=1
    # val not in chars:break
    for val in src:
        if val not in chars:
            break
        s_index += 1
    if s_index == e_index:
        return ''
    # val in chars, continue e_index -=1
    # val not in chars:break
    for val in src[::-1]:
        if val not in chars:
            break
        e_index -= 1
    return src[s_index:e_index]


testsrc1 = '    '
testsrc2 = '123abcd456'
testsrc3 = '123abcd456efg'
testsrc4 = '123abcd456efg789'

result1 = myStrip(testsrc1)
result2 = myStrip(testsrc2, chars='1234567890')
result3 = myStrip(testsrc3, chars='1234567890')
result4 = myStrip(testsrc4, chars='1234567890')

print("result1:", len(result1), ":", result1)
print("result2:", len(result2), ":", result2)
print("result3:", len(result3), ":", result3)
print("result4:", len(result4), ":", result4)
# result1: 0 :
# result2: 4 : abcd
# result3: 10 : abcd456efg
# result4: 10 : abcd456efg

strout = "result{0}:{1}:{2}"
print(strout.format(1, len(result1), result1))
print(strout.format(2, len(result2), result2))
print(strout.format(3, len(result3), result3))
print(strout.format(4, len(result4), result4))
# result1:0:
# result2:4:abcd
# result3:10:abcd456efg
# result4:10:abcd456efg
