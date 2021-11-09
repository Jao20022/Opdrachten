from tkinter import *
import Scherm


def loop():
    label.config(text=Scherm.scherm())
    label.after(5000, loop)

root = Tk()
label = Label(master=root)
label.pack(padx=40,pady=40)
loop()
root.mainloop()