# def sum():
#    total = 0
#    while True:
#        nextInt = input('next int:')
#        if nextInt == 'quit':
#            break
#        total += int(nextInt)
#    print(total)
#
#
# sum()


telefoonboek = {

    'Dinesh': '06-12345678',
    'Bart': '06-12955672'
}

naam = input("Van wie wilt u het nummer? ")
if naam in telefoonboek:
    print(telefoonboek[naam])

naam = input("Wie wilt u toevoegen? ")
nummer = input("En welk nummer hoort daarbij? ")
telefoonboek[naam] = nummer
print(telefoonboek)

nummer = input("Bij welk nummer wilt u de naam weten? ")
for naam in telefoonboek.keys():
    if telefoonboek[naam] == nummer:
        print("Dit nummer is van "+ naam)

for naam, nummer in telefoonboek.items():
    print(f"{naam} heeft het nummer: {nummer}")