import psycopg2
import datetime
import requests
import json
from tkinter import *

def database_connectie(databasefile):
    with open(databasefile, 'r') as json_file:
        data = json.load(json_file)
        host = data['host']
        database = data['database']
        user = data['user']
        password = data['password']
        port = data['port']
    return  host, database, user, password, port

def locatie_ophalen():
    r = requests.get('https://ipapi.co/json').json()
    if 'error' in r:
        return 'onbekend'
    locatie = r['city']
    return locatie


def zuil(id, locatie):
    sql = 'select * from zuil'
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    if (id, locatie) in rows:
        return False
    for row in rows:
        if id in row:
            sql = "UPDATE zuil set locatie = %s WHERE id = %s"
            cur = con.cursor()
            cur.execute(sql, (locatie, id))
            if cur.rowcount <= 1:
                con.commit()
                return True
    if (id,locatie) not in rows:
        sql = "INSERT INTO zuil (id,locatie) VALUES (%s, %s)"
        cur = con.cursor()
        cur.execute(sql, (id, locatie))
    if cur.rowcount <= 1:
        con.commit()
        return True
    return False



# exporteert bericht naar database
def export(bericht, naam, datum_bericht, tijd_bericht, zuilid):
    status = 0
    sql = '''
        INSERT INTO bericht (bericht, naam, datum_bericht, tijd_bericht, zuilid, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
    cur = con.cursor()
    cur.execute(sql, (bericht, naam, datum_bericht, tijd_bericht, zuilid, status))
    if cur.rowcount <= 1:
        con.commit()
        return True
    return False


# Vraag of nog een bericht ingevuld wordt
def vervolg():
    while True:
        vervolg = input('Nog een bericht y/n:\n')
        if vervolg.lower() == 'n':
            return False
        elif vervolg.lower() == 'y':
            return True


# Vraag en controleer bericht gebruiker
def bericht_vraag():
    while True:
        ber = input("Vul een bericht in MAX 140 karakters:\n")
        if len(ber) > 140:
            print("bericht te lang. Probeer opnieuw")
        elif len(ber) == 0:
            print('bericht leeg. Probeer opnieuw')
        else:
            return ber


# Vraag en controleer naam gebruiker
def naam_vraag():
    nam = input("Vul je naam in (optioneel):\n")
    if len(nam) != 0:
        return nam





# aanmaak variabelen voor database
id = input('vul zuil serienummer in: ')
bericht = ''
naam = ''
locatie = locatie_ophalen()  # Stationsnaam invullen gebeurt maar 1 keer
valid = False
nogBericht = True

# Bestand met gegevens database
databasefile = 'DatabaseConnectie.json'
#Maakt verbinding met de database
host, database, user, password, port = database_connectie(databasefile)
con = psycopg2.connect(
    host= host,
    database= database,
    user= user,
    password= password,
    port= port)

resultaat = zuil(id, locatie)
# Zolang onderstaande loop herhaalt wordt kunnen berichten ingevuld worden
while nogBericht:
    bericht = bericht_vraag()
    naam = naam_vraag()
    datum = datetime.datetime.now().strftime('%Y-%m-%d')  # Haalt datum op en bewaart deze op in datum
    tijd = datetime.datetime.now().strftime('%H:%M:%S')  # Haalt tijd op en bewaart deze in tijd
    print([locatie, bericht, naam, datum, tijd])
    print()
    if export(bericht, naam, datum, tijd, id):
        print('succesvol verzonden')
    else:
        print('verzenden mislukt')
    nogBericht = vervolg()

con.close()
