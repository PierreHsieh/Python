# coding:utf-8
from multiprocessing import Pool, active_children
from os import getpid
from time import sleep


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
        result.append(pool.apply_async(task, (i,)))
    pool.close()
    pool.join()
    for i in range(10):
        print(result[i].get())
'''
run task 0 6252
run task 1 5308
run task 2 6212
run task 3 6252
run task 4 5308
run task 5 6212
run task 6 6252
run task 7 5308
run task 8 6212
run task 9 6252
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
