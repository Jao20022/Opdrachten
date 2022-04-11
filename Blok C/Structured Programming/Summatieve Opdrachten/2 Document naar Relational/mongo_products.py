from connect_mongodb import mongo_products
from connect_postgresql import con


def insert_products(product_id, brand, category, sub_category, doelgroep, mrsp, selling_price, soort, stock):
    sql = """INSERT INTO products
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur = con.cursor()
    cur.execute(sql,(product_id, brand, category, sub_category, doelgroep, mrsp, selling_price, soort, stock))
    con.commit()

items = mongo_products.find()
x = 0
for item in items:
    x = x +1
    print(round((x/34004)*100,2), '%',sep='')
    try:
        product_id = item['_id']
    except:
        product_id = None
    try:
        brand = item['brand']
    except:
        brand = None
    try:
        category = item['category']
    except:
        category = None
    try:
        sub_category = item['sub_category']
    except:
        sub_category = None
    try:
        doelgroep = item['properties']['doelgroep']
    except:
        doelgroep = None
    try:
        mrsp = item['price']['mrsp']
    except:
        mrsp = None
    try:
        selling_price = item['price']['selling_price']
    except:
        selling_price = None
    try:
        soort = item['properties']['soort']
    except:
        soort = None
    try:
        stock = item['properties']['stock']
    except:
        stock = None
    try:
        insert_products(product_id, brand, category, sub_category, doelgroep, mrsp, selling_price, soort, stock)
    except:
        pass
