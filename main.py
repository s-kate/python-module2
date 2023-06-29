class Book:

    def __init__(self, title, author, year):
        self.title = title
        self. author = author
        self.year = year

    def __str__(self):
        return f'{self.title} by {self.author} ({self.year})'


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        books_list = '\n'.join(str(book) for book in self.books)
        return books_list


library = Library()
book1 = Book('1984', 'George Orwell', 1948)
book2 = Book('The Kite Runner', 'Khaled Hosseini', 2003)
book3 = Book('Harry Potter and the Philosopher’s Stone', 'J.K. Rowling', 1997)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library)
