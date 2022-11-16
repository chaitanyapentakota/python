from logging import root
import tkinter
from tkinter import *
from tkinter import messagebox
root= tkinter.Tk()
root.title("DEMO")
root.geometry("600x600")

def button():
    messagebox.showinfo("status","single ready to mingle")
b = Button(root,text="press here",command=button)
b.pack()    
root.mainloop()