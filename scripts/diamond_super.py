#! -*- coding:utf-8 -*-

class Base(object):
    def __init__(self):
        print("base class inital")

class Second(Base):
    def __init__(self):
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


if __name__ == "__main__":
    print(Fourth.mro())
    test = Fourth()