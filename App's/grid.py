'''
This App illustrates the use of .grid in Tkinter
'''
#Package
from tkinter import *

window = Tk()

#creating a label widget
label = Label(window, text="Hello World! ").grid(row=0, column=0)
label2 = Label(window, text="My name is Harshman Chatterjee").grid(row=1, column=0)

#shoving it on window
#label.grid(row=0, column=0)
#label2.grid(row=0, column=1)

#event handler
window.mainloop()
