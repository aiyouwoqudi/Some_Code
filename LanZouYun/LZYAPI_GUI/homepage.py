#-*- coding:utf-8 -*-
from tkinter import *
from tkinter import font
from tkinter.ttk import Combobox
from tkinter import filedialog
import tkinter.messagebox
import os
import re
# 网盘部分
from lanzou.api import LanZouCloud

lzy = LanZouCloud()

# 名单
listdictionary = ['1567119224-陈信靖','1767112226-王浩宇','1767119201-王化东','1767119202-李齐保','1767119203-贺世超','1767119204-孟德明',
                    '1767119206-陈佳豪','1767119207-马钰彭','1767119209-许盼','1767119210-杨科','1767119211-马寅秋','1767119212-代春辉',
                    '1767119213-马宗阳','1767119214-尹嘉硕','1767119215-孙宇','1767119216-于淞','1767119217-李纪研','1767119218-王志强',
                    '1767119219-李辉','1767119220-杜文杰','1767119221-张晓博','1767119222-周晓阳','1767119223-温启','1767119224-冯琦',
                    '1767119225-黄燕坤','1767119226-薄雄峰','1767119227-唐骁','1767119228-魏楠','1767119229-顾发琛','1767119230-吴奕',
                    '1767119231-冯佳祎','1767119232-胡月英','1767119233-王慧','1767119235-赵凤杰','1767119236-孟玲慧','1767119237-张先苇',
                    '1767119238-武园园','1767119239-王乐乐','1767119240-马佳欣','1767119241-王娜娜','1768127305-李品帅','1774146331-忻五园',
                    '1774153221-陈昊'
                ]

cookie = {'ylogin': '1729256',
            'UM_distinctid': '75cc291e0d54-096f78fe735993-230346c-144000-175cc291e0e6b',
            'folder_id_c': '-1',
            'PHPSESSID': '6uokp3g66rvobna8m98qcueec111461',
            'CNZZDATA1253610886': '1691681055-1605446183-https%253A%252F%252Fup.woozooo.com%252F%7C1605451585',
            'phpdisk_info': 'VWACNwNjV2IDMw9qXDABUgBkAQoIYAFjUmRVMQcxAzBYbF9tDGwGOg49UwpZZ1I9UzUBMAE8VmUOOVc%2FDj4HNVUwAjADaFc4AzgPO1wwAWoAMwFlCDUBNFI1VWcHOANiWGVfbgxoBjwOOFM1WQpSOVM2ATYBbFYxDjxXNw44BzdVYQIx'
            }




def UploadFile(cox1,lb10):
    if lzy.login_by_cookie(cookie) == LanZouCloud.SUCCESS == LanZouCloud.SUCCESS:
        print('登录成功')
    else:
        print('登陆失败')
    code = lzy.upload_file(lb10['text'],cox1.get())
    if code != LanZouCloud.SUCCESS:
        print('上传失败!')
    if code == LanZouCloud.SUCCESS:
        print('上传成功!')


def UploadFileRename(lb5,lb10):
    # srcFile = r'C:\Users\MaZongYang\Desktop\111111.txt'
    # dstFile = r'C:\Users\MaZongYang\Desktop\这是啥.txt'
    try:
        os.rename(lb5['text'],lb10['text'])
    except Exception as e:
        print(e)
        print('rename file fail\r\n')
    else:
        print('rename file success\r\n')


def ConfirmationInformation(ey1,ey2,lb5,lb10,lb13):
    i = 0
    Studentnumbername = ey1.get()+ "-" + ey2.get()
    for sjb in listdictionary:
        i = i + 1
        if(Studentnumbername == sjb):
            tkinter.messagebox.showinfo('确认信息',"当前上传信息：\n" + Studentnumbername + "\n勿改动")
            parent_dir = os.path.dirname(lb5['text'])
            bs64_str = re.findall(r"\.(.+?)$",lb5['text'])[0]
            lb10['text'] = parent_dir + "/" + Studentnumbername + "." + bs64_str
            lb13['text'] = "修改文件名.成功"
            break
        if(Studentnumbername != sjb and i == 43):
            tkinter.messagebox.showinfo('错误',"检查学号-姓名，并重新输入")


def SelectUploadFile(lb5):
    file_path = filedialog.askopenfilename()
    lb5['text'] = file_path


def upload():
    global hp
    hp.destroy()
    up = Tk()
    up.title("电子版作业提交程序")  
    up.resizable(0,0)
    # 窗口大小以、位置以及颜色
    width = 430
    heigh = 500
    screenwidth = up.winfo_screenwidth()
    screenheight = up.winfo_screenheight()
    up.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    up.configure(bg='#ADD8E6')
    lb0=Label(up, text='ylogin：', font=(10), bg='#ADD8E6')
    lb0.grid(row=0,column=0,sticky=E)
    lb1=Label(up, text='1729256(0201)', font=(10), bg='#ADD8E6')
    lb1.grid(row=0,column=1,sticky=W)
    lb2=Label(up, text='------------选择框------------',font=(10), bg='#ADD8E6')
    lb2.grid(row=1,column=1)
    lb3=Label(up, text='上传目录：', font=(10), bg='#ADD8E6')
    lb3.grid(row=2,column=0,sticky=E)
    cox1=Combobox(up, width = 12, height = 8)
    cox1.grid(row=2,column=1,sticky=W)
    lb4=Label(up, text='选择文件：', font=(10), bg='#ADD8E6')
    lb4.grid(row=3,column=0,sticky=E)
    lb5=Label(up, text='', font=(5), bg='#FFFFFF', width=30, anchor=E)
    lb5.grid(row=3,column=1,sticky=E)
    bt1=Button(up, text='选择文件', bg='#DCDCDC', command=lambda: SelectUploadFile(lb5))
    bt1.grid(row=3,column=2,padx=5)
    lb6=Label(up, text='------------信息框------------',font=(10), bg='#ADD8E6')
    lb6.grid(row=4,column=1)
    lb7=Label(up, text='学    号：', font=(10), bg='#ADD8E6')
    lb7.grid(row=5,column=0,sticky=E,pady=5)
    ey1=Entry(up,width=30)
    ey1.grid(row=5,column=1,sticky=W)
    lb8=Label(up, text='姓    名：', font=(10), bg='#ADD8E6')
    lb8.grid(row=6,column=0,sticky=E)
    ey2=Entry(up,width=30)
    ey2.grid(row=6,column=1,sticky=W)
    bt3=Button(up, text='确认输入', bg='#DCDCDC', command=lambda: ConfirmationInformation(ey1,ey2,lb5,lb10,lb13))
    bt3.grid(row=6,column=2,padx=5)
    lb9=Label(up, text='上传格式：', font=(10), bg='#ADD8E6')
    lb9.grid(row=7,column=0,sticky=E)
    lb10=Label(up, text='', font=(10), bg='#FFFFFF', width=30, anchor=E)
    lb10.grid(row=7,column=1,sticky=E)
    bt2=Button(up, text='确认选择', bg='#DCDCDC', command=lambda: UploadFileRename(lb5,lb10))
    bt2.grid(row=7,column=2,pady=5)
    bt4=Button(up, text='开始上传', bg='#DCDCDC', command=lambda: UploadFile(cox1,lb10), width=30)
    bt4.grid(row=8,column=1,pady=5)
    lb11=Label(up, text='------------回执框------------',font=(10), bg='#ADD8E6')
    lb11.grid(row=9,column=1)
    lb12=Label(up, text='提交结果：', font=(10), bg='#ADD8E6')
    lb12.grid(row=10,column=0,sticky=E)
    lb13=Label(up, text='Wait...', font=(10), bg='#ADD8E6', width=30, anchor=W)
    lb13.grid(row=10,column=1,sticky=W)


    if lzy.login_by_cookie(cookie) == LanZouCloud.SUCCESS == LanZouCloud.SUCCESS:
        sub_dirs = lzy.get_dir_list(2577257)
        sss = str(sub_dirs)
        bs64_str = re.findall(r"id=(.+?),",sss)
        cox1["value"] = bs64_str    # #给下拉菜单设定值
        cox1.current()




def main():
    hp.title('')
    hp.resizable(0,0)
    width = 200
    heigh = 200
    screenwidth = hp.winfo_screenwidth()
    screenheight = hp.winfo_screenheight()
    hp.geometry('%dx%d+%d+%d'%(width, heigh, (screenwidth-width)/2, (screenheight-heigh)/2))
    hp.configure(bg='#ADD8E6') 
    Label(hp, text='准备提交作业\n点击下方按钮', font=('隶书', 20), cursor='clock', bg='#ADD8E6').place(x=15, y=30)
    Button(hp, text='提交作业', bg='#DCDCDC', command=upload).place(x=70, y=120) 
    Button(hp, text='  退  出  ', bg='#DCDCDC', command=hp.quit).place(x=70, y=160) 
    hp.mainloop()


hp = Tk()
main()