'''
This App illustrates how to open files with Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog

window = Tk()
window.title("Files")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
window.geometry("500x500")

def open():
    global img
    window.filename = filedialog.askopenfilename(initialdir="D:/e-Learning/Tkinter/Images", title="Select a file", filetypes=(("png files", "*.png"),("all files", "*.*")))
    #lbl =Label(window, text=window.filename).pack()
    img = ImageTk.PhotoImage(Image.open(window.filename))
    img_lbl = Label(image=img).pack()

btn = Button(window, text="Open an Image!", command=open).pack()

#event handler
window.mainloop()
