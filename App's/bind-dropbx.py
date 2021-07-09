'''
This App is to Illustrate the use of Dropboxes in Tkinter
'''
#Packages
from tkinter import *
from tkinter import ttk

root = Tk()
#window title
root.title('DropBox')
root.iconbitmap("D:/e-Learning/Tkinter/Images/india-flag.ico")
root.geometry("400x400")

def select(event):
    if click.get() == "Sunday":
        lbl = Label(root, text="Yay! It's Sunday !").pack(pady=20)
    else:
        lbl = Label(root, text=click.get()).pack(pady=20)

def comboed(event):
    if combo.get() == "Sunday":
        lbl = Label(root, text="Yay! It's Sunday !").pack(pady=20)
    else:
        lbl = Label(root, text=combo.get()).pack(pady=20)

#options
opt = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]

click = StringVar()
click.set(opt[0])

drop = OptionMenu(root, click, *opt, command=select).pack(pady=20)

combo = ttk.Combobox(root, value=opt)
combo.current(0)
combo.bind("<<ComboboxSelected>>", comboed)
combo.pack()

#btn = Button(root, text="Select from list", command=select)
#btn.pack(pady=20)

#event handler
root.mainloop()
