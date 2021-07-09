'''
This App illustrates the use of label in Tkinter
'''
#Package
from tkinter import *

#create window
window = Tk()

#creating a label widget
label = Label(window, text="Hello World!")

#shoving it on window
label.pack()

#event handler
window.mainloop()
