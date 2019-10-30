#! -*- coding:utf-8 -*-

from collections import OrderedDict

def test_dict():
    #python 3.6之后dict是有序的
    normal_dict = {}
    normal_dict["z"] = 0
    normal_dict["a"] = 4
    normal_dict["b"] = 6
    normal_dict["c"] = 1
    print(normal_dict)

    order_dict = OrderedDict()
    order_dict["z"] = 0
    order_dict["a"] = 4
    order_dict["b"] = 6
    order_dict["c"] = 1
    print(order_dict)

if __name__ == "__main__":
    test_dict()
