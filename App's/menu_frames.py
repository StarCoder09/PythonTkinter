'''
This App illustrates the use of menu frames in Tkinter
'''
#Package
from tkinter import *

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.iconbitmap("D:/e-Learning/Tkinter/Images/india-flag.ico")
root.geometry("400x400")

menu = Menu(root)
root.config(menu=menu)

#create function - Logic Section
def new_command():
    hide_frame()
    new_frame.pack(fill="both", expand=1)
    l = Label(new_frame, text="You clicked the File >> new menu").pack()
def cut_command():
    hide_frame()
    edit_frame.pack(fill="both", expand=1)
    l = Label(edit_frame, text="You clicked the Edit >> cut menu").pack()
def copy_command():
    hide_frame()
    edit1_frame.pack(fill="both", expand=1)
    l = Label(edit1_frame, text="You clicked the Edit >> copy menu").pack()
def paste_command():
    hide_frame()
    edit2_frame.pack(fill="both", expand=1)
    l = Label(edit2_frame, text="You clicked the Edit >> paste menu").pack()
def find_command():
    hide_frame()
    option_frame.pack(fill="both", expand=1)
    l = Label(option_frame, text="You clicked the Option >> find menu").pack()
def undo_command():
    hide_frame()
    option1_frame.pack(fill="both", expand=1)
    l = Label(option1_frame, text="You clicked the Option >> undo menu").pack()
def redo_command():
    hide_frame()
    option2_frame.pack(fill="both", expand=1)
    l = Label(option2_frame, text="You clicked the Option >> redo menu").pack()

def hide_frame():
    for widget in new_frame.winfo_children():
        widget.destroy()
    for widget in edit_frame.winfo_children():
        widget.destroy()
    for widget in edit1_frame.winfo_children():
        widget.destroy()
    for widget in edit2_frame.winfo_children():
        widget.destroy()
    for widget in option_frame.winfo_children():
        widget.destroy()
    for widget in option1_frame.winfo_children():
        widget.destroy()
    for widget in option2_frame.winfo_children():
        widget.destroy()
    
    new_frame.pack_forget()
    edit_frame.pack_forget()
    edit1_frame.pack_forget()
    edit2_frame.pack_forget()
    option_frame.pack_forget()
    option1_frame.pack_forget()
    option2_frame.pack_forget()

#create menu item _ Layout Section
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

#create frames
new_frame = Frame(root, width=400, height=400, bg="red")
edit_frame = Frame(root, width=400, height=400, bg="blue")
edit1_frame = Frame(root, width=400, height=400, bg="green")
edit2_frame = Frame(root, width=400, height=400, bg="yellow")
option_frame = Frame(root, width=400, height=400, bg="red")
option1_frame = Frame(root, width=400, height=400, bg="green")
option2_frame = Frame(root, width=400, height=400, bg="blue")

#event handler
root.mainloop()
