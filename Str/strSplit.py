# conding=utf-8
settings = '[google] name=Charles pwd=abc123 [yahoo] name=Hannah pwd=def567'


def get_sinfo(sinfo):
    print(sinfo)
    s_index = sinfo.find('[')
    print("===")
    e_index = sinfo.find(']')
    print(sinfo[s_index+1:e_index])

    kvinfo = sinfo[e_index+1:]
    kvs = kvinfo.split()
    print(kvs)
    for kv in kvs:
        print(kv.split('='))


def get_iniinfo(ini):
    # sessions = ini.split('[')
    # print(sessions, ":", type(sessions))
    # ['', 'google] name=Charles pwd=abc123 ', 'yahoo] name=Hannah pwd=def567'] : <class 'list'>
    # lost "["
    for s in ini.split('['):
        if s:
            get_sinfo('['+s)


def get_allsession(ini):
    s_index = 0
    s_nindex = 0
    while True:
        s_index = ini.find('[', s_nindex)
        s_nindex = ini.find('[', s_index+1)
        # print (ini[s_index:s_nindex])
        if s_nindex == -1:
            get_sinfo(ini[s_index:])
            break
        else:
            get_sinfo(ini[s_index:s_nindex])


print("1")
get_iniinfo(settings)
print("\n-----------\n2")
get_allsession(settings)
