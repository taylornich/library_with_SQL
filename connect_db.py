import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "library_management_sql"
    user = "root"
    password = "Brutus0309!"
    host = "localhost"

    try:
        conn = mysql.connector.connect (
            database = db_name,
            user = user, 
            password = password,
            host = host
        )

        if conn.is_connected:
            return conn

    except Error as e:
        print(f"Error: {e}")
        return None