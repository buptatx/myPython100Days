#! -*- coding:utf-8 -*-

import re
import datetime
from itertools import product
from random import shuffle, randint
from math import log


def create_sequence():
    x = ["百科", "健康百科", "电视节目", "24节气", "菜谱"]
    #itertools.product 函数可以实现 从n个不同的球中顺序取出x个有几种情况的问题
    y = product(x, repeat=2)
    for item in y:
        print(item)


def captain_test():
    #对hello world中的首字母取大写
    arr = 'hello world'.split()
    expect = f'{arr[0].capitalize()} {arr[1].capitalize()}'
    print(expect)


def pattern_test():
    #使用isdigit判断输入字符串是否为纯数字
    #相关的内联函数 isdigit isalpha isalnum
    input_str = input('please input your str:')
    while input_str != "stop":
        print("[%s]check result with isdigit: %s" % (input_str, input_str.isdigit()))
        input_str = input('please input your str:')


def reverse_test():
    #将字符串反转
    source = "ilovechina"
    print(source[::-1])


def remove_space_test():
    #去除首尾的空格
    source = " abcd "
    #方法1 使用内联函数strip
    print(source.strip())
    #方法2 使用split分割成不同部分再组合非空的部分
    print("".join([x for x in source.split(" ") if x != ""]))

    #rstrip去除尾部的空格
    a = "你好 中国 "
    print(a.rstrip())


def split_test():
    source = "info：xiaoZhang 33 shandong"
    #用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
    pattern_alnum = re.compile("\w+")
    res = pattern_alnum.findall(source)
    print(res)


def list_remove_duplicate_el_test():
    source = [1,2,3,1,2]
    #使用set集合，集合内的元素不可重复
    print(list(set(source)))


def str_to_list_test():
    #如何实现 "1,2,3" 变成 ["1","2","3"]
    source = "1,2,3"
    print(source.split(","))


def list_find_diff_test():
    #给定两个list，A和B，找出相同元素和不同元素
    a = [1, 6, 2, 3, 9]
    b = [0, 2, 4, 3]
    print(set(a)-set(b) | set(b) - set(a))
    print(set(a)&set(b))


def list_merge_test():
    #合并列表[1, 5, 7, 9]和[2, 2, 6, 8]
    a = [1, 5, 7, 9]
    b = [2, 2, 6, 8]
    a.extend(b)
    print(a)


def list_element_merge_test():
    #[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
    source = [[1,2],[3,4],[5,6]]
    dest = [y for x in source for y in x]
    print(dest)


def list_ele_shuffle_test():
    #如何打乱一个列表的元素
    source = [1,2,3,4,5,6,7]
    for i in range(4):
        shuffle(source)
        print(source)


def list_ele_shuffle_v2_test():
    source = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    for i in range(1, len(source)):
        idx = randint(0, i)
        value = source.pop(idx)
        source.append(value)

    print(source)


def list_del_pop_test():
    source = [1,2,3,4,5]
    #pop默认最后一个元素
    #pop可以加元素值
    #pop有返回值
    res = source.pop(1)
    print(res)
    #remove需要添加元素值
    #remove没有返回值
    res = source.remove(3)
    print(res)
    del source[1]
    print(source)


def dict_del_pop_test():
    source = {"a":2, "b":3}
    res = source.pop('a')
    print(res)
    del source['b']
    print(source)


def dict_sort_test():
    #字典为元素的列表，根据字典中age的大小进行降序排序
    source = [{'name':"alice", "age":38},
              {'name':'bob', "age":18},
              {'name':"carl", "age":28}]
    source.sort(key=lambda x:x["age"], reverse=True)
    print(source)


def dict_merge_test():
    #请合并下面两个字典 a = {"A":1,"B":2},b = {"C":3,"D":4}
    a = {"A":1,"B":2}
    b = {"C":3,"D":4}
    a.update(b)
    print(a)


def map_test():
    #如何把元组("a","b")和元组(1,2)，变为字典{"a":1,"b":2}
    k_source = ("a","b")
    w_source = (1,2)
    z = {x:y for x in k_source for y in w_source}
    print(z)


def dict_reverse_test():
    #如何交换字典{"A"：1, "B"：2}的键和值
    source = {"A":1, "B":2}
    dest = {v:k for k, v in source.items()}
    print(dest)


def check_2_test():
    t = int(input("please input a num:"))
    if t<2:
        return False
    while t>=2:
        if t%2 != 0:
            return False
        else:
            t = t/2
    return False if t != 1 else True


def check_2_bit_operate_test():
    bin_number = str(bin(int(input("please input a num:"))))
    b_pattern = re.compile("0b10+")
    return True if b_pattern.match(bin_number) else False


def show_even_below_100_test():
    print(" ".join([str(x) for x in range(101) if x%2 == 0]))


def str_append_test(num):
    #python中数字、字符串、元组是不可变的
    sstr = "first"
    for i in range(num):
        #每次循环都需要重新创建一个新的sstr
        #如果num比较大 会占用较大内存
        sstr += str(i)
    return sstr


def str_append_advanced_test(num):
    sstr = "first"
    #num比较大的时候生成式也会存在内存占用多的问题
    #sstr只重新创建一个
    sstr += "".join([str(i) for i in range(num)])
    return sstr


def re_sub_test():
    #a="张明 98 分"，用 re.sub，将 98 替换为 100
    source = "张明 98 分"
    print(re.sub(r'\b\d+\b', '100', source))


def date_test():
    #如果当前的日期为20190530，要求写一个函数输出N天后的日期，(比如 N 为 2，则输出 20190601)
    interval = int(input("please input days:"))
    #以今天为参考点，距离多少天
    #start_date = datetime.date.today()
    #以固定日期为参考点，距离多少天
    start = '20190530'
    start_date = datetime.datetime(int(start[:4]), int(start[4:6]), int(start[6:8]))
    end_date = start_date + datetime.timedelta(days=interval)

    print(end_date.strftime('%Y-%m-%d'))


def multi_shell(num):
    #接收整数参数 n，返回一个函数，函数的功能是把函数的参数和 n 相乘并把结果返回
    def multi(source):
        return source*num
    return multi


def test_multi_shell():
    test = multi_shell(5)
    print(test(10))


def filter_list_test():
    #filter 方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    source = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = filter(lambda x:x%2==1, source)
    result = [i for i in res]
    print(result)


def bubble_sort(origin_data):
    #冒泡排序平均时间复杂度 O(n**2)
    nlen = len(origin_data)
    if nlen <= 1:
        return origin_data

    for i in range(0, nlen):
        hasChanged = False
        #每轮将未排序部分的最大元素排到已排序不分的起始
        for j in range(0, nlen-i-1):
            #将最大的元素放到队列末尾
            if origin_data[j] > origin_data[j+1]:
                hasChanged = True
                origin_data[j], origin_data[j+1] = origin_data[j+1], origin_data[j]
        #如果单轮冒泡排序，没有任何的元素改变 则认为排序结束
        if not hasChanged:
            break
    return origin_data


def insert_sort(origin_data):
    #插入排序，使用效率比冒泡及比较排序广发
    #属于原地排序|稳定排序，只需要额外一个元素空间
    #平均时间复杂度O(n**2)
    nlen = len(origin_data)
    if nlen <= 1:
        return origin_data

    for i in range(1, nlen):
        temp = origin_data[i]
        temp_idx = 0
        #单轮确定该元素在已排序子序列中的插入位置
        for j in range(i-1, -1, -1):
            #如果当前元素比要插入的元素大，则将该元素右移
            if origin_data[j] > origin_data[i]:
                origin_data[j+1] = origin_data[j]
            else:
                temp_idx = j+1
                break
        #插入元素
        origin_data[temp_idx] = temp

    return origin_data


def cmp_sort(origin_data):
    #比较排序
    #平均时间复杂度O(n**2)，非稳定的排序
    nlen = len(origin_data)
    if nlen <= 1:
        return origin_data

    for i in range(nlen):
        max = 0
        idx = 0
        #单轮查找出最大的元素的索引以及元素的值
        for j in range(nlen-i):
            if origin_data[j] > max:
                max = origin_data[j]
                idx = j
        #将最大的元素移动到列表的末尾
        origin_data[nlen-1-i] , origin_data[idx] = origin_data[idx], origin_data[nlen-1-i]
        print(origin_data)

    return origin_data


def merge_sort(s_list):
    #归并排序使用分而治之的方法
    #平均时间复杂度nlog(n)
    #稳定的排序
    if len(s_list) == 1:
        return s_list

    c = len(s_list)//2
    #对整个列表排序就是对 左侧子列表排序 右侧子列表排序
    #然后将两个排序后的子列表 结合
    left = merge_sort(s_list[:c])
    right = merge_sort(s_list[c:])
    return combine_merge(left, right)


def combine_merge(list1, list2):
    temp = []
    i = 0
    j = 0
    list_1_len = len(list1)
    list_2_len = len(list2)

    #对于两个子序列 值小的添加到结果列表并将游标前移
    while i < list_1_len and j < list_2_len:
        if list1[i] <= list2[j]:
            temp.append(list1[i])
            i += 1
        else:
            temp.append(list2[j])
            j += 1

    #添加剩余部分
    temp.extend(list1[i:])
    temp.extend(list2[j:])

    return temp


def quick_sort(source):
    #快速排序 平均时间复杂度nlog(n)
    #稳定排序
    #每次使用的空间只有1
    if len(source) == 1:
        return source

    #对列表中的数据进行排序，返回游标
    #游标左侧的数比游标小
    #游标右侧的数比游标大
    q = partiton(source)
    #递归
    #对左右子列表再进行排序
    left = quick_sort(source[:q])
    right = quick_sort(source[q:])

    return left + right


def partiton(src_list):
    if len(src_list) == 1:
        return src_list

    temp = src_list[-1]
    i = j = 0
    sle_idx = len(src_list) - 1
    #采用了类似与插入排序的思想
    #使用两个游标
    #j依次遍历列表，遇到比末尾元素大的就将j和i的元素交换
    #保证左侧的元素比列表尾元素小
    while i < sle_idx and j < sle_idx:
        if src_list[j] < temp:
            src_list[i], src_list[j] = src_list[j], src_list[i]
            i += 1
        j += 1

    src_list[i], src_list[-1] = src_list[-1], src_list[i]
    return i


def sort_test():
    source = [3, 1, 2, 7, 9, 4, 5, 6]
    # print(bubble_sort(source[:]))
    # print(insert_sort(source[:]))
    # print(cmp_sort(source[:]))
    # print(merge_sort(source[:]))
    print(quick_sort(source[:]))


def carry_bit_test():
    # 表示把8进制的54转换成十进制数并输出结果。
    # 8可以是2、8，10，16等进制数
    num = int(input("please input number:"))
    bit = int(input("please input bit(1~10):"))
    res = list()
    while num != 0:
        res.append(num%bit)
        num = num//bit

    print("".join([str(x) for x in res[::-1]]))


def carry_bit_to_dec():
    num = int(input("please input number:"))
    bit = int(input("please input bit(1~10):"))

    num_str = str(num)[::-1]
    print(sum([int(num_str[i])*(bit**i) for i in range(len(num_str))]))


def check_ipv4():
    check_str = input("please input data:")
    p = re.compile("^(25[0-5]|^2[0-4]\d|^1\d{2}|^[1-9]\d|^[1-9])(\.(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)){3}$")
    print("%s:%s" % (check_str, True if p.match(check_str) else False))


def is_ipv4():
    #没有校验首部份为0的情况
    check_str = input("please input data:")
    res = True if [1]*4 == [x.isdigit() and 0 <= int(x) <= 255 for x in check_str.split(".")] else False
    print("%s:%s" % (check_str, res))


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

    for i in range(n):
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


def cal_idx(n):
    if n < 1:
        return 0

    loop = cal_loop(n)
    seq = create_seq(loop)
    return find_n_1(seq, n)


def left_move_test():
    steps = int(input("please input steps for left move:"))
    print(1<<steps)


def cal_n_one_idx_test(n):
    if n <1 or not isinstance(int, n):
        return -1
    elif n == 1:
        return 1

    loop = 0
    for i in range(2, n):
        if 2**(i-1) <= 2*n and 2*n <= 2**i:
            loop = i
            break

    return cal_n_one_idx_test() + 2**loop


if __name__ == "__main__":
    # create_sequence()
    # captain_test()
    # pattern_test()
    # reverse_test()
    # remove_space_test()
    # split_test()
    # list_remove_duplicate_el_test()
    # str_to_list_test()
    # list_find_diff_test()
    # list_merge_test()
    # list_element_merge_test()
    # list_ele_shuffle_test()
    # dict_del_pop_test()
    # list_del_pop_test()
    # dict_sort_test()
    # dict_merge_test()
    # map_test()
    # dict_reverse_test()
    # print(check_2_test())
    # print(check_2_bit_operate_test())
    # show_even_below_100_test()
    # print(str_append_test(10))
    # print(str_append_advanced_test(10))
    # re_sub_test()
    # date_test()
    # test_multi_shell()
    # filter_list_test()
    # sort_test()
    # carry_bit_test()
    # carry_bit_to_dec()
    # check_ipv4()
    # is_ipv4()
    # list_ele_shuffle_v2_test()
    # print(create_seq(2))
    # print(cal_loop(5))
    print(cal_idx(5))
    # print(cal_idx(0))
    # print(cal_idx(1))
    # left_move_test()