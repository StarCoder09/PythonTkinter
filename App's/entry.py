'''
This App show the use of entry box in Tkinter
'''
#Package
from tkinter import *

window = Tk()

e = Entry(window, width=50,) #bg="yellow", fg="red", borderwidth=10
e.pack()
e.insert(0, "Enter ur name:")

def click():
    hello = "Hello " + e.get()
    label = Label(window, text=hello)
    label.pack()

button = Button(window, command=click, fg="red", bg="#000000")
button.pack()

#event handler
window.mainloop()
