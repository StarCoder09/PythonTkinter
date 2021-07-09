'''
This App Illustrates an Image viewer in Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("Image Viewer")
window.iconbitmap('D:/e-Learning/Tkinter/Images/p.ico')

my_img1 = ImageTk.PhotoImage(Image.open("D:/e-Learning/Tkinter/Images/calculator.ico"))
my_img2 = ImageTk.PhotoImage(Image.open("D:/e-Learning/Tkinter/Images/Database.ico"))
my_img3 = ImageTk.PhotoImage(Image.open("D:/e-Learning/Tkinter/Images/Delete.ico"))
my_img4 = ImageTk.PhotoImage(Image.open("D:/e-Learning/Tkinter/Images/find.ico"))
my_img5 = ImageTk.PhotoImage(Image.open("D:/e-Learning/Tkinter/Images/India-flag.ico"))
my_img6 = ImageTk.PhotoImage(Image.open("D:/e-Learning/Tkinter/Images/p.ico"))
my_img7 = ImageTk.PhotoImage(Image.open("D:/e-Learning/Tkinter/Images/speak.ico"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

status = Label(window, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
              
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(window, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(window, text="<<", command=lambda: back(image_num-1))
    if image_num == 7:
        button_forward = Button(window, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(window, text="Image " + str(image_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
def back(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(window, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(window, text="<<", command=lambda: back(image_num-1))
    if image_num == 1:
        button_back = Button(window, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(window, text="Image " + str(image_num) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(window, text="<<", command=back, state=DISABLED)
button_quit = Button(window, text="Exit program", command=window.quit)
button_forward = Button(window, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

#event handler
window.mainloop()
