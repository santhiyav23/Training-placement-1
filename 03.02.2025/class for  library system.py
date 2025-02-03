class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book}' to the library.")

    def show_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("No books in the library.")

library = Library()

library.add_book("The Catcher in the Rye")
library.add_book("To Kill a Mockingbird")
library.show_books()
