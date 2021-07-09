'''
This App illustrates the menu options in Tkinter
'''
#Package
from tkinter import *

root = Tk()
root.title('Menu')
root.iconbitmap("D:/e-Learning/Tkinter/Images/india-flag.ico")
root.geometry("400x400")

menu = Menu(root)
root.config(menu=menu)

#create function - Logic Section
def new_command():
    l = Label(root, text="You clicked an New Dropdown option!").pack()
def cut_command():
    l = Label(root, text="You clicked an Cut Dropdown option!").pack()
def copy_command():
    l = Label(root, text="You clicked an Copy Dropdown option!").pack()
def paste_command():
    l = Label(root, text="You clicked an Paste Dropdown option!").pack()
def find_command():
    l = Label(root, text="You clicked an Find Dropdown option!").pack()
def undo_command():
    l = Label(root, text="You clicked an Undo Dropdown option!").pack()
def redo_command():
    l = Label(root, text="You clicked an Redo Dropdown option!").pack()

#create menu item - Layout Section
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_command)
edit_menu.add_command(label="Paste", command=paste_command)
edit_menu.add_command(label="Copy", command=copy_command)

option_menu = Menu(menu)
menu.add_cascade(label="Option", menu=option_menu)
option_menu.add_command(label="Find", command=find_command)
option_menu.add_command(label="Undo", command=undo_command)
option_menu.add_command(label="Redo", command=redo_command)

#event handler
root.mainloop()
