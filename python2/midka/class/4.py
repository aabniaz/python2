class Book():
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __str__(self):
        return f'title: {self.title}, author: {self.author}, isbn: {self.ISBN}'
        
class LibraryCatalog():
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"added '{book.title}' to the library catalog.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'removed {book.title}, {book.author}')
        else: print('book not found')

    def display_books(self):
        if self.books:
            print("books available in the library:")
            for book in self.books:
                print(book)
        else:
            print("the library catalog is empty.")

book1 = Book("1984", "George Orwell", "9780451524935")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

library = LibraryCatalog()
library.add_book(book1)
library.add_book(book2)
library.display_books()

library.remove_book(book1)
library.display_books()

library.remove_book(book1)