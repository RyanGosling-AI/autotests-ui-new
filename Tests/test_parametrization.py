import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    print(f'Number: {number}')


@pytest.mark.parametrize('number, expected', [(1,1), (2,4), (3,9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('browsers', ['chromium', 'firefox', 'webkit'])
@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
def test_multiplication_of_browsers(os: str, browsers: str):
    assert len(os + browsers) > 0


@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operations(self, user: str, account: str):
        ...

    def test_user_without_operations(self, user: str):
        ...

users = {
    '70000000011': 'User with money in bank account',
    '70000000022': 'User without money in bank account',
    '70000000033': 'User with operation in bank account'
}


@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...