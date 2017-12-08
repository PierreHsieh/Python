# coding:utf-8

from multiprocessing import Queue, Process
from time import sleep


def task(qu):
    print('start get msg:')
    msg = qu.get()
    print('get msg:', msg)


if __name__ == '__main__':
    q = Queue(10)
    p = Process(target=task, args=(q, ))
    p.start()
    sleep(1)
    print('P put msg')
    q.put(1)
    p.join()

# start get msg:
# P put msg
# get msg: 1
