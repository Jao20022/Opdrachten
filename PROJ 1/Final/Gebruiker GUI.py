from tkinter import *
import Gebruiker


def reset(): # Leegt de error en success label
    errorLabel.config(text='')
    status.config(text='')


def verstuur(): # Wanneer gebruiker op verstuur knop drukt, voegt deze functie het toe aan de daatabase.
    status.config(text='')
    naam = Gebruiker.naam_controle(naamEntry.get())
    bericht = berichtEntry.get()
    code = Gebruiker.bericht_check(bericht)
    if code < 1:
        error(code)
    if code == 1:
        print('success')
        errorLabel.config(text='')
        if Gebruiker.export(bericht, naam):
            status.config(text='Succesvol verstuurd')
    status.after(5000, reset) # reset de GUI na 5 seconden voor de volgende gebruiker


def error(code): # Geeft error afhankelijk van de situatie
    if code == 0:
        print("veld leeg")
        errorLabel.config(text="*veld leeg")
    elif code == -1:
        print('Te lang')
        errorLabel.config(text="*Bericht te lang")


# GUI
root = Tk()
naamFrame = Frame(master=root)
berichtFrame = Frame(master=root)

# Veld voor Naam
naamLabel = Label(master=naamFrame, text="Vul je naam in (optioneel):")
naamEntry = Entry(master=naamFrame)

# Veld voor Bericht
berichtLabel = Label(master=berichtFrame, text="vul je bericht in max 140 karakters:")
berichtEntry = Entry(master=berichtFrame)


# Verstuur Knop
button = Button(master=root, text='Verstuur', command=verstuur)

# Status berichten
errorLabel = Label(master=berichtFrame, fg='red')
status = Label(master=root, fg='blue')

# Packed alle onderdelen van de GUI
berichtFrame.pack(pady=10)
naamFrame.pack(pady=10)

naamLabel.pack(pady=5, padx=40)
naamEntry.pack(pady=5)

berichtLabel.pack(pady=5, padx=40)
berichtEntry.pack(pady=5)

errorLabel.pack()
status.pack()

button.pack(pady=15)

root.mainloop()
