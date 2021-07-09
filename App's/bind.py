'''
This App is to illustrate binding keyboard events,
events are listed, just change them to see what happens...
'''
#Packages
from tkinter import *

root = Tk()
root.title('KeyBoard Key Binder')
root.iconbitmap("D:/e-Learning/Tkinter/Images/india-flag.ico")
root.geometry("400x400")

def click(event):
    lbl = Label(root, text="You Clicked this Button : " + event.keysym)
    #+ event.char)#+ str(event.x) + " " + str(event.y) <- add this to above to get cursor location
    lbl.pack()

btn = Button(root, text="Click Me!")
btn.bind("<Key>", click)

'''
#   events   #
Button-1: message appears when you left click on button
Button-2: message appears when you click on scroll button on button
Button-3: message appears when you right click on button
Enter   : move cursor in the button to see magic
Leave   : move cursor out of button to see magic
FocusIn : tab to highlight button
FocusOut: tab to highlight button
Return  : press tab to highlight button then press enter key
Key     : press tab to highlight button the any key on keyboard to see magic
'''
btn.pack(pady=20)

#event handler
root.mainloop()
