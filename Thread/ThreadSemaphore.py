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
    for i in range(20):
        p = Process(target=eat, args=(se, ar, lock, i))
        p.start()

'''
3 ar_index 0
1 ar_index 1
0 ar_index 2
2 ar_index 3
11 ar_index 4
11 leave 4
12 ar_index 4
12 leave 4
4 ar_index 4
1 leave 1
15 ar_index 1
4 leave 4
16 ar_index 4
0 leave 2
3 leave 0
19 ar_index 0
6 ar_index 2
2 leave 3
8 ar_index 3
19 leave 0
5 ar_index 0
16 leave 4
13 ar_index 4
15 leave 1
7 ar_index 1
5 leave 0
9 ar_index 0
6 leave 2
17 ar_index 2
7 leave 1
10 ar_index 1
10 leave 1
8 leave 3
18 ar_index 1
14 ar_index 3
18 leave 1
13 leave 4
9 leave 0
14 leave 3
17 leave 2
'''
