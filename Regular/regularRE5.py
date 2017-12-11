# conding=utf-8
import re

'''
|
匹配|左右任意一個表達式，100|\d[1,2]

(…)(…)
括號中的表達式作為分組，編號默認加1

\<num>
引用編號為num的分組匹配到的字符串;(\d)test\1

(?P<name>)
分組起別名: (?P<name>\d)

(?p=name)
引用別名為name的分組匹配到的結果: (?P<id>\d)test\id

(?:…)
不分組
'''

m = re.match(r'ab|bc', 'abcd')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 2), match='ab'> : <class '_sre.SRE_Match'>

m = re.match(r'ab|bc', 'bcd')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 2), match='bc'> : <class '_sre.SRE_Match'>

m = re.match(r'[1-9]?\d$', '00')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'[1-9]?\d$', '99')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 2), match='99'> : <class '_sre.SRE_Match'>

m = re.match(r'[1-9]?\d$|100', '100')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 3), match='100'> : <class '_sre.SRE_Match'>

# =====================================

print(m.groups(), ':', type(m.groups()))
# () : <class 'tuple'>

m = re.match(r'([1-9]?\d$)|(100)', '100')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 3), match='100'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()))
# 100 : (None, '100') : <class 'tuple'>

m = re.match(r'(\d)\w', '1a')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 2), match='1a'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()))
# 1a : ('1',) : <class 'tuple'>

s = '1 Don 12'
m = re.match(r'(\d{1,2}) ([a-zA-Z]{2,20}) ([1-9]?\d|100)', s)
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 8), match='1 Don 12'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()))
# 1 Don 12 : ('1', 'Don', '12') : <class 'tuple'>

# =====================================

# 1aaa1 or 2aaa2
# <book>..</book>
m = re.match(r'(\d)\w+(\d)', '1001')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 4), match='1001'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()))
# 1001 : ('1', '1') : <class 'tuple'>

m = re.match(r'(\d)\w+(\d)', '1002')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 4), match='1002'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()))
# 1002 : ('1', '2') : <class 'tuple'>

m = re.match(r'(\d)\w+(\1)', '1001')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 4), match='1001'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()))
# 1001 : ('1', '1') : <class 'tuple'>

# =====================================

m = re.match(r'(?P<id>\d)\w+(\1)', '2aa2')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 4), match='1001'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()), m.groupdict())
# 2aa2 : ('2', '2') : <class 'tuple'> {'id': '2'}

s = '1 Don 12'
m = re.match(r'(?P<id>\d{1,2}) (?P<name>[a-zA-Z]{2,20}) (?P<score>[1-9]?\d|100)', s)
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 8), match='1 Don 12'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()), m.groupdict())
# 1 Don 12 : ('1', 'Don', '12') : <class 'tuple'> {'id': '1', 'name': 'Don', 'score': '12'}

# =====================================

m = re.match(r'(?P<id>\d)\w+(?P=id)', '2aa2')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 4), match='2aa2'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()), m.groupdict())
# 2aa2 : ('2',) : <class 'tuple'> {'id': '2'}

# =====================================

m = re.match(r'(?:\d){2}', '11')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 2), match='11'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()), m.groupdict())
# 11 : () : <class 'tuple'> {}

m = re.match(r'(?:\d){2}', '12')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 2), match='12'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()), m.groupdict())
# 12 : () : <class 'tuple'> {}

m = re.match(r'\w(?:\d){2}', 'd12')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 3), match='d12'> : <class '_sre.SRE_Match'>
print(m.group(), ':', m.groups(), ':', type(m.groups()), m.groupdict())
# d12 : () : <class 'tuple'> {}
