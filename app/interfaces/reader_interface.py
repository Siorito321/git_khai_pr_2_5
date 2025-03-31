from abc import ABC, abstractmethod
from app.interfaces.book_interface import BookInterface


class ReaderInterface(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_address(self) -> str:
        pass

    @abstractmethod
    def get_contact_info(self) -> str:
        pass

    @abstractmethod
    def get_borrowed_books(self) -> list[BookInterface]:
        pass