from tkinter import *
from tkinter.messagebox import showerror


def clicked():
    for i in range(0,200):
        bericht = "error"+' ' + str(i)
        showerror(title='getfucked', message=bericht)

root = Tk()
label = Label(text='tekst')
label.pack(pady=40,padx=40)

button = Button(master=root, text='FuckSHit', command=clicked)
button.pack()

root.mainloop()