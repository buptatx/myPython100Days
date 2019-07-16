#! -*- coding:utf-8 -*-


def max_sub_list_sum():
    items = list(map(int, input().split()))

    size = len(items)
    overall, partial = {}, {}
    #初始化 overall partical 字典
    overall[size-1] = partial[size-1] = items[size-1]
    #倒序
    for i in range(size-2, -1, -1):
        #partial[i] 为items[i] 与 items[i]+向后的全部元素的和 取较大者
        partial[i] = max(items[i], partial[i+1] + items[i])
        #判断当前的总和 和 截止上一个元素的总和 取较大值
        overall[i] = max(partial[i], overall[i+1])

    print(partial)
    print(overall)
    print(overall[0])


if __name__ == "__main__":
    max_sub_list_sum()