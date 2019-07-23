#! -*- coding:utf-8 -*-


def fib(num):
    #带有yield的函数，生成器
    a,b = 0,1
    for _ in range(num):
        a, b = b, a+b
        yield a


class Fib(object):
    def __init__(self, count):
        self.count = count
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= self.count:
            raise StopIteration()
        else:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a

if __name__ == "__main__":
    count = int(input("please input the fibanacci number count:"))
    for i in fib(count):
        print(i, end=" ")
    print()

    for i in Fib(count):
        print(i, end=" ")
    print()