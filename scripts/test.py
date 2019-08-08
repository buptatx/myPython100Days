#! -*- coding:utf-8 -*-

from itertools import product


def create_sequence():
    x = ["百科", "健康百科", "电视节目", "24节气", "菜谱"]
    #itertools.product 函数可以实现 从n个不同的球中顺序取出x个有几种情况的问题
    y = product(x, repeat=2)
    for item in y:
        print(item)


if __name__ == "__main__":
    create_sequence()