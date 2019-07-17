#! -*- coding:utf-8 -*-

import itertools

def print_list(items):
    for item in items:
        print(item)
    print()

permutations = itertools.permutations('ABCD')
print_list(permutations)

combination = itertools.combinations('ABCD', 3)
print_list(combination)

product = itertools.product('ABCD', '123')
print_list(product)

