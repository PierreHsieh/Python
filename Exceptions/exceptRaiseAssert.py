# coding:utf-8


def func(a, b):
    assert b != 0, 'b is zero!!'
    if b == 0:
        raise ValueError('b is zero!')
    return a/b


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
  File "I:\Git_Public\Python\Exceptions\exceptRaiseAssert.py", line 22, in <module>
    print(func(10, 0))
  File "I:\Git_Public\Python\Exceptions\exceptRaiseAssert.py", line 5, in func
    assert b != 0, 'b is zero!!'
AssertionError: b is zero!!
'''
print('====== 2')
print(foo(list('123')))
# 6
print('====== 3')
# print(foo(123))
'''
Traceback (most recent call last):
  File "I:\Git_Public\Python\Exceptions\exceptRaiseAssert.py", line 35, in <module>
    print(foo(123))
  File "I:\Git_Public\Python\Exceptions\exceptRaiseAssert.py", line 12, in foo
    assert isinstance(vals, list), ('vals is not list!')
AssertionError: vals is not list!
'''