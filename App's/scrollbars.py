'''
This App illustrates how to use scroll bar in Tkinter
'''
#Packeges
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Scroll Bars')
root.iconbitmap("D:/e-Learning/Tkinter/Images/india-flag.ico")
root.geometry("500x500")

#create main frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

#create canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#add scroll bar to canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

#create frame inside canvas
sec_frame = Frame(my_canvas)

#add new frame to window in canvas
my_canvas.create_window((0,0), window=sec_frame, anchor="nw")

lbl = Label(sec_frame, text="Scroll to the bottom!!").grid(row=0, column=0, pady=5, padx=5)

for thing in range(100):
    Button(sec_frame, text=f'Button {thing} Yo!').grid(row=thing+1, column=0, pady=5, padx=5)

lbl = Label(sec_frame, text="This text should appear when you scroll to the bottom!!").grid(row=thing+2, column=0, pady=5, padx=5)

#event handler
root.mainloop()
