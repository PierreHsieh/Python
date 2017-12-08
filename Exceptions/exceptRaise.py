# coding:utf-8
from os.path import exists

path = r'.\file\test.txt'


class FileError(IOError):
    pass


result = exists(path)
print ('result:', result)
# result: False
if not result:
    raise FileError('File Not found')
'''
Traceback (most recent call last):
  File "I:\Git_Public\Python\Exceptions\exceptDefException.py", line 14, in <module>
    raise FileError('File Not found')
__main__.FileError: File Not found
'''