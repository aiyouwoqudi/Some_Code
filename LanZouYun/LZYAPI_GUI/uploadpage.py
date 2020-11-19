from tkinter import *


def upload():
    loginFrame = Tk()
    loginFrame.title("电子版作业提交程序")  
    # 窗口大小以、位置以及颜色
    width = 430
    heigh = 500
    screenwidth = loginFrame.winfo_screenwidth()
    screenheight = loginFrame.winfo_screenheight()
    loginFrame.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    loginFrame.configure(bg='#ADD8E6') 
    Button( loginFrame, text='Button', bg='gray').pack()
    loginFrame.withdraw()
    