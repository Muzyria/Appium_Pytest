import pytest


@pytest.fixture
def driver():
    print()
    print("START conftest 1")
    yield "__ROOT_CONFTEST__"
    print()
    print("finish conftest 1")
