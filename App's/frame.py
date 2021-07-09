'''
This App illustrates the use of frames in Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("Frame")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')

frame = LabelFrame(window, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Do not Click Me!!!")
b2 = Button(frame, text="Do not Click Me!!!")
b.grid(row=0, column=0)
b2.grid(row=0, column=1)

#event handler
window.mainloop()
