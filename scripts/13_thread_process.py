#! -*- coding:utf-8 -*-


from multiprocessing import Process
from os import getpid
from random import randint
from threading import Thread, currentThread
from time import time, sleep


def download_task(filename, showinfo=0):
    """
    模拟下载函数
    :param filename:待下载的文件名称
    :param showinfo:0 打印 1 打印进程id 2 打印线程id
    :return:
    """
    if showinfo == 1:
        print('current pid %d' % getpid())
    elif showinfo == 2:
        print('current pid %s thread id %s' % (getpid(), currentThread().getName()))

    print("download begin %s..." % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s download finish, time cost %d' % (filename, time_to_download))


def serial_process():
    start = time()
    download_task('python.pdf')
    download_task('Hot.avi')
    end = time()
    print('total time cost:%d' % (end - start))


def multi_process():
    start = time()
    p1 = Process(target=download_task, args=('python.pdf', 1,))
    p2 = Process(target=download_task, args=('Hot.avi', 1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('total time cost:%d' % (end - start))


def multi_thread():
    start = time()
    t1 = Thread(target=download_task, args=('Python.pdf', 2,))
    t2 = Thread(target=download_task, args=('Hot.avi', 2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('total time cost:%d' % (end - start))


if __name__ == "__main__":
    serial_process()
    multi_process()
    multi_thread()