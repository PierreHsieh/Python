# conding:utf8


def slices(listl):
    lens = len(listl)
    for index, val in enumerate(listl):
        print(val)
        j = index+1
        while j < lens:
            # print(listl[j:])
            for v in listl[j:]:
                print(listl[index:j], v)
            j += 1


listl = [1, 2, 3]
slices(listl)
# 1
# [1] 2
# [1] 3
# [1, 2] 3
# 2
# [2] 3
# 3
