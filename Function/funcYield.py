# coding:utf-8


listnum = []
for val in range(1, 101):
    if val % 2 == 0:
        listnum.append(val)

print('1:', listnum)
# 1: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
print('2:', [val for val in range(1, 101) if val % 2 == 0])
# 2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
print('3:', list((val for val in range(1, 101) if val % 2 == 0)))
# 3: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
print('4:', list(filter(lambda val: val % 2 is 0, range(1, 101))))
# 4: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
print('----------- 1')


def genTestData():
    print('call 1')
    yield '1'
    print('call 2')
    yield '2'
    print('call 3')
    yield '3'
    print('call 4')
    yield '4'


gen1 = genTestData()
print(type(gen1))
print('======== 1')
print(next(gen1))
print('======== 2')
print(next(gen1))
print('======== 3')
print(next(gen1))
print('======== 4')
print(next(gen1))
'''
<class 'generator'>
======== 1
call 1
1
======== 2
call 2
2
======== 3
call 3
3
======== 4
call 4
4
'''
print('----------- 2')


def genEven():
    val = 1
    while val <= 100:
        print('val =', val)
        if val % 2 is 0:
            print('call yield 1')
            yield (val)
            print('call yield 2')
        val += 1


gen2 = genEven()
print('======== 1')
next(gen2)
print('======== 2')
next(gen2)
print('======== 3')
next(gen2)
print('======== 4')
next(gen2)
'''
======== 1
val = 1
val = 2
call yield 1
======== 2
call yield 2
val = 3
val = 4
call yield 1
======== 3
call yield 2
val = 5
val = 6
call yield 1
======== 4
call yield 2
val = 7
val = 8
call yield 1

'''
print('----------- 3')


def genData():
    val = yield '1'
    print('val = ', val, type(val))
    yield '2'
    print('val = ', val, type(val))


gen3 = genData()
print('======== 1')
print(next(gen3))
print('======== 2')
print(next(gen3))
'''
======== 1
1
======== 2
val =  None <class 'NoneType'>
2
'''

print('----------- 4')
gen4 = genData()
print('======== 1')
print(next(gen4))
print('======== 2')
d = gen4.send(None)
print(d)
'''
======== 1
1
======== 2
val =  None <class 'NoneType'>
2
'''

print('----------- 5')
gen5 = genData()
print('======== 1')
print(next(gen5))
print('======== 2')
d = gen5.send(3)
print(d)
'''
======== 1
1
======== 2
val =  3 <class 'int'>
2
'''

gen5.close()
# gen5.send('  ')
