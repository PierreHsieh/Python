# coding:utf-8
from random import randint

d = {}
for key in range(1, 10):
    d[key] = randint(0, 100)

print(d, type(d))
for key, val in d.items():
    print(key, val)
