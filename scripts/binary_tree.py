#! -*- coding:utf-8 -*-


class Node(object):
    def __init__(self, data=None):
        self._data = data
        self._left = None
        self._right = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node


def pre_order(tree):
    if tree is None:
        return False
    print(tree.data, end="->")
    pre_order(tree.left)
    pre_order(tree.right)


def mid_order(tree):
    if tree is None:
        return False

    mid_order(tree.left)
    print(tree.data, end="->")
    mid_order(tree.right)


def sur_order(tree):
    if tree is None:
        return False

    sur_order(tree.left)
    sur_order(tree.right)
    print(tree.data, end="->")


if __name__ == "__main__":
    root_node = Node('a')
    left_node = Node('b')
    right_node = Node('c')
    root_node.left = left_node
    root_node.right = right_node

    pre_order(root_node)
    print("end")

    mid_order(root_node)
    print("end")

    sur_order(root_node)
    print("end")