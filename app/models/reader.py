from app.interfaces.reader_interface import ReaderInterface
from app.models.book import Book


class Reader(ReaderInterface):
    def __init__(self, name: str, address: str, contact_info: str):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.borrowed_books = []

    def get_name(self) -> str:
        return self.name

    def get_address(self) -> str:
        return self.address

    def get_contact_info(self) -> str:
        return self.contact_info

    def get_borrowed_books(self) -> list[Book]:
        return self.borrowed_books

    def borrow_book(self, book: Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        self.borrowed_books.remove(book)