# conding=utf-8
import re

# re.search(pattern, string, flags)
# re.findall(pattern, string, flags)
# re.split(pattern, string, maxsplit, flags)
# re.sub(pattern, repl, string, count, flags)

m = re.search(r'\d+', 'Andrew 89 Berton 90')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(7, 9), match='89'> : <class '_sre.SRE_Match'>

m = re.search(r'[1-9]?\d', 'Andrew 89 Berton 90')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(7, 9), match='89'> : <class '_sre.SRE_Match'>

m = re.search(r'[1-9]?\d', 'Andrew 199 Berton 90')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(7, 9), match='19'> : <class '_sre.SRE_Match'>

# =====================================

m = re.findall(r'\d', 'a1b2c3')
print(m, ':', type(m))
# ['1', '2', '3'] : <class 'list'>

m = re.findall(r'\d+', 'a11b22c33')
print(m, ':', type(m))
# ['11', '22', '33'] : <class 'list'>

s = 'ndrew:89 Berton:90 Chester:42 Duke:65'
m = re.findall(r'[1-9]?\d', s)
print(m, ':', type(m))
# ['89', '90', '42', '65'] : <class 'list'>

r = list(map(int, m))
print(sum(r) , ':', sum(r) / len(r))
# 286 : 71.5

# =====================================

m = re.split(r'\d', 'a1b2c3')
print(m, ':', type(m))
# ['a', 'b', 'c', ''] : <class 'list'>

m = re.split(r'\d', 'a1b2c3d')
print(m, ':', type(m))
# ['a', 'b', 'c', 'd'] : <class 'list'>

s = '1,Andrew:90'
m = re.split(r'[,:]', s)
print(m, ':', type(m))
# ['1', 'Andrew', '90'] : <class 'list'>

# =====================================

s = 'passwd:123456'
m = re.sub(r'\d+', '*', s)
print(m, ':', type(m))
# passwd:* : <class 'str'>

s = 'passwd:123456'
m = re.sub(r'\d', '*', s)
print(m, ':', type(m))
# passwd:****** : <class 'str'>

# -------------------------------------

def mySub(m):
    s = m.group()
    print( 'in mySub:s:', s)
    return  'xxx'


s1 = 'Andrew:89'
m = re.sub(r'\d+', mySub, s1)
print(m, ':', type(m))
# in mySub:s: 89
# Andrew:xxx : <class 'str'>


def mySub(m):
    s = m.group()
    score = int(s)
    if score >= 60:
        return 'Pass'
    return  'NoPass'


s = 'Andrew:89, Berton:90, Chester:42, Duke:65'
m = re.sub(r'[1-9]?\d', mySub ,s)
print(m, ':', type(m))
# Andrew:Pass, Berton:Pass, Chester:NoPass, Duke:Pass : <class 'str'>
