import sys
from app.models.book import Book
from app.models.reader import Reader
from app.models.library_management import LibraryManagementSystem


class LibraryManagementSystemCLI:
    def __init__(self):
        self.library = LibraryManagementSystem()

    def display_menu(self):
        print("\nLibrary Management System CLI")
        print("1. Add Book")
        print("2. Register Reader")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Exit")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = int(input("Enter publication year: "))

        # Check if the book already exists in the library
        existing_book = next((b for b in self.library.books if b.get_title() == title and b.get_author() == author),
                             None)
        if existing_book:
            print(f"Book '{title}' by {author} already exists in the library.")
            return

        book = Book(title, author, year)
        self.library.add_book(book)
        print(f"Book '{title}' by {author} added.")

    def register_reader(self):
        name = input("Enter reader's name: ")
        address = input("Enter reader's address: ")
        contact_info = input("Enter reader's contact info: ")

        # Check if the reader is already registered
        existing_reader = next((r for r in self.library.readers if r.get_name() == name), None)
        if existing_reader:
            print(f"Reader '{name}' is already registered.")
            return

        reader = Reader(name, address, contact_info)
        self.library.register_reader(reader)
        print(f"Reader '{name}' registered.")

    def lend_book(self):
        title = input("Enter the title of the book to lend: ")
        reader_name = input("Enter the reader's name: ")

        # Find the book and reader
        book = next((b for b in self.library.books if b.get_title() == title), None)
        reader = next((r for r in self.library.readers if r.get_name() == reader_name), None)

        if not book:
            print(f"No book found with the title '{title}'.")
            return
        if not reader:
            print(f"No reader found with the name '{reader_name}'.")
            return

        # Check if the book is already lent to another reader
        if not book.available:
            print(f"Book '{title}' is already lent to another reader.")
            return

        if self.library.lend_book(book, reader):
            print(f"Book '{title}' lent to {reader_name}.")
        else:
            print(f"Book '{title}' is unavailable.")

    def return_book(self):
        title = input("Enter the title of the book to return: ")
        reader_name = input("Enter the reader's name: ")

        # Find the book and reader
        book = next((b for b in self.library.books if b.get_title() == title), None)
        reader = next((r for r in self.library.readers if r.get_name() == reader_name), None)

        if not book:
            print(f"No book found with the title '{title}'.")
            return
        if not reader:
            print(f"No reader found with the name '{reader_name}'.")
            return

        # Check if the book is currently lent
        if not book.available:
            print(f"Book '{title}' has not been lent out.")
            return

        self.library.return_book(book, reader)
        print(f"Book '{title}' returned by {reader_name}.")

    def search_books(self):
        title = input("Enter title to search (leave empty to skip): ")
        author = input("Enter author to search (leave empty to skip): ")
        year_input = input("Enter year to search (leave empty to skip): ")

        year = int(year_input) if year_input else None
        books = self.library.search_books(title, author, year)

        if books:
            print("\nSearch Results:")
            for book in books:
                print(f"Title: {book.get_title()}, Author: {book.get_author()}, Year: {book.get_publication_year()}")
        else:
            print("No books found matching the search criteria.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.register_reader()
            elif choice == '3':
                self.lend_book()
            elif choice == '4':
                self.return_book()
            elif choice == '5':
                self.search_books()
            elif choice == '6':
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid option, please try again.")
