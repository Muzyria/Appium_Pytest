import pytest
from selenium import webdriver


class BaseTest:
    driver_geco: webdriver.Firefox = None

    @pytest.fixture(autouse=True)
    def setup(self, request: pytest.FixtureRequest):
        request.cls.my_atr = "it is My atr"

    @classmethod
    def set_gecko_driver(cls):
        cls.driver_geco = webdriver.Firefox()
        print()
        print("START GECKO")
        print(cls.driver_geco.session_id)

    @classmethod
    def stop_gecko_driver(cls):
        cls.driver_geco.quit()
        print()
        print("STOP GECKO")


