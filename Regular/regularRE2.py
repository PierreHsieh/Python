# conding=utf-8
import re

'''
.
匹配任意字符（除了\n）

[...]
匹配字符集

\
轉義符：\\ \. \* ....
\d / \D
匹配數字/非數字

\s / \S
匹配空白/非空白字符

\w / \W
匹配單詞字符[a-zA-Z0-9]/非單詞字符
'''

m = re.match(r'.', '123')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='1'> : <class '_sre.SRE_Match'>

m = re.match(r'.', 'A23')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='A'> : <class '_sre.SRE_Match'>

m = re.match(r'.', 'a23')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='a'> : <class '_sre.SRE_Match'>

m = re.match(r'.', '#23')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='#'> : <class '_sre.SRE_Match'>

m = re.match(r'.', '\r23')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='\r'> : <class '_sre.SRE_Match'>

m = re.match(r'.', '\n23')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'.', '\n23', re.S)
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='\n'> : <class '_sre.SRE_Match'>

# =====================================

m = re.match(r'[1234567890]', '012')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='0'> : <class '_sre.SRE_Match'>

m = re.match(r'[123456789]', '012')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'[0-9]', '42')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='4'> : <class '_sre.SRE_Match'>

m = re.match(r'[a-z]', 'abc')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='a'> : <class '_sre.SRE_Match'>

m = re.match(r'[a-zA-Z]', 'Abc')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='A'> : <class '_sre.SRE_Match'>

m = re.match(r'[a-zA-Z0-9]', '0bc')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='0'> : <class '_sre.SRE_Match'>

# =====================================

m = re.match(r'\.', '.42')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='.'> : <class '_sre.SRE_Match'>

m = re.match(r'\.', 'a42')
print(m, ':', type(m))
# None : <class 'NoneType'>

# =====================================

m = re.match(r'\d', '42')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='4'> : <class '_sre.SRE_Match'>

m = re.match(r'\d', 'a2')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'\D', '42')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'\D', 'a2')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='a'> : <class '_sre.SRE_Match'>

# =====================================

m = re.match(r'\s', ' a2')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match=' '> : <class '_sre.SRE_Match'>

m = re.match(r'\s', '\na2')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='\n'> : <class '_sre.SRE_Match'>

m = re.match(r'\s', '\aa2')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'\S', '\aa2')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='\x07'> : <class '_sre.SRE_Match'>

m = re.match(r'\S', '\ra2')
print(m, ':', type(m))
# None : <class 'NoneType'>

# =====================================

m = re.match(r'\w', '22')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='2'> : <class '_sre.SRE_Match'>

m = re.match(r'\w', 'A2')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='A'> : <class '_sre.SRE_Match'>

m = re.match(r'\w', '#2')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'\W', '#2')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='#'> : <class '_sre.SRE_Match'>

m = re.match(r'\W', '\r2')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 1), match='\r'> : <class '_sre.SRE_Match'>

m = re.match(r'\W', '22')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'\d\w[a-z]', '40aabc')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 3), match='40a'> : <class '_sre.SRE_Match'>

m = re.match(r'\d\w[a-z]', '4@aabc')
print(m, ':', type(m))
# None : <class 'NoneType'>
