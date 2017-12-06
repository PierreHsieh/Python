# coding=utf-8
finpath = r'.\file\in.txt'
foutpath = r'.\file\out.txt'


def filterFile(fname, fs):
    f = open(fname)
    fsave = open(fs, 'w')
    mark = 0
    flag = ''
    for line in f:
        if '#' in line:
            if line.strip().startswith('#'):
                print(line.find('#'), ":", line.strip().startswith('#'), type(line))
                continue
            print(line.find('#'), ":", line[:line.find('#')])			
            fsave.write(line[:line.find('#')] + '\n')
            continue
        print(line.strip())
        fsave.write(line)
    f.close()
    fsave.close()


filterFile(finpath, foutpath)