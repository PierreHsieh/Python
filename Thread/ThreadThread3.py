# coding:utf-8
from threading import Thread, Lock, Condition
from time import sleep

num = 0
lock = Lock()
con = Condition()


def producer():
    global num
    count = 100
    lock.acquire()
    con.acquire()
    num = 10
    while(count > 0):
        if num > 10:
            con.wait()
            lock.release()
        num += 1
        count -= 1
        print('in p:num=', num, count)
        # sleep(0.1)
    con.release()
    sleep(0.1)
    lock.release()


def consumer():
    global num
    count = 100
    sleep(0.1)
    while(count > 0):
        con.acquire()
        if num > 0:
            num -= 1
            print('in c:num=', num, count)
        if num <= 10:
            con.notify()
            # print('in c:num=', num, count)
        con.release()
        lock.acquire()
        count -= 1
        # sleep(0.1)


def startThread(func):
    t = Thread(target=func)
    t.start()
    return t


if __name__ == '__main__':
    print(num)
    t = startThread(consumer)
    producer()
    t.join()
    print(num)
'''
0
in p:num= 11 99
in c:num= 10 100
in p:num= 11 98
in c:num= 10 99
in p:num= 11 97
in c:num= 10 98
in p:num= 11 96
in c:num= 10 97
in p:num= 11 95
in c:num= 10 96
in p:num= 11 94
in c:num= 10 95
in p:num= 11 93
in c:num= 10 94
in p:num= 11 92
in c:num= 10 93
in p:num= 11 91
in c:num= 10 92
in p:num= 11 90
in c:num= 10 91
in p:num= 11 89
in c:num= 10 90
in p:num= 11 88
in c:num= 10 89
in p:num= 11 87
in c:num= 10 88
in p:num= 11 86
in c:num= 10 87
in p:num= 11 85
in c:num= 10 86
in p:num= 11 84
in c:num= 10 85
in p:num= 11 83
in c:num= 10 84
in p:num= 11 82
in c:num= 10 83
in p:num= 11 81
in c:num= 10 82
in p:num= 11 80
in c:num= 10 81
in p:num= 11 79
in c:num= 10 80
in p:num= 11 78
in c:num= 10 79
in p:num= 11 77
in c:num= 10 78
in p:num= 11 76
in c:num= 10 77
in p:num= 11 75
in c:num= 10 76
in p:num= 11 74
in c:num= 10 75
in p:num= 11 73
in c:num= 10 74
in p:num= 11 72
in c:num= 10 73
in p:num= 11 71
in c:num= 10 72
in p:num= 11 70
in c:num= 10 71
in p:num= 11 69
in c:num= 10 70
in p:num= 11 68
in c:num= 10 69
in p:num= 11 67
in c:num= 10 68
in p:num= 11 66
in c:num= 10 67
in p:num= 11 65
in c:num= 10 66
in p:num= 11 64
in c:num= 10 65
in p:num= 11 63
in c:num= 10 64
in p:num= 11 62
in c:num= 10 63
in p:num= 11 61
in c:num= 10 62
in p:num= 11 60
in c:num= 10 61
in p:num= 11 59
in c:num= 10 60
in p:num= 11 58
in c:num= 10 59
in p:num= 11 57
in c:num= 10 58
in p:num= 11 56
in c:num= 10 57
in p:num= 11 55
in c:num= 10 56
in p:num= 11 54
in c:num= 10 55
in p:num= 11 53
in c:num= 10 54
in p:num= 11 52
in c:num= 10 53
in p:num= 11 51
in c:num= 10 52
in p:num= 11 50
in c:num= 10 51
in p:num= 11 49
in c:num= 10 50
in p:num= 11 48
in c:num= 10 49
in p:num= 11 47
in c:num= 10 48
in p:num= 11 46
in c:num= 10 47
in p:num= 11 45
in c:num= 10 46
in p:num= 11 44
in c:num= 10 45
in p:num= 11 43
in c:num= 10 44
in p:num= 11 42
in c:num= 10 43
in p:num= 11 41
in c:num= 10 42
in p:num= 11 40
in c:num= 10 41
in p:num= 11 39
in c:num= 10 40
in p:num= 11 38
in c:num= 10 39
in p:num= 11 37
in c:num= 10 38
in p:num= 11 36
in c:num= 10 37
in p:num= 11 35
in c:num= 10 36
in p:num= 11 34
in c:num= 10 35
in p:num= 11 33
in c:num= 10 34
in p:num= 11 32
in c:num= 10 33
in p:num= 11 31
in c:num= 10 32
in p:num= 11 30
in c:num= 10 31
in p:num= 11 29
in c:num= 10 30
in p:num= 11 28
in c:num= 10 29
in p:num= 11 27
in c:num= 10 28
in p:num= 11 26
in c:num= 10 27
in p:num= 11 25
in c:num= 10 26
in p:num= 11 24
in c:num= 10 25
in p:num= 11 23
in c:num= 10 24
in p:num= 11 22
in c:num= 10 23
in p:num= 11 21
in c:num= 10 22
in p:num= 11 20
in c:num= 10 21
in p:num= 11 19
in c:num= 10 20
in p:num= 11 18
in c:num= 10 19
in p:num= 11 17
in c:num= 10 18
in p:num= 11 16
in c:num= 10 17
in p:num= 11 15
in c:num= 10 16
in p:num= 11 14
in c:num= 10 15
in p:num= 11 13
in c:num= 10 14
in p:num= 11 12
in c:num= 10 13
in p:num= 11 11
in c:num= 10 12
in p:num= 11 10
in c:num= 10 11
in p:num= 11 9
in c:num= 10 10
in p:num= 11 8
in c:num= 10 9
in p:num= 11 7
in c:num= 10 8
in p:num= 11 6
in c:num= 10 7
in p:num= 11 5
in c:num= 10 6
in p:num= 11 4
in c:num= 10 5
in p:num= 11 3
in c:num= 10 4
in p:num= 11 2
in c:num= 10 3
in p:num= 11 1
in c:num= 10 2
in p:num= 11 0
in c:num= 10 1
10

'''
