# coding:utf-8
fpath = r'.\file\math.txt'


def parseFile(fname):
    result = {}
    f = open(fname)
    for line in f:
        tmp = [val.strip(':') for val in line.strip().split()]
        # print(tmp, type(tmp))
        # ['1', 'name_1', '90'] <class 'list'>
        d = dict(name=tmp[1], score=tmp[2])
        # print(d, type(d))
        # {'name': 'name_1', 'score': '90'} <class 'dict'>
        result[int(tmp[0])] = d
    # print(result)
    # {1: {'name': 'name_1', 'score': '90'}, 2: {'name': 'name_2', 'score': '75'}, 3: {'name': 'name_3', 'score': '35'}, 4: {'name': 'name_4', 'score': '66'}, 5: {'name': 'name_5', 'score': '41'}, 6: {'name': 'name_6', 'score': '77'}, 7: {'name': 'name_7', 'score': '97'}, 8: {'name': 'name_8', 'score': '72'}, 9: {'name': 'name_9', 'score': '60'}, 10: {'name': 'name_10', 'score': '39'}}
    f.close()
    return result


def searchByIds(dinfo, id, *arg):
    key = 'score'
    keys = list(arg)

    # print(arg, type(arg))
    # (5, 8, 10) <class 'tuple'>
    # print(list(arg), type(list(arg)))
    # [5, 8, 10] <class 'list'>

    keys.insert(0, id)

    scores = []
    for i in keys:
        scores.append((dinfo[i][key]))

    # print(list(keys), type(keys))
    # [1, 5, 8, 10] <class 'list'>
    # print(scores, type(scores))
    # ['90', '41', '72', '39'] <class 'list'>

    # print(zip(keys, scores), type(zip(keys, scores)))
    # <zip object at 0x0216E4E0> <class 'zip'>
    # print(list(zip(keys, scores)), type(list(zip(keys, scores))))
    # [(1, '90'), (5, '41'), (8, '72'), (10, '39')] <class 'list'>
    # print(dict(list(zip(keys, scores))), type(dict(list(zip(keys, scores)))))
    # {1: '90', 5: '41', 8: '72', 10: '39'} <class 'dict'>

    return (dict(list(zip(keys, scores))))


result = parseFile(fpath)
# print(result)
# {1: {'name': 'name_1', 'score': '90'}, 2: {'name': 'name_2', 'score': '75'}, 3: {'name': 'name_3', 'score': '35'}, 4: {'name': 'name_4', 'score': '66'}, 5: {'name': 'name_5', 'score': '41'}, 6: {'name': 'name_6', 'score': '77'}, 7: {'name': 'name_7', 'score': '97'}, 8: {'name': 'name_8', 'score': '72'}, 9: {'name': 'name_9', 'score': '60'}, 10: {'name': 'name_10', 'score': '39'}}
results = searchByIds(result, 1, 5, 8, 10)
print(results)
# {1: '90', 5: '41', 8: '72', 10: '39'}
