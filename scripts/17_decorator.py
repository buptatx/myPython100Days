#！-*- coding:utf-8 -*-

def get_celebrator(char):
    def print_style(func):
        def inner(*args, **kwargs):
            print(char*15)
            res = func(*args, **kwargs)
            return res
        return inner
    return print_style


@get_celebrator('=')
@get_celebrator('*')
def my_print(content):
    print(content)
    return len(content) if len(content)>0 else -1


if __name__ == "__main__":
    content = input('please input your content:')
    res = my_print(content)
    print("my print res is %s" % res)