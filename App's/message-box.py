'''
This App illustrtes the use of message boxes in Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

window = Tk()
window.title("Message")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
window.geometry("400x200")

#Types of message boxes : showinfo   showwarning    showerror    askquestion    askokcancel     askyesno

def popup():
    response = messagebox.askyesno("Popup!", "Hello World!")
    #Label(window, text=response).pack()
    if response == 1:
        Label(window, text="U clicked YES!").pack()
    else:
        Label(window, text="U clicked NO!!").pack()

Button(window, text="Popup", command=popup).pack()

#event handler
window.mainloop()
