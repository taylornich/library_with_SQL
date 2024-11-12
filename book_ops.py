from connect_db import connect_database
from mysql.connector import Error
from book import Book

def add_book():
    title = input("Enter the title of the book you would like to add: ")
    author_name = input("Enter the book's author: ")
    publication_date = input("Enter the publication date of the book (YYYY-MM-DD): ")
    isbn = input("Enter the ISBN of the book: ")
    
    conn = connect_database()
    
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id FROM Authors WHERE name = %s"
            cursor.execute(query, (author_name,))
            author = cursor.fetchone()

            if author:
                author_id = author[0]
            else:
                query = "INSERT INTO Authors (name) VALUES (%s)"
                cursor.execute(query, (author_name,))
                conn.commit()
                author_id = cursor.lastrowid

            query = "INSERT INTO Books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (title, author_id, isbn, publication_date))
            conn.commit()
            print(f"'{title}' has been added to the books database successfully.")

        except Error as e:
            print(f"Error: {e}")
            
        finally:
            cursor.close()
            conn.close()


def borrow_book():
    title = input("Enter the title of the book you would like to borrow: ")
    library_ID = input("Enter your library ID: ")  
    borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")

    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor()

            query = "SELECT id FROM Users WHERE library_id = %s"
            cursor.execute(query, (library_ID,))
            user = cursor.fetchone()

            if not user:
                print(f"There is no user associated with the given library ID, {library_ID}.")
                return
            
            user_id = user[0]

            query = "SELECT id, availability FROM Books WHERE title = %s"
            cursor.execute(query, (title,))
            book = cursor.fetchone()

            if book:
                book_id, availability = book
                if availability:
                    query = "UPDATE Books SET availability = FALSE WHERE id = %s"
                    cursor.execute(query, (book_id,))
                    
                    query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
                    cursor.execute(query, (user_id, book_id, borrow_date))
                    conn.commit()
                    print(f"You have successfully borrowed '{title}'.")
                else:
                    print(f"'{title}' is currently unavailable.")
            else:
                print(f"'{title}' was not found in the database.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def return_book():
    title = input("Enter the title of the book you would like to return: ")
    library_ID = input("Enter your library ID: ")
    return_date = input("Enter the return date (YYYY-MM-DD): ")

    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id, availability FROM Books WHERE title = %s"
            cursor.execute(query, (title,))
            book = cursor.fetchone()

            if book:
                book_id, availability = book
                if not availability:
                    query = "UPDATE Books SET availability = TRUE WHERE id = %s"
                    cursor.execute(query, (book_id,))

                    query = "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND book_id = %s AND return_date IS NULL"
                    cursor.execute(query, (return_date, library_ID, book_id))
                    
                    conn.commit()
                    print(f"'{title}' has been returned successfully.")
                
                else:
                    print("According to records, you have not borrowed this book.")
            
            else:
                print(f"'{title}' was not found in the database.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()


def search_book():
    title = input("Enter the title of the book you would like to search for: ")

    conn = connect_database()
    
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT b.title, a.name, b.isbn, b.publication_date, b.availability FROM Books b JOIN Authors a ON b.author_id = a.id WHERE b.title = %s"
            cursor.execute(query, (title,))
            results = cursor.fetchall()

            if results:
                for row in results:
                    print(f"Title: {row[0]}, Author: {row[1]}, ISBN: {row[2]}, Publication Date: {row[3]}, Available: {'Yes' if row[4] else 'No'}")
            else:
                print(f"No books found with the title '{title}'.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()

def display_books():
    conn = connect_database()

    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT b.title, a.name, b.isbn, b.publication_date, b.availability FROM Books b JOIN Authors a ON b.author_id = a.id"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                for row in result:
                    print(f"Title: {row[0]}, Author: {row[1]}, ISBN: {row[2]}, Publication Date: {row[3]}, Available: {'Yes' if row[4] else 'No'}")
            else:
                print("The book database is currently empty.")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()