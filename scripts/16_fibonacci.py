#! -*- coding:utf-8 -*-

def fib_memory(num, temp={}):
    if num in (1,2):
        return 1
    try:
        return temp[num]
    except:
        temp[num] = fib_memory(num-1) + fib_memory(num-2)
        return temp[num]


def fib_time(num):
    a = 0
    b = 1
    for i in range(num):
        a, b = b, a+b
    return a


if __name__ == "__main__":
    print(fib_memory(10))
    print(fib_time(10))