import psycopg2
import datetime
import json
from TwitterAPI import TwitterAPI




# Haalt gegevens voor databse connectie uit json
def database_connectie(databasefile):
    with open(databasefile, 'r') as json_file:
        data = json.load(json_file)
        host = data['host']
        database = data['database']
        user = data['user']
        password = data['password']
        port = data['port']
    return host, database, user, password, port


# Tweet goedgekeurd bericht
def tweet(keyfile, bericht, naam, datum, locatie):
    with open(keyfile, 'r') as json_file:
        data = json.load(json_file)
        consumer_key = data['consumer_key']
        consumer_secret = data['consumer_secret']
        access_token_key = data['access_token_key']
        access_token_secret = data['access_token_secret']
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    text = f"{naam}\n\n{bericht}\n\n{locatie} | {datum}"
    r = api.request('statuses/update', {'status': text})
    return r.status_code

# Controle of er een int als id is ingevuld
def CheckID(moderatorid): 
    try:
        id = int(moderatorid)
        return 0, id
    except ValueError:
        return -1, 0

# Verwisselt Status code met leesbaar alternatief
def code_status(code):  
    status = ['Onbeoordeeld', 'Afkeur', 'Goedkeur']
    return status[code]

# Voegt de moderator toe aan de database, verandert de naam of doet niks.
def moderator_naam_database(id, naam):  
    sql = 'select * from moderator'
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    if (id, naam) in rows:
        return True
    for row in rows:
        if id in row:
            sql = "UPDATE moderator set naam = %s WHERE id = %s"
            cur = con.cursor()
            cur.execute(sql, (naam, id))
            if cur.rowcount <= 1:
                con.commit()
                return True
    if (id, naam) not in rows:
        sql = "INSERT INTO moderator (id,naam) VALUES (%s, %s)"
        cur = con.cursor()
        cur.execute(sql, (id, naam))
    if cur.rowcount <= 1:
        con.commit()
        return True
    return False

# Haal berichten op uit de database
def readin():  
    sql = '''
    select bericht.id, naam, bericht, locatie, datum_bericht asc, tijd_bericht asc
    from bericht, zuil
    where bericht.zuilid = zuil.id
    and status = 0 limit 1
    '''
    cur = con.cursor()
    cur.execute(sql)
    try:
        rows = cur.fetchall()[0]
    except IndexError:
        return -1
    id = rows[0]
    naam = rows[1]
    bericht = rows[2]
    locatie = rows[3]
    datum = rows[4]
    if naam == None:
        naam = 'Anoniem'
    return id, naam, bericht, locatie, datum




# Verandert de informatie van goedgekeurde berichten in de database
def export_goed(berichtid, moderatorid):  # exporteert de gemodereerde berichten
    datum = datetime.datetime.now().strftime('%Y-%m-%d')  # Haalt datum op en bewaart deze op in datum
    tijd = datetime.datetime.now().strftime('%H:%M:%S')  # Haalt tijd op en bewaart deze in tijd
    status = 2
    sql = '''
        UPDATE bericht
        set status = %s, moderatorid = %s, datum_moderatie = %s, tijd_moderatie = %s
        WHERE id = %s
        '''
    cur = con.cursor()
    cur.execute(sql, (status, moderatorid, datum, tijd, berichtid))
    if cur.rowcount <= 1:
        con.commit()
        print(True)
        return True
    print(False)
    return False

# Verandert de informatie van afgekeurde berichten in de database
def export_slecht(berichtid, moderatorid, opmerking):  # exporteert de gemodereerde berichten
    datum = datetime.datetime.now().strftime('%Y-%m-%d')  # Haalt datum op en bewaart deze op in datum
    tijd = datetime.datetime.now().strftime('%H:%M:%S')  # Haalt tijd op en bewaart deze in tijd
    status = 1
    sql = '''
        UPDATE bericht
        set status = %s, moderatorid = %s, opmerking = %s
        WHERE id = %s
        '''
    cur = con.cursor()
    cur.execute(sql, (status, moderatorid, opmerking, berichtid))
    if cur.rowcount <= 1:
        con.commit()
        print(True)
        return True
    print(False)
    return False

# Haalt de berichten die afgekeurd zijn uit de database en formatterd ze in een lijst
def print_afgekeurde_berichten(): 
    lijst = []
    sql = '''
        select bericht.id, bericht.naam, bericht, locatie, datum_bericht , tijd_bericht, moderator.naam, status, opmerking
        from bericht, zuil, moderator
        where  status = 1
        and bericht.zuilid = zuil.id
        and bericht.moderatorid = moderator.id
        '''
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    try:
        x = rows[0]
    except IndexError:
        print('Geen afgekeurde berichten')
        return -1
    for row in rows:
        id = row[0]
        naam = row[1]
        bericht = row[2]
        locatie = row[3]
        datum = row[4]
        tijd = row[5]
        moderator = row[6]
        status = code_status(row[7])
        opmerking = row[8]
        if naam == None:
            naam = 'Anoniem'
        lijst.append(f'''
        locatie: {locatie}
        Moment: {datum} {tijd}
        Naam: {naam}
        Bericht: {bericht}
        Moderator: {moderator}
        Status: {status}
        Opmerking: {opmerking}
        ''')
    return lijst




# Standaard variablelen voor correcte werking en verbinding database
keyfile = 'TwitterAPI.json'
databasefile = 'Database.json'
host, database, user, password, port = database_connectie(databasefile)
con = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port)




