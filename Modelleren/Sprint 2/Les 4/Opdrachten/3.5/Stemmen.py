#Vraag om gebruiker input (naam en leeftijd)
naam = input('Vul je naam in: ')
leeftijd = int(input('Vul je leeftijd in: '))

#als leeftijd meer is dan 18 print dat gebruiker mag stemmen
#Anders print dat gebruiker niet mag stemmen
if leeftijd >=18:
    print(naam, "je mag stemmen")
else:
    print(naam, "je mag niet stemmen")


