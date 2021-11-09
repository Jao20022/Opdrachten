"""
Format bericten.txt:
    [Stationsnaam, Bericht, Naam, Datum, Tijd, Moderator, opmerking(Goedkeur/Afkeur)]
"""
import datetime

# exporteert bericht naar bestanda
def export():
    database = open('Berichten.txt', 'a')  # opent de "Database" om berichten aan toe te voegen
    database.writelines(stationsnaam + ',' + bericht + ',' + naam + ',' + datum + ',' + tijd + ',\n')
    database.close()

# Vraag of nog een bericht ingevuld wordt
def vervolg():
    vervolg = input('Nog een bericht y/n:\n')
    if not vervolg.lower() == 'y':
        return False
    else:
        return True

# Vraag en controleer bericht gebruiker
def bericht_vraag():
    ber = input("Vul een bericht in MAX 140 karakters:\n")
    if len(ber) > 140:
        print("bericht te lang. Probeer opnieuw")
    elif len(ber) == 0:
        print('bericht leeg. Probeer opnieuw')
    else:
        return ber

# Vraag en controleer naam gebruiker
def naam_vraag():
    nam = input("Vul je naam in (optioneel):\n")
    if len(nam) == 0:  # controleert of er een naam is ingevuld en vult zelf 'anoniem' in als er geen naam gegeven is.
        nam = 'anoniem'
    else:
        return nam

    # aanmaak variabelen voor database # #


# aanmaak variabelen voor database
bericht = ''
naam = ''
datum = datetime.datetime.now().strftime('%d-%m-%Y')  # Haalt datum op en bewaart deze op in datum
tijd = datetime.datetime.now().strftime('%H:%M:%S')  # Haalt tijd op en bewaart deze in tijd
stationsnaam = input("Vul naam Station in: ")  # Stationsnaam invullen gebeurt maar 1 keer
valid = False
nogBericht = True

# Zolang onderstaande loop herhaalt wordt kunnen berichten ingevuld worden
while nogBericht:
    bericht = bericht_vraag()
    naam = naam_vraag()
    print([stationsnaam, bericht, naam, datum, tijd])
    export()
    nogBericht = vervolg()
