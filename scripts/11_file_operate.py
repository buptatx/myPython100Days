#! -*_ coding:utf-8 -*-


from math import sqrt
import unittest


def file_read_test():
    try:
        with open("致橡树.txt", "r", encoding="utf-8") as mf:
            print(mf.read())
    except FileNotFoundError:
        print("file not found")
    except LookupError:
        print("unknown encoding")
    except UnicodeDecodeError:
        print("load data error")


def is_prime(n):
    if not isinstance(n, int) or n <= 1:
        return False

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def write_data():
    file_handles = []
    file_names = ["a.txt", 'b.txt', 'c.txt']
    prefix = "../data/"

    try:
        for i in file_names:
            file_handles.append(open(prefix+i, "w", encoding="utf-8"))

        for single in range(1, 10000):
            if is_prime(single):
                if single < 100:
                    fidx = 0
                elif single < 1000:
                    fidx = 1
                else:
                    fidx = 2
                file_handles[fidx].write(str(single) + '\n')
    except Exception as e:
        print(str(e))
    finally:
        for i in file_handles:
            if i:
                i.close()
    print("process done")


class PrimeTest(unittest.TestCase):
    def test_1_not_prime(self):
        self.assertFalse(is_prime(1))

    def test_0_not_prime(self):
        self.assertFalse(is_prime(0))

    def test_1point5_not_prime(self):
        self.assertFalse(is_prime(1.5))

    def test_2_is_prime(self):
        self.assertTrue(is_prime(2))

    def test_5_is_prime(self):
        self.assertTrue(is_prime(5))

    def test_8_not_prime(self):
        self.assertFalse(is_prime(8))


if __name__ == "__main__":
    #file_read_test()
    #unittest.main()
    write_data()