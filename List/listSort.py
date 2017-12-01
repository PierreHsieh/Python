# conding=utf-8
from random import randint

listn = []
for i in range(5):
    listn.append(randint(0, 100))

print(listn)
# [33, 81, 70, 98, 72]

listn.reverse()
print(listn)
# [72, 98, 70, 81, 33]

listn.sort()
print(listn)
# [33, 70, 72, 81, 98]

lists = ['hello world',  'java', 'c', 'python', 'c++', 'c#', 'Qt']
lists.sort()
print(lists)
# ['Qt', 'c', 'c#', 'c++', 'hello world', 'java', 'python']

lists.sort(key=len)
print(lists)
# ['c', 'Qt', 'c#', 'c++', 'java', 'python', 'hello world']

listListSource = [[90, 90, 89], [80, 99, 70], [70, 100, 100]]
print(listListSource)
# [[90, 90, 89], [80, 99, 70], [70, 100, 100]]


def getListFirst(listn):
    return listn[0]


listListSource.sort(key=getListFirst)
print(listListSource)
# [[70, 100, 100], [80, 99, 70], [90, 90, 89]]
