from abc import ABC, abstractmethod

from app.interfaces.book_interface import BookInterface
from app.interfaces.reader_interface import ReaderInterface


class LibraryManagementSystemInterface(ABC):
    @abstractmethod
    def add_book(self, book: BookInterface) -> None:
        pass

    @abstractmethod
    def register_reader(self, reader: ReaderInterface) -> None:
        pass

    @abstractmethod
    def lend_book(self, book: BookInterface, reader: ReaderInterface) -> bool:
        pass

    @abstractmethod
    def return_book(self, book: BookInterface, reader: ReaderInterface) -> None:
        pass

    @abstractmethod
    def search_books(self, title: str = "", author: str = "", year: int = None) -> list[BookInterface]:
        pass
