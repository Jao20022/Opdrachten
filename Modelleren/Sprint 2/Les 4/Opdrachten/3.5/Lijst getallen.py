#Maak lijst getallen
getallen = [234,2,34,23,42,34,23,42,34,23,4,234,2,334,4,65,6,735,6,23,125,64,7,65]

#Maak variabele som met waarde 0
som = 0

#voor elk getal: getal even is tel getal bij som op
for n in getallen:
    if n % 2 ==0:
        som + n
        print(n)
