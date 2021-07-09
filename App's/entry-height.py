'''
This App illustrates how to give custom height to entry boxes in Tkinter
'''
#Packages
from tkinter import *

root = Tk()
root.title('Entry Height')
root.geometry("400x400")

def click():
    hello = "Hello " + e.get()
    lbl = Label(root, text=hello)
    e.delete(0, 'end')
    lbl.pack(pady=5)

e = Entry(root, width=50, font=('Helvetica', 30))
e.pack(padx=5, pady=5)

b = Button(root, text="Submit your Name", command=click)
b.pack(pady=5)

#event handler
root.mainloop()
