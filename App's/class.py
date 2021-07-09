'''
This App illustrates that how to use Classes in Tkinter
'''
from tkinter import *

root = Tk()
root.title('Class Example')
root.iconbitmap("D:/e-Learning/Tkinter/Images/india-flag.ico")
root.geometry("400x400")

class elder:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.btn = Button(master, text="Click Me!", command=self.clicker)
        self.btn.pack(pady=20)

    def clicker(self):
        print("Look at u...u clicked a button!") #<-- prints on the terminal
        
e = elder(root)

#event handler
root.mainloop()
