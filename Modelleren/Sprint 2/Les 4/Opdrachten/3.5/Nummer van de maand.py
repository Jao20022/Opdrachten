#Vraag nummer van de maan
nummer = int(input("Vul nummer van de maand in: "))

#Als nummer 3-5 : print lente
#Als nummer 6-8: print zomer
#Als nummer 9-11: print herfst
if nummer in range(3,6):
    print('Lente')
elif nummer in range(7,9):
    print('Zomer')
elif nummer in range(9,12):
    print('Herfst')
else:
    print('Winter')


