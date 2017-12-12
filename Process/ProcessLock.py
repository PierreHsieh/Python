# coding:utf-8
from multiprocessing import Semaphore, Array, Lock, Process
from random import uniform
from time import sleep

se = Semaphore(5)
ar = Array('i', 5)
lock = Lock()


def eat(se, ar, lock, idnum):
    se.acquire()

    lock.acquire()
    for index, val in enumerate(ar):
        if val == 0:
            ar[index] = 1
            break
    lock.release()

    print(idnum, 'ar_index', index)
    sleep(uniform(0, 1))

    lock.acquire()
    ar[index] = 0
    print(idnum, 'leave', index)
    lock.release()

    se.release()


if __name__ == '__main__':
    for idnum in range(20):
        p = Process(target=eat, args=(se, ar, lock, idnum))
        p.start()

'''
2 ar_index 0
3 ar_index 1
4 ar_index 2
1 ar_index 3
0 ar_index 4
0 leave 4
7 ar_index 4
2 leave 0
8 ar_index 0
1 leave 3
6 ar_index 3
4 leave 2
5 ar_index 2
3 leave 1
9 ar_index 1
6 leave 3
13 ar_index 3
8 leave 0
12 ar_index 0
5 leave 2
14 ar_index 2
7 leave 4
11 ar_index 4
11 leave 4
16 ar_index 4
9 leave 1
10 ar_index 1
14 leave 2
15 ar_index 2
12 leave 0
17 ar_index 0
15 leave 2
18 ar_index 2
18 leave 2
19 ar_index 2
17 leave 0
13 leave 3
10 leave 1
16 leave 4
19 leave 2
'''
