'''
This App is to Illustrate the use of .grid_forget in Tkinter
'''
#Package
from tkinter import *

root = Tk()
root.title('Overwrite Labels by deleting last read.')
root.iconbitmap("D:/e-Learning/Tkinter/Images/India-flag.ico")
root.geometry("400x400")

myLabel = Label(root)

'''def myDelete():
    myLabel.grid_forget()
    #myLabel.destroy()
    myButton['state'] = NORMAL
    #print(myButton.winfo_exists())
    DeleteButton['state'] = DISABLED
'''

def myClick():
    global myLabel
    myLabel.destroy()
    
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    
    e.delete(0, 'end')
    myLabel.grid(row=3, column=0, pady=10)
    #myButton['state'] = DISABLED
    #DeleteButton['state'] = NORMAL

e = Entry(root, width=17, font=('Helvetica', 30))
e.grid(row=0, column=0, padx=10, pady=10)

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.grid(row=1, column=0, pady=10)

#DeleteButton = Button(root, text="Delete Text", command=myDelete)
#DeleteButton.grid(row=2, column=0, pady=10)

#event handler
root.mainloop()
