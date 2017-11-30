# coding=utf-8


def listToStr(listl):
    result = ''
    tmp = str(listl)
    print(tmp, "\n",
          tmp[1:-1], "\n",
          tmp.strip('[]'), "\n",
          tmp[1:-1].replace(', ', ''))
    print("===")

    result = str(listl).strip('[]').replace(', ', '')
    print(result)

    result = str(listl)[1:-1].replace(', ', '')
    print(result)

    result = ''
    for val in listl:
        result += str(val)
    print(result)


listl = [1, 2, 3, 4, 5]
listToStr(listl)
