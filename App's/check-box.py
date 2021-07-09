'''
This App illustrates Check box in Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

window = Tk()
window.title("Check Boxes")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
window.geometry("400x400")

def show():
    lbl = Label(window, text=var.get()).pack()

var = StringVar()

c = Checkbutton(window, text="Check this box, I dare you!", variable=var, onvalue="Pizza", offvalue="Burger")
c.deselect()
c.pack()


btn = Button(window, text="Show selection", command=show).pack()

#event handler
window.mainloop()
