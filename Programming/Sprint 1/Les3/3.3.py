uurCheck = True
antalCheck = True

while uurCheck:
    try:
        uurloon = float(input('Wat verdien je per uur: '))
        uurCheck = False
    except ValueError:
        print('invalid input')

while aantalCheck:
    try:
        aantalUur = float(input("Hoeveel uur heb je gewerkt: "))

        aantalCheck = False
    except ValueError:
        print('invalid input')

loon = round(uurloon * aantalUur, 2)

print(str(aantalUur) + ' uur werken levert €' + str(loon) + ' op')
