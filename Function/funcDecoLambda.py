# coding:utf-8


def cmpByscore(info):
    return float(info[1])


def cmpByLens(info):
    return int(info[2])


def cmpByCom(info):
    return int(info[3])


def parseFile(func):
    print('call parseFile', func, type(func))
    # call parseFile <function sortBysocre at 0x01E974B0> <class 'function'>
    # call parseFile <function sortByLens at 0x01E97420> <class 'function'>
    # call parseFile <function sortByCom at 0x01E97390> <class 'function'>
    def sorefunc(fname):
        f = open(fname, encoding='utf8')
        minfo = list(map(lambda line: line.strip().split(), f.readlines()))
        # print(minfo, type(minfo))
        # [['尋夢環遊記', '9.1', '105', '196098'], ['至暗時刻', '8.6', '125', '26270'], ['綠地黃花', '8.2', '103', '578'], ['日常對話', '8.1', '88', '1532'], ['方法派', '6.8', '82', '5844'], ['火車司機日記', '7.7', '85', '401'], ['奪金四賤客', '7.0', '96', '2293'], ['真白之戀', '7.5', '97', '345'], ['川流之島', '7.1', '98', '507'], ['泥土之界', '7.2', '134', '204'], ['王牌特工2', '7.1', '141', '132995'], ['英倫對決', '7.2', '113', '70422'], ['光', '6.8', '101', '424'], ['精靈寶可夢', '9.9', '99', '36'], ['小丑回魂', '7.4', '135', '38377'], ['我能說', '8.8', '119', '12825'], ['晝顏', '6.5', '125', '3813'], ['忌日快樂', '7.3', '96', '23408']] <class 'list'>
        func(minfo)
        f.close()
    return sorefunc


# sortBysocre = parseFile(sortBysocre)
@parseFile
def sortBysocre(minfo):
    minfo.sort(key=cmpByscore, reverse=True)
    print(minfo)


# sortByLens = parseFile(sortByLens)
@parseFile
def sortByLens(minfo):
    minfo.sort(key=cmpByLens, reverse=True)
    print(minfo)


# sortByCom = parseFile(sortByCom)
@parseFile
def sortByCom(minfo):
    minfo.sort(key=cmpByCom, reverse=True)
    print(minfo)


fpath = r'.\file\moviePlay.txt'
sortBysocre(fpath)
sortByLens(fpath)
sortByCom(fpath)
