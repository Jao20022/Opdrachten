stationsnaam = input("Vul de stationsnaam in: ")


def module1(b, n):
    if 140 >= len(b) > 0:  # controleert of het bericht MAX 140 characters heeft
        berichten.append([b, n])  # voegt het bericht van de gebruiker toe aan de lijst met alle berichten


def module2(unmod):
    print(unmod)  # lees ongemodereerde berichten in
    print()  # lege regel
    while len(unmod) > 0:  # herhaal het proces tot de lijst met ongemodereerde berichten op zijn
        item = unmod[0]  # assigned het eerste object uit de lijst aan de variabele item
        print(item)  # print het bericht
        print()  # Lege ruimte tussen reactie en bericht
        invalid = True  # maakt een loop tot het juiste bericht is teruggegeven
        while invalid:
            controle = input("goedkeur of afkeur: ")
            if controle == 'goedkeur':
                print("Het bericht: ", '"', item[0], '"', " is goedgekeurd", sep='')  # toont bericht goedgekeurd
                goedkeur.append(item)  # voegt het bericht toe aan lijst met goedgekeurde berichten
                berichten.remove(item)  # verwijdert het bericht van de lijst met berichten
                invalid = False
            elif controle == 'afkeur':
                print("Het bericht: ", '"', item[0], '"', " is afgekeurd", sep='')  # toont bericht afgekeurd
                afkeur.append(item)  # voegt het bericht toe aan lijst met afgekeurde berichten
                berichten.remove(item)  # verwijdert het bericht van de lijst met berichten
                invalid = False
            else:
                print('Invalid input')  # vertel de moderator dat wat ingevuld fout is


goedkeur = []  # lijst met goedgekeurde berichten
afkeur = []  # lijst met afgekeurde berichten
berichten = [['hoi', 'jan'], ['bericht', 'naam']]  # lijst met test berichten

# Roept module 1 op en laat de gebruiker een bericht en een naam achterlaten
module1(input("Vul een bericht in(max 140 characters: "), input("Vul een naam in (optioneel): "))

# Roept module 2 op met de berichten
module2(berichten)

# print de lijst met goedgekeurde berichten
print(goedkeur)

# TODO: herschrijf code zodat de gemodereerde berichten worden geprint met "afgekeurd" of "goedgekeurd"
