# coding:utf-8
fpath = r'.\file\math.txt'


def parseFile(fname):
    result = {}
    f = open(fname)
    for line in f:
        tmp = [val.strip(':') for val in line.strip().split()]
        d = dict(name=tmp[1], math=tmp[2])
        result[int(tmp[0])] = d
    # print(result)
    f.close()
    return result


def searchByIds(dinfo, id, *arg):
    key = 'math'
    keys = list(arg)
    keys.insert(0, id)
    scores = []
    for i in keys:
        scores.append((dinfo[i][key]))
    return (dict(list(zip(keys, scores))))


def cmpb(x, y):
    return x >= y


def cmps(x, y):
    return x < y


def searchByRange(dinfo, sid=1, eid=None, passline=None, cmpfunc=cmpb):
    if eid is None:
        eid = len(dinfo)
    scores = []
    for id in range(sid, eid+1):
        scores.append(dinfo[id]['math'])
    # print(scores)
    # ['56', '53', '65', '74', '82', '32', '66', '34', '51', '53', '65', '43', '52', '52', '95', '79', '36', '52', '36', '75', '86', '36', '100',     '69', '76', '92', '67', '42', '90', '72']
    # print(len(scores))
    # 30
    if passline is None:
        return scores
    pass_scores = [val for val in scores if cmpfunc(int(val), passline)]
    # print(pass_scores)
    # ['56', '53', '65', '32', '66', '34', '51', '53', '65', '43', '52', '52', '36', '52', '36', '36', '69', '67', '42']
    return pass_scores


def update(dinfo, uid, **kwargs):
    # print(kwargs, type(kwargs))
    # {'math': 90, 'biology': 80} <class 'dict'>
    did = dinfo[uid]
    # print(id(did), type(did), id(dinfo[uid]), type(dinfo[uid]))
    # 35494912 <class 'dict'> 35494912 <class 'dict'>
    for key in kwargs:
        # print(key, kwargs[key])
        # math 90
        # biology 80
        did[key] = kwargs[key]


result = parseFile(fpath)
# print(result)
# {1: {'name': 'name_1', 'math': '56'}, 2: {'name': 'name_2', 'math': '53'}, 3: {'name': 'name_3', 'math': '65'}, 4: {'name': 'name_4', 'math': '74'}, 5: {'name': 'name_5', 'math': '82'}, 6: {'name': 'name_6', 'math': '32'}, 7: {'name': 'name_7', 'math': '66'}, 8: {'name': 'name_8', 'math': '34'}, 9: {'name': 'name_9', 'math': '51'}, 10: {'name': 'name_10', 'math': '53'}, 11: {'name': 'name_11', 'math': '65'}, 12: {'name': 'name_12', 'math': '43'}, 13: {'name': 'name_13', 'math': '52'}, 14: {'name': 'name_14', 'math': '52'}, 15: {'name': 'name_15', 'math': '95'}, 16: {'name': 'name_16', 'math': '79'}, 17: {'name': 'name_17', 'math': '36'}, 18: {'name': 'name_18', 'math': '52'}, 19: {'name': 'name_19', 'math': '36'}, 20: {'name': 'name_20', 'math': '75'}, 21: {'name': 'name_21', 'math': '86'}, 22: {'name': 'name_22', 'math':'36'}, 23: {'name': 'name_23', 'math': '100'}, 24: {'name': 'name_24', 'math': '69'}, 25: {'name': 'name_25', 'math': '76'}, 26: {'name': 'name_26', 'math': '92'}, 27: {'name': 'name_27', 'math': '67'}, 28: {'name': 'name_28', 'math': '42'}, 29: {'name': 'name_29', 'math': '90'}, 30: {'name': 'name_30', 'math': '72'}, 31: {'name': 'name_31', 'math': '99'}, 32: {'name': 'name_32', 'math': '64'}, 33: {'name': 'name_33', 'math': '71'}, 34: {'name': 'name_34', 'math': '67'}, 35: {'name': 'name_35', 'math': '46'}, 36: {'name': 'name_36', 'math': '49'}, 37: {'name': 'name_37', 'math': '37'}, 38: {'name': 'name_38', 'math': '46'}, 39: {'name': 'name_39', 'math': '87'}, 40: {'name': 'name_40','math': '62'}}
results = searchByIds(result, 1, 5, 8, 10)
print(results)
# {1: '56', 5: '82', 8: '34', 10: '53'}

resultr = searchByRange(result, 1, 30, 70, cmps)
print(resultr)
# ['56', '53', '65', '32', '66', '34', '51', '53', '65', '43', '52', '52', '36', '52', '36', '36', '69', '67', '42']

update(result, 1, math=90, biology=80)
print(result)
# {1: {'name': 'name_1', 'math': 90, 'biology': 80}, 2: {'name': 'name_2', 'math': '53'}, 3: {'name': 'name_3', 'math': '65'}, 4: {'name': 'name_4', 'math': '74'}, 5: {'name': 'name_5', 'math': '82'}, 6: {'name': 'name_6', 'math': '32'}, 7: {'name': 'name_7', 'math': '66'}, 8: {'name': 'name_8', 'math': '34'}, 9: {'name': 'name_9', 'math': '51'}, 10: {'name': 'name_10', 'math': '53'}, 11: {'name': 'name_11', 'math': '65'}, 12: {'name': 'name_12', 'math': '43'}, 13: {'name': 'name_13', 'math': '52'}, 14: {'name': 'name_14', 'math': '52'}, 15: {'name': 'name_15', 'math': '95'}, 16: {'name': 'name_16', 'math': '79'}, 17: {'name': 'name_17', 'math': '36'}, 18: {'name': 'name_18', 'math': '52'}, 19: {'name': 'name_19', 'math': '36'}, 20: {'name': 'name_20', 'math': '75'}, 21: {'name': 'name_21', 'math': '86'}, 22: {'name': 'name_22', 'math': '36'}, 23: {'name': 'name_23', 'math': '100'}, 24: {'name': 'name_24', 'math': '69'}, 25: {'name': 'name_25', 'math': '76'}, 26: {'name': 'name_26', 'math': '92'}, 27: {'name': 'name_27', 'math': '67'}, 28: {'name': 'name_28', 'math': '42'}, 29: {'name': 'name_29', 'math': '90'}, 30: {'name': 'name_30', 'math': '72'}, 31: {'name': 'name_31', 'math': '99'}, 32: {'name': 'name_32', 'math': '64'}, 33: {'name': 'name_33', 'math': '71'}, 34: {'name': 'name_34', 'math': '67'}, 35: {'name': 'name_35', 'math': '46'}, 36: {'name': 'name_36', 'math': '49'}, 37: {'name': 'name_37', 'math': '37'}, 38: {'name': 'name_38', 'math': '46'}, 39: {'name': 'name_39', 'math': '87'}, 40: {'name': 'name_40', 'math': '62'}}
