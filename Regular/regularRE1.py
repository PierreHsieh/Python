# conding=utf-8
import re

# re.compile(pattern, flags=0)
# re.match(pattern, string, flags=0)
'''
m = re.match
Match對象 說明
m.start()/m.end()
匹配開始和結束時的索引        # list

m.span()
匹配索引開始結束組成元組      # tuple

m.group()
匹配的字符串                  # str

m.groups()
包含所有子組的元組            # tuple

m. groupdict()
返回匹配的所有命名子組的字典  # dict
'''
'''
flag
描述

Re.I
匹配對大小寫不敏感

Re.L
做本地化識別匹配

Re.M
多行匹配，改變'^'和'$'的行為

Re.S
點任意匹配模式，改變'.'的行為

Re.U
根據Unicode字符集解析字符

Re.X
正則表達式可以是多行， 忽略空白字符，並可以加入註釋
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
