#maak lijst getallen
import random

getallen = []

for i in range(101):
    getallen.append(random.randint(0,100))




#print getallen een voor een
for i in getallen:
    if i % 2 ==0:
     print(i, end=' ')






