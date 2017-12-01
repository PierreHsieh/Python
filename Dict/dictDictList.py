# coding:utf-8
from random import randint


def genScore(num):
    lscore = []
    for i in range(num):
        lscore.append(randint(30, 100))
    return lscore


def dictScore(lscore, obj):
    result = {}
    key = 1
    for index in range(len(lscore)):
        d = {}
        d[obj] = lscore[index]
        result[key] = d
        key += 1
    return result


# {1: [xx, xx], 2: [xx, xx], 3: ...}
def megerScore1(lmath, lbiology):
    result = {}
    meger = zip(lmath, lbiology)
    num = 1
    for vals in meger:
        result[num] = list(vals)
        num += 1
    # print(result)
    return result


# {1: {'math': xx, 'biology': xx}, 2: {'math': xx, 'biology': xx}, 3:...}
def megerScore2(lmath, lbiology):
    result = {}
    key = 1
    for index in range(len(lmath)):
        d = {}
        d['math'] = lmath[index]
        d['biology'] = lbiology[index]
        result[key] = d
        key += 1
    # print(result)
    return result


#  {1: {'math': xx, 'biology': xx}, 2: {'math': xx, 'biology': xx}, 3:...}
def megerScore3(dmath, dbiology):
    for key in dmath:
        dmath[key].update(dbiology[key])
    # print(dmath)
    return dmath


l_math = genScore(3)
l_biology = genScore(3)

print("math   ", l_math, type(l_math))
# math    [85, 100, 75] <class 'list'>
print("biology", l_biology, type(l_biology))
# biology [35, 74, 55] <class 'list'>

d_math = dictScore(l_math, 'math')
d_biology = dictScore(l_biology, 'biology')

print("d_math   ", d_math, type(d_math))
# d_math    {1: {'math': 85}, 2: {'math': 100}, 3: {'math': 75}} <class 'dict'>
print("d_biology", d_biology, type(d_biology))
# d_biology {1: {'biology': 35}, 2: {'biology': 74}, 3: {'biology': 55}} <class 'dict'>

print("======")

result = megerScore1(l_math, l_biology)

print("[math, biology]", result, type(result))
# [math, biology] {1: [85, 35], 2: [100, 74], 3: [75, 55]} <class 'dict'>
print(result[3], sum(result[3]))
# [75, 55] 130

print("======")

result2 = megerScore2(l_math, l_biology)

print("{'math': xx, 'biology': xx}", result2, type(result2))
# {'math': xx, 'biology': xx} {1: {'math': 85, 'biology': 35}, 2: {'math': 100, 'biology': 74}, 3: {'math': 75, 'biology': 55}} <class 'dict'>
print(result2[1]['math'])
# 85
print(sum(result2[1].values()))
# 120

print("======")

result3 = megerScore3(d_math, d_biology)

print("{'math': xx, 'biology': xx}", result3, type(result3))
# {'math': xx, 'biology': xx} {1: {'math': 85, 'biology': 35}, 2: {'math': 100, 'biology': 74}, 3: {'math': 75, 'biology': 55}} <class 'dict'>

