import pytest


@pytest.fixture(scope="class")
def driver():
    print()
    print("START conftest 2")
    yield "__TESTS_CONFTEST__"
    print()
    print("finish conftest 2")
