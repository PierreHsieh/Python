# coding:utf-8
from threading import Thread, active_count, enumerate
from time import sleep

'''
Threading Func
.Thread
.active_count
.enumerate
.Semaphore
.Lock
.Event
.Condition
.settrace()
.setporfile()

Threading.thread Func
.start()
.run()
.join()
.setDaemon()
.is_alive()
'''
def threadFunc():
    sleep(1)
    print('call thread_func')
    print(active_count())
    for t in enumerate():
        print('thread:', t)


def createThread():
    t = Thread(target=threadFunc)
    t.setName('T1')
    t.setDaemon(True)  # main thread del => del all sub thread
    # t.run()  # 2
    t.start()  # 1
    return t


if __name__ == '__main__':
    t = createThread()
    t.join()  # 2
'''
# 1
call thread_func
2
thread: <_MainThread(MainThread, started 3592)>
thread: <Thread(T1, started daemon 1604)>
'''
'''
# 2
call thread_func
1
thread: <_MainThread(MainThread, started 4136)>
'''