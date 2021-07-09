'''
This App is to illustrate that how to apply color on buttons
'''
from tkinter import *

window = Tk()

def click():
    label = Label(window, text="Looky here! You clicked me!!!")
    label.pack()

#button
button = Button(window, text="Click Me!", command=click, fg="red", bg="#000000")
button.pack()

#event handler
window.mainloop()
