import random

Getal = random.randint(0,10)

while True:
    try:
        Gok = int(input('Vul een gok in: '))
        if Gok == Getal:
            print('Correct')
            break
        else:
         print('Probeer het nog een keer.')
    except ValueError:
        print('Vul een getal in.')
    