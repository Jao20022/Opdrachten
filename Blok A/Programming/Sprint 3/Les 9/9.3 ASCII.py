def code(invoerstring):
    stri = str()
    for i in invoerstring:
        stri += chr(ord(i) + 3)
    return stri


Gebruiker = input("vul een Naam in: ")
Beginstation = input("vul een Beginstation in: ")
Eindstation = input("vul een Eindstation in: ")

tekst = Gebruiker + Beginstation + Eindstation
new = code(tekst)
print(f"{tekst} vertaald naar {new}")
