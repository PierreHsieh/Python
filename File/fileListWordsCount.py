# coding:utf-8
fpath = r'.\file\song.txt'


def parse_file(fname):
    result = 0
    f = open(fname)

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
        result += len(words)
    print(result)
    f.close()
    return result


result = parse_file(fpath)
