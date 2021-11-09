"""
Format berichten.txt:
    [Stationsnaam, Bericht, Naam, Datum, Tijd, Moderator, opmerking(Goedkeur/Afkeur)]
"""


def readin():  # Leest de berichten uit het bestand
    database = open('Berichten.txt', 'r')
    lijst = database.readlines()
    database.close()
    return lijst


def mooi():  # Zet de gegevens uit readin() om in een bruikbare vorm
    inn = readin()
    lengte = len(inn)
    uitt = []
    for index in range(len(inn)):
        uitt.insert(index, inn[index].split(','))
        uitt[index].pop()
    return uitt


def moderate(bericht):  # Controle berichten
    print("\n\n")  # Print de berichten
    print('Station: ', bericht[0])
    print('Datum: ', bericht[3], bericht[4])
    print('Naam: ', bericht[2])
    print('Bericht: ', bericht[1], '\n\n')

    invalid = True  # maakt een loop tot het juiste bericht is teruggegeven
    while invalid:
        controle = input("goedkeur of afkeur: ")
        if controle == 'goedkeur':
            return 'goedkeur'
        elif controle == 'afkeur':
            return 'afkeur'
        else:
            print('Invalid input')  # vertel de moderator dat wat ingevuld fout is


def reset():  # leegt de berichten
    database = open('Berichten.txt', 'w')
    database.write('')
    database.close()


def export(lijst):  # exporteert de gemodereerde berichten
    reset()
    database = open('Berichten.txt', 'a')
    for kort in lijst:
        for item in kort:
            database.write(item.strip("'"))
            database.write(',')
        database.write('\n')
    database.close()


moderator = input("Vul je naam in:\n")
lijst = []

for item in mooi():  # Gaat alle berichten af en als ze nog niet gemodereerd zijn gebeurt dat
    if len(item) == 5:
        item.append(moderator)
        item.append(moderate(item))
    print(item)
    lijst.append(item)

export(lijst)
