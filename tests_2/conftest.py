import pytest
from base.base_test import BaseTest


def pytest_addoption(parser):
    print("=== START pytest_addoption ===")
    parser.addoption("--my-option1", action="store", default="default_value")

    print("=== END pytest_addoption ===")


@pytest.fixture
def driver(add_multiple_attributes, request: pytest.FixtureRequest):
    print()

    print("START conftest 2")
    print("->")
    # print(dir(request.config.option))
    yield "__ROOT_CONFTEST_2__"
    print()
    print("finish conftest 2")


@pytest.fixture(scope="function")
def start_chrome_base():
    BaseTest.set_chrome_driver()
    yield
    BaseTest.stop_chrome_driver()
