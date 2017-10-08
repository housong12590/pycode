from tkinter import *


class Window(object):
    def __init__(self):
        self.tk = Tk()
        self.tk.geometry('800x600+500+250')
        self.tk.title("数据采集")
        entry_text = StringVar()
        Entry(self.tk, textvariable=entry_text).grid(sticky="W")  # 单行文本输入
        entry_text.set("请输入搜索关键字")

        btn_text = StringVar()
        self.btn_search = Button(self.tk, bd=2, command=setSearchClickListener, textvariable=btn_text, width='6',
                                 height="1")
        btn_text.set("搜索")
        self.btn_search.grid(row=0, column=1)

    def search(self):
        print("search...")

    def setSearchClickListener(self, func):
        self.btn_search.bind("<Return>", func=func)

    def show(self):
        self.tk.mainloop()

def setSearchClickListener():
    print("asdfasdf")
