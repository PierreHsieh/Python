# coding:utf-8
listl = ['', 0, 1, 2, []]
print([val for val in listl if val])
# [1, 2]
print(list(filter(None, listl)))
# [1, 2]


def isEven(val):
    return val % 2 is 0


result = filter(lambda val: val % 2 is 0, range(0, 20))
print(list(result))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


def myCmp(vals):
    # print('call myCmp')
    return int(vals[2]) >= 60


fpath = r'.\file\math.txt'
f = open(fpath)
minfo = map(lambda line: line.strip().split(), f.readlines())
minfo = list(minfo)
print(minfo)
# [['1', 'name_1:', '56'], ['2', 'name_2:', '53'], ['3', 'name_3:', '65'], ['4', 'name_4:', '74'], ['5', 'name_5:', '82'], ['6', 'name_6:', '32'], ['7', 'name_7:', '66'], ['8', 'name_8:', '34'], ['9', 'name_9:', '51'], ['10', 'name_10:', '53'], ['11', 'name_11:', '65'], ['12', 'name_12:', '43'], ['13', 'name_13:', '52'], ['14', 'name_14:', '52'], ['15', 'name_15:', '95'], ['16', 'name_16:', '79'], ['17', 'name_17:', '36'], ['18', 'name_18:', '52'], ['19', 'name_19:', '36'], ['20', 'name_20:', '75'], ['21', 'name_21:', '86'], ['22', 'name_22:', '36'], ['23', 'name_23:', '100'], ['24', 'name_24:', '69'], ['25', 'name_25:', '76'], ['26', 'name_26:', '92'], ['27', 'name_27:', '67'], ['28', 'name_28:', '42'], ['29', 'name_29:', '90'], ['30', 'name_30:', '72'], ['31', 'name_31:', '99'], ['32', 'name_32:', '64'], ['33', 'name_33:', '71'], ['34', 'name_34:', '67'], ['35', 'name_35:', '46'], ['36', 'name_36:', '49'], ['37', 'name_37:', '37'], ['38', 'name_38:', '46'], ['39', 'name_39:', '87'], ['40', 'name_40:', '62']]

# mpass = filter(lambda vals: int(vals[2]) >= 60, minfo)
mpass = filter(myCmp, minfo)
print('run filter')
print(mpass, type(mpass))
# <filter object at 0x02184BB0> <class 'filter'>
print(list(mpass))
# [['3', 'name_3:', '65'], ['4', 'name_4:', '74'], ['5', 'name_5:', '82'], ['7', 'name_7:', '66'], ['11', 'name_11:', '65'], ['15', 'name_15:', '95'], ['16', 'name_16:', '79'], ['20', 'name_20:', '75'], ['21', 'name_21:', '86'], ['23', 'name_23:', '100'], ['24', 'name_24:', '69'], ['25', 'name_25:', '76'], ['26', 'name_26:', '92'], ['27', 'name_27:', '67'], ['29', 'name_29:', '90'], ['30', 'name_30:', '72'], ['31', 'name_31:', '99'], ['32', 'name_32:', '64'], ['33', 'name_33:', '71'], ['34', 'name_34:', '67'], ['39', 'name_39:', '87'], ['40', 'name_40:', '62']]
