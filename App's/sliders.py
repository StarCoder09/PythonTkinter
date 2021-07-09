'''
This App illustrates the use of Sliders to set window size in Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

window = Tk()
window.title("Sliders")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
window.geometry("400x400")

def slide1():
    #lbl = Label(window, text=horizontal.get()).pack()
    window.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

#def slide2(var):
    #lbl = Label(window, text=vertical.get()).pack()
    #window.geometry(str(vertical.get()) + "")

vertical = Scale(window, from_=0, to=650)
vertical.pack()

horizontal = Scale(window, from_=0, to=1300, orient=HORIZONTAL)
horizontal.pack()

#lbl = Label(window, text=horizontal.get()).pack()

btn = Button(window, text="Click to fetch size!", command=slide1).pack()
#btn2 = Button(window, text="Click to fetch vertical", command=slide2).pack()

#event handler
window.mainloop()
