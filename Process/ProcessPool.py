# coding:utf-8
from multiprocessing import Pool, active_children
from os import getpid
from time import sleep, time


def task(num):
    print('run task', num, getpid())
    sleep(0.1)
    return str(num)


if __name__ == "__main__":
    pool = Pool(processes=3)
    result = []
    print(active_children())
    # [<SpawnProcess(SpawnPoolWorker-1, started daemon)>, <SpawnProcess(SpawnPoolWorker-3, started daemon)>, <SpawnProcess(SpawnPoolWorker-2, started daemon)>]

    for i in range(10):
        print('--->', time())
        # pool.apply_async(func, (msg,))

        # print(type(pool.apply(task, (i,))))
        # <class 'str'>

        # print(pool.apply_async(task, (i,)))
        # <multiprocessing.pool.ApplyResult object at 0x029E4750>
        # print(type(pool.apply_async(task, (i,))))
        # <class 'multiprocessing.pool.ApplyResult'>

        result.append(pool.apply_async(task, (i,)))
        print('<---', time())
    pool.close()
    pool.join()

    for i in range(10):
        print(result[i].get())
'''
# pool.apply_async(func, (msg,))
[<SpawnProcess(SpawnPoolWorker-3, started daemon)>, <SpawnProcess(SpawnPoolWorker-2, started daemon)>, <SpawnProcess(SpawnPoolWorker-1, started daemon)>]
---> 1513090202.6627834
<--- 1513090202.6727834
---> 1513090202.6727834
<--- 1513090202.6727834
---> 1513090202.6727834
<--- 1513090202.6727834
---> 1513090202.6727834
<--- 1513090202.6727834
---> 1513090202.6727834
<--- 1513090202.6727834
---> 1513090202.6727834
<--- 1513090202.6727834
---> 1513090202.6727834
<--- 1513090202.6727834
---> 1513090202.6727834
<--- 1513090202.6727834
---> 1513090202.6727834
<--- 1513090202.6727834
---> 1513090202.6727834
<--- 1513090202.6727834
run task 0 4080
run task 1 1484
run task 2 4044
run task 3 1484
run task 4 4080
run task 5 4044
run task 6 1484
run task 7 4080
run task 8 4044
run task 9 1484
0
1
2
3
4
5
6
7
8
9
'''
'''
# pool.apply(func, (msg,))
[<SpawnProcess(SpawnPoolWorker-3, started daemon)>, <SpawnProcess(SpawnPoolWorker-1, started daemon)>, <SpawnProcess(SpawnPoolWorker-2, started daemon)>]
---> 1513090236.7678533
run task 0 6368
<--- 1513090236.9978535
---> 1513090236.9978535
run task 1 6804
<--- 1513090237.0978537
---> 1513090237.0978537
run task 2 6384
<--- 1513090237.1978538
---> 1513090237.1978538
run task 3 6368
<--- 1513090237.297854
---> 1513090237.297854
run task 4 6804
<--- 1513090237.397854
---> 1513090237.397854
run task 5 6384
<--- 1513090237.4978542
---> 1513090237.4978542
run task 6 6368
<--- 1513090237.5978541
---> 1513090237.5978541
run task 7 6804
<--- 1513090237.6978545
---> 1513090237.6978545
run task 8 6384
<--- 1513090237.7978547
---> 1513090237.7978547
run task 9 6368
<--- 1513090237.8978548
Traceback (most recent call last):
  File "D:/Temp/GitHub/Python/Thread/ThreadPool.py", line 29, in <module>
    print(result[i].get())
AttributeError: 'str' object has no attribute 'get'
'''