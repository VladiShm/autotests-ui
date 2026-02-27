import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize('number', [1, 2, 3, 0, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number, expected):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os, browser):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser):
    print(f'running test {browser}')


@pytest.mark.parametrize('user', ['Bob', 'Kate'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        print(f'running test {user} with {account}')

    def test_user_without_operations(self, user: str):
        print(f'running test {user}')


users = {
    '+834324234': 'user with money',
    '+83433224234': 'user without money',
    '+83432423432': 'user with operations'
}


@pytest.mark.parametrize('phone_number', users.keys(),
                         ids=lambda phone_number: f'{users[phone_number]} {phone_number}')
def test_identifiers(phone_number: str):
    pass
