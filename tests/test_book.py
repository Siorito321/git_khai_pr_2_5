import unittest
from app.models.book import Book, TitleProvider, AuthorProvider, YearProvider


class TestTitleProvider(unittest.TestCase):
    def test_get_title(self):
        provider = TitleProvider("Test Title")
        self.assertEqual(provider.get_title(), "Test Title")


class TestAuthorProvider(unittest.TestCase):
    def test_get_author(self):
        provider = AuthorProvider("Test Author")
        self.assertEqual(provider.get_author(), "Test Author")


class TestYearProvider(unittest.TestCase):
    def test_get_publication_year(self):
        provider = YearProvider(2024)
        self.assertEqual(provider.get_publication_year(), 2024)


class TestBook(unittest.TestCase):
    def setUp(self):
        self.title_provider = TitleProvider("Sample Title")
        self.author_provider = AuthorProvider("Sample Author")
        self.year_provider = YearProvider(2023)
        self.book = Book(self.title_provider, self.author_provider, self.year_provider)

    def test_get_title(self):
        self.assertEqual(self.book.get_title(), "Sample Title")

    def test_get_author(self):
        self.assertEqual(self.book.get_author(), "Sample Author")

    def test_get_publication_year(self):
        self.assertEqual(self.book.get_publication_year(), 2023)

    def test_is_available_initial(self):
        self.assertTrue(self.book.is_available())

    def test_set_availability(self):
        self.book.set_availability(False)
        self.assertFalse(self.book.is_available())
        self.book.set_availability(True)
        self.assertTrue(self.book.is_available())
