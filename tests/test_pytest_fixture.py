import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print('autouse отправляем данные в сервис аналитики')


@pytest.fixture(scope='session')
def settings():
    print('session инициализируем настройки автотестов')


@pytest.fixture(scope='class')
def user():
    print('class создаем данные пользователя один раз на тестовый класс')


@pytest.fixture(scope='function')
def browser():
    print('function открывем браузер на каждый тест')


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        pass

    def test_user_can_create_course(self, settings, user, browser):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass