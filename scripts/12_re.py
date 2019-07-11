#! -*- coding:utf-8 -*-

import re

def test_re():
    username = input("input username:")
    qq = input('input qq account:')

    m1 = re.match(r'^\w{6,20}$', username)
    if not m1:
        print('please input valid username')

    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('please input valid account')

    if m1 and m2:
        print('access')


def test_phone():
    #pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print("--------华丽的分隔线--------")

    for item in pattern.finditer(sentence):
        print(item.group())
    print("--------华丽的分隔线--------")

    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, endpos=m.end())


def test_replace():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.I)
    print(purified)


def test_split():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[,.，。]', poem)
    print(sentence_list)

    result = [x for x in sentence_list if x != '']
    print(result)


if __name__ == "__main__":
    #test_re()
    #test_phone()
    #test_replace()
    test_split()