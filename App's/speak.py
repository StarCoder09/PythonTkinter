'''
This App is a Text-to-Speech Recognition App in Tkinter
'''
#Packages
from tkinter import *
import pyttsx3

#check pyttsx3 documentation at python.org for knowing how to edit this code.

root = Tk()
root.title('Text to Speech App')
root.iconbitmap("D:/e-Learning/Tkinter/Images/speak.ico")
root.geometry("400x400")

def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 120) # <- speed of voice
    volume = engine.getProperty('volume')   
    #print (volume)       <- volume                  
    engine.setProperty('volume',1.0)
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0, END)

lbl = Label(root, text="Write Something Below!", font=("Helvetica", 25))
lbl.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 25))
my_entry.pack(pady=20)

button = Button(root, text="Speak", command=talk)
button.pack(pady=20)

#event handler
root.mainloop()
