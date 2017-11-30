# coding=utf8
# test123@163.com
# [a-z][a-z][0-9]@xxx.com
mail = 'test123@168.com'
print('start with[a-z]:', mail[0].isalpha())
# start with[a-z]: True

print('@ in mail      :', '@' in mail)
# @ in mail      : True

print('end with .com  :', mail.endswith('.com'))
# end with .com  : True

s_index = mail.rfind('@')
e_index = mail.rfind('.')
print(s_index)
# 7
print(e_index)
# 11
print('@-.com value>0 :', e_index > s_index)
# @-.com value>0 : True

print('name is d&a    :', mail[:s_index].isalnum())
# name is d&a    : True

testStr = 'Python C C++'
tmp = testStr.lower()
print('python' in tmp)
# True
