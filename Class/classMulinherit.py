# coding:utf-8


class A(object):

    def test(self):
        print('A:test()')

    def testA(self):
        print('testA')


class B(object):

    def test(self):
        print('B:test()')

    def testB(self):
        print('testB')


class C(A, B):
    pass


class D(B, A):
    pass


c = C()
c.testA()
# testA
c.testB()
# testB

c.test()
# A:test()
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

d = D()
d.test()
# B:test()
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
