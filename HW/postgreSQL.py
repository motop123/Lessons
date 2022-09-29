import psycopg2
from config import host, user, password, db_name
connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
    )
try:
    #connect ti exist database

    #the cursor for perfoming database operations
    # connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
