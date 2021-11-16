'''
#vraag gebruiker om naam en leeftijd
naam = input("Vul je naam in: ")
leeftijd = input("Vul je leeftijd in: ")

#print dat de gebruiker mag stemmen als de leeftijd gelijk is aan of meer is dan 18
if int(leeftijd) >= 18:
    print(naam, ", You can vote.", sep='')
else:
    print(naam, ", You can't vote.", sep='')
'''

'''
word = input('Enter a word: ')


for letter in reversed(word):
    if letter in 'eyuioa':
      print(letter)

'''

for i in range(11):
    print(i, end=' ')

print()
for i in range(1, 10, 2):
    print(i, end=' ')