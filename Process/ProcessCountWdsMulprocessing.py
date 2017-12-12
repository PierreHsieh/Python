# coding:utf-8
from multiprocessing import Queue, Process
from os import walk
from os.path import join
from time import time

path = r'.\file\fiction'


def countFiles(fpath):
    flist = []
    gen = walk(fpath)
    for tpath, dirs, files in gen:
        # print(tpath, dirs, files)
        for name in files:
            fname = join(tpath, name)
            flist.append(fname)
    return flist


class ParseFileList(Process):
    def __init__(self, flist, queue):
        self.flist = flist
        self.result = 0
        self.q = queue
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
            wds += self.countWordsByFile(fname)
        print('PFL', wds)
        self.result = wds
        self.q.put(wds)
        # PFL 184648
        # PFL 639961

    def run(self):
        self.countWdsByFlist()


if __name__ == "__main__":
    q = Queue(10)
    s_time = time()
    flist = countFiles(path)
    snum = int(len(flist) / 2)
    # p = Process(target=countwdsbyflist, args=(flist[snum:],))
    # print((flist[snum:],))
    # (['.\\file\\fiction\\David Copperfield.txt', '.\\file\\fiction\\Jane Eyre.txt', '.\\file\\fiction\\Oliver Twist.txt', '.\\file\\fiction\\Romeo and Juliet.txt'],)

    p = ParseFileList(flist[snum:], q)
    p.start()
    mainP = ParseFileList(flist[:snum], q)
    mainP.run()
    # print(flist)
    # countWdsByFlist(flist[:snum])
    p.join()
    result = 0
    for i in range(q.qsize()):
        tmp = q.get()
        print('sresult =', tmp)
        result += tmp
    e_time = time()
    print('result :', result)
    # sresult = 184648
    # sresult = 639961
    # result : 824609
    print(s_time, e_time, e_time - s_time)
    # 1512720522.1481838 1512720522.3527095 0.20452570915222168
