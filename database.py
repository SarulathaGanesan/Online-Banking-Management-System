import mysql.connector
from config import HOST,USER,PASSWORD,DATABASE
try:
    connection=mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    if connection.is_connected():
        print("Database Connected Successfully!")

except mysql.connector.Error as err:
    print("Error:",err)