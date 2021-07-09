'''
This App is to Illustrate the use of .pack_forget() in Tkinter
'''
#Package
from tkinter import *

root = Tk()
root.title('...')
root.iconbitmap("D:/e-Learning/Tkinter/Images/India-flag.ico")
root.geometry("400x400")

def myDelete():
    #myLabel.pack_forget()
    myLabel.destroy()
    myButton['state'] = NORMAL
    #print(myButton.winfo_exists())
    DeleteButton['state'] = DISABLED

def myClick():
    global myLabel
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    e.delete(0, 'end')
    myLabel.pack(pady=10)
    myButton['state'] = DISABLED
    DeleteButton['state'] = NORMAL

e = Entry(root, width=50, font=('Helvetica', 30))
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack(pady=10)

DeleteButton = Button(root, text="Delete Text", command=myDelete)
DeleteButton.pack(pady=10)

#event handler
root.mainloop()
