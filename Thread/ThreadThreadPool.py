from threading import Thread
from queue import Queue


class threadPool(object):
    def __init__(self, num=5):
        self.qtask = Queue()
        self.qresult = Queue()
        self.tnum = num
        self.tlist = []

    def task(self):
        while True:
            try:
                func, args, kwargs = self.qtask.get(timeout=1)
                result = func(*args, **kwargs)
                self.qresult.put(result)
            except:
                print('no task in poll')
                break

    def start(self):
        for i in range(self.tnum):
            t = Thread(target=self.task)
            self.tlist.append(t)
            t.start()

    def addTask(self, func, *args, **kwargs):
        self.qtask.put((func, args, kwargs))

    def join(self):
        for t in self.tlist:
            t.join()

    def getResult(self):
        rlist = []
        for i in range(self.qresult.qsize()):
            r = self.qresult.get()
            rlist.append(r)
        return rlist


def testfunc(num, **kwargs):
    print('call test func', num, kwargs)
    return str(num)


if __name__ == '__main__':
    tpool = threadPool(4)
    for i in range(40):
        tpool.addTask(testfunc, i)
    tpool.start()
    tpool.join()
    rs = tpool.getResult()
    for r in rs:
        print(r)
'''
call test func 0 {}
call test func 1 {}
call test func 2 {}
call test func 3 {}
call test func 4 {}
call test func 5 {}
call test func 7 {}
call test func 8 {}
call test func 9 {}
call test func 10 {}
call test func 11 {}
call test func 12 {}
call test func 13 {}
call test func 6 {}
call test func 16 {}
call test func 18 {}
call test func 17 {}
call test func 14 {}
call test func 15 {}
call test func 20 {}
call test func 21 {}
call test func 23 {}
call test func 24 {}
call test func 22 {}
call test func 19 {}
call test func 26 {}
call test func 27 {}
call test func 25 {}
call test func 29 {}
call test func 30 {}
call test func 28 {}
call test func 32 {}
call test func 33 {}
call test func 31 {}
call test func 35 {}
call test func 36 {}
call test func 34 {}
call test func 38 {}
call test func 39 {}
call test func 37 {}
no task in poll
no task in poll
no task in poll
no task in poll
0
1
2
3
4
5
7
8
9
10
11
12
13
6
16
18
17
14
20
21
23
24
22
19
15
26
27
29
30
28
25
32
33
35
36
34
31
38
37
39
'''
