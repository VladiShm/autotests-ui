import pytest

SYSTEM_VERSION = 'v1.0.0'


@pytest.mark.skipif(SYSTEM_VERSION == 'v1.0.1', reason='not supported v1.0.1')
def test_system_version_valid():
    pass


@pytest.mark.skipif(SYSTEM_VERSION == 'v1.0.0', reason='not supported v1.0.0')
def test_system_version_invalid():
    pass
