from connect_postgresql import con
import time

def select_sql(sql):
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

def most_similar(product_id):
    sql = f"""
        SELECT brand, category, sub_category, doelgroep, soort FROM products
        WHERE product_id = {product_id} 
    """

    primary_brand, primary_category, primary_sub_category, primary_doelgroep, primary_soort = select_sql(sql)[0]

    sql = f"""
        SELECT product_id, brand, category, sub_category, doelgroep, soort FROM products
        WHERE product_id != {product_id} AND stock != 0
    """
    list = []
    for item in select_sql(sql):
        score = 0
        id, brand, category, sub_category, doelgroep, soort = item
        if brand == primary_brand:
            score = score + 1
        if category == primary_category:
            score = score + 1 
        if sub_category == primary_sub_category:
            score = score + 1
        if doelgroep == primary_doelgroep:
            score = score + 1
        if soort == primary_soort:
           score = score + 1
        list.append([score, id])
        
    list = sorted(list, reverse=True)[:4]
    new_list = []
    for i in list:
        new_list.append(i[1])
    return new_list

print(most_similar("'33298'"))