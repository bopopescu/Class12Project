from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class MainWindow:
    def __init__(self, master):
        self.master=master
        self.master.geometry('1530x770+0+0')
        self.master.title("Hotel Management System")
        self.master.config(bg='powder blue')

        #======================================Frames============================================================

        frame = Frame(self.master)
        frame.grid()

        mainframe = Frame(frame)
        mainframe.pack(side=LEFT)

        sideframe = Frame(frame)
        sideframe.pack(side=RIGHT)

        topframe = Frame(mainframe, bd=14, bg='cadet blue', relief='ridge', height=100, width=1200)
        topframe.pack(side=TOP)

        midframe = Frame(mainframe, bd=14, bg='ghost white', relief='ridge', height=665, width=1200, padx=20, pady=20)
        midframe.pack(side=BOTTOM)

        leftframe = Frame(midframe, bd=14, bg='powder blue', relief='ridge', height=597, width=766)
        leftframe.pack(side=LEFT)

        rightframe = Frame(midframe, bd=14, bg='cadet blue', relief='ridge', height=597, width=366)
        rightframe.pack(side=RIGHT)

        buttonframe = Frame(sideframe, bd=14, bg='powder blue', relief='ridge', height=765, width=330)
        buttonframe.pack()


if __name__ == '__main__':
    root=Tk()
    application=MainWindow(root)
    root.mainloop()
