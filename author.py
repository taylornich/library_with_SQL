class Author:

    def __init__(self, author, biography):
        self._author = author
        self._biography = biography

    def get_author(self):
        return self._author
    
    def set_author(self, author):
        if not isinstance(author, str):
            raise ValueError("Author must be a valid string.")
        self._author = author

    def get_biography(self):
        return self._biography
    
    def set_biography(self, biography):
        if not isinstance(biography, str):
            raise ValueError("Biography must be a valid string.")
        self._biography = biography