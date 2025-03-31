import pytest
from app.models.book import Book
from app.models.reader import Reader
from app.models.library_management import LibraryManagementSystem

@pytest.fixture
def setup_library():
    library = LibraryManagementSystem()
    book = Book("1984", "George Orwell", 1949)
    reader = Reader("Alice", "123 Main St", "alice@example.com")
    return library, book, reader

def test_add_book(setup_library):
    library, book, _ = setup_library
    library.add_book(book)
    assert book in library.books

def test_register_reader(setup_library):
    library, _, reader = setup_library
    library.register_reader(reader)
    assert reader in library.readers

def test_lend_book(setup_library):
    library, book, reader = setup_library
    library.add_book(book)
    library.register_reader(reader)
    success = library.lend_book(book, reader)
    assert success is True
    assert not book.is_available()
    assert book in reader.get_borrowed_books()

def test_return_book(setup_library):
    library, book, reader = setup_library
    library.add_book(book)
    library.register_reader(reader)
    library.lend_book(book, reader)
    library.return_book(book, reader)
    assert book.is_available()
    assert book not in reader.get_borrowed_books()

def test_search_books(setup_library):
    library, book, _ = setup_library
    library.add_book(book)
    results = library.search_books(title="1984")
    assert len(results) == 1
    assert results[0].get_title() == "1984"
