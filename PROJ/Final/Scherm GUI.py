from tkinter import *
import Scherm

# TODO: evt. afbeeldingen bij weer
# TODO: Font selectie

def loop():
    label.config(text=Scherm.scherm())
    label.after(5000, loop)

root = Tk()
achter= Frame(master=root, background ='lightblue')
afbeelding=Frame(master=achter)
label = Label(master=achter,
              background='white',
              font=('monospace', 50),
              width=30,
              height=5)

achter.pack()
label.pack(side=LEFT,padx=100,pady=100)
loop()
root.mainloop()