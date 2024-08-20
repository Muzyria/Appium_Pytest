import pytest
from selenium import webdriver
from base.base_test import BaseTest


def pytest_addoption(parser):
    print("=== START pytest_addoption 1 ===")
    parser.addoption("--run_slow",
                     default="False",
                     # choices=("True", "False")
                     )

    print("=== END pytest_addoption 1 ===")


@pytest.fixture(scope="class", autouse=True)
def add_class_attribute(request):
    request.cls.class_attribute = "Class-level attribute"


@pytest.fixture
def add_multiple_attributes(request):
    request.node.attr1 = "Attribute 1"
    request.node.attr2 = 42
    request.node.attr3 = [1, 2, 3]


@pytest.fixture
def driver(add_multiple_attributes):
    print()

    print("START conftest 1")
    yield "__ROOT_CONFTEST__"
    print()
    print("finish conftest 1")


@pytest.fixture(scope="module", autouse=True)
def start_geco_base():
    BaseTest.set_gecko_driver()
    yield
    BaseTest.stop_gecko_driver()



@pytest.fixture
def gecko_driver():
    driver = webdriver.Firefox()
    yield driver
    print()
    print("QUIT GECKO")
    driver.quit()


@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    print()
    print("QUIT CHROME")
    driver.quit()


