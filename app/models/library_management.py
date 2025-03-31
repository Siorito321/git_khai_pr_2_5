from app.interfaces.library_management_interface import LibraryManagementSystemInterface
from app.models.book import Book
from app.models.reader import Reader


class LibraryManagementSystem(LibraryManagementSystemInterface):
    def __init__(self) -> None:
        self.books = []
        self.readers = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def register_reader(self, reader: Reader) -> None:
        self.readers.append(reader)

    def lend_book(self, book: Book, reader: Reader) -> bool:
        if book in self.books and book.is_available():
            book.set_availability(False)
            reader.borrow_book(book)
            return True
        return False

    def return_book(self, book: Book, reader: Reader) -> None:
        if book in reader.get_borrowed_books():
            book.set_availability(True)
            reader.return_book(book)

    def search_books(self, title: str = "", author: str = "", year: int = None) -> list[Book]:
        return [book for book in self.books if
                (title in book.get_title() if title else True) and
                (author in book.get_author() if author else True) and
                (book.get_publication_year() == year if year else True)]