'''
This App id to illustrates how to use dropdown boxes with Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

window = Tk()
window.title("Drop Boxes")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
window.geometry("400x400")

#Drop Down Boxes

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]

def show():
    lbl = Label(window, text=click.get()).pack()

click = StringVar()
click.set(options[0])

drop = OptionMenu(window, click, *options)
drop.pack()

btn = Button(window, text="Show Selected", command=show).pack()

#event handler
window.mainloop()
