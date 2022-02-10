Grootte = int(input('Hoe groot? '))

for i in range(Grootte):
    Space = Grootte-i
    print(' '*Space + '*'*i)

for i in range(Grootte,1,-1):
    Space = Grootte-i
    print(' '*Space + '*'*i)