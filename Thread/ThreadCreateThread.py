# coding:utf-8
from threading import Thread
from time import sleep


def threadFunc():
    print('call thread_func')
    # while(True):
    #    pass
    sleep(10)


def createThread():
    t = Thread(target=threadFunc)
    t.start()
    return t


if __name__ == '__main__':
    t = createThread()
    threadFunc()
    t.join()
# call thread_func
# call thread_func
