class Book:
    # attributes: title, author
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
         
    # print book attributes
    def __str__(self):
        return f"{self.title}, by {self.author}, {self.available}"

book1 = Book("1984", "George Orwell")
print(book1)
class User:
    # attributes: name, borrowed_books
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    # methods
    # borrow a book
    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name}, borrowed {book}")
        else:
            print(f"{book} is not available")
            
    # return a book
    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name}, returned {book}")
    # print user name, borrowed books
    def __str__(self):
        return self.name
    
class Library:
    # attributes: books, users
    def __init__(self):
        self.books = []
        self.users = []
    # methods: add book, add_user, display books
    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book} to the library")
        
    def add_user(self, user):
        self.users.append(user)
        print(f"Registered {user} as a user")
        
    def display_books(self):
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(f"{book} - {status}")
            
# create Library
library = Library()

# add books
book1 = Book("1984", "George Orwell")
library.add_book(book1)

book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book2)

