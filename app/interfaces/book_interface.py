from abc import ABC, abstractmethod
from typing import List

class BookInterface(ABC):
    @abstractmethod
    def get_title(self) -> str:
        pass

    @abstractmethod
    def get_author(self) -> str:
        pass

    @abstractmethod
    def get_publication_year(self) -> int:
        pass

    @abstractmethod
    def is_available(self) -> bool:
        pass
