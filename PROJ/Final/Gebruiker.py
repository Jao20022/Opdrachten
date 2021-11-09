import psycopg2
import datetime
import requests
import json

# Haalt gegevens voor databse coonectie uit json
def database_connectie(databasefile):
    with open(databasefile, 'r') as json_file:
        data = json.load(json_file)
        host = data['host']
        database = data['database']
        user = data['user']
        password = data['password']
        port = data['port']
    return host, database, user, password, port

# Vind de locatie van het zuil via IP
def locatie_ophalen():
    r = requests.get('https://ipapi.co/json').json()
    if 'error' in r:
        return 'onbekend'
    locatie = r['city']
    return locatie

# Zorgt dat de correcte informatie van het zuil in de database staat
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
    if (id, locatie) not in rows:
        sql = "INSERT INTO zuil (id,locatie) VALUES (%s, %s)"
        cur = con.cursor()
        cur.execute(sql, (id, locatie))
    if cur.rowcount <= 1:
        con.commit()
        return True
    return False


# exporteert bericht naar database
def export(bericht, naam):
    global id
    datum_bericht = datetime.datetime.now().strftime('%Y-%m-%d')  # Haalt datum op en bewaart deze op in datum
    tijd_bericht = datetime.datetime.now().strftime('%H:%M:%S')  # Haalt tijd op en bewaart deze in tijd
    status = 0
    sql = '''
        INSERT INTO bericht (bericht, naam, datum_bericht, tijd_bericht, zuilid, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
    cur = con.cursor()
    cur.execute(sql, (bericht, naam, datum_bericht, tijd_bericht, id, status))
    if cur.rowcount <= 1:
        con.commit()
        return True
    return False


# Controleert bericht van de gebruiker
def bericht_check(ber):
    if len(ber) > 140:
        return -1
    elif len(ber) == 0:
        return 0
    else:
        return 1


# Maakt de naam variable leeg of maakt MAX 20 karakters.
def naam_controle(naam):
    try:
        return naam[0:20]
    except NameError:
        pass


# Standaard variablelen voor correcte werking en verbinding database
id = '650-543-4800'
locatie = locatie_ophalen()  
databasefile = 'Database.json'
host, database, user, password, port = database_connectie(databasefile)
con = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port)


