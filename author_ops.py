from connect_db import connect_database
from mysql.connector import Error
from author import Author


def add_author():
    author_name = input("Enter the name of the author you would like to add: ")
    biography = input("Enter a short biography for the author: ")

    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id FROM Authors WHERE name = %s"
            cursor.execute(query, (author_name,))
            existing_author = cursor.fetchone()

            if existing_author:
                print(f"The author, {author_name}, already exists in the database.")
            else:
                query = "INSERT INTO Authors (name, biography) VALUES (%s, %s)"
                cursor.execute(query, (author_name, biography))
                conn.commit()
                print(f"'{author_name}' has been added to the Authors table successfully.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def view_author():
    author_name = input("Enter the name of the author you would like to view: ")

    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT name, biography FROM authors WHERE name = %s"
            cursor.execute(query, (author_name,))
            author = cursor.fetchone()

            if author:
                print(f"Author: {author[0]}, Biography: {author[1]}")
            else:
                print(f"Author '{author_name}' not found in the database.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def display_authors():
    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT name, biography FROM authors"
            cursor.execute(query)
            authors = cursor.fetchall()

            if authors:
                for author in authors:
                    print(f"Name: {author[0]}, Biography: {author[1]}")
            else:
                print("No authors found in the database.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()