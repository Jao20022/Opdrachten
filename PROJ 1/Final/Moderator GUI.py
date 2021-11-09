from tkinter import *
import Moderator

# Controle inloggegevens moderator
def TryLogin():
    global moderatorid
    Naam = NaamEntry.get()
    moderatorid = IDEntry.get()
    code, moderatorid = Moderator.CheckID(moderatorid)
    if code == 0:
        LoginError.config(text='')
        if Moderator.moderator_naam_database(moderatorid, Naam):
            MainMenu()
    else:
        LoginError.config(text='Foute ID')

# Toont scherm Login
def LoginMenu():
    Terug.pack_forget()
    Main.pack_forget()
    Controle.pack_forget()
    Afgekeurd.pack_forget()
    Afkeur.pack_forget()

# Toont scherm start menu
def MainMenu():
    Login.pack_forget()
    Terug.pack_forget()
    Main.pack_forget()
    Controle.pack_forget()
    Afgekeurd.pack_forget()
    Afkeur.pack_forget()
    Main.pack()

# Maakt variabele nummer lager tenzij 0
def NummerLager():
    global Nummer
    if not Nummer == 0:
        AfgekeurdError.config(text="")
        Nummer -= 1
    AfgekeurdMenu()

# Maakt variabele nummer hoger
def NummerHoger():
    global Nummer
    Nummer += 1
    AfgekeurdMenu()

# Toont scherm afgekeurde menu
def AfgekeurdMenu():
    Login.pack_forget()
    Main.pack_forget()
    Controle.pack_forget()
    Afgekeurd.pack_forget()
    Afkeur.pack_forget()
    Terug.pack(side=TOP, padx=10, pady=20)
    if Moderator.print_afgekeurde_berichten() == -1: # Als er geen afgekeurde berichten zijn
        AfgekeurdBericht.config(text="Geen Afgekeurde Berichten", fg='red')
        VolgendeButton.pack_forget()
        VorigeButton.pack_forget()
    else:
        lijst = Moderator.print_afgekeurde_berichten()
        try: 
            AfgekeurdBericht.config(text=lijst[Nummer], fg='black')
        except IndexError:# Als Nummer te hoog is
            NummerLager()
        VorigeButton.pack(side=LEFT, padx=10, pady=10)
        VolgendeButton.pack(side=LEFT, padx=10, pady=10)
    Afgekeurd.pack()

# Toont scherm voor opmerking
def AfkeurMenu():
    Terug.pack_forget()
    Controle.pack_forget()
    Afkeur.pack()

# Voegt goedgekeurd toe aan database en toont scherm controle menu
def Goedkeur():
    Moderator.export_goed(berichtid,moderatorid)
    ControleMenu()

# Voegt afgekeurd toe aan database en toont scherm controle menu
# Of geeft een foutmelding
def Weiger():
    op = Opmerking.get()
    if len(op) > 0:
        OpmerkingError.config(text='')
        Moderator.export_slecht(berichtid,moderatorid,op)
        ControleMenu()
    else:
        OpmerkingError.config(text='Opmerking veld mag niet leeg zijn')

#Toont menu voor controle berichten
def ControleMenu():
    Afkeur.pack_forget()
    Login.pack_forget()
    Main.pack_forget()
    Controle.pack_forget()
    Afgekeurd.pack_forget()
    Afkeur.pack_forget()
    Terug.pack(side=TOP, padx=10, pady=20)
    if Moderator.readin() == -1: # Als er geen berichten zijn
        Bericht.config(text="Geen Berichten", fg='red')
        GoedkeurButton.pack_forget()
        AfkeurButton.pack_forget()
    else: # Als er wel berichten zijn
        global berichtid
        berichtid, naam, bericht, locatie, datum = Moderator.readin()
        Bericht.config(text=f'''
        id: {berichtid}
        locatie: {locatie}
        datum: {datum}
        Naam: {naam}
        Bericht: {bericht}
        ''', fg='black')
        AfkeurButton.pack(side=BOTTOM,padx=10, pady=10)
        GoedkeurButton.pack(side=BOTTOM,padx=10, pady=10)
    Controle.pack()

# Aanmaak standaard variabelen
moderatorid = int
berichtid = int

# GUI
root = Tk()

# Login Scherm
Login = Frame(master=root)
NaamLabel = Label(master=Login, text='Naam')
NaamEntry = Entry(master=Login)
IDLabel = Label(master=Login, text='ID')
IDEntry = Entry(master=Login)
LoginError = Label(master=Login, fg='red')
LoginButton = Button(master=Login, text='LOGIN', command=TryLogin)

Login.pack()
NaamLabel.pack(anchor=W, pady=5)
NaamEntry.pack()
IDLabel.pack(anchor=W, pady=5)
IDEntry.pack()
LoginError.pack()
LoginButton.pack()

# Knop terug naar Start menu
Terug = Button(master=root, text="MAIN", command=MainMenu)
Terug.pack(side=TOP, padx=10, pady=20)

# Scherm Start menu
Main = Frame(master=root)
StopButton = Button(master=Main, text='Ik wil stoppen', command=quit)
ControleButton = Button(master=Main, text='Controle Berichten', command=ControleMenu)
AfgekeurdButton = Button(master=Main, text='Toon afgekeurde berichten', command=AfgekeurdMenu)

Main.pack(side=LEFT)
StopButton.pack(anchor=SW, pady=5, padx=10)
ControleButton.pack(anchor=SW, pady=5, padx=10)
AfgekeurdButton.pack(anchor=SW, pady=5, padx=10)

# Scherm Controle berichten
Controle = Frame(master=root)
Bericht = Label(master=Controle, text='Bericht')
GoedkeurButton = Button(master=Controle, text='Goedkeur', command=Goedkeur)
AfkeurButton = Button(master=Controle, text='Afkeur', command=AfkeurMenu)

Controle.pack()
Bericht.pack(padx=30)
AfkeurButton.pack()
GoedkeurButton.pack()

# scherm toevoeging opmerking
Afkeur = Frame(master=root)
AfkeurLabel = Label(master=Afkeur, text='Opmerking')
Opmerking = Entry(master=Afkeur)
OpmerkingError = Label(master=Afkeur, fg='red')
VerstuurOpmerking = Button(master=Afkeur, text='Verstuur', command=Weiger)

Afkeur.pack()
AfkeurLabel.pack()
Opmerking.pack()
OpmerkingError.pack()
VerstuurOpmerking.pack()

# Scherm Afgekeurde berichten
Afgekeurd = Frame(master=root)
AfgekeurdBericht = Label(master=Afgekeurd, text="")
AfgekeurdError = Label(master=Afgekeurd, fg='red')
VolgendeButton = Button(master=Afgekeurd, text='Volgende', command=NummerHoger)
VorigeButton = Button(master=Afgekeurd, text='Vorige', command=NummerLager)

Afgekeurd.pack()
AfgekeurdBericht.pack(anchor=W, padx=10)
AfgekeurdError.pack()
VorigeButton.pack(side=LEFT, padx=10, pady=10)
VolgendeButton.pack(side=RIGHT, padx=10, pady=10)

# Wordt als index gebruikt om andere afgekeurde berichten te tonen
Nummer = 0

LoginMenu()
root.mainloop()
