import psycopg2
import datetime
import json
from TwitterAPI import TwitterAPI


# TODO: TwitterAPI


def database_connectie(databasefile):
    with open(databasefile, 'r') as json_file:
        data = json.load(json_file)
        host = data['host']
        database = data['database']
        user = data['user']
        password = data['password']
        port = data['port']
    return  host, database, user, password, port

# Tweet berichten
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


def moderator_gegevens():  # Invullen gegevens van de moderator
    moderatornaam = input('Vul je naam in:\n')
    while True:
        try:
            moderatorid = int(input("Vul je id in:\n"))
            return moderatorid, moderatornaam
        except ValueError:
            continue


def code_status(code):  # verwisselt code uit de database met een leesbaar alternatief
    status = ['onbeoordeeld', 'afkeur', 'goedkeur']
    return status[code]


def moderator_naam_database(id, naam):  # Voegt de moderator toe aan de database, verandert de naam of doet niks.
    sql = 'select * from moderator'
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    if (id, naam) in rows:
        return False
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


def readin():  # Leest de berichten uit de database
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
        return 0
    id = rows[0]
    naam = rows[1]
    bericht = rows[2]
    locatie = rows[3]
    datum = rows[4]
    if naam == None:
        naam = 'Anoniem'
    return id, naam, bericht, locatie, datum


def moderate(naam, bericht, locatie, datum):  # Controle berichten
    print(f"\nlocatie: {locatie}")
    print(f"Datum: {datum}")
    print(f"Naam: {naam}")
    print(f"Bericht: {bericht} \n")
    print('----------------------------------------')
    while True:
        controle = input("goedkeur of afkeur: ")
        if controle.lower() == 'goedkeur':
            return True, ''
        elif controle.lower() == 'afkeur':
            opmerking = input("Voeg een opmerking toe: ")
            return False, opmerking
        else:
            print('Invalid input')  # vertel de moderator dat wat ingevuld fout is


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
        return True
    return False


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
        return True
    return False


def print_afgekeurde_berichten():  # Print berichten die afgekeurd zijn
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
        return
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
        print(f"\nlocatie: {locatie}")
        print(f"Datum: {datum}")
        print(f"Naam: {naam}")
        print(f"Bericht: {bericht} \n")
        print(f"Moderator: {moderator}")
        print(f"Status: {status}")
        print(f"Opmerking: {opmerking}\n")
        print('----------------------------------------')


def menu():  # Print menu
    print(("1: Ik wil stoppen"))
    print("2: Volgende bericht")
    print("3: Print een overzicht met afgekeurde berichten")
    x = input('>')
    return x


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

# Keys twitterAPI
keyfile = 'TwitterAPI.json'
# Invullen gegevens moderator
moderatorid, moderatornaam = moderator_gegevens()
moderator_naam_database(moderatorid, moderatornaam)

while True:  # Loop van programma
    x = menu()
    if x == '1':  # Moderator wil stoppen
        break
    elif x == '2':  # Moderator wil volgende bericht controlleren
        try:
            id, naam, bericht, locatie, datum = readin()
            evaluatie, opmerking = moderate(naam, bericht, locatie, datum)
            if evaluatie:
                tweet(keyfile, bericht, naam, datum, locatie)
                print(export_goed(id, moderatorid))
            else:
                export_slecht(id, moderatorid, opmerking)
        except TypeError:
            print('geen berichten\n')
    elif x == '3':  # Moderator wil afgekeurde berichten printen
        print_afgekeurde_berichten()
