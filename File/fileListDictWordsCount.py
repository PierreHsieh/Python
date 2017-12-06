# coding:utf-8
fpath = r'.\file\song.txt'


def wordCount(fname):
    f = open(fname)
    dtmp = {}
    for line in f:
        words = [word for word in line.strip().split(' ') if word.strip()]
        # "There's    a    hero\n"
        # print(line.strip())
        # "There's    a    hero"
        # print(line.split(' '))
        # ["There's", '', '', '', 'a', '', '', '', 'hero\n']
        # print(words)
        # ["There's", 'a', 'hero']
        # print(len(words))
        # 3
        for word in words:
            if word in dtmp:
                dtmp[word] += 1
            else:
                dtmp[word] = 1
    f.close()
    return dtmp


def wordCmp(d):
    return list(d.values())[0]
    # ld[0] ~ ld[n]


def wordSort(dwords):
    '''
    # --- big dict => tuple => list=> small dict ---
    for item in dwords.items():
        print(item, type(item))
        # ("There's", 2) <class 'tuple'>
        print([item], type([item]))
        # [("There's", 2)] <class 'list'>
        print(dict([item]), type(dict([item])))
        # {"There's": 2} <class 'dict'>
        # ---   ---
        ld = [dict([item])]
        print(ld, type(ld))
        # [{"There's": 2}] <class 'list'>
        break
    '''
    ld = [dict([item]) for item in dwords.items()]
    # print(type(ld))
    # <class 'list'>
    # pint(ld)
    # [{"There's": 2}, {'a': 5}, {'hero': 3}, {'If': 2}, {'you': 14}, {'look': 1}, {'inside': 2}, {'your': 3}, {'heart': 1}, {'You': 2}, {"don't": 2}, {'have': 1}, {'to': 4}, {'be': 3}, {'afraid': 1}, {'of': 1}, {'what': 1}, {'are': 2}, {'an': 1}, {'answer': 1}, {'reach': 1}, {'into': 1}, {'soul': 1}, {'And': 6}, {'the': 6}, {'sorrow': 1}, {'that': 1}, {'know': 2}, {'will': 3}, {'melt': 1}, {'away': 2}, {'then': 1}, {'comes': 1}, {'alone': 2}, {'With': 1}, {'strength': 1}, {'carry': 1}, {'on': 1}, {'cast': 1}, {'fears': 1}, {'aside': 1}, {'can': 2}, {'survive': 1}, {'So': 1}, {'when': 1}, {'feel': 1}, {'like': 1}, {'hope': 1}, {'is': 1}, {'gone': 1}, {'Look': 1}, {'and': 1}, {'strong': 1}, {"you'll": 2}, {'finally': 1}, {'see': 1}, {'truth': 1},{'That': 1}, {'lies': 1}, {'in': 1}, {"It's": 1}, {'long': 1}, {'road': 1}, {'When': 1}, {'face': 1}, {'world': 1}, {'No': 1}, {'one': 1}, {'reaches': 1}, {'out': 1}, {'hand': 1}, {'for': 1}, {'hold': 1}, {'find': 2}, {'love': 1}, {'if': 1}, {'search': 1}, {'within': 1}, {'yourself': 1}, {'emptiness': 1}, {'felt': 1}, {'disappear': 1}, {'Lord': 1}, {'knows': 1}, {'dreams': 1}, {'hard': 1}, {'follow': 1}, {'But': 1}, {'let': 1}, {'anyone': 1}, {'tear': 1}, {'them': 1}, {'Hold': 1}, {'on,': 1}, {'there': 1}, {'tomorrow': 1}, {'In': 1}, {'time,': 1}, {'way': 1}]

    # List[ Dict{ key : val}] => Dict.values => List => val => list(ld[0].values())[0]
    # print(ld[0].values(), type(ld[0]))
    # dict_values([2]) <class 'dict'>
    # print(list(ld[0].values()), type(list(ld[0].values())))
    # [2] <class 'list'>
    # print(list(ld[0].values())[0], type(list(ld[0].values())[0]))
    # 2 <class 'int'>

    ld.sort(key = wordCmp)
    # int(ld)
    # [{'look': 1}, {'heart': 1}, {'have': 1}, {'afraid': 1}, {'of': 1}, {'what': 1}, {'an': 1}, {'answer': 1}, {'reach': 1}, {'into': 1}, {'soul': 1}, {'sorrow': 1}, {'that': 1}, {'melt': 1}, {'then': 1}, {'comes': 1}, {'With': 1}, {'strength': 1}, {'carry': 1}, {'on': 1}, {'cast': 1}, {'fears': 1}, {'aside': 1}, {'survive': 1}, {'So': 1}, {'when': 1}, {'feel': 1}, {'like': 1}, {'hope': 1}, {'is': 1}, {'gone': 1}, {'Look': 1}, {'and': 1}, {'strong': 1}, {'finally': 1}, {'see': 1}, {'truth': 1}, {'That': 1}, {'lies': 1}, {'in': 1}, {"It's": 1}, {'long': 1}, {'road': 1}, {'When': 1}, {'face': 1}, {'world': 1}, {'No': 1}, {'one': 1}, {'reaches': 1}, {'out': 1}, {'hand': 1}, {'for': 1}, {'hold': 1}, {'love': 1}, {'if': 1}, {'search': 1}, {'within':1}, {'yourself': 1}, {'emptiness': 1}, {'felt': 1}, {'disappear': 1}, {'Lord': 1}, {'knows': 1}, {'dreams': 1}, {'hard': 1}, {'follow': 1}, {'But': 1}, {'let': 1}, {'anyone': 1}, {'tear': 1}, {'them': 1}, {'Hold': 1}, {'on,': 1}, {'there': 1}, {'tomorrow': 1}, {'In': 1}, {'time,': 1}, {'way': 1}, {"There's": 2}, {'If': 2}, {'inside': 2}, {'You': 2}, {"don't": 2}, {'are': 2}, {'know': 2}, {'away': 2}, {'alone': 2}, {'can': 2}, {"you'll": 2}, {'find': 2}, {'hero': 3}, {'your': 3}, {'be': 3}, {'will': 3}, {'to': 4}, {'a': 5}, {'And': 6}, {'the': 6}, {'you': 14}]
    return ld


result = wordCount(fpath)
# print(type(result))
# <class 'dict'>
# print(result)
# {"There's": 2, 'a': 5, 'hero': 3, 'If': 2, 'you': 14, 'look': 1, 'inside': 2, 'your': 3, 'heart': 1, 'You': 2, "don't": 2, 'have': 1, 'to': 4, 'be': 3, 'afraid': 1, 'of': 1, 'what': 1, 'are': 2, 'an': 1, 'answer': 1, 'reach': 1, 'into': 1, 'soul': 1, 'And': 6, 'the': 6, 'sorrow': 1, 'that': 1, 'know': 2, 'will': 3, 'melt': 1, 'away': 2, 'then': 1, 'comes': 1, 'alone': 2, 'With': 1, 'strength': 1, 'carry': 1, 'on': 1, 'cast': 1, 'fears': 1, 'aside': 1, 'can': 2, 'survive': 1, 'So': 1, 'when': 1, 'feel': 1, 'like': 1, 'hope': 1, 'is': 1, 'gone': 1, 'Look': 1, 'and': 1, 'strong': 1, "you'll": 2,'finally': 1, 'see': 1, 'truth': 1, 'That': 1, 'lies': 1, 'in': 1, "It's": 1, 'long': 1, 'road': 1, 'When': 1, 'face': 1, 'world': 1, 'No': 1, 'one':1, 'reaches': 1, 'out': 1, 'hand': 1, 'for': 1, 'hold': 1, 'find': 2, 'love': 1, 'if': 1, 'search': 1, 'within': 1, 'yourself': 1, 'emptiness': 1, 'felt': 1, 'disappear': 1, 'Lord': 1, 'knows': 1, 'dreams': 1, 'hard': 1, 'follow': 1, 'But': 1, 'let': 1, 'anyone': 1, 'tear': 1, 'them': 1, 'Hold': 1,'on,': 1, 'there': 1, 'tomorrow': 1, 'In': 1, 'time,': 1, 'way': 1}
wordresult = wordSort(result)
# print(type(wordresult))
# <class 'list'>
# print(wordresult)
# [{'look': 1}, {'heart': 1}, {'have': 1}, {'afraid': 1}, {'of': 1}, {'what': 1}, {'an': 1}, {'answer': 1}, {'reach': 1}, {'into': 1}, {'soul': 1}, {'sorrow': 1}, {'that': 1}, {'melt': 1}, {'then': 1}, {'comes': 1}, {'With': 1}, {'strength': 1}, {'carry': 1}, {'on': 1}, {'cast': 1}, {'fears': 1}, {'aside': 1}, {'survive': 1}, {'So': 1}, {'when': 1}, {'feel': 1}, {'like': 1}, {'hope': 1}, {'is': 1}, {'gone': 1}, {'Look': 1}, {'and': 1}, {'strong': 1}, {'finally': 1}, {'see': 1}, {'truth': 1}, {'That': 1}, {'lies': 1}, {'in': 1}, {"It's": 1}, {'long': 1}, {'road': 1}, {'When': 1}, {'face': 1}, {'world': 1}, {'No': 1}, {'one': 1}, {'reaches': 1}, {'out': 1}, {'hand': 1}, {'for': 1}, {'hold': 1}, {'love': 1}, {'if': 1}, {'search': 1}, {'within':1}, {'yourself': 1}, {'emptiness': 1}, {'felt': 1}, {'disappear': 1}, {'Lord': 1}, {'knows': 1}, {'dreams': 1}, {'hard': 1}, {'follow': 1}, {'But': 1}, {'let': 1}, {'anyone': 1}, {'tear': 1}, {'them': 1}, {'Hold': 1}, {'on,': 1}, {'there': 1}, {'tomorrow': 1}, {'In': 1}, {'time,': 1}, {'way': 1}, {"There's": 2}, {'If': 2}, {'inside': 2}, {'You': 2}, {"don't": 2}, {'are': 2}, {'know': 2}, {'away': 2}, {'alone': 2}, {'can': 2}, {"you'll": 2}, {'find': 2}, {'hero': 3}, {'your': 3}, {'be': 3}, {'will': 3}, {'to': 4}, {'a': 5}, {'And': 6}, {'the': 6}, {'you': 14}]
print(wordresult[-2:])
# [{'the': 6}, {'you': 14}]
