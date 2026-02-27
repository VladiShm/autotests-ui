import pytest


@pytest.mark.xfail(reason='bug in this test')
def test_with_bug():
    assert 1 == 1


def test_without_bug():
    pass
