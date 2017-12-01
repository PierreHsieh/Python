# coding=utf-8
queue = []


def Qinit():
    queue.clear()


def Qput(msg):
    queue.append(msg)


def Qpop():
    if len(queue):
        val = queue.pop(0)
        return val


def Qshow():
    for val in queue:
        print(val)


while True:
    val = input('Command：')
    if val == 'i':
        msg = input('Input Msg:')
        Qput(msg)
    elif val == 'p':
        msg = Qpop()
        print('PopMsg:', msg)
    elif val == 's':
        Qshow()
    elif val == 'c':
        Qinit()
    elif val == 'q':
        break
    else:
        print("i -> insert msg\n\
p -> pop msg\n\
s -> show queue\n\
c -> clear queue\n\
q -> exit")
