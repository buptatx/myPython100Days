#! -*- coding:utf-8 -*-

"""
计算第n个1的索引
"""

def cal_idx(n):
    """
    计算第n个1
    :param n:第几个
    :return:索引位置
    """
    if n < 1:
        return -1

    loop = cal_loop(n)
    seq = create_seq(loop)
    print(seq)
    return find_n_1(seq, n)


def cal_n_idx(n, c_int):
    """
    计算第n个数的索引值
    :param n: 求的n
    :param c_int:要求的数 合法值 0，1
    :return: 第n个数的索引值
    """
    #健壮性判断 如果n<1或者n不是整数，或者c_int不是0，1都会返回-1
    if n < 1 or not isinstance(n, int) or c_int not in [0, 1]:
        return -1
    #第一个0和第一个1的索引
    elif n == 1:
        return 0 if c_int == 0 else 1

    #计算第n个0或1是属于第几轮循环
    loop = 0
    for i in range(2, n+1):
        if 2**(i-1) <= 2*n and 2*n <= 2**i:
            loop = i
            break

    #求第n个1的位置等于 第(n-轮数)个0的位置+2*轮数个元素的偏移
    return cal_n_idx(n-loop, 0 if c_int == 1 else 1) + 2*loop


def create_seq(n):
    #起始值为0，求反01，作为输入求反0110，再求反
    #第一组 0 第二组 01 第三组 0110 第四组 01101001 第五组 0110100110010110
    #返回第n组的序列
    if n == 1:
        return "0"
    else:
        pre = create_seq(n-1)
        #当前轮的序列 = 上一轮的序列 + 上一轮序列的各位取反
        return pre + "".join(["0" if x == "1" else "1" for x in pre])


def cal_loop(n):
    #计算是第几轮
    if n < 2:
        return n + 1

    for i in range(n+1):
        #每两个字符中包含一个1，第n个1意味着有2n个字符
        #每轮的字符数符合2**n，计算第n个字符在第几轮
        if 2**(i-1) <= 2*n and 2*n <= 2**i:
            return i + 1


def find_n_1(seq, n):
    count = 0
    for i in range(0, len(seq)):
        #平均时间复杂度O(n)的遍历
        if seq[i] == "1":
            count += 1
            if count == n:
                return i


if __name__ == "__main__":
    print(cal_idx(5))
    print(cal_n_idx(5, 1))
