"""
Format bericten.txt:
    [Stationsnaam, Bericht, Naam, Datum, Tijd, Moderator, opmerking(Goedkeur/Afkeur)]
"""
import datetime

def reset():
    database = open('test1.txt', 'w')
    database.write('')
    database.close()
def ex(list):
    reset()
    database = open('test1.txt', 'a')
    for items in list:
        print(items)
        string = str(items).strip('[]')
        print(string)
        database.write(string + '\n')
    database.close()

def readin(): # Haalt de berichten uit de database en stopt ze in een lijst
    database = open('test.txt', 'r')
    lines = database.read().count('\n')
    database.close()
    database = open('test.txt', 'r')
    masterlist = []
    for items in range(lines):
        temp = database.readline().split(', ')
        if not 'goedkeur' in temp or not 'afkeur' in temp:
            masterlist.append(temp)
    return masterlist

masterlist = readin()
print(masterlist)
def mod():
    invalid = True  # maakt een loop tot het juiste bericht is teruggegeven
    while invalid:
        controle = input("goedkeur of afkeur: ")
        if controle == 'goedkeur':
            return True
        elif controle == 'afkeur':
            return False
        else:
            print('Invalid input')  # vertel de moderator dat wat ingevuld fout is



print(readin())
for bericht in readin():
    index = readin().index(bericht)
    masterlist[index].pop()
    print('Station: ', bericht[0])
    print('Datum: ', bericht[3], bericht[4])
    print('Naam: ', bericht[2])
    print('Bericht: ', bericht[1], '\n\n')
    if True:
        masterlist[index].append('Goedkeur')
    else:
        masterlist[index].append('Afkeur')


ex(masterlist)


