from connect_postgresql import con

id = "'59dce47fa56ac6edb4c4c86b'"
sql = f"""
    SELECT * from profiles
    WHERE profile_id = {id}
"""
cur = con.cursor()
cur.execute(sql)
rows = cur.fetchall()
for row in rows:
    print(row[1])