from connect_db import connect_database
from mysql.connector import Error
from user import User

def add_user():
    name = input("Enter your first and last name: ")
    library_ID = input("Enter your library ID: ")

    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT library_id FROM Users WHERE library_id = %s"
            cursor.execute(query, (library_ID,))
            existing_user = cursor.fetchone()

            if existing_user:
                print(f"The library ID {library_ID} already exists in the database.")
            else:
                query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"
                cursor.execute(query, (name, library_ID))
                conn.commit()
                print(f"'{name}' has been added to the User database successfully.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def view_user_details():
    library_ID = input("Enter the Library ID of the user you would like to view: ")

    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT name, library_id FROM Users WHERE library_id = %s"
            cursor.execute(query, (library_ID,))
            user = cursor.fetchone()

            if user:
                print(f"User details: Name: {user[0]}, Library ID: {user[1]}")
            else:
                print(f"User with Library ID {library_ID} not found in the database.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def display_users():
    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT name, library_id FROM Users"
            cursor.execute(query)
            users = cursor.fetchall()

            if users:
                for user in users:
                    print(f"Name: {user[0]}, Library ID: {user[1]}")
            else:
                print("User database is currently empty.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()