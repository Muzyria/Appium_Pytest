import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")



@pytest.fixture
def driver(request: pytest.FixtureRequest):
    print()

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


