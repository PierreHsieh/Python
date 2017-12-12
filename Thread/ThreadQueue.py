# coding:utf-8

from multiprocessing import Queue, Process
from time import sleep


def task(qu):
    print('task start get msg:')
    msg = qu.get()
    print('task get msg:', msg)


if __name__ == '__main__':
    q = Queue(10)
    p = Process(target=task, args=(q, ))
    p.start()
    sleep(1)
    print('main P put msg')
    q.put(1)
    p.join()
'''    
    q.put()
    q.get()
    q.put_nowait()
    q.get_nowait()
    q.empty()
    q.full()
    q.qsize()
'''

# task start get msg:
# main P put msg
# task get msg: 1
