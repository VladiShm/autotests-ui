import pytest


@pytest.mark.smoke
def test_some_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...


@pytest.mark.smoke
@pytest.mark.regression
class TestSuite:

    def test_case1(self):
        ...

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password_reset(self):
        ...

    def test_logout(self):
        ...

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.slow
@pytest.mark.critical
def critical_login():
    pass