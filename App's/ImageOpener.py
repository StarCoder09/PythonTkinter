'''
This App is to Illustrate that how to open an second window on click of a button.
'''

#Packages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

window = Tk()
#window title
window.title("Image Window Opener")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')

def open():
    global img
    top = Toplevel()
    #window title
    top.title("Second Image Window")
    top.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
    #lbl = Label(top, text="Hello World").pack()
    img = ImageTk.PhotoImage(Image.open("D:/e-Learning/Tkinter/Images/Assam.png"))
    lbl2 = Label(top, image=img).pack()
    #second button
    btn = Button(top, text="Close Window", command=top.destroy).pack()

#button
btn = Button(window, text="Click to view second window", command=open).pack()

#event handler
window.mainloop()
