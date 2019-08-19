#! -*- coding:utf-8 -*-

import queue

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

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
    #先序二叉树遍历
    if tree is None:
        return False

    #先遍历左子树，再根结点，再右子树
    print(tree.data, end="->")
    pre_order(tree.left)
    pre_order(tree.right)


def mid_order(tree):
    #中序二叉树遍历
    if tree is None:
        return False

    #先遍历左子树，再根结点，再右子树
    mid_order(tree.left)
    print(tree.data, end="->")
    mid_order(tree.right)


def sur_order(tree):
    # 后序二叉树遍历
    if tree is None:
        return False

    # 先遍历左子树，再右子树，再根结点
    sur_order(tree.left)
    sur_order(tree.right)
    print(tree.data, end="->")


def tree_depth(tree, depth=0):
    if tree is None:
        return depth

    #二叉树的深度 = 左子树的深度与右子树的深度的较大值 + 1
    return max(tree_depth(tree.left, depth), tree_depth(tree.right, depth)) + 1


def tree_width(tree):
    cur_width = 1
    max_width = 0
    q = queue.Queue()
    q.put(tree)

    while not q.empty():
        node = q.get()
        cur_width -= 1
        if node.left is not None:
            q.put(node.left)
            cur_width += 1
        if node.right is not None:
            q.put(node.right)
            cur_width += 1

        if cur_width>max_width:
            max_width = cur_width

    print("tree max width is %d" % max_width)


if __name__ == "__main__":
    root_node = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))

    pre_order(root_node)
    print("end")

    mid_order(root_node)
    print("end")

    sur_order(root_node)
    print("end")

    print(tree_depth(root_node))

    tree_width(root_node)