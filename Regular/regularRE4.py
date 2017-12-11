# conding=utf-8
import re

'''
^
匹配開頭，多行匹配

$
匹配結尾，多行匹配

\A \Z
匹配字符串開頭和結尾
'''

m = re.match(r'\d+', '123d')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 3), match='123'> : <class '_sre.SRE_Match'>

m = re.match(r'\d+$', '123d')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.match(r'\d+$', '1234')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 4), match='1234'> : <class '_sre.SRE_Match'>

# =====================================

m = re.search(r'\d+', '123d')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 3), match='123'> : <class '_sre.SRE_Match'>

m = re.search(r'\d+$', '123d')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.search(r'^\d+$', '1234')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 4), match='1234'> : <class '_sre.SRE_Match'>

m = re.search(r'^\d+$', '1234d456d678')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.search(r'^\d+$', '1234d\n456d\n678')
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.search(r'^\d+$', '1234d\n456d\n678', re.MULTILINE)
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(11, 14), match='678'> : <class '_sre.SRE_Match'>

# =====================================

m = re.search(r'\A\d+\Z', '1234d\n456d\n678', re.MULTILINE)
print(m, ':', type(m))
# None : <class 'NoneType'>

m = re.search(r'\A\d+\Z', '1234', re.MULTILINE)
print(m, ':', type(m))
# _sre.SRE_Match object; span=(0, 4), match='1234'> : <class '_sre.SRE_Match'>

# =====================================

# email, 6-15, [a-zA-Z0-9][\w_]{5,14}#xx.com  xx->[\w], 2-6
m = re.match(r'\w[\w_]{5,14}@[\w]{2,6}\.com$', 'pythonTest@123.com')
print(m, ':', type(m))
# <_sre.SRE_Match object; span=(0, 18), match='pythonTest@123.com'> : <class '_sre.SRE_Match'>
