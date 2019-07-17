#! -*- coding:utf-8 -*-

"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""


class Thing(object):
    def __init__(self, name, price, weight):
        self._price = price
        self._weight = weight
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price > 0:
            self._price = price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self._weight = weight

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._price/self._weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def thief():
    """
    将二维因素降维到一维，新增属性 价值重量比
    按价值重量比降序排列，如果超重不拿 不超重拿
    :return:
    """
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'thief take {thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f'total price: {total_price} dollars')


if __name__ == '__main__':
    thief()