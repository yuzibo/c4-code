#!/usr/bin/python
# -*- coding: UTF-8 -*-


# File Name: tk1.py
# mail: tsu.yubo@gmail.com
# Created Time: 2019年06月21日 星期五 07时40分48秒


import sys
import os
from Tkinter import *
import tkMessageBox

class Gui(object):

    def __init__(self):
        self.top = Tk()
        self.top.geometry('400x200')
        self.top.resizable(width=False, height=True)
        self.text = Entry(self.top, text='show text')
        # 设置布局
        self.button1 = Button(self.top, text="start", command=self.get_text)
        self.button2 = Button(self.top, text="quit", command=self.top.quit)
        self.button3 = Button(self.top, text="run", command=self.write_file)
        #self.top.quit.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.text.pack()

        # mainloop

        self.top.mainloop()

    def get_text(self):
        text = test()
        self.text.insert(INSERT, text)

    def write_file(self):
        wrote_file = open('mn.py','w+')
        wrote_file.write('#!/usr/bin/python' + '\n' +self.text.get() + '\n')
        wrote_file.close()

def test():
    return "hello"

def main():
    Gui()

if __name__ == '__main__':
    main()

