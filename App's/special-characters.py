'''
This App illustrates the use of Special Characters in Tkinter
'''
#Package
from tkinter import *

root = Tk()
root.title('Special Characters')
root.iconbitmap("D:/e-Learning/Tkinter/Images/india-flag.ico")
root.geometry("400x400")

l = Label(root, text='41' + u'\u00b0', font=("Helvetica", 30)).pack(pady=5)
#https://en.wikipedia.org/wiki/List_of_Unicode_characters

#event handler
root.mainloop()
