#! -*- coding:utf-8 -*-

from collections import defaultdict

def test():
    a = defaultdict(list)
    a['a'].append(1)
    a['a'].append(2)
    a['b'].append(3)
    a['b'].append(4)

    for item in a:
        print(a[item])


if __name__ == "__main__":
    test()