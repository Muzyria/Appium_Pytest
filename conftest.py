import pytest
from selenium import webdriver


@pytest.fixture(scope="class" ,autouse=True)
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


