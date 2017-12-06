# coding:utf-8
from random import randint

fpath = r'.\file\math_report.txt'
fpass = r'.\file\math_report_pass.txt'


def createReport(fname, num):
    f = open(fname, 'w')
    for i in range(1, num+1):
        info = '%d name_%d: %d\n' % (i, i, randint(30, 100))
        f.write(info)
    f.close()


def filterReport(fname, fpass):
    fr = open(fname)
    fw = open(fpass, 'w')
    for line in fr:
        linfo = line.strip().split(':')
        print(linfo, type(linfo))
        # ['1 name_1', ' 60'] <class 'list'>
        score = int(linfo[-1].strip())
        if score >= 60:
            fw.write(line)
    fr.close()
    fw.close()


createReport(fpath, 40)
filterReport(fpath, fpass)
