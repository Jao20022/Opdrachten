from tkinter import *
import Scherm


def loop():
    label.config(text=Scherm.scherm())
    label.after(5000, loop)

root = Tk()
label = Label(master=root,
              background='lightblue',
              foregroun='white',
              font=('Helvetica', 50),
              width=30,
              height=10)
label.pack()
loop()
root.mainloop()