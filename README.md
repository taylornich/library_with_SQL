The Library with SQL is a simple library management system using Python and SQL to manage books, users, and authors. It allows the user to perform a variety of functions for each category previously listed. 

In order to set up and use the program, clone the repository, ensure mysql-connector-python is installed using pip. Then set up the MySQL Database making sure to replace the connect_database() function in the code with your own MySQL credentials. 
Once you run the main_menu.py within the program, the system will display a main menu giving you the options to choose Book Operations, Author Operations, or User Operations.

Book Operations:
1. Add books - allows the user to add books to the database using the title, author, isbn and publication date, 
2. Borrow books - allows the user to borrow a book using the book title and the user's library id.
3. Return books - allows the user to return a book using the book title and the user's library id.
4. Search for books - allows the user to search for a book using the title, shows the user the book's information. 
5. Display all books - displays all books and their respective information. 

User Operations:
1. Add users
2. View user details
3. Display all users

Author Operations
1. Add authors
2. View author details
3. Display all authors

Each submenu allows the user to return to the main menu if the user chooses to. 
Each category, books, authors, and users, has their own operations file and their own getter and setter files. 
