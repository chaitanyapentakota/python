from distutils.command.build_scripts import first_line_re
from tkinter import *
mw= Tk()
mw.title('calculator')

def clear():
    db.delete(0,END)

def but_clk(num):
    cur_num= db.get()
    clear()
    f_num= cur_num + num
    db.insert(0,f_num)

first_num=0
math = ''

def caluclator(math_type):
    global first_num, math
    math= math_type
    first_num= db.get()
    clear()

def equal():
    result=''

    global first_num
    seconf_num = db.get()
    clear()
    if math=='add':
        result = int(first_num)+ int(seconf_num)
    elif math=='sub':
        result = int(first_num) - int(seconf_num)
    if math=='mul':
        result = int(first_num) * int(seconf_num)
    if math=='div':
        result = int(first_num) // int(seconf_num)        

    db. insert(0,str(result))    





db = Entry(mw, width=14, font=('arial',28), justify=RIGHT)
but_0= Button(mw,text='0',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('0'))
but_1= Button(mw,text='1',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('1'))
but_2= Button(mw,text='2',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('2'))
but_3= Button(mw,text='3',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('3'))
but_4= Button(mw,text='4',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('4'))
but_5= Button(mw,text='5',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('5'))
but_6= Button(mw,text='6',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('6'))
but_7= Button(mw,text='7',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('7'))
but_8= Button(mw,text='8',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('8'))
but_9= Button(mw,text='9',padx=36,pady=10,font=('arial',14),command=lambda:but_clk('9'))
but_clr= Button(mw, text='clear',padx=74,pady=10,font=('arial',14), command= clear)
but_div= Button(mw,text='//',padx=38,pady=10,font=('arial',14), command=lambda:caluclator('div'))
but_mul= Button(mw,text='*',padx=38,pady=10,font=('arial',14), command=lambda:caluclator('mul')) 
but_sub= Button(mw,text='-',padx=38,pady=10,font=('arial',14), command=lambda:caluclator('sub'))
but_add= Button(mw,text='+',padx=36,pady=10,font=('arial',14), command=lambda:caluclator('add'))
but_equal= Button(mw,text='=',padx=36,pady=40,font=('arial',14),command=equal)  




but_equal.grid(row=5,column=2,rowspan=2, padx=2,pady=2)
but_add.grid(row=6,column=1,padx=2,pady=2)
but_sub.grid(row=6,column=0,padx=2,pady=2)
but_mul.grid(row=5,column=1,padx=2,pady=2)
but_div.grid(row=5,column=0,padx=2,pady=2)

but_clr.grid(row=4,column=1,columnspan=2,padx=2,pady=2)
but_0.grid(row=4,column=0,padx=2,pady=2)

but_1.grid(row=3,column=0,padx=2,pady=2)
but_2.grid(row=3,column=1,padx=2,pady=2)
but_3.grid(row=3,column=2,padx=2,pady=2)

but_4.grid(row=2,column=0,padx=2,pady=2)
but_5.grid(row=2,column=1,padx=2,pady=2)
but_6.grid(row=2,column=2,padx=2,pady=2)

but_7.grid(row=1,column=0,padx=2,pady=2)
but_8.grid(row=1,column=1,padx=2,pady=2)
but_9.grid(row=1,column=2,padx=2,pady=2)

db.grid(row=0,column=0, columnspan=3, padx=10,pady=10)

mw.mainloop()