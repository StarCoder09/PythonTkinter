'''
This App illustrates how to use In-built color picker in Tkinter
'''
#Packages
from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title('Color Picker')
root.iconbitmap("D:/e-Learning/Tkinter/Images/india-flag.ico")
root.geometry("400x400")

def colour():
    color = colorchooser.askcolor()[1]
    lbl = Label(root, text=color).pack(pady=5)
    lbl_2 = Label(root, text="It's the colour u picked!", font=("Helvetica", 30), bg=color)
    lbl_2.pack()

btn = Button(root, text="Pick a color...", command=colour).pack()

#event handler
root.mainloop()
