'''
This App illustrates the use of Matplotlib-pyplot in Tkinter
'''
#Packages
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

window = Tk()
window.title("Plots")
window.iconbitmap('D:/e-Learning/Tkinter/Images/India-flag.ico')
window.geometry("200x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50) #go to matplotlib website to explore more...
    plt.show()

btn = Button(window, text="Graph It", command=graph).pack()

#event handler
window.mainloop()
