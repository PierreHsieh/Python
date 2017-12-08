# coding:utf-8
from os import getpid, getppid
from multiprocessing import freeze_support, Process
from time import sleep


def task():
    print(getpid(), getppid())
    print('call in task')
    sleep(1)
    print('task exit!')


if __name__ == '__main__':
    freeze_support()
    p = Process(target=task)
    print('main pid:', getpid())
    p.start()
    p.join()
    print('main Process exit!!')
'''
main pid: 4252
5416 4252
call in task
task exit!
main Process exit!!
'''
