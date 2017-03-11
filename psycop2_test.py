import psycopg2
import sys

db_con = None

try:
    db_con = psycopg2.connect(database="dvdrental", 
            user="postgres", password ="postgres")
    cursor = db_con.cursor()
    cursor.execute("select * from film")
    print(cursor.fetchone())
except psycopg2.DatabaseError as e:
    print("Error {1}").format(e)
    sys.exit(1)
finally:
    if db_con:
        db_con.close()
    
