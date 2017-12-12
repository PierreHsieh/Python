# coding:utf-8
from os import walk
from os.path import join
from time import time

path = r'.\file\fiction'


def countWordsByFile(fname):
    result = 0
    with open(fname) as f:
        for line in f:
            wds = line.strip().split()
            result += len(wds)
    print(fname, result)
    # .\file\fiction\a b c's of science.txt 3000
    # .\file\fiction\a christmas carol.txt 29117
    # .\file\fiction\a tale of two cities.txt 140429
    # .\file\fiction\Aesop's Fables.txt 12102
    # .\file\fiction\David Copperfield.txt 261269
    # .\file\fiction\Jane Eyre.txt 189996
    # .\file\fiction\Oliver Twist.txt 162437
    # .\file\fiction\Romeo and Juliet.txt 26259
    return result


def countWords(fpath):
    result = 0
    gen = walk(fpath)
    for tpath, dirs, files in gen:
        print(tpath, ':', dirs, ':', files)
        # .\file\fiction : [] : ["a b c's of science.txt", 'a christmas carol.txt', 'a tale of two cities.txt', "Aesop's Fables.txt", 'David Copperfield.txt', 'Jane Eyre.txt', 'Oliver Twist.txt', 'Romeo and Juliet.txt']
        for name in files:
            fname = join(tpath, name)
            # print(fname)
            # .\file\fiction\a b c's of science.txt
            result += countWordsByFile(fname)
    print(result)
    # 824609
    return result


if __name__ == "__main__":
    s_time = time()
    countWords(path)
    e_time = time()
    print(s_time, e_time, e_time - s_time)
'''
1512719981.9660892 1512719982.114608 0.14851880073547363
'''
