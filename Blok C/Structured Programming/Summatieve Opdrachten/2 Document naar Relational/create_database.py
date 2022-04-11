from connect_postgresql import con

products = """
        CREATE TABLE products (
            product_id varchar NOT NULL PRIMARY KEY,
            brand varchar,
            category varchar,
            sub_category varchar,
            doelgroep varchar,
            mrsp integer,
            selling_price integer,
            soort varchar,
            stock int
        );
    """

profiles = """
        CREATE TABLE profiles (
         profile_id varchar NOT NULL PRIMARY KEY,
         viewed_before text ARRAY
         );
        """



cur = con.cursor()
cur.execute(products)
cur.execute(profiles)
con.commit()
