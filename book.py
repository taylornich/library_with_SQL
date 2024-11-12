from datetime import date

class Book: 
    def __init__(self, title, author, isbn, publication_date):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._publication_date = publication_date
        self._availability = True


    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if not isinstance(title, str):
            raise ValueError("The title must be a valid string.")
        self._title = title

    def get_author(self):
        return self._author
    
    def set_author(self, author):
        if not isinstance(author, str):
            raise ValueError("Author must be a valid string.")
        self._author = author

    def get_publication_date(self):
        return self._publication_date
    
    def set_publication_date(self, publication_date):
        if not isinstance(publication_date, date):
            raise ValueError("Publication date must be a valid date.")
        self._publication_date = publication_date

    def get_isbn(self):
        return self._isbn
    
    def set_isbn(self, isbn):
        if not isinstance(isbn, str):
            raise ValueError("ISBN must be a valid string.")
        self._genre = isbn

    def is_available(self):
        return self._availability
    
    def set_availability(self, availability):
        self._availability = availability
