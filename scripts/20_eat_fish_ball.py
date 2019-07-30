#! -*- coding:utf-8 -*-

import threading
import time


balls_count = 0
eat_fish_balls = 0
con = threading.Condition()

class Waiter(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global balls_count
        global eat_fish_balls

        con.acquire()
        while eat_fish_balls < 10:
            print('开始添加')
            balls_count += 1
            print('当前锅中鱼丸数:%d' % balls_count)
            time.sleep(1)

            if balls_count >= 5:
                print('鱼丸达到上限5个，不能再加了')
                con.notify()
                con.wait()

        con.notify()
        print('总共吃了%d个鱼丸，给钱' % eat_fish_balls)
        con.release()

class Consumers(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global eat_fish_balls
        global balls_count

        con.acquire()
        while eat_fish_balls < 10:
            print("吃吃吃")
            balls_count -= 1
            eat_fish_balls += 1
            print('当前锅里的鱼丸数:%d' % balls_count)
            time.sleep(2)
            if balls_count < 1:
                print('服务员')
                con.notify()
                con.wait()

        con.notify()
        print("总共吃了%d个鱼丸" % eat_fish_balls)
        con.release()


if __name__ == "__main__":
    waiter = Waiter()
    consumer = Consumers()
    waiter.start()
    consumer.start()
    waiter.join()
    consumer.join()

