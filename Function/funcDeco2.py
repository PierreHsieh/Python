# coding:utf-8
from time import strftime


def LogInit(tag):
    print('call loginit', tag)
    def Log(func):
        print('call log', func, type(func))
        def LogOut(msg):
            times = strftime('%Y-%m-%d:%H-%M-%S')
            msg = tag + ':' + times + ',' + msg
            func(msg)
        return LogOut
    return Log


# @LogInfo('Debug') => LogInfo('Debug'): return Log => @Log
# logd=log(logd)
@LogInit('Debug')
def Logd(msg):
    print('%s' % msg)


@LogInit('Info')
def LogI(msg):
    print('%s' % msg)


@LogInit('Error')
def LogE(msg):
    print('%s' % msg)


Logd('Test')
Logd('Test')
LogI('Test')

'''
call loginit Debug
call log <function Logd at 0x021F7468> <class 'function'>
call loginit Info
call log <function LogI at 0x021F73D8> <class 'function'>
call loginit Error
call log <function LogE at 0x021F7348> <class 'function'>
Debug:2017-12-08:11-08-12,Test
Debug:2017-12-08:11-08-12,Test
Info:2017-12-08:11-08-12,Test
'''
