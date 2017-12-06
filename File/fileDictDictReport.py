# coding:utf-8
from random import randint
from pygal import Bar

fmath = r'.\file\math.txt'
fbiology = r'.\file\biology.txt'
fmegre = r'.\file\megre.txt'
fsvg = r'.\file\scoreSpread.svg'


def createReport(fname, num):
    f = open(fname, 'w')
    for i in range(1, num+1):
        info = '%d name_%d: %d\n' % (i, i, randint(30, 100))
        f.write(info)
    f.close()


def parseReport(fname, obj, dreport):
    f = open(fname)
    for line in f:
        '''
        for val in line.strip().split():
            print(val)
            # 1
            # name_1:
            # 30
        '''
        # print(line, type(line))
        # 1 name_1: 30\n <class 'str'>
        num, name, score = [val.strip(' :') for val in line.strip().split()]
        # print(num, name, score, type(num), type(name), type(score))
        # 1 name_1 30 <class 'str'> <class 'str'> <class 'str'>
        # print(type(dreport))
        # <class 'dict'>
        if num not in dreport:
            dreport[num] = {}
            # print(dreport, type(dreport), type(dreport[num]))
            # {'1': {}} <class 'dict'> <class 'dict'>
        dreport[num].setdefault('name', name)
        dreport[num].setdefault(obj, score)
        # break


def megreReport(fname, dreport):
    f = open(fname, 'w')
    for val in range(1, 41):
        key = str(val)
        # print(key)
        # 1 ~ 40
        subd = dreport[key]
        subkeys = list(subd.keys())
        # print(subd, type(subd), subkeys, type(subkeys))
        # {'name': 'name_1', 'math': '67', 'biology': '86'} <class 'dict'> ['name', 'math', 'biology'] <class 'list'>
        subkeys.remove('name')
        winfo = '%s %s: ' % (key, subd['name'])
        # print(winfo, type(winfo))
        # 1 name_1:  <class 'str'>
        lscore = [subd[k] for k in subkeys]
        winfo += ' '.join(lscore)
        # print(winfo, type(winfo))
        # 1 name_1: 54 51 <class 'str'>
        f.write(winfo + '\n')
    f.close()


def searchById(id, dreport):
    subd = dreport[str(id)]
    subkeys = list(subd.keys())
    subkeys.remove('name')
    result = [int(subd[k]) for k in subkeys]
    # print([[k, subd[k]] for k in subkeys])
    # [['math', '94'], ['biology', '35']]
    return result


def showScore(obj, dreport):
    lscore = [int(dreport[k][obj]) for k in dreport.keys()]
    print(lscore, type(lscore))
    # [97, 98, 98, 68, 79, 79, 47, 86, 51, 64] <class 'list'>

    lall = [sum(searchById(k, dreport)) for k in dreport.keys()]
    print(lall, type(lall))
    # [166, 139, 188, 108, 111, 157, 116, 185, 132, 121] <class 'list'>

    print(sum(lscore)/len(lscore))
    # 64.65
    print('%s max:%d' % (obj, max(lscore)))
    # math max:98
    print('%s min:%d' % (obj, min(lscore)))
    # math min:30
    print('%s max:%d' % ('all', max(lall)))
    # all max:170
    print('%s min:%d' % ('all', min(lall)))
    # all min:72


def setVal(ds, val):
    key = '0-59'
    if val >= 60:
        ten = val - val % 10
        if val == 100:
            ten = 90
        key = '%d-%d' % (ten, ten + 9 + (ten / 90))
        # print(ten, key)
        # 90 90-100
        # 60 60-69
        # 60 60-69
        # 80 80-89
    ds[key] += 1


def scoreSpread(dreport, obj):
    keys = ['0-59']
    [keys.append('%d-%d' % (val, val + 9 + (val / 90))) for val in range(60, 100, 10)]
    # print(keys, type(keys))
    # ['0-59', '60-69', '70-79', '80-89', '90-100'] <class 'list'>

    dspread = dict.fromkeys(keys, 0)
    # print(dspread, type(dspread))
    # {'0-59': 0, '60-69': 0, '70-79': 0, '80-89': 0, '90-100': 0} <class 'dict'>

    lscore = [int(dreport[k][obj]) for k in dreport.keys()]
    # print(lscore, type(lscore))
    # [85, 96, 36, 44, 81, 61, 93, 57, 45, 97] <class 'list'>

    [setVal(dspread, val) for val in lscore]
    # print(dspread, type(dspread))
    # {'0-59': 3, '60-69': 2, '70-79': 3, '80-89': 1, '90-100': 1} <class 'dict'>

    return dspread


def genSvg(fpath, mathd, biologyd):
    keys = ['0-59']
    [keys.append('%d-%d' % (val, val + 9 + (val / 90))) for val in range(60, 100, 10)]
    # print(keys, type(keys))
    # ['0-59', '60-69', '70-79', '80-89', '90-100'] <class 'list'>

    line_chart = Bar()
    # print(line_chart, type(line_chart))
    # <pygal.graph.bar.Bar object at 0x02F24330> <class 'pygal.graph.bar.Bar'>

    line_chart.title = 'Score Spread'
    # print(line_chart.title, type(line_chart.title))
    # Score Spread <class 'str'>

    line_chart.x_labels = keys
    # print(line_chart.x_labels, type(line_chart.x_labels))
    # ['0-59', '60-69', '70-79', '80-89', '90-100'] <class 'list'>

    line_chart.add('math', mathd.values())
    line_chart.add('biology', biologyd.values())
    # print(mathd, type(mathd))
    # {'0-59': 3, '60-69': 2, '70-79': 3, '80-89': 0, '90-100': 2} <class 'dict'>
    # print(mathd.values(), type(mathd.values()))
    # dict_values([3, 2, 3, 0, 2]) <class 'dict_values'>

    line_chart.render_to_file(fpath)


s_num = 40
reportlist = {}
createReport(fmath, s_num)
createReport(fbiology, s_num)

parseReport(fmath, 'math', reportlist)
parseReport(fbiology, 'biology', reportlist)
# print(reportlist)
# {'1': {'name': 'name_1', 'math': '56', 'biology': '98'}, '2': {'name': 'name_2', 'math': '82', 'biology': '34'}, '3': ... '10': {'name': 'name_10', 'math': '59', 'biology': '43'}}

megreReport(fmegre, reportlist)
# print(reportlist)

result = searchById(1, reportlist)
print(result)
# [91, 50]

showScore('math', reportlist)
showScore('biology', reportlist)

mathd = scoreSpread(reportlist, 'math')
#biologyd = scoreSpread(reportlist, 'biology')
#genSvg(fsvg, mathd, biologyd)
