# coding:utf-8

from multiprocessing import Array, Value, Process, Lock

val = Value('i', 0)
lock = Lock()


def task(val, lock):
    num = 50
    while num > 0:
        lock.acquire()
        if val.value > 0:
            print('-1 in task val:', val.value)
            val.value -= 1
            print('-2 in task val:', val.value)

        lock.release()
        num -= 1


def product(val, lock):
    num = 50
    while num > 0:
        lock.acquire()
        if val.value < 0:
            print(' in product val:', val.value)
        val.value += 1
        print ('+2 in product val:', val.value)
        lock.release()
        num -= 1


if __name__ == '__main__':
    p = Process(target=product, args=(val, lock))
    p.start()
    p1 = Process(target=task, args=(val, lock))
    p1.start()
    task(val, lock)
    p.join()
    p1.join()
'''
+2 in product val: 1
-1 in task val: 1
-2 in task val: 0
+2 in product val: 1
-1 in task val: 1
-2 in task val: 0
+2 in product val: 1
-1 in task val: 1
-2 in task val: 0
+2 in product val: 1
-1 in task val: 1
-2 in task val: 0
+2 in product val: 1
-1 in task val: 1
-2 in task val: 0
+2 in product val: 1
-1 in task val: 1
-2 in task val: 0
+2 in product val: 1
+2 in product val: 2
+2 in product val: 3
+2 in product val: 4
+2 in product val: 5
+2 in product val: 6
+2 in product val: 7
+2 in product val: 8
+2 in product val: 9
+2 in product val: 10
+2 in product val: 11
+2 in product val: 12
+2 in product val: 13
+2 in product val: 14
+2 in product val: 15
+2 in product val: 16
+2 in product val: 17
+2 in product val: 18
+2 in product val: 19
+2 in product val: 20
+2 in product val: 21
+2 in product val: 22
+2 in product val: 23
+2 in product val: 24
+2 in product val: 25
+2 in product val: 26
+2 in product val: 27
+2 in product val: 28
+2 in product val: 29
+2 in product val: 30
+2 in product val: 31
+2 in product val: 32
+2 in product val: 33
+2 in product val: 34
+2 in product val: 35
+2 in product val: 36
+2 in product val: 37
+2 in product val: 38
+2 in product val: 39
+2 in product val: 40
+2 in product val: 41
+2 in product val: 42
+2 in product val: 43
+2 in product val: 44

'''
