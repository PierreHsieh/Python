# coding:utf-8


def test(fname):
    try:
        mnames = []
        #f = open(fname)
        f = open(fname, encoding='utf8')
        for line in f:
            result = line.split()
            print(float(result[1]))
            mnames.append(result[0])
        return mnames
    except:
        print('catch an exception')
        return mnames
    finally:
        f.close()
        print('do finally')
        return []


fpath = r'.\file\moviePlay.txt'
print(test(fpath))
# === except ===
# catch an exception
# do finally
# []

'''
9.1
8.6
8.2
8.1
6.8
7.7
7.0
7.5
7.1
7.2
7.1
7.2
6.8
9.9
7.4
8.8
6.5
7.3
do finally
[]
'''
