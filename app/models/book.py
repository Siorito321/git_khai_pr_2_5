from app.interfaces.book_interface import BookInterface


class Book(BookInterface):
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def get_title(self) -> str:
        return self.title

    def get_author(self) -> str:
        return self.author

    def get_publication_year(self) -> int:
        return self.year

    def is_available(self) -> bool:
        return self.available

    def set_availability(self, available: bool) -> None:
        self.available = available