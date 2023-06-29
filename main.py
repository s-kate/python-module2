class Book:

    def __init__(self, name, author, year, pages):
        self.year = year
        self.name = name
        self.author = author
        self.pages = pages

    @staticmethod
    def count_books_year(books_list, year):
        count = 0
        for book in books_list:
            if book.year == year:
                count += 1
        return count


book1 = Book('1984', 'George Orwell', 1948, 300)
book2 = Book('The Kite Runner', 'Khaled Hosseini', 2003, 450)
book3 = Book('Harry Potter and the Philosopher’s Stone', 'J.K. Rowling', 1997, 500)
book4 = Book('Into Thin Air', 'John Krakaver', 1997, 205)
book_list = [book1, book2, book3, book4]

year_for_book = 1997
count_books = Book.count_books_year(book_list, year_for_book)
print(f'Number of books published in {year_for_book}: {count_books}')
