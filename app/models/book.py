from app.interfaces.book_interface import BookInterface

class Book(BookInterface):
    """Dependent class"""
    def __init__(self, title_provider, author_provider, year_provider):

        self.title = title_provider.get_title()
        self.author = author_provider.get_author()
        self.year = year_provider.get_publication_year()
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


class TitleProvider:
    """Independent class"""
    def __init__(self, title: str):
        self._title = title

    def get_title(self) -> str:
        return self._title

class AuthorProvider:
    """Independent class"""
    def __init__(self, author: str):
        self._author = author

    def get_author(self) -> str:
        return self._author

class YearProvider:
    """Independent class"""
    def __init__(self, year: int):
        self._year = year

    def get_publication_year(self) -> int:
        return self._year
