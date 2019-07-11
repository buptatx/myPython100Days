#! -*- coding:utf-8 -*-

import time
import tkinter
import tkinter.messagebox


def download():
    time.sleep(10)
    tkinter.messagebox.showinfo('info', 'download finish')


def show_about():
    tkinter.messagebox.showinfo('about', 'author:zhangpeng')


def tkinter_single_process_test():
    top = tkinter.Tk()
    top.title('single Process')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    b1 = tkinter.Button(panel, text='download', command=download)
    b1.pack(side='left')
    b2 = tkinter.Button(panel, text='about', command=show_about)
    b2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == "__main__":
    tkinter_single_process_test()