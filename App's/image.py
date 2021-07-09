'''
This App illustrates a simple image viewer 
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("Images")
window.iconbitmap('D:/e-Learning/Tkinter/Images/p.ico')

my_img = ImageTk.PhotoImage(Image.open("Images/p.ico"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(window, text="Exit program", command=window.quit)
button_quit.pack()

#event handler
window.mainloop()
