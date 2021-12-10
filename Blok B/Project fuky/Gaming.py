'''
Dit programma heeft dezelfde functie als 'filterdata.py'.
De twee output files zijn al vergeleken, maar komen niet overeen.
Ik weet niet hoe dat komt.
'''

import json


# in file de ongefilterde database
#outfile gefilterd op alleen de namen
# lst is de lijst waar alle spellen in komen

in_file = 'steam.json'
outfile = 'gamenames.json'
lst = []


# leest alle spellen uit de de json file en zet ze in een lijst
with open(in_file) as json_file:
    data = json.load(json_file)
      
    for i in range(len(data)):
        lst.append({"game": data[i]["name"]})
        print(i)
    #print(lst)
    print('----------\n',len(lst))

# scrhijft lst naar de outfile
with open(outfile, "w") as writeFile:
        json.dump(lst, writeFile, indent=4)