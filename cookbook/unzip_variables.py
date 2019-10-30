#! -*- coding:utf-8 -*-

def test():
    #计算前7个月的数据平均数 和 第8个月的数据
    #求两者的平均
    *trailing_qtrs, current_qtr =  [10, 8, 7, 1, 9, 5, 10, 3]
    print(trailing_qtrs)
    print(len(trailing_qtrs))
    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    avg_qtr = (trailing_avg, current_qtr)
    print(avg_qtr)
    return avg_qtr


def test_record():
    #根据数据返回结果的tag走不通的逻辑
    record = [
        ("foo", 1, 2),
        ("bar", "hello"),
        ("foo", 3,4)
    ]

    def do_foo(x,y):
        print("foo", x, y)

    def do_bar(content):
        print("bar", content)

    def dispatch(record):
        for tag, *data in record:
            if tag == "foo":
                do_foo(*data)
            elif tag == "bar":
                do_bar(data)
            else:
                print("unexpected data")

    dispatch(record)


def test_ign():
    #对于不需要的数据直接丢弃
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*ign, year) = record
    print(name, year)


def my_sum(o_data):
    head, *tail = o_data
    return head + my_sum(tail) if tail else head


if __name__ == "__main__":
    #test()
    #test_record()
    #test_ign()
    res = my_sum([10, 5, 6, 7, 9, 1, 3, 4, 5])
    print(res)