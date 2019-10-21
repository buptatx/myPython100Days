#! -*- coding:utf-8 -*-

class Base(object):
    def __init__(self):
        print("base class inital")

class Second(Base):
    def __init__(self):
        #super 指的是 MRO 中的下一个类
        super().__init__()
        print("second class go")

class Third(Base):
    def __init__(self):
        super().__init__()
        print("third class go")

class Fourth(Second, Third):
    def __init__(self):
        super().__init__()
        print("fourth class initial")

class A(object):
    def __init__(self):
        print("inital method from A")

class B(A):
    def b(self):
        print("B.func b")

class C(A):
    def c(self):
        print("C.func c")

class D(B, C):
    pass


if __name__ == "__main__":
    print(Fourth.mro())
    test = Fourth()

    d = D()
    d.c()