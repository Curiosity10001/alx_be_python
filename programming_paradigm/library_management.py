class Book:
    def __init__(self,title,author,is_checked_out = False):
        self.title = title
        self.author = author
        self._is_checked_out=is_checked_out
    
    def book_is_checked_out(self):
        self._is_checked_out = True
        
     def return_book(self):
        self._is_checked_out = False
        
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self,book: Book):
        self._books.append (book)
        
    def check_out_book(book: Book):
        if book in self._books :
            book.book_is_checked_out()
        
    def return_book(book: Book):
        if book in self._books :
            book.return_book()
            
    def list_available_books():
        for book in self_books :
            if not book._is_checked_out :
                def list_available_books(self):

    for book in self._books:
        if not book._is_checked_out:
            print(f"{book.title} by {book.author}")