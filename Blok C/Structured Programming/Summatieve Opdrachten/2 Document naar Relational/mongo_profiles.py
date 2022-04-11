from connect_mongodb import mongo_profiles
from connect_postgresql import con
from psycopg2 import extras

def insert_products(profile_id, viewed_before):
    sql = """INSERT INTO profiles
    VALUES (%s, %s)
    """
    cur = con.cursor()
    cur.execute(sql,(profile_id, viewed_before))
    con.commit()

items = mongo_profiles.find()
x = 0
for item in items:
    x = x +1
    print(round((x/2081649)*100,2), '%',sep='')
    

    try:
        profile_id = str(item['_id'])
    except:
        profile_id = None
    try:
        viewed_before = item['recommendations']['viewed_before']
    except:
        viewed_before = None
    try:
        insert_products(profile_id, viewed_before)
    except:
        pass

