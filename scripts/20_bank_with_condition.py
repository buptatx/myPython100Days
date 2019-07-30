#! -*- coding:utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import time,sleep

import threading
import queue


class Account():
    """银行账号"""
    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)
        self.transactions = 0

    def withdraw(self, money):
        with self.condition:
            if money > self.balance:
                self.condition.wait()
                return False
            else:
                new_balance = self.balance - money
                sleep(0.001)
                self.balance = new_balance
                self.transactions += 1
            self.condition.notify()
            return True

    def deposit(self, money):
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            self.transactions += 1
            self.condition.notify_all()

def add_money(account, queue):
    money = randint(5, 10)
    account.deposit(money)

    record = "[" + str(time()) + "]" + threading.current_thread().name + ":" + str(money) + '===>' + str(account.balance)
    print(record)
    queue.put(record)

    sleep(0.5)

def sub_money(account, queue):
    money = randint(10, 30)
    res = account.withdraw(money)
    if res:
        record = "[" + str(time()) + "]" + threading.current_thread().name + ":" + str(money) + "<===" + str(account.balance)
        print(record)
        queue.put(record)
    else:
        record = "[" + str(time()*100) + "]" + threading.current_thread().name + ":" + str(money) + "<===" + str(account.balance) + "failed"
        print(record)
        queue.put(record)
    sleep(1)

def bank_test():
    account = Account()
    record_queue = queue.Queue(12)
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account, record_queue)
            pool.submit(sub_money, account, record_queue)

    while not record_queue.empty():
        print(record_queue.get())
    print("final count :%d" % account.balance)


if __name__ == '__main__':
    bank_test()