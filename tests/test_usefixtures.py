import pytest


@pytest.fixture
def clear_books_database() -> None:
    print('удаляем')


@pytest.fixture
def fill_books_database() -> None:
    print('заполняем')

@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books():
    print("Читаем все книги")

@pytest.mark.usefixtures('fill_books_database', 'clear_books_database')
class TestLibrary:
    def test_read_book(self):
        print('читаем из класса')

    def test_delete_book(self):
        print('удаляем из класса')