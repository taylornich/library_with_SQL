import book_ops
import user_ops
import author_ops


def main_menu():
    while True:

        print('''Welcome to the Library Management System!
                
            Main Menu:
            1. Book Operations
            2. User Operations
            3. Author Operations
            4. Quit''')
            
        choice = input("Please enter the corresponding number of the function you wish to use: ")

        if choice == '1':
            book_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            author_menu()
        elif choice == '4':
            print("Quitting application")
            quit()
        else:
            print("That is not a valid menu  choice. Please choose from options 1-4.")


def book_menu():
    while True:

        print(''' Book Operations
            1. Add a new book
            2. Borrow a book
            3. Return a book
            4. Search for a book
            5. Display all books
            6. Return to main menu''')
        
        book_choice = input("Enter the number of the function you would like to do: ")

        if book_choice == '1':
            book_ops.add_book()
        elif book_choice == '2':
            book_ops.borrow_book()
        elif book_choice == '3':
            book_ops.return_book()
        elif book_choice == '4':
            book_ops.search_book()
        elif book_choice == '5':
            book_ops.display_books()
        elif book_choice == '6':
            break
        else: 
            print("That is not a valid menu option. Please choose from options 1-5.")


def user_menu():
    while True:

        print('''User Operations:
            1. Add a new user
            2. View user details
            3. Display all users
            4. Return to main menu''')
        
        user_choice = input("What would you like to do? Please enter your choice in 1-3 format: ")

        if user_choice == '1':
            user_ops.add_user()
        elif user_choice == '2':
            user_ops.view_user_details()
        elif user_choice == '3':
            user_ops.display_users()
        elif user_choice == '4':
            break
        else:
            print("That is not a valid menu option. Please choose from options 1-3.")
        

def author_menu():
    while True:

        print('''Author Operations:
            1. Add a new author
            2. View author details
            3. Display all authors
            4. Return to main menu''')
        

        author_choice = input("What would you like to do? Please enter your choice in 1-3 format: ")

        if author_choice == '1':
            author_ops.add_author()
        elif author_choice == '2':
            author_ops.view_author()
        elif author_choice == '3':
            author_ops.display_authors()
        elif author_choice == '4':
            break
        else:
            print("That is not a valid menu option. Please choose from options 1-3.")


if __name__ == "__main__":
    main_menu()