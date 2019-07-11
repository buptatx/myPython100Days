#! -*- coding:utf-8 -*-


from time import sleep
from threading import Thread, Lock


class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, count):
        self._lock.acquire()
        try:
            new_balance = self._balance + count
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.balance += self._money


def test_multi_thread():
    account = Account()
    threads = []

    for i in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('process done. account balance %d' % account.balance)


if __name__ == "__main__":
    test_multi_thread()