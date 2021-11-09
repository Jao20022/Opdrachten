#vraag gebruiker om leeftijd en of 'ie een paspoort heeft
leeftijd = input("Geef je leefijd: ")
paspoort = input('Nederlands paspoort: ')

# als de gebruiker een paspoort heeft en ouder is dan 18 print dat gebruiker mag stemmen
#print anders dat gebruiker niet mag stemmen
if int(leeftijd) >= 18 and paspoort == 'ja':
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Je mag niet stemmen!")