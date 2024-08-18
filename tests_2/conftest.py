import pytest


@pytest.fixture
def driver(add_multiple_attributes):
    print()

    print("START conftest 2")
    yield "__ROOT_CONFTEST_2__"
    print()
    print("finish conftest 2")