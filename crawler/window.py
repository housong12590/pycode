from tkinter import *


class Window(object):
    def __init__(self):
        self.tk = Tk()
        self.tk.title("数据采集")
        Entry(self.tk, text=" input your text here").pack()
        self.btn_search = Button(self.tk, bd=2, text=' 搜索', width='6', height="1")
        self.btn_search.pack()

    def search(self):
        print("search...")

    def setSearchClickListener(self, func):
        self.btn_search.bind("<Return>", func=func)

    def show(self):
        self.tk.mainloop()
