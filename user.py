class User:

    def __init__(self, name, library_ID):
        self._name = name
        self._library_ID = library_ID
        self._borrowed_books = []

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("User name must be a valid string.")
        self._name = name

    def get_library_ID(self):
        return self._library_ID
    
    def set_library_ID(self, library_ID):
        if not isinstance(library_ID, str):
            raise ValueError("Library ID must be a valid string.")
        self._library_ID = library_ID

    def get_borrowed_books(self):
        return self._borrowed_books
    
