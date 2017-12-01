# coding:utf-8


def listin(list1, list2):
    inlist = []
    for val in list1:
        if val in list2:
            inlist.append(val)
            # print(inlist)
    print(inlist)
    return inlist


def bestwork(skill, worklist):
    result = []
    for work in worklist:
        result.append(listin(skill, work))
    return result


ln = ['python', 'Qt', 'git', 'linux', 'c']
lm = [['python', 'django', 'hadoop', 'sql', 'spark', 'scala', 'Qt'],
      ['python', 'django', 'git', 'linux', 'sql', 'web', 'c']]
result = bestwork(ln, lm)
print(result)
