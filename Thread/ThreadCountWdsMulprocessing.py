# coding:utf-8
from multiprocessing import Process
from os import walk
from os.path import join
from time import time

path = r'.\file\fiction'


def countWordsByFile(fname):
    result = 0
    with open(fname) as f:
        for line in f:
            wds = line.strip().split()
            result += len(wds)
    # print(fname, result)
    return result


def countFiles(fpath):
    flist = []
    gen = walk(fpath)
    for tpath, dirs, files in gen:
        # print(tpath, dirs, files)
        for name in files:
            fname = join(tpath, name)
            flist.append(fname)
    return flist


def countWdsByFlist(flist):
    wds = 0
    for fname in flist:
        wds += countWordsByFile(fname)
    print(wds)


class ParseFileList(Process):
    def __init__(self, flist):
        self.flist = flist
        self.result = 0
        super(ParseFileList, self).__init__()

    def countWordsByFile(self, fname):
        result = 0
        with open(fname) as f:
            for line in f:
                wds = line.strip().split()
                result += len(wds)
        # print(fname, result)
        return result

    def countWdsByFlist(self):
        wds = 0
        for fname in self.flist:
            wds += countWordsByFile(fname)
        print('PFL', wds)
        # PFL 184648
        # PFL 639961

    def run(self):
        self.countWdsByFlist()


if __name__ == "__main__":
    s_time = time()
    flist = countFiles(path)
    snum = int(len(flist) / 2)
    # p = Process(target=countwdsbyflist, args=(flist[snum:],))
    p = ParseFileList(flist[snum:])
    p.start()
    mainP = ParseFileList(flist[:snum])
    mainP.run()
    # print(flist)
    # countWdsByFlist(flist[:snum])
    p.join()
    e_time = time()
    print(s_time, e_time, e_time - s_time)
    # 1512720522.1481838 1512720522.3527095 0.20452570915222168
