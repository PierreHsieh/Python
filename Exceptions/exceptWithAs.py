# coding:utf-8

class TestWith(object):

    def __enter__(self):
        print('call enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('call exit')

    def test(self):
        print('this is test')


with TestWith() as t:
    t.test()
# call enter
# this is test
# call exit

def test(fname):
    try:
        mnames = []
        with open(fname, encoding='utf8') as f: # f = open(fname, encoding='utf8'), __enter__
            for line in f:
                result = line.split()
                mnames.append(result[0])
        #f.close()
        return mnames
    except:
        print('catch an exception')
        return mnames
    finally:
        print('f state:', f.closed)


fpath = r'.\file\moviePlay.txt'
print(test(fpath))
# catch an exception
# f state: True
# []
'''
f state: True
['尋夢環遊記', '至暗時刻', '綠地黃花', '日常對話', '方法派', '火車司機日記', '奪金四賤客', '真白之戀', '川流之島', '泥土之界', '王牌特工2', '英倫對決', '光', '精靈寶可夢', '小丑回魂', '我能說', '晝顏', '忌日快樂']
'''