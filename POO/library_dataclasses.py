from dataclasses import dataclass, field

@dataclass
class Book:
    title: str = ''
    author: str = ''
    available: bool = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

@dataclass
class User:
    name: str
    borrowed_books: list = field(default_factory=[])

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book}")
        else:
            print(f"{book} is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book}")

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []
        self.users = []

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

# Example usage:
library = Library()

# Adding books
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)

# Adding users
user1 = User("Alice")
user2 = User("Bob")
library.add_user(user1)
library.add_user(user2)

# Borrowing and returning books
user1.borrow_book(book1)  # Alice borrows '1984'
user2.borrow_book(book1)  # Bob tries to borrow '1984' but it's not available
user1.return_book(book1)  # Alice returns '1984'
user2.borrow_book(book1)  # Bob borrows '1984' now it's available

# Display books
library.display_books()
