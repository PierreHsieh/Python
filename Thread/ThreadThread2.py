# coding:utf-8
from threading import Thread, active_count, enumerate
from time import sleep


def threadFunc():
    sleep(1)
    print('call thread_func')
    print(active_count())
    for t in enumerate():
        print(t)


def createThread():
    t = Thread(target=threadFunc)
    t.setName('T1')
    t.setDaemon(True)
    t.run()
    return t


if __name__ == '__main__':
    t = createThread()
    # t.join()
'''
call thread_func
1
<_MainThread(MainThread, started 7416)>
'''
