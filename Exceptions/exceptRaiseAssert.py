# coding:utf-8


# raise NameError('A is not define', 'check')
'''
Traceback (most recent call last):
  File "E:/Git_Public/Python/Exceptions/exceptRaiseAssert.py", line 4, in <module>
    raise NameError('A is not define', 'check')
NameError: ('A is not define', 'check')
'''

def func(a, b):
    assert b != 0, 'b is zero!!' # b = 0 => False => Error
    if b == 0:
        raise ValueError('b is zero!')
    return (a / b)


def foo(vals):
    assert isinstance(vals, list), ('vals is not list!')
    if not isinstance(vals, list):
        raise TypeError('vals is not list!')
    vals = [int(val) for val in vals]
    return sum(vals)


print(func(10, 2))
# 5.0
print('====== 1')
# print(func(10, 0))
'''
Traceback (most recent call last):
  File "E:/Git_Public/Python/Exceptions/exceptRaiseAssert.py", line 30, in <module>
    print(func(10, 0))
  File "E:/Git_Public/Python/Exceptions/exceptRaiseAssert.py", line 13, in func
    assert b != 0, 'b is zero!!' # b = 0 => False => Error
AssertionError: b is zero!!
'''
print('====== 2')
print(foo(list('123')))
# 6
print('====== 3')
# print(foo(123))
'''
Traceback (most recent call last):
  File "E:/Git_Public/Python/Exceptions/exceptRaiseAssert.py", line 43, in <module>
    print(foo(123))
  File "E:/Git_Public/Python/Exceptions/exceptRaiseAssert.py", line 20, in foo
    assert isinstance(vals, list), ('vals is not list!')
AssertionError: vals is not list!
'''