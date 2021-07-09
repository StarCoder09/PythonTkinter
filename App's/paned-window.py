'''
This App illustrates the use of paned windows(resizing windows) in Tkinter 
'''
#Package
from tkinter import *

root = Tk()
root.title('Paned Windows')
root.iconbitmap("D:/e-Learning/Tkinter/Images/india-flag.ico")
root.geometry("400x400")

#Panels
panel_1 = PanedWindow(bd=4, relief="raised", bg="red")
panel_1.pack(fill=BOTH, expand=1)

left = Label(panel_1, text="Left Panel")
panel_1.add(left)

panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
panel_1.add(panel_2)

top = Label(panel_2, text="Top Panel")
panel_2.add(top)

bottom = Label(panel_2, text="Bottom Panel")
panel_2.add(bottom)

#event handler
root.mainloop()
