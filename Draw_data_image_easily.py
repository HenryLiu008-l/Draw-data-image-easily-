import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# 设置字体参数以正常显示中文
plt.rcParams["font.sans-serif"] = "SimHei"

#获取文件地址
def folder_path():
    global folder_path
    root=tk.Tk()
    root.withdraw()
    folder_path=filedialog.askopenfilename()

#创建窗口
win1=tk.Tk()
win1.title('auto_analyse_Data')
a1=win1.maxsize()
k,g=a1
win1.geometry(f'300x300+{k//3}+{g//3}')

#创建顶部菜单
menubar=Menu(win1)
win1.config(menu=menubar)
menubar.add_command(label='文件',command=folder_path)

#创建选项
var1=tk.IntVar()
var2=tk.IntVar()
def show():
    num1=var1.get()
    num2=var2.get()
    if num1==1:
        label1.config(text='文件为Excel格式')
    else:
        label1.config(text='文件为CSV格式')
    if num2==1:
        label2.config(text='生成折线图')
    elif num2==2:
        label2.config(text='生成柱状图')
    else:
        label2.config(text='生成点状图')
var1.set(1)
var2.set(1)
label1=tk.Label(win1,text='默认选项为Excel',width=30,bg='lightyellow')
label2=tk.Label(win1,text='默认生成折线图',width=30,bg='lightyellow')
label1.pack()
label2.pack()

#方便创建选项
class Var():
    def __init__(self,win,name,variable,value,command):
        self.name=name
        self.variable=variable
        self.value=value
        self.var=tk.Radiobutton(win,text=name,variable=variable,value=value,command=command)

#创建选项
Excel=Var(win1,'Excel',var1,1,show)
Csv=Var(win1,'Csv',var1,2,show)
Plot=Var(win1,'Plot',var2,1,show)
Bar=Var(win1,'Bar',var2,2,show)
Scatter=Var(win1,'Scatter',var2,3,show)
Excel.var.place(x=90,y=50)
Csv.var.place(x=160,y=50)
Plot.var.place(x=50,y=70)
Bar.var.place(x=120,y=70)
Scatter.var.place(x=190,y=70)

#关闭窗口时终止程序
win1.protocol(name='WM_DELETE_WINDOW',func=exit)

#数据可视化
def read():
    global dataFrame
    if var1.get()==1:
        dataFrame=pd.read_excel(folder_path)
    else:
        dataFrame=pd.read_csv(folder_path,encoding="utf-8")
    plt.figure(figsize=(10,5),facecolor='white')
def visual():
    if var2.get()==1:
        plt.plot(dataFrame[s1.get()],dataFrame[s2.get()],marker='o',color='orange',label=s2.get())
    elif var2.get()==2:
        plt.bar(dataFrame[s1.get()],dataFrame[s2.get()],label=s2.get())
    else:
        plt.scatter(dataFrame[s1.get()],dataFrame[s2.get()],label=s2.get())
    plt.xlabel(s1.get())
    plt.ylabel(s2.get())
    plt.legend()
    plt.tight_layout()
    plt.show()
    plt.close()

#创建子窗口
def child_win():
    child_win=tk.Toplevel()
    child_win.geometry(f'300x300+{k//3}+{g//3}')
    child_win.title('值的操作')
    s3=tk.StringVar()
    s4=tk.StringVar()
    s5=tk.StringVar()
    e3=Entry_Label(child_win,s3,'对象1',120,30)
    e4=Entry_Label(child_win,s4,'值or对象2',120,70)
    e5=Entry_Label(child_win,s5,'增加列名',120,110)
    var3=tk.IntVar()
    def method():
        num=var3.get()
        if num==1:
            label3.config(text='修改值')
        elif num==2:
            label3.config(text='求和')
        elif num==3:
            label3.config(text='求差')
        elif num==4:
            label3.config(text='求极')
        else:
            label3.config(text='求商')
    var3.set(1)
    label3=tk.Label(child_win,text='默认修改值',width=30,bg='lightyellow')
    label3.pack()
    change=Var(child_win,'Change',var3,1,method)
    sum=Var(child_win,'Sum',var3,2,method)
    difference=Var(child_win,'Difference',var3,3,method)
    product=Var(child_win,'Product',var3,4,method)
    quotient=Var(child_win,'Quotient',var3,5,method)
    change.var.place(x=20,y=160)
    sum.var.place(x=80,y=160)
    difference.var.place(x=20,y=180)
    product.var.place(x=80,y=180)
    quotient.var.place(x=20,y=200)
    def option():
        if var3.get()==1:
            dataFrame[s3.get()]=float(s4.get())
        elif var3.get()==2:
            dataFrame[s5.get()]=dataFrame[s3.get()]+dataFrame[s4.get()]
        elif var3.get()==3:
            dataFrame[s5.get()]=dataFrame[s3.get()]-dataFrame[s4.get()]
        elif var3.get()==4:
            dataFrame[s5.get()]=dataFrame[s3.get()]*dataFrame[s4.get()]
        else:
            dataFrame[s5.get()]=dataFrame[s3.get()]/dataFrame[s4.get()]
    tk.Button(child_win,text='执行',command=option).place(x=180,y=170)
    child_win.mainloop()

#创建输入框
s1=tk.StringVar()
s2=tk.StringVar()
class Entry_Label():
    def __init__(self,win,textvariable,text,x,y):
        self.enrty=tk.Entry(win,textvariable=textvariable,width=10,font=('黑体',10)).place(x=x,y=y)
        self.lable=tk.Label(win,text=text,font=('黑体',10)).place(x=x/2-10,y=y)
e1=Entry_Label(win1,s1,'X轴选取',120,110)
e2=Entry_Label(win1,s2,'Y轴选取',x=120,y=150)
tk.Button(win1,text='读取',command=read,width=10).place(x=20,y=180)
tk.Button(win1,text='生成',command=visual,width=10).place(x=200,y=180)
tk.Button(win1,text='增改值',command=child_win,width=10).place(x=110,y=180)
win1.mainloop()