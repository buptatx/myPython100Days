#! -*- coding:utf-8 -*-


"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
"""
import time
import threading

from concurrent.futures import ThreadPoolExecutor


class Account(object):
    """银行账户"""
    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


class AddMonkeyThread(threading.Thread):
    """自定义操作"""
    def __init__(self, acount, money):
        self.account = acount
        self.money = money
        super().__init__()

    def run(self):
        self.account.deposit(self.money)


def test_deposit():
    account = Account()
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        future = pool.submit(account.deposit, 1)
        futures.append(future)

    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)

if __name__ == "__main__":
    test_deposit()