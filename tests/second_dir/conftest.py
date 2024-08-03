import pytest




@pytest.fixture
def driver():
    print()

    print("START conftest 3")
    yield "__SECOND_CONFTEST__"
    print()
    print("finish conftest 3")


