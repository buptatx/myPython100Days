#! -*- coding:utf-8 -*-

import time
import tkinter
import tkinter.messagebox
from threading import Thread


def test_async_process():
    class DownloadHandler(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('info', 'download finish')
            b1.config(state=tkinter.NORMAL)

    def download():
        b1.config(state=tkinter.DISABLED)
        DownloadHandler(daemon=True).start()

    def show_info():
        tkinter.messagebox.showinfo('about', 'author:zhangpeng')

    top = tkinter.Tk()
    top.title('single_async_process')
    top.geometry('250x160')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    b1 = tkinter.Button(panel, text='download', command=download)
    b1.pack(side='left')
    b2 = tkinter.Button(panel, text='about', command=show_info)
    b2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == "__main__":
    test_async_process()
