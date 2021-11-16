lijst = []
while True:
    invoer = input("Vul een getal in:")
    if invoer == '0':
        break
    lijst.append(int(invoer))

print('Er zijn', len(lijst), 'getallen ingevoerd, de som is:', sum(lijst))
