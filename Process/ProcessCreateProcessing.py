# coding:utf-8
from os import getpid, getppid
from time import sleep
# from multiprocessing import freeze_support, Process, cpu_count
import multiprocessing


'''
from multiprocessing import
Process()
cpu_count()
current_process()
Pipe()
Queue()
Lock()
Semaphore()
'''
'''
from multiprocessing import Process
.start()
.run()
.exitcode
.terminate()
.join()
p.ident
'''
value = 100
def task():
    global value;
    print('in task value:', value)
    value = 101
    print('in task value:', value)
    print('task getpid:', getpid(), 'getppdi:', getppid())
    print('call in task')
    sleep(1)
    print('task exit!')


if __name__ == '__main__':
    print('cpu count:', multiprocessing.cpu_count())
    print('current process:', multiprocessing.current_process())
    multiprocessing.freeze_support()
    p = multiprocessing.Process(target=task)
    print('main getpid:', getpid())
    p.start()
    print('ident:', p.ident)
    print('exitcode:', p.exitcode)
    # p.terminate()
    # p.run()
    p.join()
    print('exitcode:', p.exitcode)
    print('in main value:', value)
    print('main Process exit!!')
'''
cpu count: 12
current process: <_MainProcess(MainProcess, started)>
main getpid: 6888
ident: 2916
exitcode: None
in task value: 100
in task value: 101
task getpid: 2916 getppdi: 6888
call in task
task exit!
exitcode: 0
in main value: 100
main Process exit!!
'''
