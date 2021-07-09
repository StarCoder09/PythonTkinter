'''
This App illutrates a Calculator in Tkinter
'''
#Packages
from tkinter import *

window = Tk()
window.title("Calculator")
window.iconbitmap('D:/e-Learning/Tkinter/Images/calculator.ico')

#Logic Section
e = Entry(window, width=50, borderwidth=5) 
e.grid(row=0, column=0, columnspan=3,  padx=10, pady=10)

def b_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def b_point():
    current = e.get()
    e.insert(0, str("."))

def b_clear():
    e.delete(0, END)

def b_add():
    fst_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(fst_num)
    e.delete(0, END)

def b_equal():
    scd_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(scd_num))
    if math == "subtraction":
        e.insert(0, f_num - float(scd_num))
    if math == "multiplication":
        e.insert(0, f_num * float(scd_num))
    if math == "division":
        e.insert(0, f_num / float(scd_num))
    if math == "modulus":
        e.insert(0, f_num % float(scd_num))

def b_minus():
    fst_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(fst_num)
    e.delete(0, END)

def b_mul():
    fst_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(fst_num)
    e.delete(0, END)

def b_div():
    fst_num = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(fst_num)
    e.delete(0, END)

#doesn't work at the moment, pls provide suggestions for how to make % work.
def b_mod():
    fst_num = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = float(fst_num)
    e.delete(0, END)

#define buttons - Layout Section
button1 = Button(window, text="1", padx=40, pady=20, command=lambda: b_click(1))
button2 = Button(window, text="2", padx=40, pady=20, command=lambda: b_click(2))
button3 = Button(window, text="3", padx=40, pady=20, command=lambda: b_click(3))
button4 = Button(window, text="4", padx=40, pady=20, command=lambda: b_click(4))
button5 = Button(window, text="5", padx=40, pady=20, command=lambda: b_click(5))
button6 = Button(window, text="6", padx=40, pady=20, command=lambda: b_click(6))
button7 = Button(window, text="7", padx=40, pady=20, command=lambda: b_click(7))
button8 = Button(window, text="8", padx=40, pady=20, command=lambda: b_click(8))
button9 = Button(window, text="9", padx=40, pady=20, command=lambda: b_click(9))
button0 = Button(window, text="0", padx=40, pady=20, command=lambda: b_click(0))

button_P = Button(window, text=".", padx=42, pady=20, command=b_point)
button_equal = Button(window, text="=", padx=39, pady=20, command=b_equal)
button_clear = Button(window, text="C", padx=40, pady=20, command=b_clear)

button_add = Button(window, text="+", padx=39, pady=20, command=b_add)
button_minus = Button(window, text="-", padx=40, pady=20, command=b_minus)
button_mul = Button(window, text="x", padx=39, pady=20, command=b_mul)
button_div = Button(window, text="/", padx=41, pady=20, command=b_div)
button_mod = Button(window, text="%", padx=38, pady=20, command=b_mod)

#putting button on screen
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=0)

button_add.grid(row=4, column=1)
button_minus.grid(row=5, column=1)
button_mul.grid(row=5, column=0)
button_div.grid(row=5, column=2)
button_mod.grid(row=6, column=1)
button_P.grid(row=4, column=2)

button_equal.grid(row=6, column=0)
button_clear.grid(row=6, column=2)

#event handler
window.mainloop()
