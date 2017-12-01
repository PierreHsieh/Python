# coding:utf-8


def inserVal(lmegre, val):
    for index, v in enumerate(lmegre):
        if val <= v:
            lmegre.insert(index, val)
            return
    lmegre.append(val)


def insertList(lmegre, listmn):
    for val in listmn:
        if not lmegre:
            lmegre.append(val)
        else:
            inserVal(lmegre, val)
    print(lmegre)


def listMegre(lm, ln):
    lmegre = []
    insertList(lmegre, lm)
    insertList(lmegre, ln)


listm = [4, 3, 5, 6, 2, 2, 3, 1]
listn = [0, 5, 8, 7, 10, 9]
listMegre(listm, listn)
