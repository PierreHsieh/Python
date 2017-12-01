# coding:utf-8


def getListByObj(lists, objid):
    '''
    lobjs = []
    for val in lists:
        print(val)
        lobjs.append(val[objid])
    print(lobjs)
    print("====")
    '''
    z = zip(*lists)
    print(z, type(z))
    # <zip object at 0x0214C918> <class 'zip'>
    for index, vals in enumerate(z):
        if objid == index:
            return list(vals)
    return []


def getAverage(lists):
    return sum(lists)/len(lists)


listlistSource = [[80, 90, 78], [88, 99, 100], [77, 88, 60]]
print(listlistSource, type(listlistSource))
result = getListByObj(listlistSource, 0)
print(result)
aveNum = getAverage(result)
print("ave:", aveNum)


print("=====")
listTupleSource = [(80, 90, 78), (88, 99, 100), (77, 88, 60)]
print(listTupleSource, type(listTupleSource))
result = getListByObj(listlistSource, 0)
print(result)
aveNum = getAverage(result)
print("ave:", aveNum)


print("=====")
a = [80, 90, 78]
b = [88, 99, 100]
c = [77, 88, 60, 50]
listTupleSource = zip(a, b, c)
print(listTupleSource, type(listTupleSource))
# <zip object at 0x007EC940> <class 'zip'>

listlistSource = map(list, zip(*listTupleSource))
print(listlistSource, type(listlistSource))
# <map object at 0x02174930> <class 'map'>

result = getListByObj(listlistSource, 0)
print(result)
aveNum = getAverage(result)
print("ave:", aveNum)


print("=====")
a = [80, 90, 78]
b = [88, 99, 100]
c = [77, 88, 60, 50]
listTupleSource = zip(a, b, c)
print(listTupleSource, type(listTupleSource))
# <zip object at 0x007EC940> <class 'zip'>

listTupleSource = list(listTupleSource)
print(listTupleSource, type(listTupleSource))
# [(80, 88, 77), (90, 99, 88), (78, 100, 60)] <class 'list'>

listlistSource = map(list, zip(*listTupleSource))
print(listlistSource, type(listlistSource))
# <map object at 0x02174930> <class 'map'>

listlistSource = list(listlistSource)
print(listlistSource, type(listlistSource))
# [[80, 90, 78], [88, 99, 100], [77, 88, 60]] <class 'list'>

result = getListByObj(listlistSource, 0)
print(result)
aveNum = getAverage(result)
print("ave:", aveNum)
