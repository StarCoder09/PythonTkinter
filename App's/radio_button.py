'''
This App illustrates the use of radio buttons in Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("Frame")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
window.geometry("400x400")

#r = IntVar()
#r.set("1")

modes = [
    ("Pepperoni","Pepproni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
    ]

pizz = StringVar()
pizz.set("Pepperoni")

for text, mode in modes:
    Radiobutton(window, text=text, variable=pizz, value=mode).pack(anchor=W)
    

def click(value):
    label = Label(window, text=value).pack()

#Radiobutton(window, text="Option 1", variable=r, value=1, command=lambda: click(r.get())).pack()
#Radiobutton(window, text="Option 2", variable=r, value=2, command=lambda: click(r.get())).pack()
#Radiobutton(window, text="Option 3", variable=r, value=3, command=lambda: click(r.get())).pack()

#label = Label(window, text=pizz.get()).pack()

button = Button(window, text="Click Me!", command=lambda: click(pizz.get())).pack()

#event handler
window.mainloop()
