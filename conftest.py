import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    print()
    print("START conftest 1")
    yield "__ROOT_CONFTEST__"
    print()
    print("finish conftest 1")


@pytest.fixture
def some_driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


