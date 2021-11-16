import psycopg2

def artiekelen_ophalen():
    sql = "SELECT * FROM boek"
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]:20} |   {row[1]}")

def artiekel_opslaan(titel, auteur, uitgever, boeknr, isbn):
    sql = "INSERT INTO boek VALUES (%s, %s, %s, %s, %s)"
    cur = con.cursor()
    cur.execute(sql, (titel, auteur, uitgever, boeknr, isbn))
    if cur.rowcount == 1:
        con.commit()
        return True
    else:
        return False



con = psycopg2.connect(
    host='localhost',
    database='Bibliotheek',
    user='postgres',
    password='password',
    port=5433
)

artiekelen_ophalen()
resultaat = artiekel_opslaan('titel', "auteur", "No Idea", 5, 383748147)
print(resultaat)
con.close()

