from tkinter import *
import Scherm

# TODO: evt. afbeeldingen bij weer
# TODO: Font selectie

def loop():
    label.config(text=Scherm.scherm())
    label.after(5000, loop)

root = Tk()
label = Label(master=root,
              background='lightblue',
              foregroun='white',
              font=('monospace', 50),
              width=30,
              height=10)
label.pack()
loop()
root.mainloop()