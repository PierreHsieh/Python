# conding=utf-8
import re

# re.compile(pattern, flags=0)
# re.match(pattern, string, flags=0)
'''
m = re.match
m.start()/m.end()   # list
m.span()            # tuple
m.group()           # str
m.groups()          # tuple
m.groupdict()       # dict
'''
'''
flag
re.l
re.L
re.M
re.S
re.U
re.X
'''


p = re.compile(r'\d')
print(p, ':', type(p))
# re.compile('\\d') : <class '_sre.SRE_Pattern'>

m = p.match('1d')
print(m, ':', type(m))
# _sre.SRE_Match object; span=(0, 1), match='1'> : <class '_sre.SRE_Match'>

# =====================================

m = re.match(p, '10d')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='1'> : <class '_sre.SRE_Match'>

m = re.match(r'\d', '10d')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='1'> : <class '_sre.SRE_Match'>

print(m.group())
# 1
print(m.start(), m.end())
# 0 1
print(m.span())
# (0, 1)

m = re.match(r'a', 'abc')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='a'> : <class '_sre.SRE_Match'>

m = re.match(r'a', 'Abc')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'a', 'Abc', re.I)
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='A'> : <class '_sre.SRE_Match'>
