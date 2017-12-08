# coding:utf-8
from random import randint


def funcAdd(x, y, z):
    return int(x) + int(y) + int(z)


listnum = [str(val) for val in range(1, 5)]
print(listnum, type(listnum))
# ['1', '2', '3', '4'] <class 'list'>
print([int(val) for val in listnum])
# [1, 2, 3, 4]
print(list(map(int, listnum)))
# [1, 2, 3, 4]
print("=========")

gen = lambda lens: [str(randint(30, 100)) for val in range(lens)]
list1 = gen(4)
list2 = gen(4)
list3 = gen(4)
print(list1, list2, list3)
# ['35', '58', '41', '80'] ['47', '34', '66', '82'] ['73', '44', '48', '79']
print(list(map(lambda *args: sum(map(int, args)), list1, list2, list3, list1, list2)))
# 35+47+73+35+47=237, 58+34+44+58+34=228, 41+66+48+41+66=262, 80+82+79+80+82=4.3
# [237, 228, 262, 403]
print("=========")

fpath = r'.\file\moviePlay.txt'
f = open(fpath, encoding='utf8')
result = map(lambda line: line.strip().split()[:2], f.readlines())
print(result, type(result))
# <map object at 0x006C2830> <class 'map'>
result = list(result)
# print(result, type(result))
# [['尋夢環遊記', '9.1'], ['至暗時刻', '8.6'], ['綠地黃花', '8.2'], ['日常對話', '8.1'], ['方法派', '6.8'], ['火車司機日記', '7.7'], ['奪金四賤客', '7.0'], ['真白之戀', '7.5'], ['川流之島', '7.1'], ['泥土之界', '7.2'], ['王牌特工2', '7.1'], ['英倫對決', '7.2'], ['光', '6.8'], ['精靈寶可夢', '9.9'], ['小丑回魂', '7.4'], ['我能說', '8.8'], ['晝顏', '6.5'], ['忌日快樂', '7.3']] <class 'list'>
result.sort(key=lambda vals: vals[1])
for val in result:
    print(val)
'''
['晝顏', '6.5']
['方法派', '6.8']
['光', '6.8']
['奪金四賤客', '7.0']
['川流之島', '7.1']
['王牌特工2', '7.1']
['泥土之界', '7.2']
['英倫對決', '7.2']
['忌日快樂', '7.3']
['小丑回魂', '7.4']
['真白之戀', '7.5']
['火車司機日記', '7.7']
['日常對話', '8.1']
['綠地黃花', '8.2']
['至暗時刻', '8.6']
['我能說', '8.8']
['尋夢環遊記', '9.1']
['精靈寶可夢', '9.9']
'''

listn1 = [1, 2, 3]
listn2 = [1, 2]
print(list(map(lambda x, y: x+y, listn1, listn2)))
# [2, 4]
