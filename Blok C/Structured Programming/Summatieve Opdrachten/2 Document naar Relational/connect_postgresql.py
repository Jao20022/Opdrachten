import psycopg2

con = psycopg2.connect(
    host="localhost",
    database = "huwebshop",
    user = "postgres",
    password = "password"
)
