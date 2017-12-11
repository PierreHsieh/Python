# conding=utf-8
import re

'''
*
匹配前一個字符0次或者無限次

+
匹配前一個字符1次或者無限次

？
匹配前一個字符0次或者1次

{m}/{m,n}
匹配前一個字符m次或者m到n次

*?/+?/??
匹配模式變為非貪婪（盡可能少匹配字符）
'''

m = re.match(r'\d', 'a123')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'\d*', '123')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 3), match='123'> : <class '_sre.SRE_Match'>

m = re.match(r'\d*', '123abc')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 3), match='123'> : <class '_sre.SRE_Match'>

m = re.match(r'\d*', 'a123abc')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 0), match=''> : <class '_sre.SRE_Match'>

m = re.match(r'\d+', '123abc')
print(m, ':', type(m))
# _sre.SRE_Match object; span=(0, 3), match='123'> : <class '_sre.SRE_Match'>

# =====================================

m = re.match(r'[1-9]?', '1')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='1'> : <class '_sre.SRE_Match'>

m = re.match(r'[1-9]?', '0')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 0), match=''> : <class '_sre.SRE_Match'>

m = re.match(r'[1-9]?\d', '9')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='9'> : <class '_sre.SRE_Match'>

m = re.match(r'[1-9]?\d', '100')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 2), match='10'> : <class '_sre.SRE_Match'>

# =====================================

m = re.match(r'\w[\w_]{5,9}', '1234567890')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 10), match='1234567890'> : <class '_sre.SRE_Match'>

m = re.match(r'\w[\w_]{5,9}', '12345678901')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 10), match='1234567890'> : <class '_sre.SRE_Match'>

m = re.match(r'\w[\w_]{5,9}$', '12345678901')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'\w[\w_]{5,9}$', '123456789')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 9), match='123456789'> : <class '_sre.SRE_Match'>

m = re.match(r'\w[\w_]{5,9}$', 'a_12345678')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 10), match='a_12345678'> : <class '_sre.SRE_Match'>

m = re.match(r'\w[\w_]{5,9}$', 'a_12')
print(m, ':', type(m))
# None : <class 'NoneType'>

# =====================================

m = re.match(r'\w*?', '100')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 0), match=''> : <class '_sre.SRE_Match'>

m = re.match(r'\w+?', '100')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='1'> : <class '_sre.SRE_Match'>

m = re.match(r'\w??', '100')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 0), match=''> : <class '_sre.SRE_Match'>
